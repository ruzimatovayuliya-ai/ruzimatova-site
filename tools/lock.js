/* размеры блоков фиксируются по более длинному из RU/KZ, чтобы при смене языка ничего не прыгало.
   Страница незаметно (до отрисовки) показывается на обоих языках, замеряется всё видимое – в том числе тексты,
   которые рисует скрипт, – и каждому блоку ставится минимальный размер по большему из двух.
   Пересчёт – при загрузке, смене языка, вкладки, перерисовке списков и размера окна. */
let lockBusy=false;const lockDone=new Set();
function lockSizes(reset){
  if(lockBusy||typeof lockSetLang!=='function')return;lockBusy=true;
  const root=document.body;
  const cur=lang,other=cur==='kz'?'ru':'kz';
  const scr=[...document.querySelectorAll('.as.on,.rd')].map(e=>[e,e.scrollTop]),sx=scrollX,sy=scrollY;
  try{
    if(reset===true)lockDone.clear();
    if(reset===true)document.querySelectorAll('[data-lk]').forEach(el=>{const o=el.getAttribute('data-lk').split('|');el.style.minWidth=o[0];el.style.minHeight=o[1]||'';el.removeAttribute('data-lk')});
    const SKIP=/^(SCRIPT|STYLE|svg|path|circle|rect|defs|stop|linearGradient|g|line|polyline|ellipse|BR|INPUT|TEXTAREA|SELECT|IMG|VIDEO|IFRAME|CANVAS)$/;
    const snap=()=>{const m=new Map();
      const walk=(el,key)=>{let i=0;for(const c of el.children){const k=key+'/'+(i++);if(SKIP.test(c.tagName)||c.hasAttribute('data-nolock'))continue;
        const r=c.getBoundingClientRect();if(!r.width&&!r.height)continue;const z=c.currentCSSZoom||1;m.set(k,{el:c,w:r.width/z,h:r.height/z});walk(c,k)}};
      walk(root,'');return m};
    /* несколько проходов: блок, ставший шире, может перенести строку у соседа – доводим, пока оба языка не совпадут.
       Минимумы копятся между сменами языка и сбрасываются только при загрузке и смене размера окна */
    for(let pass=0;pass<4;pass++){
      lockSetLang(other);const A=snap();lockSetLang(cur);const B=snap();let n=0;
      for(const [k,b] of B){const a=A.get(k);if(!a)continue;const dw=Math.abs(a.w-b.w),dh=Math.abs(a.h-b.h);if(dw<=.5&&dh<=.5)continue;
        const el=b.el;if(getComputedStyle(el).display==='inline')continue;
        if(!el.hasAttribute('data-lk'))el.setAttribute('data-lk',el.style.minWidth+'|'+el.style.minHeight);
        if(dw>.5)el.style.minWidth=Math.max(a.w,b.w)+'px';if(dh>.5)el.style.minHeight=Math.max(a.h,b.h)+'px';
        if(a.el===el)n++}  /* блок, который скрипт пересоздаёт при смене языка, фиксируется сразу, без повторных проходов */
      if(!n)break}
  }catch(e){console.warn('lockSizes',e)}
  finally{scr.forEach(([e,t])=>e.scrollTop=t);if(scrollX!==sx||scrollY!==sy)scrollTo(sx,sy);lockBusy=false}
}
/* перехватываем смену языка и перерисовки, чтобы фиксация всегда была до того, как картинка появится на экране */
const lockSetLang=setLang;
setLang=function(l){lockBusy=true;try{lockSetLang(l)}finally{lockBusy=false}lockSizes()};
/* только в самом тренажёре: на сайте мокап сам листает вкладки, там пересчёт – при смене языка */
/* вкладка, уже замеренная при этом размере окна, повторно не замеряется – переключение остаётся мгновенным */
if(document.getElementById('ptr'))['go','drawArts','drawVids','drawAns','openArt'].forEach(n=>{const f=window[n];if(typeof f!=='function')return;
  window[n]=function(){const r=f.apply(this,arguments);if(n==='go'){const k=arguments[0];if(lockDone.has(k))return r;lockDone.add(k)}lockSizes();return r}});
{let t;addEventListener('resize',()=>{clearTimeout(t);t=setTimeout(()=>lockSizes(true),200)});
 (document.fonts?document.fonts.ready:Promise.resolve()).then(()=>lockSizes(true));addEventListener('load',()=>lockSizes(true))}
