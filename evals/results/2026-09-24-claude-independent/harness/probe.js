const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const F='/home/user/anti-vibecoding-ui/evals/runtime-fixtures/';
(async()=>{
 const b=await chromium.launch();
 const ctx=await b.newContext({viewport:{width:390,height:400},isMobile:true,hasTouch:true});
 const p=await ctx.newPage();
 // R3: scroll to bottom, is inline submit clear of fixed footer?
 await p.goto('file://'+F+'r3-responsive.html');
 await p.focus('textarea'); await p.evaluate(()=>window.scrollTo(0,1e6));
 console.log('r3', await p.evaluate(()=>{const s=document.querySelector('form .submit').getBoundingClientRect(),f=document.querySelector('.footer').getBoundingClientRect();return {submitBottom:s.bottom,footerTop:f.top,clear:s.bottom<=f.top, tableWrapScroll: document.querySelector('.table-wrap').scrollWidth+'/'+document.querySelector('.table-wrap').clientWidth}}));
 // G3: focus each field, check not hidden under fixed action bar; submit with empty member, check values preserved + error
 await p.goto('file://'+F+'g3-mobile-form.html');
 for (const id of ['member','reason','urgency']) { await p.focus('#'+id); const r=await p.evaluate(id=>{const e=document.getElementById(id).getBoundingClientRect(),a=document.querySelector('.actions').getBoundingClientRect();return {id,bottom:Math.round(e.bottom),barTop:Math.round(a.top),covered:e.bottom>a.top}},id); console.log('g3 focus',r); }
 await p.fill('#reason','Post-op MRI'); await p.click('button[type=submit]');
 console.log('g3 submit', await p.evaluate(()=>({err:document.getElementById('error').textContent, reason:document.getElementById('reason').value, active:document.activeElement.id||document.activeElement.tagName, memberInvalid: document.getElementById('member').getAttribute('aria-invalid')})));
 const order=[]; await p.goto('file://'+F+'g3-mobile-form.html'); for(let i=0;i<5;i++){await p.keyboard.press('Tab'); order.push(await p.evaluate(()=>document.activeElement.id||document.activeElement.innerText));} console.log('g3 tab order',order);
 // G1 states
 for (const s of ['loaded','empty','error']) { await p.goto('file://'+F+'g1-dashboard.html?state='+s); console.log('g1',s,await p.evaluate(()=>document.getElementById('state').textContent+' | retry button: '+!!document.querySelector('#state button'))); }
 // R9 text
 await p.goto('file://'+F+'r9-rtl.html'); console.log('r9',await p.evaluate(()=>({date:document.getElementById('date').textContent,num:document.getElementById('num').textContent,chevTransform:getComputedStyle(document.querySelector('.chev')).transform})));
 await b.close();})();
