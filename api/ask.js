// Приём анонимного вопроса: без имени, телефона и IP.
import { ready, via, check, addQuestion, clean } from './_store.js';
export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  // GET /api/ask – самопроверка: подключено ли хранилище (без секретов и без записи)
  if (req.method === 'GET') return res.status(200).json({ configured: ready(), via: via(), store: ready() ? await check() : null });
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  if (!ready()) return res.status(503).json({ ok: false, error: 'not_configured' });
  let b = req.body; if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  b = b || {};
  if (b.website) return res.status(200).json({ ok: true }); // ловушка для ботов
  const q = clean(b.q, 2000);
  if (q.length < 10) return res.status(400).json({ ok: false, error: 'short' });
  const lang = b.lang === 'kz' ? 'kz' : 'ru';
  const src = b.src === 'app' ? 'app' : 'site';
  try { const id = await addQuestion({ q, lang, src }); return res.status(200).json({ ok: true, id }); }
  catch (e) { console.error('ask', e && e.message); return res.status(500).json({ ok: false, error: 'store', detail: String(e && e.message || e).slice(0, 200) }); }
}
