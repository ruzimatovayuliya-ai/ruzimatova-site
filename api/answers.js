// Опубликованные ответы врача – для «Тонуса» и сайта.
import { ready, publishedAnswers } from './_store.js';
export default async function handler(req, res) {
  if (!ready()) { res.setHeader('Cache-Control', 'no-store'); return res.status(200).json([]); }
  try {
    const a = await publishedAnswers();
    res.setHeader('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=600');
    return res.status(200).json(a);
  } catch (e) { console.error('answers', e && e.message); res.setHeader('Cache-Control', 'no-store'); return res.status(200).json([]); }
}
