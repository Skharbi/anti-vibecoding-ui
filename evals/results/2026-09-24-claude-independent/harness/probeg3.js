const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:400},isMobile:true,hasTouch:true});
await p.goto('file://'+process.cwd()+'/h/G3/index.html');await p.waitForTimeout(300);
const res=[];for(let i=0;i<14;i++){await p.keyboard.press('Tab');res.push(await p.evaluate(()=>{const a=document.activeElement;const r=a.getBoundingClientRect();const fx=[...document.querySelectorAll('*')].filter(e=>getComputedStyle(e).position==='fixed'&&e.offsetHeight>0&&!e.contains(a)).map(e=>e.getBoundingClientRect());const cov=fx.some(f=>r.top>=f.top-1&&r.bottom<=f.bottom+1);const part=fx.some(f=>r.bottom>f.top&&r.top<f.bottom);return (a.id||a.tagName)+(cov?'[HIDDEN]':part?'[partial]':'')}));}
console.log('tab',res.join(' > '));
// fill first name then Continue with others empty
const inputs=await p.$$('input:not([type=hidden]):not([type=checkbox]):not([type=radio])');if(inputs[0]){await inputs[0].fill('Maria');}
await p.getByRole('button',{name:/continue/i}).click();await p.waitForTimeout(200);
console.log('after continue',await p.evaluate(()=>({active:document.activeElement.id||document.activeElement.tagName,firstVal:document.querySelector('input:not([type=hidden])').value,invalid:[...document.querySelectorAll('[aria-invalid=true]')].map(e=>e.id),alerts:[...document.querySelectorAll('[role=alert],.error-summary')].map(e=>e.innerText.slice(0,80))})));
await b.close();})();
