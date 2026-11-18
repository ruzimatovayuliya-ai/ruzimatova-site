
/* размеры текстов фиксируются по более длинному из RU/KZ, чтобы при смене языка ничего не прыгало */
function lockSizes(again){
  const els=[...document.querySelectorAll('[data-kz]')].filter(el=>!el.closest('[data-nolock]')&&(el.offsetParent||getComputedStyle(el).position==='fixed'));
  els.forEach(el=>{if(el.dataset.ru===undefined)el.dataset.ru=el.innerHTML;if(!again){el.style.minWidth='';el.style.minHeight=''}});
  const m=new Map(),par=new Set();
  els.forEach(el=>{if(getComputedStyle(el).display==='inline'&&el.parentElement){par.add(el.parentElement);if(!again)el.parentElement.style.minHeight=''}});
  const all=[...els,...par];
  for(const v of ['ru','kz']){els.forEach(el=>{el.innerHTML=el.dataset[v]});if(typeof typo==='function')typo(document.body);
    all.forEach(el=>{const r=el.getBoundingClientRect(),o=m.get(el)||{w:0,h:0};m.set(el,{w:Math.max(o.w,r.width),h:Math.max(o.h,r.height)})})}
  els.forEach(el=>{el.innerHTML=lang==='kz'?el.dataset.kz:el.dataset.ru});if(typeof typo==='function')typo(document.body);
  els.forEach(el=>{
    const d=getComputedStyle(el).display,pd=el.parentElement?getComputedStyle(el.parentElement):null,o=m.get(el);
    const rowItem=pd&&/flex/.test(pd.display)&&!/column/.test(pd.flexDirection);
    if(d==='inline')return;
    if(d.startsWith('inline')||rowItem)el.style.minWidth=Math.ceil(o.w)+'px';
    else el.style.minHeight=Math.ceil(o.h)+'px'});
  par.forEach(el=>{if(!els.includes(el))el.style.minHeight=Math.ceil(m.get(el).h)+'px'});
}
{let t;const run=()=>{try{lockSizes();lockSizes(1)}catch(e){}};
 addEventListener('resize',()=>{clearTimeout(t);t=setTimeout(run,200)});
 (document.fonts?document.fonts.ready:Promise.resolve()).then(run);addEventListener('load',run)}
