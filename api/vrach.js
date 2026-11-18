// Закрытые действия врача: список вопросов, ответ, публикация, удаление.
import { ready, checkKey, allQuestions, getQuestion, saveQuestion, deleteQuestion, rebuildAnswers, clean } from './_store.js';
export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  let b = req.body; if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  b = b || {};
  if (!checkKey(b.key)) { await new Promise(r => setTimeout(r, 600)); return res.status(401).json({ ok: false, error: 'key' }); }
  if (!ready()) return res.status(503).json({ ok: false, error: 'not_configured' });
  try {
    if (b.action === 'list') return res.json({ ok: true, items: await allQuestions() });
    if (b.action === 'save' || b.action === 'publish' || b.action === 'hide') {
      const it = await getQuestion(String(b.id || ''));
      if (!it) return res.status(404).json({ ok: false });
      if (b.a !== undefined) it.a = clean(b.a, 6000);
      if (b.aq !== undefined) it.aq = clean(b.aq, 2000);
      if (b.action === 'publish') { if (!it.a) return res.status(400).json({ ok: false, error: 'empty' }); it.status = 'published'; }
      if (b.action === 'hide') it.status = 'hidden';
      if (b.action === 'save' && it.status === 'new' && it.a) it.status = 'draft';
      await saveQuestion(it);
      if (b.action !== 'save' || it.status === 'published') await rebuildAnswers();
      return res.json({ ok: true, item: it });
    }
    if (b.action === 'delete') { await deleteQuestion(String(b.id || '')); await rebuildAnswers(); return res.json({ ok: true }); }
    return res.status(400).json({ ok: false });
  } catch (e) { console.error('vrach', e && e.message); return res.status(500).json({ ok: false }); }
}
