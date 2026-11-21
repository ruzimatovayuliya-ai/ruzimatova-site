// Статистика посещений для кабинета: только по паролю кабинета.
import { checkKey } from './_store.js';
import { statsReady, redis, day, hash } from './_stats.js';
export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  let b = req.body; if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  b = b || {};
  if (!checkKey(b.key)) { await new Promise(r => setTimeout(r, 600)); return res.status(401).json({ ok: false }); }
  if (!statsReady()) return res.json({ ok: true, configured: false });
  // период: последние N дней (1 = сегодня) или свои даты from–to (YYYY-MM-DD, до 92 дней)
  const re = /^\d{4}-\d{2}-\d{2}$/; let days = [];
  if (re.test(b.from || '') && re.test(b.to || '')) {
    let a = Date.parse(b.from + 'T00:00:00Z'), z = Date.parse(b.to + 'T00:00:00Z'); if (a > z) [a, z] = [z, a];
    for (let t = a; t <= z && days.length < 92; t += 864e5) days.push(new Date(t).toISOString().slice(0, 10));
  } else {
    const n = Math.min(90, Math.max(1, parseInt(b.days, 10) || 30));
    for (let i = n - 1; i >= 0; i--) days.push(day(Date.now() - i * 864e5));
  }
  const n = days.length;
  const H = ['d', 'g', 'c', 'dv', 'src', 'sec', 'ex', 'art', 'vid', 'test'];
  const cmds = [];
  for (const d of days) { for (const k of H) cmds.push(['HGETALL', k + ':' + d]); cmds.push(['PFCOUNT', 'u:' + d + ':site'], ['PFCOUNT', 'u:' + d + ':app']); }
  cmds.push(['PFCOUNT', ...days.map(d => 'u:' + d + ':site')], ['PFCOUNT', ...days.map(d => 'u:' + d + ':app')], ['PFCOUNT', ...days.map(d => 'u:' + d + ':all')], ['PFCOUNT', ...days.map(d => 'pw:' + d)]);
  try {
    const r = await redis(cmds); let i = 0; const per = [], sum = {};
    for (const d of days) {
      const o = { d };
      for (const k of H) { o[k] = hash(r[i++]); if (k !== 'd') { sum[k] = sum[k] || {}; for (const [a, v] of Object.entries(o[k])) sum[k][a] = (sum[k][a] || 0) + v; } }
      o.us = r[i++] || 0; o.ua = r[i++] || 0; per.push({ d, us: o.us, ua: o.ua, vs: o.d['view:site'] || 0, va: o.d['view:app'] || 0 });
      sum.d = sum.d || {}; for (const [a, v] of Object.entries(o.d)) sum.d[a] = (sum.d[a] || 0) + v;
    }
    const uniq = { site: r[i++] || 0, app: r[i++] || 0, all: r[i++] || 0, pwa: r[i++] || 0 };
    return res.json({ ok: true, configured: true, days: n, per, sum, uniq });
  } catch (e) { console.error('stats', e && e.message); return res.status(500).json({ ok: false }); }
}
