// Счётчики посещений в Upstash Redis (Vercel Storage → Upstash for Redis). Без IP, имён и телефонов – только общие цифры.
const cfg = () => {
  const u = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
  const t = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  return u && t ? { u: u.replace(/\/$/, ''), t } : null;
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
