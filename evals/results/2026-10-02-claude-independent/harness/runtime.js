// Chromium-only runtime evidence for execution-gated cases. Outputs JSON + screenshots.
const { chromium } = require(process.env.PW || 'playwright');
const path = require('path'), fs = require('fs');
const S = __dirname, OUT = path.join(S, 'runtime'); fs.mkdirSync(OUT, { recursive: true });
const REPO = '<repo>/evals/runtime-fixtures';
const targets = [
  ['R3-task', path.join(S, 'run/tasks/R3-R3-1/claims.html')],
  ['R3-fixture', path.join(REPO, 'r3-responsive.html')],
  ['R9-fixture', path.join(REPO, 'r9-rtl.html')],
  ['G1-generated', path.join(S, 'run/tasks/G1-G1-1/index.html')],
  ['G2-generated', path.join(S, 'run/tasks/G2-G2-1/index.html')],
  ['G3-generated', path.join(S, 'run/tasks/G3-G3-1/index.html')],
  ['G1-fixture', path.join(REPO, 'g1-dashboard.html')],
  ['G2-fixture', path.join(REPO, 'g2-portfolio.html')],
  ['G3-fixture', path.join(REPO, 'g3-mobile-form.html')],
  ['P1-task', path.join(S, 'run/tasks/P1-P1-1/checkout.html')],
  ['P1-fixture', path.join(REPO, 'p1-browser-feature.html')],
];
const widths = [320, 390, 768, 1280];
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
  const results = { browser: browser.version(), date: new Date().toISOString(), targets: {} };
  for (const [name, file] of targets) {
    if (!fs.existsSync(file)) { results.targets[name] = { missing: true }; continue; }
    const r = { file, widths: {} };
    for (const w of widths) {
      const ctx = await browser.newContext({ viewport: { width: w, height: w < 800 ? 780 : 900 }, locale: name.startsWith('R9') ? 'ar-SA' : 'en-US', hasTouch: w < 800 });
      const page = await ctx.newPage(); const errors = [];
      page.on('pageerror', e => errors.push(String(e))); page.on('console', m => m.type() === 'error' && errors.push(m.text()));
      await page.goto('file://' + file); await page.waitForTimeout(400);
      const m = await page.evaluate(() => {
        const de = document.documentElement;
        const vis = el => { const b = el.getBoundingClientRect(), cs = getComputedStyle(el); return b.width > 0 && b.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
        const ctrls = [...document.querySelectorAll('button,a[href],input,select,textarea,[tabindex]')].filter(vis);
        const small = ctrls.filter(e => { const b = e.getBoundingClientRect(); return (b.height < 24 || b.width < 24) && e.tagName !== 'A'; }).length;
        const unlabeled = [...document.querySelectorAll('input:not([type=hidden]),select,textarea')].filter(e => !(e.labels && e.labels.length) && !e.getAttribute('aria-label') && !e.getAttribute('aria-labelledby')).length;
        const fixed = [...document.querySelectorAll('*')].filter(e => ['fixed', 'sticky'].includes(getComputedStyle(e).position)).map(e => { const b = e.getBoundingClientRect(); return { tag: e.tagName, cls: e.className, top: Math.round(b.top), bottom: Math.round(b.bottom), h: Math.round(b.height) }; });
        return { scrollW: de.scrollWidth, clientW: de.clientWidth, overflowX: de.scrollWidth > de.clientWidth + 1, dir: de.dir || getComputedStyle(document.body).direction, lang: de.lang, controls: ctrls.length, smallTargets: small, unlabeled, fixed, h1: document.querySelectorAll('h1').length, title: document.title };
      });
      // keyboard: tab through first 25 stops; record focus visibility
      const tabs = [];
      for (let i = 0; i < 25; i++) {
        await page.keyboard.press('Tab');
        const f = await page.evaluate(() => { const e = document.activeElement; if (!e || e === document.body) return null; const cs = getComputedStyle(e); return { tag: e.tagName, text: (e.innerText || e.value || e.getAttribute('aria-label') || '').trim().slice(0, 30), outline: cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0, shadow: cs.boxShadow !== 'none' }; });
        if (!f) break; tabs.push(f);
      }
      m.tabStops = tabs.length; m.focusInvisible = tabs.filter(t => !t.outline && !t.shadow).length; m.errors = errors;
      await page.screenshot({ path: path.join(OUT, `${name}-${w}.png`), fullPage: true });
      r.widths[w] = m; await ctx.close();
    }
    results.targets[name] = r;
  }
  // G3 generated: submit empty, check values preserved after typing one field and errors visible; reduced viewport (keyboard approximation)
  for (const name of ['G3-generated', 'G3-fixture']) {
    const file = targets.find(t => t[0] === name)[1]; if (!fs.existsSync(file)) continue;
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true });
    const page = await ctx.newPage(); await page.goto('file://' + file);
    const firstText = page.locator('input[type=text],input:not([type])').first();
    let typed = null; if (await firstText.count()) { await firstText.fill('Test Value'); typed = 'Test Value'; }
    const submit = page.locator('button[type=submit],input[type=submit],form button').last();
    let r = { hasSubmit: await submit.count() > 0 };
    if (r.hasSubmit) {
      await submit.click(); await page.waitForTimeout(500);
      r.afterSubmit = await page.evaluate(() => ({ invalid: document.querySelectorAll('[aria-invalid=true]').length, alerts: [...document.querySelectorAll('[role=alert],[aria-live]')].map(e => e.innerText.trim().slice(0, 80)).filter(Boolean), focused: document.activeElement && (document.activeElement.id || document.activeElement.tagName) }));
      r.valuePreserved = typed ? (await firstText.inputValue()) === typed : null;
      await page.setViewportSize({ width: 390, height: 450 }); // approximate visual viewport with keyboard open
      await page.locator('input,textarea').first().focus(); await page.waitForTimeout(200);
      r.submitVisibleAt450 = await submit.evaluate(e => { const b = e.getBoundingClientRect(); return b.bottom <= innerHeight && b.top >= 0; });
    }
    results.targets[name].interaction = r; await ctx.close();
  }
  // P1: forced-off Navigation API (fallback check only, not Safari/Firefox evidence)
  for (const name of ['P1-task', 'P1-fixture']) {
    const file = targets.find(t => t[0] === name)[1];
    const ctx = await browser.newContext(); const page = await ctx.newPage(); const errors = [];
    page.on('pageerror', e => errors.push(String(e)));
    await page.addInitScript(() => { try { delete window.navigation; Object.defineProperty(window, 'navigation', { value: undefined, configurable: true }); } catch (e) {} });
    await page.goto('file://' + file); await page.waitForTimeout(400);
    results.targets[name].navigationForcedOff = { errors, body: (await page.innerText('body')).slice(0, 200) };
    await ctx.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(OUT, 'results.json'), JSON.stringify(results, null, 1));
  console.log('done', results.browser);
})();
