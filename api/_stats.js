// Счётчики посещений в Upstash Redis (Vercel Storage → Upstash for Redis). Без IP, имён и телефонов – только общие цифры.
// Переменные могут прийти с любой приставкой (KV_, STORAGE_KV_, UPSTASH_REDIS_ и т.п.) – ищем пару «…_REST_API_URL/TOKEN» или «…_REST_URL/TOKEN»
const cfg = () => {
  const e = process.env;
  const u0 = e.KV_REST_API_URL || e.UPSTASH_REDIS_REST_URL;
  const t0 = e.KV_REST_API_TOKEN || e.UPSTASH_REDIS_REST_TOKEN;
  if (u0 && t0) return { u: u0.replace(/\/$/, ''), t: t0 };
  for (const k of Object.keys(e)) {
    const m = k.match(/^(.*)_(KV_REST_API|REDIS_REST)_URL$/);
    if (!m) continue;
    const t = e[m[1] + '_' + m[2] + '_TOKEN'];
    if (e[k] && t && /^https:/.test(e[k])) return { u: e[k].replace(/\/$/, ''), t };
  }
  return null;
};
export const statsReady = () => !!cfg();
export async function redis(cmds) {
  const c = cfg(); if (!c || !cmds.length) return null;
  const r = await fetch(c.u + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + c.t, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) });
  if (!r.ok) throw new Error('redis ' + r.status);
  return (await r.json()).map(x => x.result);
}
// день по времени Алматы (UTC+5)
export const day = (ms = Date.now()) => new Date(ms + 5 * 3600e3).toISOString().slice(0, 10);
export const hash = a => { const o = {}; if (Array.isArray(a)) for (let i = 0; i < a.length; i += 2) o[a[i]] = +a[i + 1]; return o; };
