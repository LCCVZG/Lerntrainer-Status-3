'use strict';
/* Status 3 – Notfallmedizin-Trainer. Single-file app logic (no build step). */
const D = window.S3DATA;
const APPV = D.version;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const rnd = n => Math.floor(Math.random() * n);
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = rnd(i + 1); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const clone = o => JSON.parse(JSON.stringify(o));
const pad = n => String(n).padStart(2, '0');
const dayKey = (d = new Date()) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
const addDays = (d, n) => { const x = new Date(d); x.setDate(x.getDate() + n); return x; };
const fmtNum = (x, dec) => { const s = (dec == null ? +(+x).toFixed(2) : (+x).toFixed(dec)) + ''; return s.replace('.', ','); };
const linkify = s => esc(s).replace(/(https?:\/\/[^\s;)]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
function seeded(str) { let h = 2166136261; for (const c of str) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619); } return () => { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; return ((h >>> 0) % 100000) / 100000; }; }

const QS = D.questions;
const QN = QS.filter(q => q.t !== 'case');
const CASES = QS.filter(q => q.t === 'case');
const BYID = Object.fromEntries(QS.map(q => [q.id, q]));
const TOPIC_COL = { REA: '#E5322D', AW: '#1F6FE0', KAR: '#C2185B', NEU: '#7C4DFF', TRA: '#D9480F', PAE: '#0F9D8A', TOX: '#5E8C1A', PHA: '#B7791F', TAK: '#455A64', MANV: '#C99700', GEF: '#FF6F00' };
const TYPE = { mtf: 'Wahr/Falsch ×5', order: 'Reihenfolge', match: 'Zuordnen', cloze: 'Lückentext', num: 'Rechnen', img: 'EKG & Bild', case: 'Einsatz' };
const PAL = ['#1F6FE0', '#E5322D', '#0F9D8A', '#B7791F', '#7C4DFF', '#C2185B'];

/* ---------------- Icons ---------------- */
const I = (p, extra = '') => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ${extra}>${p}</svg>`;
const IC = {
  home: I('<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>'),
  learn: I('<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/><path d="M9 7h6M9 11h6"/>'),
  cases: I('<path d="M3 17V9a2 2 0 0 1 2-2h9l4 4h2a1 1 0 0 1 1 1v5"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/><path d="M8 10h3M9.5 8.5v3"/>'),
  duel: I('<path d="M14.5 3.5l6 6-9 9-6-6z"/><path d="M3 21l4-4M9.5 3.5l-6 6 3 3"/>'),
  profile: I('<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>'),
  session: I('<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>'),
  exam: I('<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 3v3h6V3M9 11h6M9 15h4"/>'),
  bolt: I('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
  triage: I('<path d="M4 4h12l4 4v12H4z"/><circle cx="9" cy="9" r="2"/><path d="M8 14h8M8 17h5"/>'),
  memo: I('<rect x="3" y="6" width="14" height="14" rx="2"/><path d="M7 3h12a2 2 0 0 1 2 2v12"/>'),
  heart: '<svg viewBox="0 0 24 24"><path fill="#E5322D" d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z"/></svg>',
  heartOff: '<svg viewBox="0 0 24 24"><path fill="none" stroke="#8a9ab3" stroke-width="2" d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z"/></svg>',
  flame: I('<path d="M12 22c4 0 7-3 7-7 0-5-5-7-5-12-3 2-6 6-6 9-1-1-2-2-2-4-2 2-1 6-1 7 0 4 3 7 7 7z"/>'),
  star: I('<path d="M12 2l3 7h7l-5.5 4.5 2 7.5-6.5-4.5L5.5 21l2-7.5L2 9h7z"/>'),
  check: I('<path d="M4 12l5 5L20 6"/>'),
  x: I('<path d="M6 6l12 12M18 6L6 18"/>'),
  phone: I('<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>'),
  grip: I('<circle cx="9" cy="6" r="1"/><circle cx="15" cy="6" r="1"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><circle cx="9" cy="18" r="1"/><circle cx="15" cy="18" r="1"/>'),
  trophy: I('<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3a3 3 0 0 1-3 4M7 5H4a3 3 0 0 0 3 4"/>'),
  ecg: I('<path d="M2 12h5l2-5 3 10 2-7 2 2h6"/>'),
  moon: I('<path d="M21 13A9 9 0 1 1 11 3a7 7 0 0 0 10 10z"/>'),
  sun: I('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
  shield: I('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>'),
  brain: I('<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 5 2V4a3 3 0 0 0-2 0zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-5 2V4a3 3 0 0 1 2 0z"/>'),
  clock: I('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
  flag: I('<path d="M5 21V4M5 4h12l-2 4 2 4H5"/>'),
  siren: I('<path d="M7 18v-6a5 5 0 0 1 10 0v6"/><path d="M5 18h14v3H5zM12 3v2M4 8l1.5 1M20 8l-1.5 1"/>'),
};

/* ---------------- State ---------------- */
const SKEY = 's3:v1';
const DEF = {
  xp: 0, prog: {}, hist: {}, streak: { cur: 0, best: 0, last: null }, badges: {}, mis: null, cases: {},
  blitz: { best: 0, runs: 0 }, sprint: { best: 0, runs: 0 }, duel: { n: 0, names: ['Notarzt', 'NotSan'], hist: [] },
  exams: [], memoSeen: {}, run: 0, bestRun: 0, firstUse: null, pomo: { done: 0 }, review: { checks: {}, notes: '', done: null },
  settings: { theme: 'auto', fx: 'on', sound: true, order: 'smart', algo: 'mstart', examDate: '', learn: { topics: [], types: [], status: 'all' } },
};
function merge(a, b) { for (const k in b) { if (b[k] && typeof b[k] === 'object' && !Array.isArray(b[k]) && a[k] && typeof a[k] === 'object' && !Array.isArray(a[k])) merge(a[k], b[k]); else a[k] = b[k]; } return a; }
function load() { try { const r = localStorage.getItem(SKEY); if (r) return merge(clone(DEF), JSON.parse(r)); } catch (e) { } return clone(DEF); }
let S = load();
if (!S.firstUse) S.firstUse = Date.now();
function save() { try { localStorage.setItem(SKEY, JSON.stringify(S)); } catch (e) { } }

/* ---------------- FX: sound, haptics, confetti, toast ---------------- */
let AC;
function tone(f, d, type = 'sine', v = .07, when = 0) {
  if (!S.settings.sound) return;
  try {
    AC = AC || new (window.AudioContext || window.webkitAudioContext)();
    const t = AC.currentTime + when, o = AC.createOscillator(), g = AC.createGain();
    o.type = type; o.frequency.setValueAtTime(f, t); g.gain.setValueAtTime(v, t); g.gain.exponentialRampToValueAtTime(.0001, t + d);
    o.connect(g).connect(AC.destination); o.start(t); o.stop(t + d + .03);
  } catch (e) { }
}
const SND = {
  ok: () => { tone(660, .1); tone(990, .16, 'sine', .07, .09); },
  bad: () => tone(150, .28, 'square', .045),
  buzz: () => tone(520, .14, 'sawtooth', .05),
  lvl: () => [523, 659, 784, 1046].forEach((f, i) => tone(f, .2, 'triangle', .08, i * .12)),
  siren: () => { for (let i = 0; i < 4; i++) tone(i % 2 ? 587 : 440, .3, 'triangle', .05, i * .32); },
  tick: () => tone(1400, .03, 'square', .02),
};
const buzzV = ms => { try { navigator.vibrate && navigator.vibrate(ms); } catch (e) { } };
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function fx(style = 'burst', n = 140) {
  if (reducedMotion || S.settings.fx === 'reduced') return;
  const cv = $('#fx'), ctx = cv.getContext('2d'), W = innerWidth, H = innerHeight, dpr = devicePixelRatio || 1;
  cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const cols = ['#1F6FE0', '#5AB0FF', '#E5322D', '#FFC21A', '#3CF0A0', '#FFFFFF', '#FF7A1A'];
  const ps = Array.from({ length: n }, () => {
    const b = { r: Math.random() * 6 + 3, c: cols[rnd(cols.length)], a: Math.random() * 6, va: (Math.random() - .5) * .3, sh: rnd(3) };
    if (style === 'rain') return Object.assign(b, { x: Math.random() * W, y: -20 - Math.random() * H * .5, vx: (Math.random() - .5) * 2, vy: Math.random() * 3 + 3, g: .04 });
    return Object.assign(b, { x: W / 2 + (Math.random() - .5) * 80, y: H * .42, vx: (Math.random() - .5) * 16, vy: -Math.random() * 13 - 3, g: .36 });
  });
  const t0 = performance.now(), dur = style === 'rain' ? 3 : 2.3;
  (function fr(t) {
    const el = (t - t0) / 1000; ctx.clearRect(0, 0, W, H); let alive = false;
    for (const p of ps) {
      p.vy += p.g; p.x += p.vx; p.y += p.vy; p.vx *= .99; p.a += p.va; const life = Math.max(0, 1 - el / dur);
      if (p.y < H + 20 && life > 0) alive = true;
      ctx.save(); ctx.globalAlpha = life; ctx.translate(p.x, p.y); ctx.rotate(p.a); ctx.fillStyle = p.c;
      if (p.sh === 0) { ctx.beginPath(); ctx.arc(0, 0, p.r / 2, 0, 7); ctx.fill(); } else if (p.sh === 1) ctx.fillRect(-p.r / 6, -p.r, p.r / 3, p.r * 2); else ctx.fillRect(-p.r / 2, -p.r / 4, p.r, p.r / 2);
      ctx.restore();
    }
    if (alive && el < dur + .2) requestAnimationFrame(fr); else ctx.clearRect(0, 0, W, H);
  })(t0);
}
let toastT;
function toast(msg, icon) {
  const t = $('#toast'); t.innerHTML = (icon || '') + `<span>${msg}</span>`; t.classList.add('on');
  clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove('on'), 2600);
}
function xpFly(n) {
  if (n <= 0) return; const d = document.createElement('div'); d.className = 'xpfly'; d.textContent = `+${n} XP`; document.body.appendChild(d); setTimeout(() => d.remove(), 1200);
}

/* ---------------- Ranks ---------------- */
const RANKS = [
  [0, 'Praktikant', 'Prakt.'], [150, 'Rettungshelfer', 'RH'], [400, 'Rettungssanitäter', 'RS'], [800, 'Notfallsanitäter', 'NotSan'],
  [1400, 'Notarzt in Ausbildung', 'NA i. A.'], [2200, 'Notarzt', 'NA'], [3300, 'Leitender Notarzt', 'LNA'], [4700, 'ÄLRD', 'ÄLRD'], [6500, 'Legende der Leitstelle', 'Legende'],
];
const rankOf = xp => { let i = 0; RANKS.forEach((r, k) => { if (xp >= r[0]) i = k; }); return i; };
function rankBadge(i, size = 58) {
  const cols = ['#8A9AB3', '#5E8C1A', '#0F9D8A', '#1F6FE0', '#7C4DFF', '#C2185B', '#E5322D', '#FF7A1A', '#FFC21A'];
  const c = cols[i] || '#FFC21A'; const stars = Math.min(i, 5);
  let st = ''; for (let k = 0; k < stars; k++) { const x = 32 - (stars - 1) * 5 + k * 10; st += `<path transform="translate(${x} 22) scale(.32)" d="M0 -14L4 -4H14L6 2L9 13L0 6L-9 13L-6 2L-14 -4H-4Z" fill="#FFD23F"/>`; }
  return `<svg viewBox="0 0 64 64" width="${size}" height="${size}" class="badge"><path d="M32 4l24 8v18c0 16-11 26-24 30C19 56 8 46 8 30V12z" fill="${c}"/><path d="M32 9l19 6v15c0 13-9 21-19 25-10-4-19-12-19-25V15z" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>${st}<text x="32" y="44" text-anchor="middle" font-size="${i >= 7 ? 9 : 10}" font-weight="900" fill="#fff" font-family="system-ui">${esc(RANKS[i][2])}</text></svg>`;
}
function addXP(n) {
  if (!n) return;
  const before = rankOf(S.xp); S.xp += n;
  const h = hist(); h.xp += n;
  const after = rankOf(S.xp);
  if (after > before) setTimeout(() => levelUp(after), 600);
  renderTop();
}
function levelUp(i) {
  $('#lvlupBox').innerHTML = `${rankBadge(i, 96)}<div class="eyebrow" style="margin-top:10px">Beförderung</div><h2 style="margin:6px 0">${esc(RANKS[i][1])}</h2><p class="muted">Neuer Dienstgrad freigeschaltet. Weiter so!</p><button class="btn pri block" id="lvlOk">Status 3 – weiter</button>`;
  $('#lvlup').classList.add('on'); SND.lvl(); fx('rain', 220);
  $('#lvlOk').onclick = () => $('#lvlup').classList.remove('on');
}

/* ---------------- History, streak ---------------- */
function hist(k = dayKey()) { return S.hist[k] || (S.hist[k] = { xp: 0, n: 0, c: 0, goal: false }); }
const DAILY_GOAL = 10;
function countAnswer(correct) {
  const h = hist(); h.n++; if (correct) h.c++;
  if (!h.goal && h.n >= DAILY_GOAL) {
    h.goal = true; const today = dayKey(), y = dayKey(addDays(new Date(), -1));
    S.streak.cur = S.streak.last === y ? S.streak.cur + 1 : (S.streak.last === today ? S.streak.cur : 1);
    S.streak.last = today; S.streak.best = Math.max(S.streak.best, S.streak.cur);
    setTimeout(() => { toast(`Tagesziel erreicht – Serie: ${S.streak.cur} Tag${S.streak.cur > 1 ? 'e' : ''}`, IC.flame); fx('burst', 100); SND.lvl(); }, 900);
  }
}
function streakNow() { const t = dayKey(), y = dayKey(addDays(new Date(), -1)); return (S.streak.last === t || S.streak.last === y) ? S.streak.cur : 0; }

/* ---------------- Missions ---------------- */
const MT = {
  ans: { t: m => `Beantworte ${m.goal} Fragen`, ev: 'answer', inc: () => 1 },
  topic: { t: m => `${m.goal} Fragen aus „${D.topics[m.x]}“`, ev: 'answer', inc: (e, m) => e.q.topic === m.x ? 1 : 0 },
  type: { t: m => `${m.goal}× fehlerfrei: ${TYPE[m.x]}`, ev: 'answer', inc: (e, m) => e.q.t === m.x && e.score >= .999 ? 1 : 0 },
  blitz: { t: m => `Blitzrunde mit ≥ ${m.thr} Punkten`, ev: 'blitz', inc: (e, m) => e.score >= m.thr ? 1 : 0 },
  sprint: { t: m => `Sichtungssprint: ≥ ${m.thr} richtig`, ev: 'sprint', inc: (e, m) => e.correct >= m.thr ? 1 : 0 },
  case: { t: () => `Einen Boss-Einsatz bestehen`, ev: 'case', inc: e => e.success ? 1 : 0 },
  session: { t: m => `Übungsrunde mit ≥ ${m.thr} %`, ev: 'session', inc: (e, m) => e.pct >= m.thr ? 1 : 0 },
  memo: { t: m => `${m.goal} Merkkarten aufklappen`, ev: 'memo', inc: () => 1 },
  duel: { t: () => `Ein Duell spielen`, ev: 'duel', inc: () => 1 },
};
function ensureMissions() {
  const k = dayKey();
  if (S.mis && S.mis.day === k) return S.mis;
  const r = seeded('s3' + k), pick = a => a[Math.floor(r() * a.length)];
  const types = ['order', 'match', 'cloze', 'num', 'img', 'mtf'];
  const first = r() < .5 ? { k: 'ans', goal: pick([10, 15]) } : { k: 'topic', goal: 5, x: pick(Object.keys(D.topics)) };
  const pool = shuffle(['type', 'blitz', 'sprint', 'case', 'session', 'memo', 'duel', 'blitz', 'sprint', 'case', 'type']).sort(() => r() - .5);
  const list = [first]; for (const p of pool) { if (list.length >= 3) break; if (!list.find(m => m.k === p)) list.push({ k: p }); }
  list.forEach(m => {
    if (m.k === 'type') { m.x = pick(types); m.goal = 3; }
    if (m.k === 'blitz') { m.thr = pick([12, 15, 18]); m.goal = 1; }
    if (m.k === 'sprint') { m.thr = pick([8, 10, 12]); m.goal = 1; }
    if (m.k === 'session') { m.thr = 70; m.goal = 1; }
    if (m.k === 'memo') m.goal = 3;
    if (m.k === 'case' || m.k === 'duel') m.goal = 1;
    m.p = 0; m.done = false;
  });
  S.mis = { day: k, list, bonus: false }; save(); return S.mis;
}
function missionEvent(ev, e) {
  const M = ensureMissions(); let changed = false;
  for (const m of M.list) {
    if (m.done || MT[m.k].ev !== ev) continue;
    const inc = MT[m.k].inc(e, m); if (!inc) continue;
    m.p = Math.min(m.goal, m.p + inc); changed = true;
    if (m.p >= m.goal) { m.done = true; addXP(30); setTimeout(() => toast(`Mission erfüllt: ${MT[m.k].t(m)} (+30 XP)`, IC.check), 400); }
  }
  if (!M.bonus && M.list.every(m => m.done)) {
    M.bonus = true; S.badges.mission = S.badges.mission || Date.now(); addXP(50);
    setTimeout(() => { toast('Alle Tagesmissionen erfüllt! +50 XP', IC.trophy); fx('rain', 200); SND.lvl(); }, 1400);
  }
  return changed;
}

/* ---------------- Badges ---------------- */
const seenN = () => QN.filter(q => S.prog[q.id]).length;
const casesDone = () => CASES.filter(c => S.cases[c.id] && S.cases[c.id].done).length;
const topicMastery = t => { const qs = QN.filter(q => q.topic === t); return qs.filter(q => S.prog[q.id] && S.prog[q.id].best >= .999).length / qs.length; };
const ECGQ = QN.filter(q => q.t === 'img' && !q.fig.startsWith('capno'));
const BADGES = [
  ['first', 'Erste Schicht', 'Erste Frage beantwortet', () => seenN() >= 1, '#1F6FE0', 'star'],
  ['q50', 'Fünfzig', '50 verschiedene Fragen bearbeitet', () => seenN() >= 50, '#0F9D8A', 'learn'],
  ['q100', 'Hundert', '100 verschiedene Fragen bearbeitet', () => seenN() >= 100, '#7C4DFF', 'learn'],
  ['qall', 'Alles gesehen', 'Alle Fragen und Einsätze bearbeitet', () => seenN() >= QN.length && casesDone() >= CASES.length, '#C2185B', 'trophy'],
  ['run10', 'Lauf', '10 Fragen in Folge vollständig richtig', () => S.bestRun >= 10, '#D9480F', 'bolt'],
  ['run25', 'Unaufhaltsam', '25 Fragen in Folge vollständig richtig', () => S.bestRun >= 25, '#E5322D', 'bolt'],
  ['s3', 'Drei Tage', 'Serie von 3 Tagen', () => S.streak.best >= 3, '#FF7A1A', 'flame'],
  ['s7', 'Wochendienst', 'Serie von 7 Tagen', () => S.streak.best >= 7, '#FF7A1A', 'flame'],
  ['s14', 'Dauerbereitschaft', 'Serie von 14 Tagen', () => S.streak.best >= 14, '#E5322D', 'flame'],
  ['mission', 'Auftrag erfüllt', 'Alle Tagesmissionen an einem Tag', () => !!S.badges.mission, '#16A36A', 'check'],
  ['blitz15', 'Schnelldenker', 'Blitzrunde ≥ 15 Punkte', () => S.blitz.best >= 15, '#FFC21A', 'bolt'],
  ['blitz30', 'Lichtgeschwindigkeit', 'Blitzrunde ≥ 30 Punkte', () => S.blitz.best >= 30, '#FFC21A', 'bolt'],
  ['sprint10', 'Sichter', 'Sichtungssprint ≥ 10 richtig', () => S.sprint.best >= 10, '#C99700', 'triage'],
  ['sprint20', 'Sichtungsprofi', 'Sichtungssprint ≥ 20 richtig', () => S.sprint.best >= 20, '#D62828', 'triage'],
  ['boss1', 'Erster Einsatz', 'Einen Boss-Einsatz bestanden', () => casesDone() >= 1, '#E5322D', 'siren'],
  ['boss3', 'Ohne Kratzer', 'Einen Einsatz mit allen 3 Herzen', () => Object.values(S.cases).some(c => c.best >= 3), '#E5322D', 'shield'],
  ['bossall', 'Alle Einsätze', 'Alle Boss-Einsätze bestanden', () => casesDone() >= CASES.length, '#7C4DFF', 'siren'],
  ['duel1', 'Herausforderer', 'Ein Duell gespielt', () => S.duel.n >= 1, '#455A64', 'duel'],
  ['duel10', 'Wachen-Champion', '10 Duelle gespielt', () => S.duel.n >= 10, '#455A64', 'duel'],
  ['exam70', 'Bestanden', 'Prüfungssimulation ≥ 70 %', () => S.exams.some(e => e.pct >= 70), '#16A36A', 'exam'],
  ['exam90', 'Mit Auszeichnung', 'Prüfungssimulation ≥ 90 %', () => S.exams.some(e => e.pct >= 90), '#FFC21A', 'exam'],
  ['ecg', 'EKG-Fuchs', 'Alle EKG-Rätsel einmal richtig', () => ECGQ.every(q => S.prog[q.id] && S.prog[q.id].best >= .999), '#C2185B', 'ecg'],
  ['night', 'Nachtdienst', 'Zwischen 22 und 5 Uhr gelernt', () => !!S.badges.night, '#13284A', 'moon'],
  ['early', 'Frühdienst', 'Zwischen 5 und 7 Uhr gelernt', () => !!S.badges.early, '#FF9F1C', 'sun'],
  ['memo10', 'Merkfähig', '10 Merkkarten aufgeklappt', () => Object.keys(S.memoSeen).length >= 10, '#B7791F', 'memo'],
  ['pomo4', 'Fokus', '4 Pomodoros abgeschlossen', () => S.pomo.done >= 4, '#E5322D', 'clock'],
  ...Object.keys(D.topics).map(t => ['m_' + t, 'Meister: ' + D.topics[t].split(' ')[0], `Alle Fragen „${D.topics[t]}“ einmal vollständig richtig`, () => topicMastery(t) >= .999, TOPIC_COL[t], 'shield']),
];
function checkBadges() {
  const hr = new Date().getHours();
  if (hr >= 22 || hr < 5) S.badges.night = S.badges.night || Date.now();
  if (hr >= 5 && hr < 7) S.badges.early = S.badges.early || Date.now();
  for (const [id, name, , test] of BADGES) {
    if (S.badges['got_' + id]) continue;
    let ok = false; try { ok = test(); } catch (e) { }
    if (ok) { S.badges['got_' + id] = Date.now(); addXP(20); setTimeout(() => { toast(`Abzeichen: ${name} (+20 XP)`, IC.trophy); SND.lvl(); fx('burst', 120); }, 1800); }
  }
}
function emit(ev, e) { missionEvent(ev, e || {}); checkBadges(); save(); renderTop(); }

/* ---------------- Progress & scoring ---------------- */
function record(q, score, mode) {
  const p = S.prog[q.id] || (S.prog[q.id] = { n: 0, best: 0, ls: 0, last: 0, ok: 0 });
  const first = p.n === 0, wasBest = p.best;
  p.n++; p.last = Date.now(); p.ls = score; p.best = Math.max(p.best, score); if (score >= .999) p.ok++;
  const full = score >= .999;
  let xp = Math.round(10 * q.lvl * score * (first || score > wasBest ? 1 : .5));
  if (full) { S.run++; S.bestRun = Math.max(S.bestRun, S.run); if (S.run % 5 === 0) xp += 10; } else S.run = 0;
  countAnswer(full); addXP(xp); emit('answer', { q, score, mode });
  return xp;
}

/* ---------------- Question types ---------------- */
const TYPES = {
  mtf: {
    init: q => ({ ord: shuffle([0, 1, 2, 3, 4]), a: {} }),
    complete: (q, st) => q.items.every((_, i) => st.a[i] !== undefined),
    eval: (q, st) => { const ok = q.items.map((it, i) => st.a[i] === it[1]); return { score: ok.filter(Boolean).length / 5, parts: ok }; },
    body(q, st, res) {
      let h = `<div class="stem">${esc(q.stem)}</div><div class="items">`;
      st.ord.forEach(i => {
        const it = q.items[i], a = st.a[i];
        const cls = res ? (res.parts[i] ? 'right' : 'wrong') : '';
        h += `<div class="it ${cls}"><div class="tx">${esc(it[0])}${res ? `<div class="sol" style="color:${it[1] ? 'var(--ok)' : 'var(--bad)'}">${it[1] ? 'WAHR' : 'FALSCH'}</div><div class="why">${esc(it[2])}</div>` : ''}</div>
          <div class="tf"><button class="w" data-tf="${i}:1" aria-pressed="${a === true}" ${res ? 'disabled' : ''} aria-label="wahr">W</button><button class="f" data-tf="${i}:0" aria-pressed="${a === false}" ${res ? 'disabled' : ''} aria-label="falsch">F</button></div></div>`;
      });
      return h + '</div>';
    },
    bind(el, q, st, rer) { el.onclick = e => { const b = e.target.closest('[data-tf]'); if (!b || b.disabled) return; const [i, v] = b.dataset.tf.split(':'); st.a[i] = v === '1'; SND.tick(); rer(); }; },
  },
  order: {
    init: q => { let o; do { o = shuffle(q.steps.map((_, i) => i)); } while (o.every((v, i) => v === i)); return { ord: o }; },
    complete: () => true,
    eval: (q, st) => { const ok = st.ord.map((v, i) => v === i); return { score: ok.filter(Boolean).length / ok.length, parts: ok }; },
    body(q, st, res) {
      let h = `<div class="stem">${esc(q.stem)}</div><div class="ord" id="ord">`;
      st.ord.forEach((v, pos) => {
        const cls = res ? (res.parts[pos] ? 'right' : 'wrong') : '';
        h += `<div class="oi ${cls}" data-pos="${pos}" data-v="${v}">${res ? '' : `<span class="grip" data-grip>${IC.grip}</span>`}<span class="nr">${pos + 1}</span><span class="tx">${esc(q.steps[v])}</span>${res ? '' : `<span class="ud"><button data-mv="${pos}:-1" aria-label="nach oben">▲</button><button data-mv="${pos}:1" aria-label="nach unten">▼</button></span>`}</div>`;
      });
      h += '</div>';
      if (res && res.score < 1) h += `<div class="fb" style="margin-top:10px"><b>Richtige Reihenfolge</b><ol style="margin:8px 0 0;padding-left:20px;line-height:1.5">${q.steps.map(s => `<li>${esc(s)}</li>`).join('')}</ol></div>`;
      return h;
    },
    bind(el, q, st, rer) {
      el.onclick = e => { const b = e.target.closest('[data-mv]'); if (!b) return; const [p, d] = b.dataset.mv.split(':').map(Number); const t = p + d; if (t < 0 || t >= st.ord.length) return;[st.ord[p], st.ord[t]] = [st.ord[t], st.ord[p]]; SND.tick(); rer(); };
      const box = $('#ord', el); if (!box) return;
      box.onpointerdown = e => {
        const g = e.target.closest('[data-grip]'); if (!g) return; e.preventDefault();
        const item = g.closest('.oi'); item.classList.add('drag'); const y0 = e.clientY; let moved = false;
        box.setPointerCapture(e.pointerId);
        const mv = ev => {
          moved = true; item.style.transform = `translateY(${ev.clientY - y0}px)`;
          const sib = [...box.children].filter(c => c !== item);
          let idx = sib.findIndex(c => { const r = c.getBoundingClientRect(); return ev.clientY < r.top + r.height / 2; }); if (idx < 0) idx = sib.length;
          const cur = [...box.children].indexOf(item);
          if (idx !== cur) { const before = sib[idx] || null; const r0 = item.getBoundingClientRect().top; box.insertBefore(item, before); const r1 = item.getBoundingClientRect().top; const off = (parseFloat(item.style.transform.slice(11)) || 0) - (r1 - r0); item.style.transform = `translateY(${off}px)`; }
        };
        const up = () => { box.removeEventListener('pointermove', mv); box.removeEventListener('pointerup', up); box.removeEventListener('pointercancel', up); item.classList.remove('drag'); item.style.transform = ''; if (moved) { st.ord = [...box.children].map(c => +c.dataset.v); SND.tick(); } rer(); };
        box.addEventListener('pointermove', mv); box.addEventListener('pointerup', up); box.addEventListener('pointercancel', up);
      };
    },
  },
  match: {
    init: q => ({ r: shuffle(q.pairs.map((_, i) => i)), pairs: {}, sel: null, selR: null }),
    complete: (q, st) => q.pairs.every((_, i) => st.pairs[i] !== undefined),
    eval: (q, st) => { const ok = q.pairs.map((_, i) => st.pairs[i] === i); return { score: ok.filter(Boolean).length / ok.length, parts: ok }; },
    body(q, st, res) {
      const rev = {}; for (const l in st.pairs) rev[st.pairs[l]] = +l;
      let h = `<div class="stem">${esc(q.stem)}</div><p class="small muted" style="margin:-6px 0 10px">${res ? '' : 'Links antippen, dann rechts den Partner wählen.'}</p><div class="mt"><div class="col">`;
      q.pairs.forEach((p, i) => {
        const pr = st.pairs[i] !== undefined; const cls = res ? (res.parts[i] ? 'right' : 'wrong') : (st.sel === i ? 'sel' : '');
        h += `<button class="mi ${cls} ${pr ? 'paired' : ''}" data-l="${i}" ${res ? 'disabled' : ''}>${esc(p[0])}${pr ? `<span class="k" style="background:${PAL[i % PAL.length]}">${i + 1}</span>` : ''}</button>`;
      });
      h += '</div><div class="col">';
      st.r.forEach(j => {
        const l = rev[j]; const pr = l !== undefined; const cls = res ? (l === j ? 'right' : 'wrong') : (st.selR === j ? 'sel' : '');
        h += `<button class="mi ${cls} ${pr ? 'paired' : ''}" data-r="${j}" ${res ? 'disabled' : ''}>${esc(q.pairs[j][1])}${pr ? `<span class="k" style="background:${PAL[l % PAL.length]}">${l + 1}</span>` : ''}</button>`;
      });
      h += '</div></div>';
      if (res && res.score < 1) h += `<div class="fb" style="margin-top:10px"><b>Lösung</b><ul style="margin:8px 0 0;padding-left:18px;line-height:1.5">${q.pairs.map(p => `<li><b>${esc(p[0])}</b> → ${esc(p[1])}</li>`).join('')}</ul></div>`;
      return h;
    },
    bind(el, q, st, rer) {
      el.onclick = e => {
        const L = e.target.closest('[data-l]'), Rb = e.target.closest('[data-r]');
        const link = (l, r) => { for (const k in st.pairs) if (st.pairs[k] === r) delete st.pairs[k]; st.pairs[l] = r; st.sel = st.selR = null; SND.tick(); };
        if (L && !L.disabled) { const l = +L.dataset.l; if (st.selR !== null) link(l, st.selR); else if (st.pairs[l] !== undefined && st.sel !== l) { delete st.pairs[l]; st.sel = l; } else st.sel = st.sel === l ? null : l; rer(); }
        if (Rb && !Rb.disabled) { const r = +Rb.dataset.r; if (st.sel !== null) link(st.sel, r); else { const owner = Object.keys(st.pairs).find(k => st.pairs[k] === r); if (owner !== undefined) delete st.pairs[owner]; st.selR = st.selR === r ? null : r; } rer(); }
      };
    },
  },
  cloze: {
    init: q => ({ opts: q.gaps.map(g => shuffle([g[0], ...g[1]])), a: {} }),
    complete: (q, st) => q.gaps.every((_, i) => st.a[i] !== undefined),
    eval: (q, st) => { const ok = q.gaps.map((g, i) => st.a[i] === g[0]); return { score: ok.filter(Boolean).length / ok.length, parts: ok }; },
    body(q, st, res) {
      const parts = q.text.split(/\{(\d+)\}/);
      let h = '<div class="cz">';
      parts.forEach((p, k) => {
        if (k % 2 === 0) { h += esc(p); return; }
        const i = +p, v = st.a[i];
        const cls = res ? (res.parts[i] ? 'right' : 'wrong') : (v !== undefined ? 'fill' : '');
        h += `<button class="gap ${cls}" data-g="${i}" ${res ? 'disabled' : ''}>${v !== undefined ? esc(v) : '…'}</button>`;
        if (res && !res.parts[i]) h += ` <b style="color:var(--ok)">→ ${esc(q.gaps[i][0])}</b>`;
      });
      return h + '</div>';
    },
    bind(el, q, st, rer) {
      el.onclick = e => {
        const g = e.target.closest('[data-g]'); if (!g || g.disabled) return; const i = +g.dataset.g;
        openSheet(`<div class="eyebrow">Lücke ${i + 1} füllen</div><div style="height:10px"></div>${st.opts[i].map((o, k) => `<button class="opt" data-o="${k}">${esc(o)}</button>`).join('')}`, box => {
          box.onclick = ev => { const b = ev.target.closest('[data-o]'); if (!b) return; st.a[i] = st.opts[i][+b.dataset.o]; closeSheet(); SND.tick(); rer(); };
        });
      };
    },
  },
  num: {
    init: () => ({ v: '' }),
    parse: v => { const x = parseFloat(String(v).replace(',', '.').replace(/\s/g, '')); return isFinite(x) ? x : null; },
    complete: (q, st) => TYPES.num.parse(st.v) !== null,
    eval(q, st) {
      const x = TYPES.num.parse(st.v), d = Math.abs(x - q.ans);
      const full = d <= q.tol + 1e-9, half = d <= Math.max(3 * q.tol, Math.abs(q.ans) * .1) + 1e-9;
      return { score: full ? 1 : half ? .5 : 0, x };
    },
    body(q, st, res) {
      let h = `<div class="stem">${esc(q.stem)}</div><div class="numin"><input id="numIn" inputmode="decimal" autocomplete="off" placeholder="Ihre Antwort" value="${esc(st.v)}" ${res ? 'disabled' : ''}><span class="unit">${esc(q.unit)}</span></div>`;
      if (res) h += `<div class="it ${res.score >= 1 ? 'right' : 'wrong'}" style="margin-top:10px"><div class="tx"><b>Lösung: ${fmtNum(q.ans)} ${esc(q.unit)}</b>${q.tol ? ` <span class="muted">(Toleranz ± ${fmtNum(q.tol)})</span>` : ''}<div class="why">Ihre Angabe: ${fmtNum(res.x)} ${esc(q.unit)}${res.score === .5 ? ' – knapp daneben (halbe Punkte)' : ''}</div></div></div>`;
      return h;
    },
    bind(el, q, st, rer, changed, submit) {
      const inp = $('#numIn', el); if (!inp) return;
      inp.oninput = () => { st.v = inp.value; changed(); };
      inp.onkeydown = e => { if (e.key === 'Enter') submit && submit(); };
    },
  },
  img: {
    init: q => ({ ord: shuffle(q.opts.map((_, i) => i)), a: null }),
    complete: (q, st) => st.a !== null,
    eval: (q, st) => ({ score: st.a === q.ok ? 1 : 0 }),
    body(q, st, res) {
      let h = `<div class="fig"><div class="figsc">${D.figs[q.fig]}</div><button class="zoom" data-zoom="${q.fig}">⤢ vergrößern</button></div>${/capno/.test(q.fig) ? '' : '<div class="small muted" style="margin:-6px 0 10px">↔ Kurve seitlich wischen oder vergrößern</div>'}<div class="stem">${esc(q.stem)}</div><div class="opts">`;
      st.ord.forEach(i => {
        const cls = res ? (i === q.ok ? 'right' : (i === st.a ? 'wrong' : '')) : '';
        h += `<button class="opt ${cls}" data-o="${i}" aria-pressed="${st.a === i}" ${res ? 'disabled' : ''}>${esc(q.opts[i])}</button>`;
      });
      return h + '</div>';
    },
    bind(el, q, st, rer) {
      el.onclick = e => {
        const z = e.target.closest('[data-zoom]'); if (z) { openZoom(z.dataset.zoom); return; }
        const b = e.target.closest('[data-o]'); if (!b || b.disabled) return; st.a = +b.dataset.o; SND.tick(); rer();
      };
    },
  },
};
function qHead(q, extra = '') {
  return `<div class="qhead"><span class="qtype t-${q.t}">${TYPE[q.t]}</span><span class="tag" style="background:${TOPIC_COL[q.topic]};color:#fff">${esc(D.topics[q.topic])}</span><span class="tag">${esc(q.sub)}</span><span class="sp"></span>${extra}<span class="tag" title="Schwierigkeit">${'●'.repeat(q.lvl)}${'○'.repeat(3 - q.lvl)}</span></div>`;
}
function feedbackHTML(q, res, xp) {
  const s = res.score, ok = s >= .999;
  const icon = ok ? `<span style="color:var(--ok)">${IC.check.replace('<svg', '<svg width="26" height="26"')}</span>` : `<span style="color:${s > 0 ? 'var(--yellow)' : 'var(--bad)'}">${(s > 0 ? IC.flag : IC.x).replace('<svg', '<svg width="26" height="26"')}</span>`;
  const label = ok ? pick(['Sitzt!', 'Lehrbuchreif.', 'Volle Punktzahl.', 'Status 4 – angekommen!', 'Sauber.']) : s > 0 ? 'Teilweise richtig' : 'Leider falsch';
  let h = `<div class="fb"><div class="res">${icon}<span>${label}</span><span class="sc">${Math.round(s * 100)} %${xp ? ` · +${xp} XP` : ''}</span></div>`;
  if (q.expl) h += `<p class="ex">${esc(q.expl)}</p>`;
  if (q.memo) h += `<div class="memo">💡 ${esc(q.memo)}</div>`;
  h += `<div class="src"><b>Quelle:</b> ${linkify(q.src)}</div></div>`;
  return h;
}
const pick = a => a[rnd(a.length)];

/* A reusable question player. opts: {exam, onDone(res,xp), onAnswer(st), nextLabel, st} */
function mountQuestion(host, q, opts = {}) {
  const T = TYPES[q.t]; const st = opts.st || T.init(q); let res = opts.res || null, xp = 0;
  const draw = () => {
    host.innerHTML = qHead(q, opts.headExtra || '') + `<div id="qbody"></div>` + (res && !opts.exam ? feedbackHTML(q, res, xp) : '') +
      `<div class="actions">${res ? (opts.exam ? '' : `<button class="btn pri grow" id="qNext">${opts.nextLabel || 'Weiter'}</button>`) : (opts.exam ? '' : `<button class="btn pri grow" id="qCheck" ${T.complete(q, st) ? '' : 'disabled'}>Prüfen</button>`)}${opts.extraBtns || ''}</div>`;
    const body = $('#qbody', host); body.innerHTML = T.body(q, st, res);
    const changed = () => { const c = $('#qCheck', host); if (c) c.disabled = !T.complete(q, st); opts.onAnswer && opts.onAnswer(st); };
    const rer = () => { body.innerHTML = T.body(q, st, res); T.bind(body, q, st, rer, changed, check); changed(); };
    T.bind(body, q, st, rer, changed, check);
    const c = $('#qCheck', host); if (c) c.onclick = check;
    const n = $('#qNext', host); if (n) n.onclick = () => opts.onNext && opts.onNext(res, xp);
    opts.afterDraw && opts.afterDraw(host);
  };
  function check() {
    if (res || !T.complete(q, st)) return;
    res = T.eval(q, st);
    xp = opts.noRecord ? 0 : record(q, res.score, opts.mode || 'learn');
    if (res.score >= .999) { SND.ok(); buzzV(20); if (S.run && S.run % 5 === 0) fx('burst', 120); } else { SND.bad(); buzzV([40, 40, 40]); }
    xpFly(xp); draw(); opts.onDone && opts.onDone(res, xp);
    const fbEl = $('.fb:last-of-type', host); if (fbEl && fbEl.scrollIntoView) setTimeout(() => fbEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 50);
  }
  draw();
  return { st, check, get res() { return res; } };
}

/* ---------------- Sheets & zoom ---------------- */
function openSheet(html, bind) { const sh = $('#sheet'), box = $('#sheetBox'); box.innerHTML = html; sh.classList.add('on'); bind && bind(box); }
function closeSheet() { $('#sheet').classList.remove('on'); }
$('#sheet').addEventListener('click', e => { if (e.target.id === 'sheet') closeSheet(); });
function openZoom(key) { $('#zoomFig').innerHTML = D.figs[key]; $('#zoomer').classList.add('on'); }
$('#zoomClose').onclick = () => $('#zoomer').classList.remove('on');

/* ---------------- Router ---------------- */
const view = $('#view');
let timers = [];
const later = (fn, ms) => { const id = setTimeout(fn, ms); timers.push(id); return id; };
const every = (fn, ms) => { const id = setInterval(fn, ms); timers.push(id); return id; };
let keyHandler = null;
document.addEventListener('keydown', e => keyHandler && keyHandler(e));
const NAV = [['home', 'Wache', 'home'], ['learn', 'Lernen', 'learn'], ['cases', 'Einsätze', 'cases'], ['duelSetup', 'Duell', 'duel'], ['profile', 'Profil', 'profile']];
const NAVMAP = { session: 'learn', exam: 'learn', memos: 'learn', caseRun: 'cases', blitz: 'home', sprint: 'home' };
let current = 'home';
function go(v, arg) {
  timers.forEach(t => { clearTimeout(t); clearInterval(t); }); timers = []; keyHandler = null;
  current = v; view.onclick = null; closeSheet(); window.scrollTo(0, 0); VIEWS[v](arg);
  const nv = NAVMAP[v] || v;
  $('#nav').innerHTML = NAV.map(([k, l, ic]) => `<button data-go="${k}" ${k === nv ? 'aria-current="page"' : ''}>${IC[ic]}<span>${l}</span></button>`).join('');
}
$('#nav').addEventListener('click', e => { const b = e.target.closest('[data-go]'); if (b) go(b.dataset.go); });
document.addEventListener('click', e => { const b = e.target.closest('[data-goto]'); if (b) { go(b.dataset.goto, b.dataset.arg); } });

function renderTop() {
  const i = rankOf(S.xp), cur = RANKS[i][0], nxt = RANKS[i + 1] ? RANKS[i + 1][0] : cur;
  $('#xpPill').innerHTML = `${IC.star}${S.xp}`;
  const sn = streakNow(); $('#streakPill').innerHTML = `${IC.flame}${sn}`; $('#streakPill').title = `Serie: ${sn} Tage (Tagesziel ${DAILY_GOAL} Antworten)`;
  $('#lvlFill').style.width = (nxt > cur ? Math.min(100, (S.xp - cur) / (nxt - cur) * 100) : 100) + '%';
}

/* ---------------- Views ---------------- */
const VIEWS = {};

VIEWS.home = () => {
  const M = ensureMissions(), i = rankOf(S.xp), nx = RANKS[i + 1];
  const wk = []; const now = new Date(); const dow = (now.getDay() + 6) % 7;
  for (let k = 0; k < 7; k++) { const d = addDays(now, k - dow), key = dayKey(d); wk.push(`<span class="${S.hist[key] && S.hist[key].goal ? 'on' : ''} ${k === dow ? 'today' : ''}"><i></i>${'MDMDFSS'[k]}</span>`); }
  const h = hist(); const total = QN.length; const seen = seenN();
  let cd = '';
  if (S.settings.examDate) { const days = Math.ceil((new Date(S.settings.examDate + 'T09:00') - now) / 864e5); if (days >= 0) cd = `<div class="card between"><div><div class="eyebrow">Prüfungstermin</div><b>${new Date(S.settings.examDate).toLocaleDateString('de-DE', { weekday: 'long', day: 'numeric', month: 'long' })}</b></div><div class="countdown" style="font-size:28px;color:var(--red)">${days === 0 ? 'heute' : 'T−' + days}</div></div>`; }
  view.innerHTML = `
  <section class="card hero"><div class="beacon"></div>
    <div class="fms"><div class="seg">3</div><div><div class="eyebrow" style="color:#9FB6D8">FMS-Status</div><h2>Einsatz übernommen</h2><p>${greet()} Heute: ${h.n}/${DAILY_GOAL} Antworten für das Tagesziel.</p></div></div>
    <div class="bar g" style="margin-top:14px;background:rgba(255,255,255,.14)"><i style="width:${Math.min(100, h.n / DAILY_GOAL * 100)}%"></i></div>
    <div class="actions"><button class="btn pri grow" data-goto="learn">${IC.bolt.replace('<svg', '<svg width="18" height="18"')} Ausrücken – lernen</button></div>
  </section>
  ${cd}
  <section class="card"><div class="rank">${rankBadge(i)}<div style="flex:1"><div class="eyebrow">Dienstgrad</div><h3>${esc(RANKS[i][1])}</h3>
    <div class="bar" style="margin-top:8px"><i style="width:${nx ? (S.xp - RANKS[i][0]) / (nx[0] - RANKS[i][0]) * 100 : 100}%"></i></div>
    <div class="small muted" style="margin-top:6px">${nx ? `${nx[0] - S.xp} XP bis ${esc(nx[1])}` : 'Höchster Rang erreicht'}</div></div></div></section>
  <section class="card"><div class="between"><div class="eyebrow">Tagesmissionen</div><span class="tag">${M.list.filter(m => m.done).length}/3${M.bonus ? ' · Bonus ✓' : ''}</span></div>
    ${M.list.map(m => `<div class="mis ${m.done ? 'done' : ''}"><span class="ck">${m.done ? IC.check.replace('<svg', '<svg width="16" height="16"') : ''}</span><span class="t">${esc(MT[m.k].t(m))}<small>${m.p}/${m.goal} · +30 XP</small></span></div>`).join('')}
  </section>
  <section class="card"><div class="between" style="margin-bottom:10px"><div class="eyebrow">Diese Woche</div><span class="small muted">${IC.flame.replace('<svg', '<svg width="14" height="14" style="vertical-align:-2px;color:#FF7A1A"')} Serie ${streakNow()} · Rekord ${S.streak.best}</span></div><div class="week">${wk.join('')}</div></section>
  <div class="eyebrow" style="margin:6px 2px 10px">Einsatzarten</div>
  <section class="tiles">
    ${tile('learn', 'learn', 'Lernen', `${seen}/${total} gesehen`, 1)}
    ${tile('session', 'session', 'Übungsrunde', '10–30 Fragen', 2)}
    ${tile('exam', 'exam', 'Prüfung', 'Ohne Feedback, Zeit', 3)}
    ${tile('blitz', 'bolt', 'Blitzrunde', `Rekord ${S.blitz.best}`, 4, 1)}
    ${tile('sprint', 'triage', 'Sichtungssprint', `Rekord ${S.sprint.best}`, 5, 1)}
    ${tile('cases', 'siren', 'Boss-Einsätze', `${casesDone()}/${CASES.length} bestanden`, 6, 1)}
    ${tile('duelSetup', 'duel', 'Duell', 'NA vs. NotSan', 7, 1)}
    ${tile('memos', 'memo', 'Merkkarten', `${D.memos.length} Karten`, 8)}
  </section>`;
};
function tile(go, ic, t, s, n, hot) { return `<button class="tile ${hot ? 'hot' : ''}" data-goto="${go}"><span class="no">${n}</span>${IC[ic].replace('<svg', `<svg style="color:${hot ? 'var(--red)' : 'var(--blue)'}"`)}<span><b>${t}</b><small>${s}</small></span></button>`; }
function greet() { const h = new Date().getHours(); return h < 5 ? 'Ruhige Nacht?' : h < 11 ? 'Guten Morgen.' : h < 17 ? 'Guten Tag.' : h < 22 ? 'Guten Abend.' : 'Nachtdienst?'; }

/* ----- Learn (endless) ----- */
function filterChips(sel, all, attr, label = x => x) { return `<div class="chips">${all.map(k => `<button class="chip" data-${attr}="${k}" aria-pressed="${sel.includes(k)}">${esc(label(k))}</button>`).join('')}</div>`; }
function learnPool() {
  const L = S.settings.learn;
  return QN.filter(q => (!L.topics.length || L.topics.includes(q.topic)) && (!L.types.length || L.types.includes(q.t)) && q.lvl >= (L.lvl || 1) &&
    (L.status === 'all' || (L.status === 'new' && !S.prog[q.id]) || (L.status === 'wrong' && S.prog[q.id] && S.prog[q.id].ls < .999)));
}
let lastSeq = -1, recent = [];
function pickNext(pool) {
  if (!pool.length) return null;
  const o = S.settings.order;
  if (o === 'seq') { const idx = pool.findIndex(q => QN.indexOf(q) > lastSeq); const q = pool[idx >= 0 ? idx : 0]; lastSeq = QN.indexOf(q); return q; }
  const cand = pool.filter(q => !recent.includes(q.id)); const P = cand.length ? cand : pool;
  if (o === 'random') return pick(P);
  const now = Date.now();
  const w = q => { const p = S.prog[q.id]; if (!p) return 100 + Math.random() * 20; const age = (now - p.last) / 864e5; return (1 - p.ls) * 70 + (1 - p.best) * 20 + Math.min(age, 30) * 2 + Math.random() * 15; };
  return P.map(q => [w(q), q]).sort((a, b) => b[0] - a[0])[0][1];
}
VIEWS.learn = () => {
  const L = S.settings.learn;
  view.innerHTML = `<h2>Lernen</h2><div class="chips" style="margin:10px 0 12px"><button class="chip" data-goto="session">${IC.session.replace('<svg', '<svg width="14" height="14" style="vertical-align:-2px"')} Übungsrunde</button><button class="chip" data-goto="exam">${IC.exam.replace('<svg', '<svg width="14" height="14" style="vertical-align:-2px"')} Prüfung</button><button class="chip" data-goto="memos">${IC.memo.replace('<svg', '<svg width="14" height="14" style="vertical-align:-2px"')} Merkkarten</button></div>
  <details class="flt" id="flt"><summary>${I('<path d="M3 5h18M6 12h12M10 19h4"/>', 'width="18" height="18"')} Filter <span class="muted small" id="fltInfo"></span></summary><div class="in">
    <div><div class="eyebrow" style="margin-bottom:6px">Themen</div>${filterChips(L.topics, Object.keys(D.topics), 'tp', k => D.topics[k])}</div>
    <div><div class="eyebrow" style="margin-bottom:6px">Fragentypen</div>${filterChips(L.types, ['mtf', 'order', 'match', 'cloze', 'num', 'img'], 'ty', k => TYPE[k])}</div>
    <div><div class="eyebrow" style="margin-bottom:6px">Schwierigkeit</div><div class="chips">${[[1, 'Alle'], [2, 'ab ●●'], [3, 'nur ●●● (EDAIC-B-Niveau)']].map(([k, l]) => `<button class="chip" data-lv="${k}" aria-pressed="${(L.lvl || 1) === k}">${l}</button>`).join('')}</div></div>
    <div><div class="eyebrow" style="margin-bottom:6px">Auswahl</div><div class="chips">${[['all', 'Alle'], ['new', 'Offene'], ['wrong', 'Falsche']].map(([k, l]) => `<button class="chip" data-st="${k}" aria-pressed="${L.status === k}">${l}</button>`).join('')}</div></div>
    <div><div class="eyebrow" style="margin-bottom:6px">Reihenfolge</div><div class="chips">${[['smart', 'Schlau'], ['random', 'Zufällig'], ['seq', 'Nummer']].map(([k, l]) => `<button class="chip" data-or="${k}" aria-pressed="${S.settings.order === k}">${l}</button>`).join('')}</div><div class="small muted" style="margin-top:6px">„Schlau“ bevorzugt neue, falsche und lange nicht gesehene Fragen.</div></div>
  </div></details>
  <div class="card" id="qhost"></div>`;
  const info = () => { const n = learnPool().length; $('#fltInfo').textContent = `· ${n} Fragen`; };
  info();
  $('#flt').addEventListener('click', e => {
    const b = e.target.closest('.chip'); if (!b) return;
    if (b.dataset.tp) { const a = L.topics, k = b.dataset.tp; a.includes(k) ? a.splice(a.indexOf(k), 1) : a.push(k); }
    if (b.dataset.ty) { const a = L.types, k = b.dataset.ty; a.includes(k) ? a.splice(a.indexOf(k), 1) : a.push(k); }
    if (b.dataset.st) L.status = b.dataset.st;
    if (b.dataset.lv) L.lvl = +b.dataset.lv;
    if (b.dataset.or) S.settings.order = b.dataset.or;
    save(); const open = $('#flt').open; VIEWS.learn(); $('#flt').open = open;
  });
  nextQ();
};
function nextQ() {
  const host = $('#qhost'); if (!host) return;
  const pool = learnPool(); const q = pickNext(pool);
  if (!q) { host.innerHTML = `<p class="center muted">Keine Fragen für diese Filter. ${S.settings.learn.status === 'wrong' ? 'Keine offenen Fehler – stark!' : ''}</p>`; return; }
  recent.push(q.id); if (recent.length > 8) recent.shift();
  const p = S.prog[q.id];
  mountQuestion(host, q, { mode: 'learn', headExtra: p ? `<span class="tag">${p.n}× · best ${Math.round(p.best * 100)} %</span>` : '<span class="tag" style="background:var(--yellow);color:#1a1a1a">neu</span>', onNext: () => { nextQ(); window.scrollTo({ top: 0, behavior: 'smooth' }); } });
}

/* ----- Session ----- */
let sess = null;
VIEWS.session = (arg) => {
  if (arg === 'retry' && sess && sess.wrong.length) { startSession(sess.wrong.map(id => BYID[id])); return; }
  const cfg = S.settings.sess || (S.settings.sess = { n: 10, topics: [] });
  view.innerHTML = `<h2 style="margin-bottom:12px">Übungsrunde</h2><div class="card">
   <div class="eyebrow" style="margin-bottom:6px">Anzahl</div><div class="chips" id="sN">${[10, 20, 30].map(n => `<button class="chip" data-n="${n}" aria-pressed="${cfg.n === n}">${n} Fragen</button>`).join('')}</div>
   <div class="eyebrow" style="margin:14px 0 6px">Themen (leer = alle)</div><div id="sT">${filterChips(cfg.topics, Object.keys(D.topics), 'tp', k => D.topics[k])}</div>
   <p class="small muted">Sofortiges Feedback nach jeder Frage, am Ende Auswertung und „Falsche wiederholen“.</p>
   <button class="btn pri block" id="sGo">Runde starten</button></div>`;
  view.onclick = e => {
    const b = e.target.closest('.chip'); if (!b) return;
    if (b.dataset.n) cfg.n = +b.dataset.n;
    if (b.dataset.tp) { const a = cfg.topics, k = b.dataset.tp; a.includes(k) ? a.splice(a.indexOf(k), 1) : a.push(k); }
    save(); VIEWS.session();
  };
  $('#sGo').onclick = () => {
    view.onclick = null;
    const pool = QN.filter(q => !cfg.topics.length || cfg.topics.includes(q.topic));
    const qs = []; const P = pool.slice(); while (qs.length < Math.min(cfg.n, P.length)) { const q = pickNext(P.filter(x => !qs.includes(x))); qs.push(q); }
    startSession(shuffle(qs));
  };
};
function startSession(qs) {
  view.onclick = null;
  sess = { qs, i: 0, scores: [], xp: 0, wrong: [] };
  const draw = () => {
    const q = sess.qs[sess.i];
    view.innerHTML = `<div class="progressline"><span>Frage ${sess.i + 1}/${sess.qs.length}</span><div class="bar"><i style="width:${sess.i / sess.qs.length * 100}%"></i></div><span>${sess.xp} XP</span></div><div class="card" id="qhost"></div>`;
    mountQuestion($('#qhost'), q, {
      mode: 'session', nextLabel: sess.i + 1 < sess.qs.length ? 'Nächste Frage' : 'Auswertung',
      onDone: (res, xp) => { sess.scores.push(res.score); sess.xp += xp; if (res.score < .999) sess.wrong.push(q.id); },
      onNext: () => { sess.i++; if (sess.i < sess.qs.length) { draw(); window.scrollTo(0, 0); } else finish(); },
    });
  };
  const finish = () => {
    const pct = Math.round(sess.scores.reduce((a, b) => a + b, 0) / sess.scores.length * 100);
    emit('session', { pct });
    if (pct >= 80) { fx('rain', 220); SND.lvl(); }
    view.innerHTML = `<div class="card center"><div class="eyebrow">Übungsrunde beendet</div><div style="font-size:56px;font-weight:900;margin:8px 0;color:${pct >= 70 ? 'var(--ok)' : 'var(--bad)'}">${pct} %</div>
      <p>${sess.scores.filter(s => s >= .999).length} von ${sess.scores.length} vollständig richtig · <b>+${sess.xp} XP</b></p>
      <div class="actions">${sess.wrong.length ? `<button class="btn pri grow" data-goto="session" data-arg="retry">${sess.wrong.length} Fehler wiederholen</button>` : ''}<button class="btn grow" data-goto="session">Neue Runde</button><button class="btn grow" data-goto="home">Zur Wache</button></div></div>
      ${sess.wrong.length ? `<div class="card"><div class="eyebrow" style="margin-bottom:8px">Nicht ganz richtig</div>${sess.wrong.map(id => `<div class="small" style="padding:6px 0;border-top:1px solid var(--line)"><span class="tag">${id}</span> ${esc((BYID[id].stem || BYID[id].text || '').replace(/\{\d+\}/g, '…')).slice(0, 110)}…</div>`).join('')}</div>` : ''}`;
  };
  draw();
}

/* ----- Exam ----- */
let exam = null;
VIEWS.exam = () => {
  if (exam && !exam.done) return drawExam();
  view.innerHTML = `<h2 style="margin-bottom:12px">Prüfungssimulation</h2><div class="card">
   <p>Zufällige Fragen aus allen Themen, <b>ohne Feedback</b> bis zur Abgabe, mit Zeitlimit. Abgabe jederzeit möglich.</p>
   <div class="grid2"><button class="btn pri" data-ex="20">20 Fragen · 20 min</button><button class="btn pri" data-ex="40">40 Fragen · 40 min</button></div><button class="btn red block" style="margin-top:10px" data-ex="20" data-hard="1">Schwer: 20 Fragen ●●● · 25 min</button>
   ${S.exams.length ? `<hr><div class="eyebrow" style="margin-bottom:6px">Letzte Ergebnisse</div>${S.exams.slice(-5).reverse().map(e => `<div class="between small" style="padding:4px 0"><span>${new Date(e.date).toLocaleDateString('de-DE')} · ${e.n} Fragen</span><b style="color:${e.pct >= 70 ? 'var(--ok)' : 'var(--bad)'}">${e.pct} %</b></div>`).join('')}` : ''}</div>`;
  view.onclick = e => {
    const b = e.target.closest('[data-ex]'); if (!b) return; view.onclick = null;
    const n = +b.dataset.ex, hard = !!b.dataset.hard; const byT = {}; QN.filter(q => !hard || q.lvl >= 3).forEach(q => (byT[q.topic] = byT[q.topic] || []).push(q));
    const qs = []; const ts = Object.keys(byT); let k = 0; const pools = Object.fromEntries(ts.map(t => [t, shuffle(byT[t])]));
    while (qs.length < n && ts.some(t => pools[t].length)) { const t = ts[k++ % ts.length]; if (pools[t].length) qs.push(pools[t].pop()); }
    exam = { qs: shuffle(qs).map(q => q.id), st: {}, i: 0, end: Date.now() + (hard ? 25 : n) * 60000, done: false, hard };
    drawExam();
  };
};
function drawExam() {
  view.onclick = null;
  const q = BYID[exam.qs[exam.i]];
  const st = exam.st[q.id] || (exam.st[q.id] = TYPES[q.t].init(q));
  view.innerHTML = `<div class="between" style="margin-bottom:10px"><b>Prüfung · Frage ${exam.i + 1}/${exam.qs.length}</b><span class="pill" style="color:var(--ink);background:var(--chip);border-color:var(--line)" id="exT"></span></div>
   <div class="card exgrid" id="exG">${exam.qs.map((id, k) => { const Q = BYID[id], s = exam.st[id]; return `<button data-k="${k}" class="${s && TYPES[Q.t].complete(Q, s) ? 'a' : ''} ${k === exam.i ? 'cur' : ''}">${k + 1}</button>`; }).join('')}</div>
   <div class="card" id="qhost"></div>
   <div class="actions"><button class="btn" id="exPrev" ${exam.i ? '' : 'disabled'}>Zurück</button><button class="btn pri grow" id="exNext">${exam.i + 1 < exam.qs.length ? 'Weiter' : 'Zur Abgabe'}</button><button class="btn red" id="exEnd">Abgeben</button></div>`;
  mountQuestion($('#qhost'), q, { exam: true, st, noRecord: true, onAnswer: () => { const b = $(`#exG [data-k="${exam.i}"]`); if (b) b.classList.toggle('a', TYPES[q.t].complete(q, st)); } });
  $('#exG').onclick = e => { const b = e.target.closest('[data-k]'); if (b) { exam.i = +b.dataset.k; drawExam(); } };
  $('#exPrev').onclick = () => { exam.i--; drawExam(); };
  $('#exNext').onclick = () => { if (exam.i + 1 < exam.qs.length) { exam.i++; drawExam(); window.scrollTo(0, 0); } else confirmEnd(); };
  $('#exEnd').onclick = confirmEnd;
  const tick = () => { const left = Math.max(0, exam.end - Date.now()); const el = $('#exT'); if (el) el.textContent = `⏱ ${Math.floor(left / 60000)}:${pad(Math.floor(left / 1000) % 60)}`; if (!left) finishExam(); };
  tick(); every(tick, 1000);
}
function confirmEnd() {
  const open = exam.qs.filter(id => { const s = exam.st[id]; return !s || !TYPES[BYID[id].t].complete(BYID[id], s); }).length;
  openSheet(`<h3>Prüfung abgeben?</h3><p class="muted">${open ? `${open} Frage(n) unbeantwortet.` : 'Alle Fragen beantwortet.'}</p><div class="actions"><button class="btn pri grow" id="cfY">Abgeben</button><button class="btn grow" id="cfN">Weiter bearbeiten</button></div>`, b => { $('#cfY', b).onclick = () => { closeSheet(); finishExam(); }; $('#cfN', b).onclick = closeSheet; });
}
function finishExam() {
  if (exam.done) return; exam.done = true; timers.forEach(t => clearInterval(t));
  let sum = 0, xp = 0; const res = {};
  exam.qs.forEach(id => { const q = BYID[id], st = exam.st[id]; let sc = 0; if (st && TYPES[q.t].complete(q, st)) { sc = TYPES[q.t].eval(q, st).score; xp += record(q, sc, 'exam'); } res[id] = sc; sum += sc; });
  const pct = Math.round(sum / exam.qs.length * 100);
  S.exams.push({ date: Date.now(), n: exam.qs.length, pct }); exam.res = res; save(); checkBadges();
  if (pct >= 70) { fx('rain', 240); SND.lvl(); } else SND.bad();
  view.innerHTML = `<div class="card center"><div class="eyebrow">Prüfungsergebnis</div><div style="font-size:60px;font-weight:900;color:${pct >= 70 ? 'var(--ok)' : 'var(--bad)'}">${pct} %</div><p>${pct >= 70 ? 'Bestanden – stark!' : 'Noch nicht bestanden – die Fehler unten durchgehen.'} · +${xp} XP</p></div>
   <div class="card"><div class="eyebrow" style="margin-bottom:8px">Fragen nachsehen</div><div class="exgrid" id="exR">${exam.qs.map((id, k) => `<button data-k="${k}" class="${res[id] >= .999 ? 'r' : 'x'}">${k + 1}</button>`).join('')}</div></div>
   <div class="card" id="qhost"><p class="muted small center">Nummer antippen, um Frage mit Lösung zu sehen.</p></div>
   <div class="actions"><button class="btn pri grow" data-goto="exam">Neue Prüfung</button><button class="btn grow" data-goto="home">Zur Wache</button></div>`;
  $('#exR').onclick = e => { const b = e.target.closest('[data-k]'); if (!b) return; const q = BYID[exam.qs[+b.dataset.k]]; const st = exam.st[q.id] || TYPES[q.t].init(q); const r = TYPES[q.t].complete(q, st) ? TYPES[q.t].eval(q, st) : { score: 0, parts: [], x: NaN }; if (!r.parts) r.parts = []; mountQuestion($('#qhost'), q, { st, res: r, noRecord: true, nextLabel: 'Schließen', onNext: () => { $('#qhost').innerHTML = ''; } }); $('#qhost').scrollIntoView({ behavior: 'smooth' }); };
  exam = Object.assign(exam, { done: true });
}

/* ----- Memos ----- */
VIEWS.memos = () => {
  const f = S.settings.memoTopic || '';
  const list = D.memos.filter(m => !f || m.topic === f);
  view.innerHTML = `<h2 style="margin-bottom:10px">Merkkarten</h2><div class="chips" style="margin-bottom:12px" id="mF"><button class="chip" data-t="" aria-pressed="${!f}">Alle</button>${[...new Set(D.memos.map(m => m.topic))].map(t => `<button class="chip" data-t="${t}" aria-pressed="${f === t}">${esc(D.topics[t])}</button>`).join('')}</div>
  ${list.map(m => `<div class="memocard"><h3 style="background:${TOPIC_COL[m.topic]};cursor:pointer" data-m="${m.id}">${esc(m.title)} <span>${S.memoSeen[m.id] ? '✓' : '＋'}</span></h3><div class="${S.settings.memoOpen === m.id ? '' : 'hidden'}" id="mb_${m.id}"><table>${m.rows.map(r => `<tr><td>${esc(r[0])}</td><td>${esc(r[1])}</td></tr>`).join('')}</table><div class="src" style="padding:0 12px 10px">${linkify(m.src)}</div></div></div>`).join('')}`;
  view.onclick = e => {
    const c = e.target.closest('#mF .chip'); if (c) { S.settings.memoTopic = c.dataset.t; save(); view.onclick = null; VIEWS.memos(); return; }
    const h = e.target.closest('[data-m]'); if (!h) return; const id = h.dataset.m; const b = $('#mb_' + id); b.classList.toggle('hidden');
    if (!b.classList.contains('hidden') && !S.memoSeen[id]) { S.memoSeen[id] = Date.now(); h.querySelector('span').textContent = '✓'; emit('memo', {}); }
  };
};

/* ----- Cases (Boss-Einsätze) ----- */
VIEWS.cases = () => {
  view.onclick = null;
  view.innerHTML = `<h2>Boss-Einsätze</h2><p class="muted small" style="margin:6px 0 14px">Verzweigte Fälle mit 3 Leben. Falsche Entscheidungen kosten ein Herz und verschlechtern den Patienten. Pro Einsatz je ein Joker: 50:50 und Hintergrunddienst.</p>
  ${CASES.map(c => { const r = S.cases[c.id]; const st = r ? r.best : 0; return `<button class="casecard" data-goto="caseRun" data-arg="${c.id}"><span class="ic" style="background:${TOPIC_COL[c.topic]}">${c.topic}</span><span style="flex:1"><b>${esc(c.title)}</b><br><span class="small muted">${esc(D.topics[c.topic])} · ${c.nodes.filter(n => !n.end).length} Entscheidungen</span></span><span class="stars">${[1, 2, 3].map(k => `<span class="${k <= st ? '' : 'off'}">★</span>`).join('')}</span></button>`; }).join('')}`;
};
function rhythmSVG(rhy) {
  const r = String(rhy || ''); let d = 'M0 12';
  if (/VF|flimmern/i.test(r)) { for (let x = 0; x <= 200; x += 4) d += ` L${x} ${12 + Math.sin(x * .35) * 6 + Math.sin(x * .13) * 3}`; }
  else if (/Asystolie|–|PEA|CPR/i.test(r) && !/Sinus/.test(r)) { d += ' L200 12'; if (/PEA/.test(r)) { d = 'M0 12'; for (let x = 0; x < 200; x += 40) d += ` L${x + 14} 12 L${x + 17} 4 L${x + 20} 18 L${x + 23} 12 L${x + 40} 12`; } }
  else { for (let x = 0; x < 200; x += 34) d += ` L${x + 12} 12 L${x + 14} 10 L${x + 16} 12 L${x + 19} 12 L${x + 21} 2 L${x + 23} 20 L${x + 25} 12 L${x + 30} 11 L${x + 34} 12`; }
  return `<svg viewBox="0 0 200 24" preserveAspectRatio="none"><path d="${d}" fill="none" stroke="#3CF0A0" stroke-width="1.6"/></svg>`;
}
let crun = null;
VIEWS.caseRun = (id) => {
  const c = BYID[id]; if (!c) return go('cases');
  crun = { c, node: c.nodes[0].id, hearts: 3, j50: true, jtel: true, vit: Object.assign({}, c.vit), xp: 0, answered: null, hidden: [], hint: false, ord: {}, wrongs: 0 };
  drawCase(true);
};
function drawCase(intro) {
  const { c } = crun; const n = c.nodes.find(x => x.id === crun.node);
  const prevVit = Object.assign({}, crun.vit);
  if (n.vit && !crun.answered) Object.assign(crun.vit, n.vit);
  const V = crun.vit; const chg = k => prevVit[k] !== V[k] && !intro ? 'changed' : '';
  const mon = `<div class="monitor"><div class="rhy">${esc(V.rhy || 'Monitor')}${rhythmSVG(V.rhy)}</div>
    <div class="v hf ${chg('HF')} ${V.HF === '–' ? '' : 'blink'}"><small>HF</small><b>${esc(V.HF ?? '–')}</b></div><div class="v rr ${chg('RR')}"><small>RR</small><b>${esc(V.RR ?? '–')}</b></div><div class="v sp ${chg('SpO2')}"><small>SpO₂</small><b>${esc(V.SpO2 ?? '–')}</b></div>
    <div class="v af ${chg('AF')}"><small>AF</small><b>${esc(V.AF ?? '–')}</b></div><div class="v gcs ${chg('GCS')}"><small>GCS</small><b>${esc(V.GCS ?? '–')}</b></div><div class="v xt ${chg('etCO2') || chg('BZ') || chg('T')}"><small>${V.etCO2 !== undefined ? 'etCO₂' : V.BZ !== undefined ? 'BZ' : V.T !== undefined ? 'Temp' : 'etCO₂'}</small><b>${esc(V.etCO2 ?? V.BZ ?? V.T ?? '–')}</b></div></div>`;
  const hearts = `<div class="hearts">${[0, 1, 2].map(k => k < crun.hearts ? IC.heart : IC.heartOff).join('')}</div>`;
  let body;
  if (n.end) {
    const stars = crun.hearts; const first = !(S.cases[c.id] && S.cases[c.id].done);
    const bonus = 20 * stars + (first ? 30 : 0);
    const rec = S.cases[c.id] || (S.cases[c.id] = { best: 0, done: false, runs: 0 }); rec.runs++; rec.done = true; rec.best = Math.max(rec.best, stars);
    addXP(bonus); crun.xp += bonus; emit('case', { success: true, stars }); fx('rain', 240); SND.lvl();
    body = `<div class="card center"><div class="eyebrow">Einsatz abgeschlossen</div><h2 style="margin:8px 0">${'★'.repeat(stars)}${'☆'.repeat(3 - stars)}</h2><p>${esc(n.txt)}</p><p><b>+${crun.xp} XP</b> in diesem Einsatz</p><div class="src">${linkify(c.src)}</div>
      <div class="actions"><button class="btn pri grow" data-goto="caseRun" data-arg="${c.id}">Nochmal</button><button class="btn grow" data-goto="cases">Alle Einsätze</button></div></div>`;
  } else if (crun.hearts <= 0 && !crun.answered) {
    emit('case', { success: false });
    body = `<div class="card center"><div class="eyebrow" style="color:var(--bad)">Einsatz gescheitert</div><h2 style="margin:8px 0">Debriefing</h2><p>Alle Leben verbraucht. Lies die Rückmeldungen und versuche es erneut – Fehler sind hier ausdrücklich erlaubt.</p><div class="src">${linkify(c.src)}</div>
      <div class="actions"><button class="btn pri grow" data-goto="caseRun" data-arg="${c.id}">Neuer Versuch</button><button class="btn grow" data-goto="cases">Alle Einsätze</button></div></div>`;
  } else {
    if (!crun.ord[n.id]) crun.ord[n.id] = shuffle(n.ch.map((_, i) => i));
    const ans = crun.answered;
    body = `<div class="card">${n === c.nodes[0] ? `<p style="margin-top:0"><b>Einsatzmeldung:</b> ${esc(c.intro)}</p><hr>` : ''}${n.txt && n.txt !== '—' ? `<p style="margin-top:0">${esc(n.txt)}</p>` : ''}<div class="stem">${esc(n.q)}</div>
      <div class="opts">${crun.ord[n.id].map(i => { const ch = n.ch[i]; const hid = crun.hidden.includes(i); const dis = ans || hid || (crun.wrongTried || []).includes(i); const cls = ans && ans.i === i ? (ch[1] ? 'right' : 'wrong') : ((crun.wrongTried || []).includes(i) ? 'wrong' : (crun.hint && ch[1] && !ans ? '' : '')); return `<button class="opt ${cls}" data-c="${i}" ${dis ? 'disabled' : ''} style="${hid ? 'opacity:.25;text-decoration:line-through' : ''}${crun.hint && ch[1] && !ans ? ';border-color:var(--yellow);box-shadow:0 0 0 3px rgba(255,194,26,.35)' : ''}">${esc(ch[0])}</button>`; }).join('')}</div>
      ${ans ? `<div class="fb"><div class="res" style="color:${ans.ok ? 'var(--ok)' : 'var(--bad)'}">${ans.ok ? 'Richtige Entscheidung' : 'Fehlentscheidung – ein Herz verloren'}</div><p class="ex">${esc(n.ch[ans.i][2])}</p></div>
        <div class="actions"><button class="btn pri grow" id="cNext">${ans.ok || ans.go ? 'Weiter' : 'Neu entscheiden'}</button></div>` :
        `<div class="actions jokers"><button class="btn sm" id="j50" ${crun.j50 ? '' : 'disabled'}>50:50</button><button class="btn sm" id="jtel" ${crun.jtel ? '' : 'disabled'}>${IC.phone.replace('<svg', '<svg width="16" height="16"')} Hintergrunddienst</button></div>`}
    </div>`;
  }
  view.innerHTML = `<div class="between" style="margin-bottom:10px"><div><div class="eyebrow">${esc(D.topics[c.topic])}</div><h2 style="font-size:20px">${esc(c.title)}</h2></div>${hearts}</div>${mon}<div style="height:12px"></div>${body}`;
  view.onclick = e => {
    const b = e.target.closest('[data-c]');
    if (b && !b.disabled && !crun.answered) {
      const i = +b.dataset.c, ch = n.ch[i], ok = !!ch[1]; const go2 = ch[3] || null;
      crun.answered = { i, ok, go: go2 }; countAnswer(ok);
      if (ok) { const xp = crun.hint ? 6 : 15; crun.xp += xp; addXP(xp); xpFly(xp); SND.ok(); buzzV(20); }
      else { crun.hearts--; crun.wrongs++; SND.bad(); buzzV([60, 40, 60]); (crun.wrongTried = crun.wrongTried || []).push(i); if (ch[4]) Object.assign(crun.vit, ch[4]); else worsen(); }
      save(); drawCase(); return;
    }
  };
  const nx = $('#cNext'); if (nx) nx.onclick = () => {
    const a = crun.answered; crun.answered = null; crun.hint = false; crun.hidden = [];
    if (crun.hearts <= 0) { drawCase(); return; }
    if (a.ok) { crun.wrongTried = []; crun.node = a.go || n.next; }
    else if (a.go) { crun.wrongTried = []; crun.node = a.go; }
    drawCase(); window.scrollTo({ top: 0, behavior: 'smooth' });
  };
  const j5 = $('#j50'); if (j5) j5.onclick = () => { const wr = n.ch.map((c2, i) => i).filter(i => !n.ch[i][1] && !(crun.wrongTried || []).includes(i)); if (wr.length) crun.hidden.push(pick(wr)); crun.j50 = false; SND.tick(); drawCase(); };
  const jt = $('#jtel'); if (jt) jt.onclick = () => { crun.hint = true; crun.jtel = false; toast('Hintergrunddienst: „Ich würde die markierte Option wählen.“', IC.phone); drawCase(); };
}
function worsen() {
  const v = crun.vit; const num = x => typeof x === 'number';
  if (num(v.SpO2)) v.SpO2 = Math.max(60, v.SpO2 - 4);
  if (num(v.HF)) v.HF = v.HF > 60 ? v.HF + 8 : Math.max(30, v.HF - 4);
  if (typeof v.RR === 'string' && /\d+\/\d+/.test(v.RR)) { const [a, b] = v.RR.split('/').map(Number); v.RR = `${Math.max(50, a - 8)}/${Math.max(30, b - 5)}`; }
}

/* ----- Blitzrunde ----- */
const STMTS = []; QN.filter(q => q.t === 'mtf').forEach(q => q.items.forEach(it => STMTS.push({ t: it[0], v: it[1], why: it[2], q: q.id, topic: q.topic })));
VIEWS.blitz = () => {
  view.onclick = null;
  view.innerHTML = `<h2>Blitzrunde</h2><div class="card"><p>60 Sekunden, ${STMTS.length} Aussagen im Pool: <b>Wahr oder falsch?</b> Jede 5er-Serie erhöht den Multiplikator (bis ×3). Wischen (rechts = wahr, links = falsch), Tasten ←/→ oder Buttons.</p>
   <div class="between"><span class="muted small">Rekord: <b>${S.blitz.best}</b> · Runden: ${S.blitz.runs}</span><button class="btn pri" id="bGo">${IC.bolt.replace('<svg', '<svg width="18" height="18"')} Start</button></div></div>`;
  $('#bGo').onclick = runBlitz;
};
function runBlitz() {
  const pool = shuffle(STMTS); let k = 0, score = 0, combo = 0, n = 0, wrong = [], right = 0; const T = 60, t0 = Date.now(); let locked = false;
  SND.siren();
  view.innerHTML = `<div class="arena"><div class="score"><span class="big" id="bS">0</span><span class="combo" id="bC"></span><span id="bT">60 s</span></div><div class="timer"><i id="bBar" style="width:100%"></i></div>
   <div class="card stmt" id="bQ"></div><div class="bigbtns"><button class="bf" data-a="0">FALSCH</button><button class="bw" data-a="1">WAHR</button></div><p class="center small muted">Wischen: ← falsch · wahr →</p></div>`;
  const showQ = () => { $('#bQ').textContent = pool[k % pool.length].t; };
  const answer = v => {
    if (locked) return; const s = pool[k % pool.length]; n++; const el = $('#bQ');
    if (v === s.v) { combo++; right++; const mult = Math.min(3, 1 + Math.floor(combo / 5)); score += mult; SND.ok(); el.className = 'card stmt ok'; if (combo % 5 === 0) { toast(`Combo ×${Math.min(3, 1 + combo / 5)}`, IC.bolt); } }
    else { combo = 0; wrong.push(s); SND.bad(); buzzV(50); el.className = 'card stmt no'; }
    void el.offsetWidth; k++; $('#bS').textContent = score; $('#bC').textContent = combo >= 5 ? `×${Math.min(3, 1 + Math.floor(combo / 5))} · ${combo}er` : combo ? `${combo}er` : ''; showQ();
  };
  showQ();
  view.querySelector('.bigbtns').onclick = e => { const b = e.target.closest('[data-a]'); if (b) answer(b.dataset.a === '1'); };
  keyHandler = e => { if (e.key === 'ArrowRight') answer(true); if (e.key === 'ArrowLeft') answer(false); };
  let sx = null; const q = $('#bQ');
  q.onpointerdown = e => { sx = e.clientX; }; q.onpointerup = e => { if (sx === null) return; const dx = e.clientX - sx; sx = null; if (Math.abs(dx) > 50) answer(dx > 0); };
  every(() => {
    const left = Math.max(0, T - (Date.now() - t0) / 1000); $('#bBar').style.width = (left / T * 100) + '%'; $('#bT').textContent = Math.ceil(left) + ' s';
    if (left <= 0) {
      locked = true; timers.forEach(t => clearInterval(t)); keyHandler = null;
      const rec = score > S.blitz.best; S.blitz.best = Math.max(S.blitz.best, score); S.blitz.runs++;
      const xp = score * 2; for (let i = 0; i < Math.floor(right / 2); i++) countAnswer(true); addXP(xp); emit('blitz', { score });
      if (rec) { fx('rain', 220); SND.lvl(); }
      view.innerHTML = `<div class="card center"><div class="eyebrow">Blitzrunde beendet</div><div style="font-size:60px;font-weight:900">${score}</div><p>${right}/${n} richtig · +${xp} XP ${rec ? '· <b style="color:var(--yellow)">Neuer Rekord!</b>' : ''}</p><div class="actions"><button class="btn pri grow" id="bAgain">Nochmal</button><button class="btn grow" data-goto="home">Zur Wache</button></div></div>
      ${wrong.length ? `<div class="card"><div class="eyebrow" style="margin-bottom:8px">Daneben – zum Nachlesen</div>${wrong.map(s => `<div class="it wrong" style="margin-bottom:8px"><div class="tx">${esc(s.t)}<div class="sol" style="color:${s.v ? 'var(--ok)' : 'var(--bad)'}">${s.v ? 'WAHR' : 'FALSCH'}</div><div class="why">${esc(s.why)} <span class="tag">${s.q}</span></div></div></div>`).join('')}</div>` : ''}`;
      $('#bAgain').onclick = runBlitz;
    }
  }, 100);
}

/* ----- Sichtungssprint ----- */
const GREEN_TXT = ['Läuft umher, Schnittwunde am Unterarm', 'Steht neben dem Bus, klagt über Nackenschmerzen', 'Geht selbstständig, Prellung am Knie', 'Hilft anderen, Platzwunde an der Stirn', 'Kommt auf Sie zu, Handgelenk geschwollen', 'Läuft, weint, Schürfwunden an beiden Händen'];
const LIE_TXT = ['Liegt am Boden, Oberschenkel fehlgestellt', 'Sitzt eingeklemmt, Schmerzen im Becken', 'Liegt neben dem Fahrzeug, Prellmarken am Thorax', 'Liegt auf dem Rücken, offene Unterschenkelfraktur', 'Sitzt am Straßenrand, kann nicht aufstehen', 'Liegt im Gras, Verbrennungen an beiden Armen', 'Liegt bäuchlings, Kopfplatzwunde', 'Sitzt an eine Wand gelehnt, Bauchschmerzen'];
const AGE = () => pick(['Mann, ca. 30', 'Frau, ca. 45', 'Jugendlicher, ca. 16', 'Frau, ca. 70', 'Mann, ca. 55', 'Frau, ca. 25']);
function genPatient(algo) {
  const r = Math.random();
  if (algo === 'prior') {
    const walk = r < .3; const p = { walk, txt: walk ? pick(GREEN_TXT) : pick(LIE_TXT), A: 'wach, Atemweg frei', B: `AF ${14 + rnd(10)}/min, unauffällig`, C: 'Radialis tastbar, Rekap < 2 s', D: 'orientiert, befolgt Aufforderungen', E: 'keine starken Rumpfschmerzen' };
    let red = null;
    if (!walk && Math.random() < .55) {
      const k = pick(['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D', 'E']);
      if (k === 'A1') { p.A = 'bewusstlos'; red = 'A: Bewusstlosigkeit'; }
      if (k === 'A2') { p.A = 'gurgelnde Atmung, drohende Verlegung'; red = 'A: drohende Atemwegsverlegung'; }
      if (k === 'B1') { p.B = `AF ${32 + rnd(10)}/min, angestrengt`; red = 'B: deutliche Störung der Atemfrequenz'; }
      if (k === 'B2') { p.B = 'lautes pathologisches Atemgeräusch (Stridor)'; red = 'B: pathologisches Atemgeräusch'; }
      if (k === 'C1') { p.C = 'Radialis nicht tastbar'; red = 'C: fehlender Radialispuls'; }
      if (k === 'C2') { p.C = 'starke Blutung Oberschenkel'; red = 'C: starke Blutung'; }
      if (k === 'D') { p.D = 'desorientiert, befolgt Aufforderungen nicht'; red = 'D: Bewusstseinsstörung'; }
      if (k === 'E') { p.E = 'starke Schmerzen im Becken/Bauch'; red = 'E: starke Rumpfschmerzen'; }
    }
    p.cat = red ? 'r' : walk ? 'g' : 'y'; p.why = red || (walk ? 'Kein Indikator positiv, gehfähig → grün' : 'Kein Indikator positiv, nicht gehfähig → gelb');
    p.rows = [['A', p.A], ['B', p.B], ['C', p.C], ['D', p.D], ['E', p.E], ['Gehfähig', walk ? 'ja' : 'nein']];
    return p;
  }
  // mSTaRT
  const p = { walk: false, bleed: false, breath: 'ja', af: 14 + rnd(12), radial: true, rekap: 1 + rnd(2) * .5, cmd: true };
  if (r < .25) p.walk = true;
  else if (r < .33) p.bleed = true;
  else if (r < .40) p.breath = 'nein';
  else if (r < .46) p.breath = 'nach Atemwegsöffnung';
  else if (r < .56) p.af = 32 + rnd(10);
  else if (r < .64) { if (Math.random() < .5) p.radial = false; else p.rekap = 3 + rnd(2); }
  else if (r < .72) p.cmd = false;
  p.txt = p.walk ? pick(GREEN_TXT) : pick(LIE_TXT);
  if (p.walk) { p.cat = 'g'; p.why = 'Gehfähig → SK III'; }
  else if (p.bleed) { p.cat = 'r'; p.why = 'Spritzende Blutung → Blutstillung, SK I'; }
  else if (p.breath === 'nein') { p.cat = 'b'; p.why = 'Keine Atmung nach Atemwegsöffnung → tot (ex)'; }
  else if (p.breath === 'nach Atemwegsöffnung') { p.cat = 'r'; p.why = 'Atmung erst nach Atemwegsöffnung → SK I'; }
  else if (p.af > 30) { p.cat = 'r'; p.why = 'AF > 30/min → SK I'; }
  else if (!p.radial || p.rekap > 2) { p.cat = 'r'; p.why = 'Radialispuls fehlt/Rekap > 2 s → SK I'; }
  else if (!p.cmd) { p.cat = 'r'; p.why = 'Befolgt Aufforderungen nicht → SK I'; }
  else { p.cat = 'y'; p.why = 'Kein Sofortkriterium, nicht gehfähig → SK II'; }
  const breathTxt = p.breath === 'ja' ? 'vorhanden' : p.breath === 'nein' ? 'keine – auch nach Atemwegsöffnung' : 'erst nach Atemwegsöffnung';
  p.rows = p.walk ? [['Gehfähig', 'ja']] : [['Gehfähig', 'nein'], ['Blutung', p.bleed ? 'spritzend, Oberschenkel' : 'keine relevante'], ['Atmung', breathTxt],
    ...(p.breath === 'nein' ? [] : [['AF', p.af + '/min'], ['Radialispuls', p.radial ? 'tastbar' : 'nicht tastbar'], ['Rekap', fmtNum(p.rekap, 1) + ' s'], ['Aufforderungen', p.cmd ? 'befolgt' : 'befolgt nicht']])];
  return p;
}
VIEWS.sprint = () => {
  view.onclick = null; const algo = S.settings.algo;
  view.innerHTML = `<h2>Sichtungssprint</h2><div class="card"><p>90 Sekunden Vorsichtung beim MANV. Ordnen Sie jedem Patienten die Kategorie zu. Fehler kosten 5 Sekunden.</p>
   <div class="eyebrow" style="margin-bottom:6px">Algorithmus</div><div class="chips" id="alg"><button class="chip" data-al="mstart" aria-pressed="${algo === 'mstart'}">mSTaRT</button><button class="chip" data-al="prior" aria-pressed="${algo === 'prior'}">PRIOR (ABCDE)</button></div>
   <p class="small muted">${algo === 'prior' ? 'PRIOR: jeder positive ABCDE-Indikator → rot; sonst gehfähig → grün, nicht gehfähig → gelb.' : 'mSTaRT: Gehen → Blutung → Atmung → AF > 30 → Puls/Rekap → Aufforderungen.'}</p>
   <div class="between"><span class="muted small">Rekord: <b>${S.sprint.best}</b></span><button class="btn pri" id="spGo">Start</button></div></div>`;
  $('#alg').onclick = e => { const b = e.target.closest('[data-al]'); if (b) { S.settings.algo = b.dataset.al; save(); VIEWS.sprint(); } };
  $('#spGo').onclick = runSprint;
};
function runSprint() {
  const algo = S.settings.algo; let T = 90, t0 = Date.now(), correct = 0, err = 0, combo = 0, p = genPatient(algo), nr = 1, locked = false; const errs = [];
  SND.siren();
  view.innerHTML = `<div class="arena"><div class="score"><span class="big" id="spS">0</span><span class="combo" id="spC"></span><span id="spT">90 s</span></div><div class="timer"><i id="spBar" style="width:100%"></i></div>
   <div class="pcard" id="spP"></div>
   <div class="triage"><button class="tr-r" data-k="r">SK I · rot</button><button class="tr-y" data-k="y">SK II · gelb</button><button class="tr-g" data-k="g">SK III · grün</button>${algo === 'mstart' ? '<button class="tr-b" data-k="b">tot · ex</button>' : ''}</div></div>`;
  const drawP = () => { $('#spP').innerHTML = `<div class="pid">Patient ${nr} · ${AGE()}</div><h3>${esc(p.txt)}</h3><div class="vs">${p.rows.map(r => `<div>${esc(r[0])}<b>${esc(r[1])}</b></div>`).join('')}</div>`; };
  drawP();
  view.querySelector('.triage').onclick = e => {
    const b = e.target.closest('[data-k]'); if (!b || locked) return;
    if (b.dataset.k === p.cat) { correct++; combo++; SND.ok(); $('#spP').style.borderColor = 'var(--ok)'; }
    else { err++; combo = 0; T -= 5; SND.bad(); buzzV(60); errs.push(p); $('#spP').style.borderColor = 'var(--bad)'; toast(p.why, IC.triage); }
    $('#spS').textContent = correct; $('#spC').textContent = combo >= 3 ? `${combo}er-Serie` : '';
    locked = true; later(() => { locked = false; p = genPatient(algo); nr++; $('#spP').style.borderColor = ''; drawP(); }, 260);
  };
  every(() => {
    const left = Math.max(0, T - (Date.now() - t0) / 1000); $('#spBar').style.width = (left / 90 * 100) + '%'; $('#spT').textContent = Math.ceil(left) + ' s';
    if (left <= 0) {
      timers.forEach(t => { clearInterval(t); clearTimeout(t); });
      const rec = correct > S.sprint.best; S.sprint.best = Math.max(S.sprint.best, correct); S.sprint.runs++;
      const xp = correct * 3; addXP(xp); emit('sprint', { correct }); if (rec) { fx('rain', 220); SND.lvl(); }
      const lbl = { r: 'SK I rot', y: 'SK II gelb', g: 'SK III grün', b: 'tot (ex)' };
      view.innerHTML = `<div class="card center"><div class="eyebrow">Sichtungssprint beendet · ${algo === 'prior' ? 'PRIOR' : 'mSTaRT'}</div><div style="font-size:60px;font-weight:900">${correct}</div><p>${correct} richtig, ${err} Fehler · +${xp} XP ${rec ? '· <b style="color:var(--yellow)">Neuer Rekord!</b>' : ''}</p><div class="actions"><button class="btn pri grow" id="spAgain">Nochmal</button><button class="btn grow" data-goto="home">Zur Wache</button></div></div>
      ${errs.length ? `<div class="card"><div class="eyebrow" style="margin-bottom:8px">Fehlsichtungen</div>${errs.map(e => `<div class="it wrong" style="margin-bottom:8px"><div class="tx"><b>${esc(e.txt)}</b><div class="why">${e.rows.map(r => r.join(': ')).join(' · ')}</div><div class="sol">Richtig: ${lbl[e.cat]} – ${esc(e.why)}</div></div></div>`).join('')}</div>` : ''}
      <div class="src">${linkify(algo === 'prior' ? 'PRIOR-Vorsichtung (Bubser et al.; DGKM/BBK). Vereinfachte Lernversion – regionale Vorgaben beachten.' : 'mSTaRT (Kanz et al., Notfall + Rettungsmedizin 2006). Vereinfachte Lernversion – regionale Vorgaben beachten.')}</div>`;
      $('#spAgain').onclick = runSprint;
    }
  }, 100);
}

/* ----- Duel ----- */
const NUMQ = QN.filter(q => q.t === 'num');
function numChoices(q) {
  const a = q.ans, dec = (String(a).split('.')[1] || '').length; const out = new Set([a]);
  const facs = shuffle([.5, .75, 1.25, 1.5, 2, .25, 3, .1, 10]);
  for (const f of facs) { if (out.size >= 4) break; let v = +(a * f).toFixed(dec); if (Math.abs(v - a) <= Math.max(q.tol * 2, Math.abs(a) * .1)) continue; if (v <= 0) continue; out.add(v); }
  let k = 1; while (out.size < 4) { out.add(+(a + k * Math.max(1, q.tol * 3)).toFixed(dec)); k++; }
  return shuffle([...out]).map(v => ({ v, ok: v === a, l: fmtNum(v) + (q.unit ? ' ' + q.unit : '') }));
}
VIEWS.duelSetup = () => {
  const C = S.settings.duel || (S.settings.duel = { rounds: 10, secs: 15, num: true, topics: [] });
  const [n1, n2] = S.duel.names;
  view.innerHTML = `<h2>Duell</h2><p class="muted small" style="margin:6px 0 14px">Ein Gerät, zwei Spieler: Handy flach zwischen euch legen. Wer zuerst richtig drückt, punktet – wer falsch drückt, schenkt dem Gegner den Punkt.</p>
  <div class="card"><div class="grid2"><label class="fld">Spieler unten<input id="dn1" value="${esc(n1)}" maxlength="14"></label><label class="fld">Spieler oben<input id="dn2" value="${esc(n2)}" maxlength="14"></label></div>
   <div class="eyebrow" style="margin:14px 0 6px">Runden</div><div class="chips" id="dR">${[10, 15, 20].map(n => `<button class="chip" data-r="${n}" aria-pressed="${C.rounds === n}">${n}</button>`).join('')}</div>
   <div class="eyebrow" style="margin:14px 0 6px">Zeit pro Runde</div><div class="chips" id="dS">${[10, 15, 20].map(n => `<button class="chip" data-s="${n}" aria-pressed="${C.secs === n}">${n} s</button>`).join('')}</div>
   <div class="eyebrow" style="margin:14px 0 6px">Rundentypen</div><div class="chips"><button class="chip" aria-pressed="true" disabled>Wahr/Falsch</button><button class="chip" id="dNum" aria-pressed="${C.num}">Schätzfragen (4 Optionen)</button></div>
   <div class="eyebrow" style="margin:14px 0 6px">Themen (leer = alle)</div><div id="dT">${filterChips(C.topics, Object.keys(D.topics), 'tp', k => D.topics[k])}</div>
   <button class="btn red block" style="margin-top:16px" id="dGo">${IC.duel.replace('<svg', '<svg width="18" height="18"')} Duell starten</button></div>
   ${S.duel.hist.length ? `<div class="card"><div class="eyebrow" style="margin-bottom:6px">Letzte Duelle</div>${S.duel.hist.slice(-6).reverse().map(h => `<div class="between small" style="padding:5px 0;border-top:1px solid var(--line)"><span>${new Date(h.d).toLocaleDateString('de-DE')} · ${esc(h.n[0])} vs. ${esc(h.n[1])}</span><b>${h.s[0]} : ${h.s[1]}</b></div>`).join('')}</div>` : ''}
   ${lastDuel ? `<div class="card"><div class="eyebrow" style="margin-bottom:8px">Auflösung letztes Duell</div>${lastDuel.map(r => `<div class="it ${r.w === 0 ? '' : ''}" style="margin-bottom:8px"><div class="tx">${esc(r.t)}<div class="sol" style="color:var(--ok)">${esc(r.sol)}</div><div class="why">${esc(r.why || '')}</div></div></div>`).join('')}</div>` : ''}`;
  view.onclick = e => {
    const b = e.target.closest('.chip'); if (!b || b.disabled) return;
    if (b.dataset.r) C.rounds = +b.dataset.r; if (b.dataset.s) C.secs = +b.dataset.s; if (b.id === 'dNum') C.num = !C.num;
    if (b.dataset.tp) { const a = C.topics, k = b.dataset.tp; a.includes(k) ? a.splice(a.indexOf(k), 1) : a.push(k); }
    S.duel.names = [$('#dn1').value || 'Notarzt', $('#dn2').value || 'NotSan']; save(); view.onclick = null; VIEWS.duelSetup();
  };
  $('#dGo').onclick = () => { S.duel.names = [$('#dn1').value.trim() || 'Notarzt', $('#dn2').value.trim() || 'NotSan']; save(); view.onclick = null; startDuel(C); };
};
let lastDuel = null;
function startDuel(C) {
  const tp = q => !C.topics.length || C.topics.includes(q.topic);
  const st = shuffle(STMTS.filter(s => tp(BYID[s.q]))), nq = shuffle(NUMQ.filter(tp));
  const rounds = []; let si = 0, ni = 0;
  for (let r = 0; r < C.rounds; r++) {
    if (C.num && nq.length && (r % 4 === 3) && ni < nq.length) { const q = nq[ni++]; const ch = numChoices(q); rounds.push({ kind: 'num', t: q.stem, ch, sol: ch.find(c => c.ok).l, why: q.expl }); }
    else { const s = st[si++ % st.length]; rounds.push({ kind: 'tf', t: s.t, v: s.v, sol: s.v ? 'WAHR' : 'FALSCH', why: s.why }); }
  }
  const D2 = $('#duel'); const names = S.duel.names; let sc = [0, 0], ri = -1, lock = true, tStart = 0;
  D2.classList.add('on'); document.body.style.overflow = 'hidden';
  const half = p => `<div class="half p${p}" id="h${p}"><div class="who"><span>${esc(names[p - 1])}</span><span class="pts" id="pt${p}">0</span></div><div class="q" id="q${p}"></div><div class="note" id="n${p}"></div><div class="ans" id="a${p}"></div></div>`;
  D2.innerHTML = half(2) + `<div class="mid"><span id="dRound">–</span><div class="timer"><i id="dBar" style="width:100%"></i></div><button id="dQuit">Ende</button></div>` + half(1);
  const setQ = html => { $('#q1').innerHTML = html; $('#q2').innerHTML = html; };
  const setN = html => { $('#n1').innerHTML = html; $('#n2').innerHTML = html; };
  const btns = r => r.kind === 'tf' ? `<button class="f" data-v="0">FALSCH</button><button class="w" data-v="1">WAHR</button>` : r.ch.map((c, i) => `<button class="mc" data-v="${i}">${esc(c.l)}</button>`).join('');
  const quit = () => { D2.classList.remove('on'); document.body.style.overflow = ''; timers.forEach(t => { clearTimeout(t); clearInterval(t); }); timers = []; go('duelSetup'); };
  $('#dQuit').onclick = () => { if (confirmQuit()) quit(); };
  function confirmQuit() { return ri >= rounds.length || window.confirm('Duell abbrechen?'); }
  let tick = null;
  const next = () => {
    ri++; $('#h1').classList.remove('win', 'lose'); $('#h2').classList.remove('win', 'lose');
    if (ri >= rounds.length) return end();
    const r = rounds[ri]; $('#dRound').textContent = `${ri + 1}/${rounds.length}`;
    setN('Bereit …'); setQ(esc(r.t)); $('#a1').innerHTML = btns(r); $('#a2').innerHTML = btns(r); lock = true;
    $$('#duel .ans button').forEach(b => b.disabled = true);
    later(() => { lock = false; setN(''); $$('#duel .ans button').forEach(b => b.disabled = false); tStart = Date.now(); SND.tick(); }, 900);
    clearInterval(tick); tick = every(() => {
      if (lock || !tStart) return; const left = Math.max(0, C.secs - (Date.now() - tStart) / 1000); $('#dBar').style.width = left / C.secs * 100 + '%';
      if (left <= 0) { lock = true; reveal(null, null); }
    }, 100);
  };
  const reveal = (p, ok) => {
    const r = rounds[ri]; tStart = 0;
    $$('#duel .ans button').forEach(b => b.disabled = true);
    if (p) { const winner = ok ? p : (p === 1 ? 2 : 1); sc[winner - 1]++; $('#pt1').textContent = sc[0]; $('#pt2').textContent = sc[1]; $('#h' + winner).classList.add('win'); $('#h' + (winner === 1 ? 2 : 1)).classList.add('lose'); r.w = winner; }
    setN(`${p ? (ok ? '✓ ' + esc(names[p - 1]) + ' richtig' : '✗ ' + esc(names[p - 1]) + ' falsch – Punkt für ' + esc(names[(p === 1 ? 2 : 1) - 1])) : '⏱ Zeit abgelaufen'} · Lösung: <b>${esc(r.sol)}</b>`);
    later(next, 2600);
  };
  D2.onpointerdown = e => {
    const b = e.target.closest('.ans button:not([data-x])'); if (!b || lock || b.disabled) return; e.preventDefault(); lock = true; SND.buzz(); buzzV(30);
    const p = b.closest('#h1') ? 1 : 2; const r = rounds[ri]; const v = +b.dataset.v;
    const ok = r.kind === 'tf' ? (v === 1) === r.v : r.ch[v].ok; ok ? SND.ok() : SND.bad(); reveal(p, ok);
  };
  const end = () => {
    clearInterval(tick); const w = sc[0] === sc[1] ? 0 : sc[0] > sc[1] ? 1 : 2;
    S.duel.n++; S.duel.hist.push({ d: Date.now(), n: names.slice(), s: sc.slice() }); if (S.duel.hist.length > 30) S.duel.hist.shift();
    addXP(20 + sc[0] * 2); emit('duel', {}); lastDuel = rounds;
    const msg = w === 0 ? 'Unentschieden!' : `${esc(names[w - 1])} gewinnt!`;
    setQ(`<div><div style="font-size:40px;font-weight:900">${sc[0]} : ${sc[1]}</div><div style="font-size:22px;margin-top:6px">${msg}</div></div>`); setN('');
    const fin = `<button data-x="again" style="grid-column:1/-1">Revanche</button><button data-x="quit" style="grid-column:1/-1;background:#1B2A42">Auflösung &amp; Ende</button>`;
    $('#a1').innerHTML = fin; $('#a2').innerHTML = fin; if (w) { $('#h' + w).classList.add('win'); }
    fx('rain', 260); SND.lvl();
    D2.onclick = e => { const b = e.target.closest('[data-x]'); if (!b) return; if (b.dataset.x === 'again') { D2.onclick = null; timers.forEach(t => { clearTimeout(t); clearInterval(t); }); startDuel(C); } else quit(); };
  };
  SND.siren(); setQ('<div style="font-size:54px;font-weight:900">3</div>');
  later(() => setQ('<div style="font-size:54px;font-weight:900">2</div>'), 700);
  later(() => setQ('<div style="font-size:54px;font-weight:900">1</div>'), 1400);
  later(next, 2100);
}

/* ----- Profile ----- */
VIEWS.profile = () => {
  view.onclick = null;
  const i = rankOf(S.xp);
  const ans = Object.values(S.prog).reduce((a, p) => a + p.n, 0), right = Object.values(S.prog).reduce((a, p) => a + p.ok, 0);
  const days = []; for (let k = 13; k >= 0; k--) { const d = addDays(new Date(), -k); const h = S.hist[dayKey(d)]; days.push({ l: d.getDate(), xp: h ? h.xp : 0, t: k === 0 }); }
  const mx = Math.max(10, ...days.map(d => d.xp));
  const tstats = Object.keys(D.topics).map(t => { const qs = QN.filter(q => q.topic === t); const seen = qs.filter(q => S.prog[q.id]); const avg = seen.length ? seen.reduce((a, q) => a + S.prog[q.id].best, 0) / seen.length : 0; return `<div class="tstat"><span>${esc(D.topics[t])}</span><span class="muted">${seen.length}/${qs.length} · ${Math.round(avg * 100)} %</span><div class="bar"><i style="width:${seen.length / qs.length * 100}%;background:${TOPIC_COL[t]}"></i></div></div>`; }).join('');
  const ystats = ['mtf', 'order', 'match', 'cloze', 'num', 'img'].map(t => { const qs = QN.filter(q => q.t === t), seen = qs.filter(q => S.prog[q.id]); const avg = seen.length ? seen.reduce((a, q) => a + S.prog[q.id].best, 0) / seen.length : 0; return `<div class="tstat"><span>${TYPE[t]}</span><span class="muted">${seen.length}/${qs.length} · ${Math.round(avg * 100)} %</span><div class="bar g"><i style="width:${avg * 100}%"></i></div></div>`; }).join('');
  const got = BADGES.filter(b => S.badges['got_' + b[0]]).length;
  const set = S.settings;
  const due = new Date((S.review.done || S.firstUse) + 365 * 864e5);
  view.innerHTML = `<section class="card"><div class="rank">${rankBadge(i, 72)}<div style="flex:1"><div class="eyebrow">Dienstgrad</div><h3>${esc(RANKS[i][1])}</h3><div class="small muted">${S.xp} XP · Serie ${streakNow()} (Rekord ${S.streak.best}) · ${got}/${BADGES.length} Abzeichen</div></div></div></section>
  <section class="card grid2" style="text-align:center"><div><div style="font-size:26px;font-weight:900">${seenN()}<span class="muted" style="font-size:14px">/${QN.length}</span></div><div class="small muted">Fragen gesehen</div></div><div><div style="font-size:26px;font-weight:900">${ans ? Math.round(right / ans * 100) : 0} %</div><div class="small muted">vollständig richtig</div></div>
   <div><div style="font-size:26px;font-weight:900">${casesDone()}<span class="muted" style="font-size:14px">/${CASES.length}</span></div><div class="small muted">Einsätze bestanden</div></div><div><div style="font-size:26px;font-weight:900">${S.blitz.best} · ${S.sprint.best}</div><div class="small muted">Rekord Blitz · Sprint</div></div></section>
  <section class="card"><div class="eyebrow" style="margin-bottom:10px">XP der letzten 14 Tage</div><div class="histo">${days.map(d => `<div class="${d.t ? 'today' : ''}" style="height:${d.xp / mx * 100}%" title="${d.xp} XP"></div>`).join('')}</div><div class="histo-l">${days.map(d => `<span>${d.l}</span>`).join('')}</div></section>
  <section class="card"><div class="eyebrow" style="margin-bottom:10px">Abzeichen</div><div class="badges">${BADGES.map(([id, n, d, , c, ic]) => `<div class="bdg ${S.badges['got_' + id] ? 'on' : ''}" title="${esc(d)}"><div class="m" style="${S.badges['got_' + id] ? `background:${c};color:#fff` : ''}">${(IC[ic] || IC.star)}</div>${esc(n)}</div>`).join('')}</div></section>
  <section class="card"><div class="eyebrow" style="margin-bottom:10px">Themen (gesehen · Ø Bestwert)</div>${tstats}</section>
  <section class="card"><div class="eyebrow" style="margin-bottom:10px">Fragentypen</div>${ystats}</section>
  <section class="card"><div class="eyebrow" style="margin-bottom:10px">Einstellungen</div>
   <div class="eyebrow" style="margin:4px 0 6px;font-size:10px">Farbschema</div><div class="chips" id="pTh">${[['auto', 'Auto'], ['light', 'Hell'], ['dark', 'Dunkel']].map(([k, l]) => `<button class="chip" data-th="${k}" aria-pressed="${set.theme === k}">${l}</button>`).join('')}</div>
   <div class="eyebrow" style="margin:12px 0 6px;font-size:10px">Effekte & Ton</div><div class="chips"><button class="chip" id="pFx" aria-pressed="${set.fx === 'on'}">Konfetti & Animation</button><button class="chip" id="pSd" aria-pressed="${set.sound}">Töne</button></div>
   <label class="fld" style="margin-top:12px">Prüfungstermin (Countdown auf der Wache)<input type="date" id="pEx" value="${esc(set.examDate)}"></label>
  </section>
  <section class="card"><div class="eyebrow" style="margin-bottom:10px">Daten</div><p class="small muted" style="margin-top:0">Alles bleibt lokal auf diesem Gerät. Für Gerätewechsel: sichern und wiederherstellen.</p>
   <div class="grid2"><button class="btn" id="pExp">Fortschritt sichern</button><button class="btn" id="pImp">Wiederherstellen</button></div><input type="file" id="pFile" accept="application/json,.json" hidden>
   <div class="actions"><button class="btn grow" id="pRev">Jährliche Inhaltsprüfung ${Date.now() > due ? '<span class="tag" style="background:var(--red);color:#fff">fällig</span>' : ''}</button><button class="btn ghost" id="pReset" style="color:var(--bad)">Zurücksetzen</button></div>
   <p class="small muted center" style="margin-bottom:0">Version ${esc(APPV)} · ${QS.length} Fragen · nächste Inhaltsprüfung ${due.toLocaleDateString('de-DE')}</p></section>`;
  $('#pTh').onclick = e => { const b = e.target.closest('[data-th]'); if (!b) return; set.theme = b.dataset.th; applyTheme(); save(); VIEWS.profile(); };
  $('#pFx').onclick = () => { set.fx = set.fx === 'on' ? 'reduced' : 'on'; save(); VIEWS.profile(); };
  $('#pSd').onclick = () => { set.sound = !set.sound; save(); VIEWS.profile(); if (set.sound) SND.ok(); };
  $('#pEx').onchange = e => { set.examDate = e.target.value; save(); };
  $('#pExp').onclick = () => { const blob = new Blob([JSON.stringify({ app: 'status3', version: APPV, exported: new Date().toISOString(), data: S })], { type: 'application/json' }); const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = `status3-backup-${dayKey()}.json`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 2000); };
  $('#pImp').onclick = () => $('#pFile').click();
  $('#pFile').onchange = async e => { try { const j = JSON.parse(await e.target.files[0].text()); if (j.app !== 'status3' || !j.data) throw 0; S = merge(clone(DEF), j.data); save(); location.reload(); } catch (x) { toast('Datei konnte nicht gelesen werden.'); } };
  $('#pReset').onclick = () => openSheet(`<h3>Fortschritt löschen?</h3><p class="muted">XP, Abzeichen und Statistik werden auf diesem Gerät gelöscht. Vorher sichern!</p><div class="actions"><button class="btn red grow" id="rsY">Ja, löschen</button><button class="btn grow" id="rsN">Abbrechen</button></div>`, b => { $('#rsY', b).onclick = () => { localStorage.removeItem(SKEY); location.reload(); }; $('#rsN', b).onclick = closeSheet; });
  $('#pRev').onclick = openReview;
};
const REVIEW_ITEMS = [
  ['erc', 'ERC/GRC-Reanimationsleitlinien (ALS, BLS, PLS, NLS, Postreanimation, besondere Umstände)'],
  ['nun', 'NUN-Versorgungspfade Niedersachsen und regionale SOP des ÄLRD (LK Oldenburg)'],
  ['s3pt', 'S3-Leitlinie Polytrauma/Schwerverletzten-Behandlung (AWMF 187-023)'],
  ['awm', 'DGAI S1 Notfallnarkose/Atemwegsmanagement, S3 Sauerstoff, S3 NIV'],
  ['card', 'ESC-Leitlinien ACS, Lungenembolie, Aorta/Hypertonie; Dr. Smith’s ECG Blog (OMI-Kriterien)'],
  ['neuro', 'DGN: Schlaganfall, Status epilepticus, Meningitis'],
  ['ana', 'S2k Anaphylaxie, NVL Asthma, S2k Verbrennung'],
  ['tox', 'GIZ-Nord/Antidotliste, Hypothermie/Ertrinken (ERC Special Circumstances)'],
  ['manv', 'Sichtung (mSTaRT/PRIOR, BBK-Konsensus), MANV-Konzept Niedersachsen'],
  ['gef', 'FwDV 500, ADR/Kemler, TEL-Konzepte (TREMA/DGU)'],
  ['recht', 'NotSanG, NRettDG/BedarfVO-RettD, BGB (Patientenverfügung, Notvertretung), StVO'],
];
function openReview() {
  const R = S.review;
  const prompt = () => `Bitte aktualisiere die Fragenbank meiner App „Status 3 · Notfallmedizin-Trainer“ (Version ${APPV}, ${QS.length} Fragen, GitHub-Repository). Prüfe alle Fragen gegen die jeweils aktuellen Fassungen folgender Quellen und korrigiere Zahlen, Dosierungen und Empfehlungen:\n${REVIEW_ITEMS.map(r => '- ' + r[1]).join('\n')}\nMeine Notizen:\n${R.notes || '(keine)'}\nBehalte Fragentypen, IDs und Quellenangaben bei und erhöhe die Version.`;
  openSheet(`<h3>Jährliche Inhaltsprüfung</h3><p class="small muted">Einmal im Jahr die Inhalte gegen aktuelle Leitlinien prüfen. Abhaken, Notizen festhalten und den Prompt an Claude übergeben.</p>
   ${REVIEW_ITEMS.map(([k, l]) => `<label class="row small" style="padding:6px 0;border-top:1px solid var(--line)"><input type="checkbox" data-rv="${k}" ${R.checks[k] ? 'checked' : ''}> ${esc(l)}</label>`).join('')}
   <label class="fld" style="margin-top:10px">Notizen<textarea id="rvN" rows="3" style="border:1px solid var(--line);border-radius:10px;padding:8px;background:var(--card)">${esc(R.notes)}</textarea></label>
   <details style="margin:10px 0"><summary class="small"><b>Prompt für Claude</b></summary><pre id="rvP" style="white-space:pre-wrap;font-size:12px;background:var(--bg2);padding:8px;border-radius:8px"></pre><button class="btn sm" id="rvC">Kopieren</button></details>
   <div class="actions"><button class="btn pri grow" id="rvD">Prüfung abgeschlossen</button><button class="btn" id="rvX">Schließen</button></div>`, b => {
    const up = () => { $('#rvP', b).textContent = prompt(); }; up();
    b.onchange = e => { const c = e.target.closest('[data-rv]'); if (c) { R.checks[c.dataset.rv] = c.checked; save(); } };
    $('#rvN', b).oninput = e => { R.notes = e.target.value; save(); up(); };
    $('#rvC', b).onclick = () => { navigator.clipboard && navigator.clipboard.writeText(prompt()).then(() => toast('Prompt kopiert')); };
    $('#rvD', b).onclick = () => { R.done = Date.now(); R.checks = {}; save(); closeSheet(); toast('Nächste Prüfung in 12 Monaten'); VIEWS.profile(); };
    $('#rvX', b).onclick = closeSheet;
  });
}

/* ---------------- Pomodoro ---------------- */
const P = { mode: 'work', left: 25 * 60, run: false, id: null };
function pRender() { $('#pomoTime').textContent = `${Math.floor(P.left / 60)}:${pad(P.left % 60)}`; $('#pomoPill').classList.toggle('idle', !P.run); const pop = $('#pomoPop'); if (!pop.classList.contains('hidden')) pDraw(); }
function pDraw() { $('#pomoPop').innerHTML = `<div class="between"><b>${P.mode === 'work' ? 'Fokus 25 min' : 'Pause 5 min'}</b><button class="btn sm ghost" id="pmX">✕</button></div><div style="font-family:var(--mono);font-size:40px;font-weight:800;text-align:center;margin:8px 0">${Math.floor(P.left / 60)}:${pad(P.left % 60)}</div><div class="grid2"><button class="btn pri sm" id="pmS">${P.run ? 'Pause' : 'Start'}</button><button class="btn sm" id="pmR">Zurücksetzen</button></div><p class="small muted" style="margin-bottom:0">Abgeschlossen: ${S.pomo.done}</p>`;
  $('#pmX').onclick = () => $('#pomoPop').classList.add('hidden');
  $('#pmS').onclick = () => { P.run = !P.run; if (P.run) { P.id = setInterval(pTick, 1000); } else clearInterval(P.id); pRender(); };
  $('#pmR').onclick = () => { clearInterval(P.id); P.run = false; P.mode = 'work'; P.left = 1500; pRender(); };
}
function pTick() { P.left--; if (P.left <= 0) { clearInterval(P.id); P.run = false; SND.lvl(); if (P.mode === 'work') { S.pomo.done++; emit('pomo', {}); toast('Pomodoro geschafft – 5 min Pause!', IC.clock); P.mode = 'break'; P.left = 300; } else { toast('Pause vorbei – weiter geht’s!', IC.clock); P.mode = 'work'; P.left = 1500; } } pRender(); }
$('#pomoPill').onclick = () => { const p = $('#pomoPop'); p.classList.toggle('hidden'); if (!p.classList.contains('hidden')) pDraw(); };

/* ---------------- Theme & boot ---------------- */
function applyTheme() { const t = S.settings.theme; if (t === 'auto') document.documentElement.removeAttribute('data-theme'); else document.documentElement.setAttribute('data-theme', t); document.documentElement.classList.toggle('fx-reduced', S.settings.fx === 'reduced'); }
applyTheme(); ensureMissions(); renderTop(); go('home'); pRender();
if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => { }));
  const hadCtrl = !!navigator.serviceWorker.controller; let refreshing = false;
  navigator.serviceWorker.addEventListener('controllerchange', () => { if (refreshing || !hadCtrl) return; refreshing = true; toast('Update installiert – App einmal neu öffnen.'); });
}
window.S3 = { S, go, BYID };
