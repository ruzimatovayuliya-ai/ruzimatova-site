// Закрытые действия врача: список вопросов, ответ, публикация, удаление.
import { ready, checkKey, role, allQuestions, getQuestion, saveQuestion, deleteQuestion, rebuildAnswers, clean } from './_store.js';
export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  let b = req.body; if (typeof b === 'string') { try { b = JSON.parse(b) } catch (e) { b = {} } }
  b = b || {};
  if (!checkKey(b.key)) { await new Promise(r => setTimeout(r, 600)); return res.status(401).json({ ok: false, error: 'key' }); }
  if (!ready()) return res.status(503).json({ ok: false, error: 'not_configured' });
  try {
    if (b.action === 'list') return res.json({ ok: true, role: role(b.key), items: await allQuestions() });
    if (['save', 'reply', 'app', 'site', 'hide', 'publish'].includes(b.action)) {
      const it = await getQuestion(String(b.id || ''));
      if (!it) return res.status(404).json({ ok: false });
      if (b.a !== undefined) it.a = clean(b.a, 6000);
      if (b.aq !== undefined) it.aq = clean(b.aq, 2000);
      const need = ['reply', 'app', 'site', 'publish'].includes(b.action) && b.on !== false;
      if (need && !it.a) return res.status(400).json({ ok: false, error: 'empty' });
      if (it.status === 'published') { it.status = 'answered'; it.app = true; } // старый формат
      if (b.action === 'publish') { it.app = true; it.status = 'answered'; }
      if (b.action === 'reply') it.status = 'answered';
      if (b.action === 'app') { it.app = b.on !== false; if (it.app) it.status = 'answered'; }
      if (b.action === 'site') { it.site = b.on !== false; if (it.site) it.status = 'answered'; }
      if (b.action === 'hide') { it.status = 'hidden'; it.app = false; it.site = false; }
      if (b.action === 'save' && it.status === 'new' && it.a) it.status = 'draft';
      it.by = role(b.key); it.ut = Date.now();
      await saveQuestion(it);
      await rebuildAnswers();
      return res.json({ ok: true, item: it });
    }
    if (b.action === 'delete') { await deleteQuestion(String(b.id || '')); await rebuildAnswers(); return res.json({ ok: true }); }
    return res.status(400).json({ ok: false });
  } catch (e) { console.error('vrach', e && e.message); return res.status(500).json({ ok: false }); }
}
