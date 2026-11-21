// Хранилище анонимных вопросов: Vercel Blob в аккаунте врача.
// Вопрос – файл q/<время>-<случайное>.json, опубликованные ответы – pub/answers.json.
import { put, get, list, del } from '@vercel/blob';
import crypto from 'node:crypto';

// ключ: либо BLOB_READ_WRITE_TOKEN, либо новый способ Vercel – BLOB_STORE_ID + OIDC (библиотека берёт токен сама)
export const ready = () => !!(process.env.BLOB_READ_WRITE_TOKEN || process.env.BLOB_STORE_ID);
export const via = () => process.env.BLOB_READ_WRITE_TOKEN ? 'token' : process.env.BLOB_STORE_ID ? 'oidc' : 'none';
// проверка связи с хранилищем без записи (для GET /api/ask)
export async function check() { try { await list({ prefix: 'q/', limit: 1 }); return { ok: true }; } catch (e) { return { ok: false, error: String(e && e.message || e).slice(0, 300) }; } }
let mode = process.env.BLOB_ACCESS || 'private';

async function save(pathname, data) {
  const body = JSON.stringify(data);
  const opt = { contentType: 'application/json', addRandomSuffix: false, allowOverwrite: true, cacheControlMaxAge: 60 };
  try { return await put(pathname, body, { ...opt, access: mode }); }
  catch (e) {
    // хранилище создано как публичное или приватное – пробуем второй вариант один раз
    const other = mode === 'private' ? 'public' : 'private';
    const r = await put(pathname, body, { ...opt, access: other });
    mode = other; return r;
  }
}
async function load(pathname) {
  for (const m of [mode, mode === 'private' ? 'public' : 'private']) {
    try {
      const r = await get(pathname, { access: m, useCache: false });
      if (!r) return null;
      return JSON.parse(await new Response(r.stream).text());
    } catch (e) { /* пробуем другой режим */ }
  }
  return null;
}
export async function addQuestion({ q, lang, src }) {
  const ts = Date.now();
  const id = ts + '-' + crypto.randomBytes(4).toString('hex');
  const item = { id, ts, q, lang, src, status: 'new', a: '', aq: '' };
  await save('q/' + id + '.json', item);
  return id;
}
export async function allQuestions() {
  const out = []; let cursor;
  do {
    const r = await list({ prefix: 'q/', cursor, limit: 1000 });
    for (const b of r.blobs) { const it = await load(b.pathname); if (it) out.push(it); }
    cursor = r.hasMore ? r.cursor : undefined;
  } while (cursor);
  return out.sort((a, b) => b.ts - a.ts);
}
export const getQuestion = id => load('q/' + id + '.json');
export const saveQuestion = it => save('q/' + it.id + '.json', it);
export const deleteQuestion = id => del('q/' + id + '.json').catch(async () => {
  const r = await list({ prefix: 'q/' + id }); if (r.blobs[0]) await del(r.blobs[0].url);
});
// куда показан ответ: it.app – «Полезное» в «Тонусе», it.site – частые вопросы на сайте (старое status:'published' = в приложении)
export const inApp = x => !!(x.a && (x.app || x.status === 'published'));
export const onSite = x => !!(x.a && x.site);
export async function rebuildAnswers() {
  const qs = await allQuestions();
  const pub = qs.filter(x => x.status !== 'hidden' && (inApp(x) || onSite(x))).map(x => ({ id: x.id, d: new Date(x.ts).toISOString().slice(0, 10), lang: x.lang, q: x.aq || x.q, a: x.a, app: inApp(x), site: onSite(x) }));
  await save('pub/answers.json', pub);
  return pub;
}
// ответы конкретной автору: по номерам вопросов, которые помнит её телефон (номер случайный, имени нет)
export async function mine(ids) {
  const out = [];
  for (const id of ids) {
    const it = await load('q/' + id + '.json'); if (!it) continue;
    const ans = it.a && (it.status === 'answered' || it.status === 'published' || it.app || it.site);
    out.push({ id: it.id, a: ans ? it.a : '', st: ans ? 'ans' : 'wait' });
  }
  return out;
}
export const publishedAnswers = async () => (await load('pub/answers.json')) || [];

// пароли кабинета хранятся только как хэши: врач, SMM, Ильяс (у всех одинаковые права)
const KEYS = { 'b5b6864b6f7f02e0e687050886400cfb3343a6998bc60a0c94d34411bf89a3f6': 'врач', 'd362d8d03bb24626320904f286c37213e9d6fab0eb24c48aea33354b453f0bb6': 'SMM', '3e30ce15bd64d6363fb0774539c7a6b1de2174b96cfd6e296c6e8d9f515173b4': 'Ильяс' };
export const role = k => { if (typeof k !== 'string' || !k) return null; const d = crypto.createHash('sha256').update('ruz:' + k).digest('hex'); return KEYS[d] || null; };
export const checkKey = k => !!role(k);
export const clean = (s, n) => String(s || '').replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, n);
