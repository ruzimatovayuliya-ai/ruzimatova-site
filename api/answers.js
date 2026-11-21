// Ответы врача для всех: /api/answers – «Полезное» в «Тонусе», /api/answers?for=site – частые вопросы на сайте.
import { ready, publishedAnswers } from './_store.js';
export default async function handler(req, res) {
  if (!ready()) { res.setHeader('Cache-Control', 'no-store'); return res.status(200).json([]); }
  try {
    const all = await publishedAnswers();
    const forSite = (req.query && req.query.for === 'site') || /[?&]for=site/.test(req.url || '');
    const a = all.filter(x => forSite ? x.site : x.app !== false);
    res.setHeader('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=600');
    return res.status(200).json(a);
  } catch (e) { console.error('answers', e && e.message); res.setHeader('Cache-Control', 'no-store'); return res.status(200).json([]); }
}
