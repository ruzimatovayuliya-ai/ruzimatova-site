// Ответы на свои вопросы: телефон присылает номера своих вопросов, получает ответы врача (лично или опубликованные).
import { ready, mine } from './_store.js';
export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  if (!ready()) return res.status(200).json({ ok: true, items: [] });
  let b = req.body; if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  const ids = (Array.isArray(b && b.ids) ? b.ids : []).map(String).filter(x => /^\d{10,16}-[0-9a-f]{8}$/.test(x)).slice(0, 20);
  try { return res.status(200).json({ ok: true, items: await mine(ids) }); }
  catch (e) { console.error('mine', e && e.message); return res.status(500).json({ ok: false }); }
}
