import re
s=open('index.html',encoding='utf-8').read()
styles=''.join(re.findall(r'<style>.*?</style>',s,re.S))
phone=re.search(r'(  <div class="phone".*?\n  </div>\n)</div></section>',s,re.S).group(1)
js=re.search(r'<script>(.*?)</script>',s,re.S).group(1)
head_js=js[:js.index('/* язык */')]
app_js=js[js.index('/* приложение «Тонус» */'):js.index('/* анимации сайта */')]
phone=phone.replace('<div class="phone" aria-label="Приложение «Тонус», демо">','<div class="phone" aria-label="Приложение «Тонус»">')
phone=phone.replace('<div class="sbar"><span>9:41</span><span class="isl"></span><span>●●●</span></div>','<div class="inst" id="inst" hidden><b id="inst-h" data-kz="<svg class=&quot;iph&quot; viewBox=&quot;0 0 24 24&quot; fill=&quot;none&quot; stroke=&quot;currentColor&quot; stroke-width=&quot;1.9&quot; stroke-linecap=&quot;round&quot; stroke-linejoin=&quot;round&quot;><rect x=&quot;7&quot; y=&quot;3&quot; width=&quot;10&quot; height=&quot;18&quot; rx=&quot;2.5&quot;/><path d=&quot;M11 18h2&quot;/></svg> Телефонға орнату – қалай?"><svg class="iph" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="3" width="10" height="18" rx="2.5"/><path d="M11 18h2"/></svg> Установить на телефон – как?</b><span id="inst-t" hidden></span><button id="inst-b" hidden data-kz="Орнату">Установить</button><button id="inst-x" aria-label="Закрыть">×</button></div>')
extra='''<style>
html,body{height:100%}
html{background:#2B2140}body{background:#2B2140;margin:0;overflow:hidden}
body::before{display:none!important}
:root{padding:0!important}
html,body{overscroll-behavior:none}
@media (max-width:599px){html,body{background:#251C36!important}}

.phone{position:fixed;inset:0;margin:0 auto;width:100%;max-width:480px;height:auto;border:0;border-radius:0;padding:0;box-shadow:none;background:none;aspect-ratio:auto}
.phone::before,.phone::after{display:none}
.scr{border-radius:0;padding:calc(env(safe-area-inset-top,0px) + 14px) 16px 0;font-size:15px}
.atabs{padding-top:8px;padding-bottom:max(8px,calc(env(safe-area-inset-bottom,0px) - 12px));margin:0 -16px}
.atab{font-size:11px}.atab svg{width:22px;height:22px}
.av{cursor:pointer}
.inst{display:grid;grid-template-columns:1fr auto;gap:4px 10px;align-items:center;background:linear-gradient(125deg,#8F6BDA,#E59CC6);color:#fff;border-radius:16px;padding:12px 14px;margin-bottom:10px;font-size:13px;line-height:1.35}
.inst[hidden]{display:none}
.inst b{font-size:13px;cursor:pointer}.inst{padding:9px 12px!important;margin-bottom:8px!important;flex:none}
.inst span{grid-column:1}
.inst button{font:700 13px Manrope,sans-serif;border:0;border-radius:10px;padding:8px 12px;background:#fff;color:#7A55B8;cursor:pointer}
#inst-x{grid-column:2;grid-row:1;background:transparent;color:#fff;font-size:20px;padding:0 4px;justify-self:end}
#inst-b{grid-column:2;grid-row:2}
.iph{width:15px;height:15px;vertical-align:-3px;margin-right:2px}
@media (max-height:600px){.as[data-s=today] .tip{display:none}}
@media (min-width:600px){body{background:linear-gradient(125deg,#8F6BDA,#B583D6 50%,#E59CC6)}.phone{top:24px;bottom:24px;height:auto;max-width:420px;border-radius:36px;overflow:hidden;box-shadow:0 40px 90px -30px #2b1440aa}.scr{border-radius:36px}}

.ptr{position:fixed;left:50%;top:calc(env(safe-area-inset-top,0px) + 8px);z-index:30;width:44px;height:44px;margin-left:-22px;border-radius:50%;background:#3E2F5C;box-shadow:0 8px 24px -8px #0009,inset 0 0 0 1px #ffffff1a;display:flex;align-items:center;justify-content:center;transform:translateY(-70px);opacity:0;pointer-events:none}
.ptr svg{width:30px;height:30px;overflow:visible}
.ptr path{stroke-dasharray:100;stroke-dashoffset:calc(100 - var(--p,0)*100)}
.ptr.go path{animation:ptrdraw 1.6s ease-in-out infinite;animation-delay:calc(var(--i)*.1s)}
@keyframes ptrdraw{0%{stroke-dashoffset:100;opacity:1}50%{stroke-dashoffset:0;opacity:1}85%,100%{stroke-dashoffset:0;opacity:0}}
.ptr.back{transition:transform .3s ease,opacity .3s}
.isteps{gap:10px!important;text-align:left}
.ist{display:flex;align-items:center;gap:10px;font-size:13px;line-height:1.35}
.isn{width:20px;height:20px;border-radius:50%;background:#ffffff1a;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none;color:var(--a-acc)}
.ist .mi{width:34px;height:34px}.ist .mi svg{width:19px;height:19px}
.ccard.hl{box-shadow:0 0 0 2px var(--a-acc)}
.desk{display:none}
@media (min-width:900px){
 /* компьютер: полноценная версия во весь экран, слева описание и QR для телефона */
 body{display:grid;grid-template-columns:minmax(280px,340px) minmax(0,1fr);height:100dvh;padding:20px;gap:24px;box-sizing:border-box}
 .desk{display:flex;flex-direction:column;gap:16px;min-height:0;overflow:auto;padding:12px 4px 12px 16px;color:#fff;font-family:Manrope,sans-serif;scrollbar-width:none}
 .desk .dlogo{width:56px;height:56px;border-radius:16px;flex:none;box-shadow:0 14px 30px -12px #2b144088}
 .desk h1{margin:0;font-size:clamp(24px,2.1vw,30px);line-height:1.15;font-weight:800;letter-spacing:-.02em;text-wrap:balance}
 .desk p{margin:0;font-size:15px;line-height:1.5;color:#ffffffe6}
 .desk .qr{margin-top:auto;display:flex;align-items:center;gap:14px;background:#fff;color:#2A2140;border-radius:18px;padding:12px 14px 12px 12px;font-size:13px;font-weight:600;line-height:1.4}
 .desk .qr svg{width:84px;height:84px;flex:none}
 .desk a{color:#fff;font-weight:700;font-size:14px;text-decoration:none;opacity:.9}.desk a:hover{opacity:1;text-decoration:underline}
 .phone{position:relative;inset:auto;transform:none;margin:0;width:100%;max-width:none;height:100%!important;min-height:0;aspect-ratio:auto;padding:0;border:0;border-radius:28px;overflow:hidden;background:none;box-shadow:0 40px 90px -30px #2b1440b3}
 .phone::before,.phone::after{display:none!important}
 .phone .scr{height:100%;border-radius:28px;padding:0 32px}
 .atabs{order:-1;margin:0 -32px!important;padding:14px 24px!important;display:flex!important;justify-content:center;gap:6px!important;border-top:0!important;border-bottom:1px solid var(--a-soft);background:color-mix(in srgb,var(--a-bg) 70%,#000)!important}
 .atab{flex-direction:row!important;gap:8px!important;font-size:14px!important;padding:10px 18px!important;border-radius:999px;white-space:nowrap}
 .atab svg{width:20px!important;height:20px!important}
 .atab:hover{color:var(--a-ink)}.atab.on{background:#ffffff14}
 .as{width:100%;max-width:560px!important;margin:0 auto!important;align-self:center;padding:20px 2px 28px;zoom:1.25}
 .as[data-s=today]{overflow-y:auto}
 .as[data-s=today] .acard:has(#a-bars){flex:none!important;max-height:none!important}
 .as[data-s=today] .bars{flex:none!important;height:84px!important}
 .as[data-s=cycle] .acard:has(#cal){flex:none!important}
 .as[data-s=cycle] .cal{grid-auto-rows:auto!important}
 .as[data-s=cycle] .cal button{height:auto!important;width:min(100%,40px)!important}
 .sheet .shc{max-width:520px;margin:0 auto;zoom:1.15}
 #inst{display:none!important}
}
@media (min-width:1500px) and (min-height:860px){.as{zoom:1.4}}
.splash{position:fixed;inset:0;z-index:50;background:radial-gradient(60% 40% at 50% 48%,#3E2F5C,#231A36);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;transition:opacity .45s ease,visibility .45s}
.splash svg{width:112px;height:112px;overflow:visible;transform:translateY(-14px)}
.splash path{stroke-dasharray:100;stroke-dashoffset:100;animation:spdraw 1.1s cubic-bezier(.4,0,.2,1) forwards;animation-delay:calc(var(--i)*.12s)}
@keyframes spdraw{to{stroke-dashoffset:0}}
.splash b{font:800 26px Manrope,sans-serif;letter-spacing:-.02em;color:#F4EEFF;opacity:0;transform:translateY(8px);animation:spin .5s ease .7s forwards}
@keyframes spin{to{opacity:1;transform:none}}
.splash.out{opacity:0;visibility:hidden}
.splash{animation:spsafe .4s ease 5s forwards}@keyframes spsafe{to{opacity:0;visibility:hidden}}
@media (prefers-reduced-motion:reduce){.splash path{animation:none;stroke-dashoffset:0}.splash b{animation:none;opacity:1;transform:none}}
</style>'''
inst_js=r'''
/* язык из сайта (тот же localStorage) */
function setLang(l){lang=l;document.documentElement.lang=l==='kz'?'kk':'ru';
  document.querySelectorAll('[data-kz]').forEach(el=>{if(el.dataset.ru===undefined)el.dataset.ru=el.innerHTML;el.innerHTML=l==='kz'?el.dataset.kz:el.dataset.ru});
  setMode(mode);appRender();instText();document.querySelector('.av').textContent=l==='kz'?'KZ':'RU';try{localStorage.setItem('lang',l)}catch(e){}}
document.querySelector('.av').title='RU / KZ';
document.querySelector('.av').onclick=()=>setLang(lang==='ru'?'kz':'ru');
/* установка на экран «Домой» */
const standalone=matchMedia('(display-mode: standalone)').matches||navigator.standalone;
const ios=/iphone|ipad|ipod/i.test(navigator.userAgent);
let dp=null;
function instText(){document.getElementById('inst-t').textContent=dp?T('Иконка появится на экране телефона, без App Store','Белгіше телефон экранында пайда болады, App Store қажет емес'):ios?T('Нажмите «Поделиться» внизу Safari, затем «На экран Домой»','Safari төменгі «Бөлісу» батырмасын, сосын «Басты экранға» басыңыз'):T('Откройте меню браузера ⋮ и выберите «Добавить на главный экран»','Браузер мәзірін ⋮ ашып, «Басты экранға қосу» таңдаңыз')}
/* при входе: сразу предлагаем добавить на экран «Домой», после установки – напоминание */
function welcomeSheet(){const scr=document.querySelector('.phone .scr');if(!scr||document.getElementById('sh-in'))return;
  const s=document.createElement('div');s.className='sheet';s.id='sh-in';
  const step=(n,ic,tx)=>'<div class="ist"><span class="isn">'+n+'</span><span class="mi">'+ic+'</span><span>'+tx+'</span></div>';
  const share='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="9" width="14" height="12" rx="3" fill="url(#mg)"/><path d="M12 3v10M8.6 6.2L12 3l3.4 3.2" stroke="url(#mg)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M12 9v4" stroke="#3E2F5C" stroke-opacity=".45" stroke-width="2" stroke-linecap="round"/></svg>';
  const plus='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5" fill="url(#mg)"/><path d="M12 8v8M8 12h8" stroke="#3E2F5C" stroke-opacity=".45" stroke-width="2.2" stroke-linecap="round"/></svg>';
  const dots='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.6" fill="url(#mg)"/><circle cx="12" cy="7.8" r="1.5" fill="#3E2F5C" opacity=".5"/><circle cx="12" cy="12" r="1.5" fill="#3E2F5C" opacity=".5"/><circle cx="12" cy="16.2" r="1.5" fill="#3E2F5C" opacity=".5"/></svg>';
  let body;
  if(dp)body='<button class="abtn" id="in-go">'+T('Добавить на экран','Экранға қосу')+'</button>';
  else if(ios)body='<div class="acard isteps">'+step(1,share,T('Нажмите «Поделиться» внизу Safari','Safari төменіндегі «Бөлісу» батырмасын басыңыз'))+step(2,plus,T('Выберите «На экран Домой»','«Басты экранға» таңдаңыз'))+'</div>';
  else body='<div class="acard isteps">'+step(1,dots,T('Откройте меню браузера ⋮','Браузер мәзірін ⋮ ашыңыз'))+step(2,plus,T('Выберите «Добавить на главный экран»','«Басты экранға қосу» таңдаңыз'))+'</div>';
  s.innerHTML='<div class="shc"><span class="mi big">'+mic('petal')+'</span><h3>'+T('Добавьте Тонус на экран','Тонусты экранға қосыңыз')+'</h3><p>'+T('Откроется как приложение, без App Store и регистрации. Так проще не пропускать 5 минут в день','App Store-сыз әрі тіркеусіз қосымша ретінде ашылады. Күніне 5 минутты өткізіп алмау оңайырақ')+'</p>'+body+'<button class="abtn ghost" id="in-x">'+T('Позже','Кейін')+'</button></div>';
  scr.appendChild(s);typo(s);
  const go=document.getElementById('in-go');if(go)go.onclick=async()=>{if(!dp)return;dp.prompt();await dp.userChoice;dp=null;s.remove()};
  document.getElementById('in-x').onclick=()=>{s.remove();try{sessionStorage.setItem('in_x','1')}catch(e){}}}
function remSheet(){if(ls.get('pf_rem',null)||ls.get('pf_rem_asked',false))return;ls.set('pf_rem_asked',true);go('club');
  setTimeout(()=>{const c=document.querySelector('.as[data-s=club] .ccard:nth-of-type(3)');if(c){c.classList.add('hl');c.scrollIntoView({block:'center',behavior:'smooth'})}},300)}
let inSkip=false;try{inSkip=sessionStorage.getItem('in_x')==='1'}catch(e){}
const wide=matchMedia('(min-width:900px)').matches;
setTimeout(()=>{if(wide)return;if(!standalone){if(!inSkip)welcomeSheet()}else remSheet()},1900);
addEventListener('beforeinstallprompt',e=>{e.preventDefault();dp=e;instText();const s=document.getElementById('sh-in');if(s){s.remove();welcomeSheet()}});
document.getElementById('inst-b').onclick=async()=>{if(!dp)return;dp.prompt();await dp.userChoice;dp=null;document.getElementById('inst').hidden=true};
document.getElementById('inst-h').onclick=()=>{const t=document.getElementById('inst-t');t.hidden=!t.hidden};
document.getElementById('inst-x').onclick=()=>{document.getElementById('inst').hidden=true;ls.set('pf_inst_x',true)};
if('serviceWorker' in navigator)navigator.serviceWorker.register('/app/sw.js',{scope:'/app/'}).catch(()=>{});
let start='ru';try{start=localStorage.getItem('lang')||'ru'}catch(e){}
setLang(start);
'''+"\n/* заставка при входе: лепесток рисуется, затем плавно исчезает */\n(()=>{const sp=document.getElementById('splash');if(!sp)return;let skip=false;try{skip=sessionStorage.getItem('ptr')==='1';sessionStorage.removeItem('ptr')}catch(e){}\n if(skip){sp.remove();return}const t0=performance.now();const hide=()=>{const w=Math.max(0,1500-(performance.now()-t0));setTimeout(()=>{sp.classList.add('out');setTimeout(()=>sp.remove(),500)},w)};\n if(document.readyState==='complete')hide();else addEventListener('load',hide);setTimeout(()=>sp&&sp.classList.add('out'),4000)})();\n"+"\n/* обновление свайпом вниз */\n(()=>{const el=document.getElementById('ptr');let y0=null,dy=0,busy=false;const TH=70;\nconst cur=()=>document.querySelector('.as.on');\naddEventListener('touchstart',e=>{if(busy||e.touches.length!==1)return;const a=cur();if(a&&a.scrollTop>0)return;if(scrollY>0)return;y0=e.touches[0].clientY;dy=0;el.classList.remove('back')},{passive:true});\naddEventListener('touchmove',e=>{if(y0===null)return;dy=Math.max(0,e.touches[0].clientY-y0);if(dy<=0)return;const d=Math.min(dy*.5,TH+20);el.style.transform='translateY('+(d-60)+'px)';el.style.opacity=Math.min(1,d/40);el.style.setProperty('--p',Math.min(1,d/TH))},{passive:true});\naddEventListener('touchend',()=>{if(y0===null)return;y0=null;el.classList.add('back');\n if(dy*.5>=TH){busy=true;el.style.transform='translateY(16px)';el.style.opacity=1;el.classList.add('go');if(navigator.vibrate)navigator.vibrate(8);try{sessionStorage.setItem('ptr','1')}catch(e){};setTimeout(()=>location.reload(),900)}\n else{el.style.transform='';el.style.opacity=0}});\n})();\n"+open('tools/lock.js',encoding='utf-8').read()
L_def="const L=a=>lang==='kz'?a[1]:a[0];\n"
html=f'''<!doctype html>
<html lang="ru"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Тонус</title>
<meta name="description" content="Упражнения для мышц тазового дна, дневник цикла и советы врача. Анонимно, без регистрации.">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#2B2140">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="apple-mobile-web-app-title" content="Тонус">
<link rel="manifest" href="/app/manifest.webmanifest">
<link rel="icon" href="/media/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/media/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap">
{styles}{extra}
</head><body>
<div class="splash" id="splash" aria-hidden="true"><svg viewBox="10 10 80 80" fill="none" stroke="url(#spg)" stroke-width="1.6" stroke-linecap="round"><defs><linearGradient id="spg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C9B4F5"/><stop offset="1" stop-color="#F2A6C9"/></linearGradient></defs><path pathLength="100" style="--i:0" d="M50 18 C80 37.84 75.5 72.56 50 80 C24.5 72.56 20 37.84 50 18Z"/><path pathLength="100" style="--i:1" d="M50 24 C74 41.92 70.4 73.28 50 80 C29.6 73.28 26 41.92 50 24Z"/><path pathLength="100" style="--i:2" d="M50 30 C68 46 65.3 74 50 80 C34.7 74 32 46 50 30Z"/><path pathLength="100" style="--i:3" d="M50 36 C62 50.08 60.2 74.72 50 80 C39.8 74.72 38 50.08 50 36Z"/><path pathLength="100" style="--i:4" d="M50 42 C56 54.16 55.1 75.44 50 80 C44.9 75.44 44 54.16 50 42Z"/></svg></div>
<aside class="desk" data-nolock aria-label="О тренажёре">
<svg class="dlogo" viewBox="0 0 100 100" aria-hidden="true"><defs><linearGradient id="dlg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9B7BE0"/><stop offset="1" stop-color="#F2A6C9"/></linearGradient></defs><rect width="100" height="100" rx="22.5" fill="url(#dlg)"/><g fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round" transform="translate(50 51) scale(1.12) translate(-50 -49)"><path opacity="1" d="M50 18 C80 37.84 75.5 72.56 50 80 C24.5 72.56 20 37.84 50 18Z"/><path opacity="0.85" d="M50 24 C74 41.92 70.4 73.28 50 80 C29.6 73.28 26 41.92 50 24Z"/><path opacity="0.7" d="M50 30 C68 46.0 65.3 74.0 50 80 C34.7 74.0 32 46.0 50 30Z"/><path opacity="0.55" d="M50 36 C62 50.08 60.2 74.72 50 80 C39.8 74.72 38 50.08 50 36Z"/><path opacity="0.4" d="M50 42 C56 54.16 55.1 75.44 50 80 C44.9 75.44 44 54.16 50 42Z"/></g></svg>
<h1 data-kz="Тонус – жамбас түбі бұлшықеттеріне арналған жаттықтырғыш">Тонус – тренажёр мышц тазового дна</h1>
<p data-kz="Күніне 5 минут, 21 күн. Тегін, анонимді, тіркеусіз. Прогресс тек сіздің құрылғыңызда сақталады.">5 минут в день, 21 день. Бесплатно, анонимно, без регистрации. Прогресс хранится только на вашем устройстве.</p>
<div class="qr"><svg viewBox="0 0 29 29" shape-rendering="crispEdges"><path fill="#2A2140" d="M0 0h1v1h-1zM1 0h1v1h-1zM2 0h1v1h-1zM3 0h1v1h-1zM4 0h1v1h-1zM5 0h1v1h-1zM6 0h1v1h-1zM8 0h1v1h-1zM11 0h1v1h-1zM15 0h1v1h-1zM16 0h1v1h-1zM18 0h1v1h-1zM20 0h1v1h-1zM22 0h1v1h-1zM23 0h1v1h-1zM24 0h1v1h-1zM25 0h1v1h-1zM26 0h1v1h-1zM27 0h1v1h-1zM28 0h1v1h-1zM0 1h1v1h-1zM6 1h1v1h-1zM9 1h1v1h-1zM10 1h1v1h-1zM11 1h1v1h-1zM12 1h1v1h-1zM13 1h1v1h-1zM14 1h1v1h-1zM16 1h1v1h-1zM17 1h1v1h-1zM18 1h1v1h-1zM20 1h1v1h-1zM22 1h1v1h-1zM28 1h1v1h-1zM0 2h1v1h-1zM2 2h1v1h-1zM3 2h1v1h-1zM4 2h1v1h-1zM6 2h1v1h-1zM8 2h1v1h-1zM10 2h1v1h-1zM11 2h1v1h-1zM14 2h1v1h-1zM15 2h1v1h-1zM16 2h1v1h-1zM17 2h1v1h-1zM18 2h1v1h-1zM19 2h1v1h-1zM20 2h1v1h-1zM22 2h1v1h-1zM24 2h1v1h-1zM25 2h1v1h-1zM26 2h1v1h-1zM28 2h1v1h-1zM0 3h1v1h-1zM2 3h1v1h-1zM3 3h1v1h-1zM4 3h1v1h-1zM6 3h1v1h-1zM9 3h1v1h-1zM10 3h1v1h-1zM12 3h1v1h-1zM14 3h1v1h-1zM17 3h1v1h-1zM18 3h1v1h-1zM22 3h1v1h-1zM24 3h1v1h-1zM25 3h1v1h-1zM26 3h1v1h-1zM28 3h1v1h-1zM0 4h1v1h-1zM2 4h1v1h-1zM3 4h1v1h-1zM4 4h1v1h-1zM6 4h1v1h-1zM9 4h1v1h-1zM10 4h1v1h-1zM13 4h1v1h-1zM14 4h1v1h-1zM15 4h1v1h-1zM18 4h1v1h-1zM22 4h1v1h-1zM24 4h1v1h-1zM25 4h1v1h-1zM26 4h1v1h-1zM28 4h1v1h-1zM0 5h1v1h-1zM6 5h1v1h-1zM8 5h1v1h-1zM9 5h1v1h-1zM11 5h1v1h-1zM15 5h1v1h-1zM17 5h1v1h-1zM22 5h1v1h-1zM28 5h1v1h-1zM0 6h1v1h-1zM1 6h1v1h-1zM2 6h1v1h-1zM3 6h1v1h-1zM4 6h1v1h-1zM5 6h1v1h-1zM6 6h1v1h-1zM8 6h1v1h-1zM10 6h1v1h-1zM12 6h1v1h-1zM14 6h1v1h-1zM16 6h1v1h-1zM18 6h1v1h-1zM20 6h1v1h-1zM22 6h1v1h-1zM23 6h1v1h-1zM24 6h1v1h-1zM25 6h1v1h-1zM26 6h1v1h-1zM27 6h1v1h-1zM28 6h1v1h-1zM9 7h1v1h-1zM10 7h1v1h-1zM11 7h1v1h-1zM14 7h1v1h-1zM15 7h1v1h-1zM16 7h1v1h-1zM18 7h1v1h-1zM19 7h1v1h-1zM20 7h1v1h-1zM0 8h1v1h-1zM2 8h1v1h-1zM6 8h1v1h-1zM7 8h1v1h-1zM10 8h1v1h-1zM12 8h1v1h-1zM13 8h1v1h-1zM14 8h1v1h-1zM19 8h1v1h-1zM23 8h1v1h-1zM26 8h1v1h-1zM28 8h1v1h-1zM4 9h1v1h-1zM8 9h1v1h-1zM10 9h1v1h-1zM11 9h1v1h-1zM12 9h1v1h-1zM13 9h1v1h-1zM14 9h1v1h-1zM17 9h1v1h-1zM18 9h1v1h-1zM19 9h1v1h-1zM20 9h1v1h-1zM21 9h1v1h-1zM22 9h1v1h-1zM23 9h1v1h-1zM27 9h1v1h-1zM28 9h1v1h-1zM0 10h1v1h-1zM1 10h1v1h-1zM3 10h1v1h-1zM6 10h1v1h-1zM7 10h1v1h-1zM9 10h1v1h-1zM12 10h1v1h-1zM15 10h1v1h-1zM18 10h1v1h-1zM19 10h1v1h-1zM21 10h1v1h-1zM22 10h1v1h-1zM23 10h1v1h-1zM25 10h1v1h-1zM26 10h1v1h-1zM28 10h1v1h-1zM1 11h1v1h-1zM3 11h1v1h-1zM4 11h1v1h-1zM9 11h1v1h-1zM10 11h1v1h-1zM11 11h1v1h-1zM13 11h1v1h-1zM19 11h1v1h-1zM20 11h1v1h-1zM22 11h1v1h-1zM23 11h1v1h-1zM24 11h1v1h-1zM25 11h1v1h-1zM3 12h1v1h-1zM6 12h1v1h-1zM7 12h1v1h-1zM8 12h1v1h-1zM10 12h1v1h-1zM12 12h1v1h-1zM13 12h1v1h-1zM15 12h1v1h-1zM16 12h1v1h-1zM18 12h1v1h-1zM20 12h1v1h-1zM22 12h1v1h-1zM23 12h1v1h-1zM28 12h1v1h-1zM0 13h1v1h-1zM1 13h1v1h-1zM3 13h1v1h-1zM4 13h1v1h-1zM5 13h1v1h-1zM9 13h1v1h-1zM10 13h1v1h-1zM11 13h1v1h-1zM16 13h1v1h-1zM17 13h1v1h-1zM19 13h1v1h-1zM20 13h1v1h-1zM21 13h1v1h-1zM22 13h1v1h-1zM27 13h1v1h-1zM28 13h1v1h-1zM0 14h1v1h-1zM2 14h1v1h-1zM3 14h1v1h-1zM4 14h1v1h-1zM6 14h1v1h-1zM7 14h1v1h-1zM8 14h1v1h-1zM9 14h1v1h-1zM13 14h1v1h-1zM14 14h1v1h-1zM16 14h1v1h-1zM19 14h1v1h-1zM20 14h1v1h-1zM22 14h1v1h-1zM28 14h1v1h-1zM1 15h1v1h-1zM2 15h1v1h-1zM5 15h1v1h-1zM8 15h1v1h-1zM10 15h1v1h-1zM12 15h1v1h-1zM14 15h1v1h-1zM15 15h1v1h-1zM16 15h1v1h-1zM18 15h1v1h-1zM20 15h1v1h-1zM21 15h1v1h-1zM23 15h1v1h-1zM1 16h1v1h-1zM2 16h1v1h-1zM3 16h1v1h-1zM6 16h1v1h-1zM7 16h1v1h-1zM8 16h1v1h-1zM9 16h1v1h-1zM11 16h1v1h-1zM13 16h1v1h-1zM14 16h1v1h-1zM19 16h1v1h-1zM22 16h1v1h-1zM28 16h1v1h-1zM1 17h1v1h-1zM2 17h1v1h-1zM4 17h1v1h-1zM7 17h1v1h-1zM9 17h1v1h-1zM10 17h1v1h-1zM13 17h1v1h-1zM14 17h1v1h-1zM19 17h1v1h-1zM20 17h1v1h-1zM21 17h1v1h-1zM22 17h1v1h-1zM23 17h1v1h-1zM26 17h1v1h-1zM27 17h1v1h-1zM28 17h1v1h-1zM0 18h1v1h-1zM1 18h1v1h-1zM2 18h1v1h-1zM3 18h1v1h-1zM4 18h1v1h-1zM6 18h1v1h-1zM9 18h1v1h-1zM11 18h1v1h-1zM12 18h1v1h-1zM15 18h1v1h-1zM17 18h1v1h-1zM18 18h1v1h-1zM19 18h1v1h-1zM21 18h1v1h-1zM25 18h1v1h-1zM28 18h1v1h-1zM2 19h1v1h-1zM5 19h1v1h-1zM12 19h1v1h-1zM13 19h1v1h-1zM18 19h1v1h-1zM22 19h1v1h-1zM23 19h1v1h-1zM0 20h1v1h-1zM1 20h1v1h-1zM4 20h1v1h-1zM6 20h1v1h-1zM8 20h1v1h-1zM9 20h1v1h-1zM10 20h1v1h-1zM13 20h1v1h-1zM15 20h1v1h-1zM16 20h1v1h-1zM19 20h1v1h-1zM20 20h1v1h-1zM21 20h1v1h-1zM22 20h1v1h-1zM23 20h1v1h-1zM24 20h1v1h-1zM25 20h1v1h-1zM27 20h1v1h-1zM8 21h1v1h-1zM9 21h1v1h-1zM10 21h1v1h-1zM16 21h1v1h-1zM18 21h1v1h-1zM20 21h1v1h-1zM24 21h1v1h-1zM25 21h1v1h-1zM26 21h1v1h-1zM28 21h1v1h-1zM0 22h1v1h-1zM1 22h1v1h-1zM2 22h1v1h-1zM3 22h1v1h-1zM4 22h1v1h-1zM5 22h1v1h-1zM6 22h1v1h-1zM8 22h1v1h-1zM10 22h1v1h-1zM11 22h1v1h-1zM12 22h1v1h-1zM13 22h1v1h-1zM14 22h1v1h-1zM16 22h1v1h-1zM17 22h1v1h-1zM18 22h1v1h-1zM20 22h1v1h-1zM22 22h1v1h-1zM24 22h1v1h-1zM28 22h1v1h-1zM0 23h1v1h-1zM6 23h1v1h-1zM10 23h1v1h-1zM11 23h1v1h-1zM12 23h1v1h-1zM14 23h1v1h-1zM15 23h1v1h-1zM16 23h1v1h-1zM19 23h1v1h-1zM20 23h1v1h-1zM24 23h1v1h-1zM28 23h1v1h-1zM0 24h1v1h-1zM2 24h1v1h-1zM3 24h1v1h-1zM4 24h1v1h-1zM6 24h1v1h-1zM11 24h1v1h-1zM12 24h1v1h-1zM13 24h1v1h-1zM14 24h1v1h-1zM16 24h1v1h-1zM19 24h1v1h-1zM20 24h1v1h-1zM21 24h1v1h-1zM22 24h1v1h-1zM23 24h1v1h-1zM24 24h1v1h-1zM25 24h1v1h-1zM0 25h1v1h-1zM2 25h1v1h-1zM3 25h1v1h-1zM4 25h1v1h-1zM6 25h1v1h-1zM9 25h1v1h-1zM10 25h1v1h-1zM12 25h1v1h-1zM13 25h1v1h-1zM14 25h1v1h-1zM18 25h1v1h-1zM19 25h1v1h-1zM21 25h1v1h-1zM23 25h1v1h-1zM24 25h1v1h-1zM25 25h1v1h-1zM26 25h1v1h-1zM27 25h1v1h-1zM0 26h1v1h-1zM2 26h1v1h-1zM3 26h1v1h-1zM4 26h1v1h-1zM6 26h1v1h-1zM8 26h1v1h-1zM10 26h1v1h-1zM14 26h1v1h-1zM15 26h1v1h-1zM17 26h1v1h-1zM18 26h1v1h-1zM21 26h1v1h-1zM24 26h1v1h-1zM27 26h1v1h-1zM28 26h1v1h-1zM0 27h1v1h-1zM6 27h1v1h-1zM11 27h1v1h-1zM13 27h1v1h-1zM14 27h1v1h-1zM15 27h1v1h-1zM16 27h1v1h-1zM20 27h1v1h-1zM22 27h1v1h-1zM23 27h1v1h-1zM24 27h1v1h-1zM25 27h1v1h-1zM0 28h1v1h-1zM1 28h1v1h-1zM2 28h1v1h-1zM3 28h1v1h-1zM4 28h1v1h-1zM5 28h1v1h-1zM6 28h1v1h-1zM8 28h1v1h-1zM9 28h1v1h-1zM10 28h1v1h-1zM12 28h1v1h-1zM14 28h1v1h-1zM16 28h1v1h-1zM18 28h1v1h-1zM20 28h1v1h-1zM22 28h1v1h-1zM24 28h1v1h-1zM28 28h1v1h-1z"/></svg><span data-kz="Телефон камерасымен сканерлеңіз – жаттықтырғыш телефонда ашылады">Наведите камеру телефона – тренажёр откроется у вас в телефоне</span></div>
<a href="/" data-kz="← Дәрігер Рузиматованың сайты">← Сайт доктора Рузиматовой</a>
</aside>
<div class="ptr" id="ptr" aria-hidden="true"><svg viewBox="10 10 80 80" fill="none" stroke="url(#ptrg)" stroke-width="3" stroke-linecap="round"><defs><linearGradient id="ptrg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C9B4F5"/><stop offset="1" stop-color="#F2A6C9"/></linearGradient></defs><path pathLength="100" style="--i:0" d="M50 18 C80 37.84 75.5 72.56 50 80 C24.5 72.56 20 37.84 50 18Z"/><path pathLength="100" style="--i:1" d="M50 24 C74 41.92 70.4 73.28 50 80 C29.6 73.28 26 41.92 50 24Z"/><path pathLength="100" style="--i:2" d="M50 30 C68 46 65.3 74 50 80 C34.7 74 32 46 50 30Z"/><path pathLength="100" style="--i:3" d="M50 36 C62 50.08 60.2 74.72 50 80 C39.8 74.72 38 50.08 50 36Z"/><path pathLength="100" style="--i:4" d="M50 42 C56 54.16 55.1 75.44 50 80 C44.9 75.44 44 54.16 50 42Z"/></svg></div>
{phone}
<script>{head_js}{L_def}{app_js}{inst_js}</script>
</body></html>'''
open('app/index.html','w',encoding='utf-8').write(html)
print(len(html))
