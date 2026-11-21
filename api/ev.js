// Приём событий посещения: просмотр, время, разделы, упражнения, статьи, видео, тест. Город и страна – из заголовков Vercel, IP не хранится.
import { statsReady, redis, day } from './_stats.js';
const T = new Set(['view', 'time', 'sec', 'ex', 'art', 'vid', 'test', 'wa']);
export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST' || !statsReady()) return res.status(204).end();
  let b = req.body; if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  b = b || {};
  const t = String(b.t || ''), p = b.p === 'app' ? 'app' : 'site', v = /^[a-z0-9]{4,16}$/.test(b.v || '') ? b.v : '';
  const x = String(b.x || '').toLowerCase().replace(/[^a-z0-9_-]/g, '').slice(0, 24);
  if (!T.has(t)) return res.status(204).end();
  const d = day(), h = req.headers || {}, cmds = [];
  if (t === 'view') {
    cmds.push(['HINCRBY', 'd:' + d, 'view:' + p, 1]);
    cmds.push(['HINCRBY', 'src:' + d, x || 'direct', 1]);
    if (v) cmds.push(['PFADD', 'u:' + d + ':' + p, v], ['PFADD', 'u:' + d + ':all', v]);
    let cc = String(h['x-vercel-ip-country'] || '').slice(0, 2), city = '';
    try { city = decodeURIComponent(String(h['x-vercel-ip-city'] || '')).slice(0, 40) } catch (e) { }
    if (cc) cmds.push(['HINCRBY', 'g:' + d, cc, 1]);
    if (city) cmds.push(['HINCRBY', 'c:' + d, (cc ? cc + ' ' : '') + city, 1]);
    const ua = String(h['user-agent'] || ''); const dev = /iPhone|iPad|iPod/.test(ua) ? 'iPhone' : /Android/.test(ua) ? 'Android' : 'компьютер';
    cmds.push(['HINCRBY', 'dv:' + d, dev, 1]);
    if (p === 'app' && b.sa && v) cmds.push(['PFADD', 'pw:' + d, v]);
  } else if (t === 'time') {
    const n = Math.min(3600, Math.max(0, parseInt(b.x, 10) || 0));
    if (n) cmds.push(['HINCRBY', 'd:' + d, 'sec:' + p, n], ['HINCRBY', 'd:' + d, 'sess:' + p, 1]);
  } else if (t === 'wa') cmds.push(['HINCRBY', 'd:' + d, 'wa:' + p, 1]);
  else if (x) cmds.push(['HINCRBY', t + ':' + d, x, 1]);
  try { await redis(cmds); } catch (e) { console.error('ev', e && e.message); }
  return res.status(204).end();
}
