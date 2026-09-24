// Usage: node render.js <outdir> <file.html>...  -> screenshots + JSON metrics at 390/768/1280 and 390x400 ("keyboard open" approximation)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const [outdir, ...files] = process.argv.slice(2);
  fs.mkdirSync(outdir, { recursive: true });
  const browser = await chromium.launch();
  console.log('browser', browser.version());
  const results = {};
  for (const f of files) {
    const name = path.basename(f, '.html');
    results[name] = {};
    for (const [w, h, tag] of [[390, 844, 'm'], [768, 1024, 't'], [1280, 800, 'd'], [390, 400, 'kbd']]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, hasTouch: w < 800, isMobile: w < 800 });
      const page = await ctx.newPage();
      const errors = [];
      page.on('pageerror', e => errors.push(String(e)));
      await page.goto('file://' + path.resolve(f));
      await page.waitForTimeout(300);
      const m = await page.evaluate(() => {
        const de = document.documentElement;
        const vis = el => { const r = el.getBoundingClientRect(); return { top: Math.round(r.top), bottom: Math.round(r.bottom), left: Math.round(r.left), right: Math.round(r.right) }; };
        const fixed = [...document.querySelectorAll('*')].filter(e => ['fixed', 'sticky'].includes(getComputedStyle(e).position)).map(e => ({ tag: e.tagName, cls: e.className, ...vis(e) }));
        const buttons = [...document.querySelectorAll('button, [type=submit], a')].map(b => ({ text: (b.innerText || '').trim().slice(0, 40), ...vis(b), w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height) }));
        const inputs = [...document.querySelectorAll('input,select,textarea')].map(i => ({ id: i.id, type: i.type, labelled: !!(i.labels && i.labels.length) || !!i.getAttribute('aria-label') || !!i.getAttribute('aria-labelledby') }));
        return { dir: de.dir || getComputedStyle(document.body).direction, scrollW: de.scrollWidth, clientW: de.clientWidth, hOverflow: de.scrollWidth > de.clientWidth, fixed, buttons: buttons.slice(0, 30), inputs, dataset: document.body.dataset.result || null, h1: document.querySelector('h1')?.innerText };
      });
      m.errors = errors;
      results[name][`${w}x${h}`] = m;
      await page.screenshot({ path: `${outdir}/${name}-${tag}.png`, fullPage: tag !== 'kbd' });
      await ctx.close();
    }
  }
  fs.writeFileSync(`${outdir}/metrics.json`, JSON.stringify(results, null, 1));
  await browser.close();
})();
