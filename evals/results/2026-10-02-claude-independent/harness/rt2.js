const { chromium } = require('/opt/node-tools/node_modules/playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const S = __dirname;
const srv = http.createServer((q, r) => { const f = path.join(S, 'run/tasks', decodeURIComponent(q.url.split('?')[0])); if (!fs.existsSync(f)) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'content-type': f.endsWith('.js') ? 'text/javascript' : 'text/html' }); r.end(fs.readFileSync(f)); }).listen(8799);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const off of [false, true]) {
    const c = await b.newContext(); const p = await c.newPage(); const errs = [];
    p.on('pageerror', e => errs.push(String(e)));
    if (off) await p.addInitScript(() => { Object.defineProperty(window, 'navigation', { value: undefined, configurable: true }); });
    await p.goto('http://localhost:8799/P1-P1-1/checkout.html'); await p.waitForTimeout(500);
    const before = await p.innerText('body'); await p.click('button').catch(e => errs.push('click:' + e.message.slice(0, 60))); await p.waitForTimeout(500);
    console.log(off ? 'NAV-OFF' : 'NAV-ON', JSON.stringify({ errs, before: before.slice(0, 80), after: (await p.innerText('body')).slice(0, 80), url: p.url() }));
    await c.close();
  }
  // G1 320 offender, G3 unfocused element
  for (const [u, w] of [['G1-G1-1/index.html', 320], ['G3-G3-1/index.html', 390]]) {
    const c = await b.newContext({ viewport: { width: w, height: 800 } }); const p = await c.newPage();
    await p.goto('http://localhost:8799/' + u); await p.waitForTimeout(500);
    console.log(u, JSON.stringify(await p.evaluate(() => [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1).slice(0, 4).map(e => e.tagName + '.' + e.className + ':' + Math.round(e.getBoundingClientRect().right)))));
    const bad = [];
    for (let i = 0; i < 25; i++) { await p.keyboard.press('Tab'); const f = await p.evaluate(() => { const e = document.activeElement, cs = getComputedStyle(e); return { d: e.tagName + '#' + e.id + '.' + e.className, vis: (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || cs.boxShadow !== 'none' }; }); if (!f.vis) bad.push(f.d); }
    console.log('  focus-without-outline:', [...new Set(bad)]);
    await c.close();
  }
  await b.close(); srv.close();
})();
