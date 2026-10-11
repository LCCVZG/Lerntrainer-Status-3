import json, sys, collections
sys.path.insert(0, '.')
import q_rea_aw, q_kar_neu, q_tra_pae, q_tox_pha, q_tak_manv_gef, q_cases, memos

TOPICS = {
    'REA': 'Reanimation & Periarrest', 'AW': 'Atemweg & Respiration', 'KAR': 'Kardiozirkulation & EKG',
    'NEU': 'Neurologie', 'TRA': 'Trauma & Verbrennung', 'PAE': 'Pädiatrie & Geburtshilfe',
    'TOX': 'Intoxikation & Umwelt', 'PHA': 'Pharmakologie', 'TAK': 'Einsatztaktik & Recht',
    'MANV': 'MANV & Sichtung', 'GEF': 'Gefahrenlagen (CBRN, TEL)',
}
Q = q_rea_aw.Q + q_kar_neu.Q + q_tra_pae.Q + q_tox_pha.Q + q_tak_manv_gef.Q + q_cases.Q
import q_hard
_rep = {q['id']: q for q in q_hard.HARD + q_hard.NUMS}
assert all(k in [x['id'] for x in Q] for k in _rep), 'unknown id in q_hard'
Q = [_rep.get(q['id'], q) for q in Q]
for q in Q:
    if q['id'] in q_hard.OPTS:
        assert q['t'] == 'img' and q['ok'] == 0
        q['opts'] = q_hard.OPTS[q['id']]
figs = json.load(open('figs.json'))

ids = [q['id'] for q in Q]
dup = [k for k, v in collections.Counter(ids).items() if v > 1]
assert not dup, dup
for q in Q:
    assert q['topic'] in TOPICS, q['id']
    if q['t'] == 'img':
        assert q['fig'] in figs, q['id']
        assert 3 <= len(q['opts']) <= 5
    if q['t'] == 'match':
        rs = [p[1] for p in q['pairs']]
        assert len(set(rs)) == len(rs), q['id']
    if q['t'] == 'cloze':
        for g in q['gaps']:
            assert g[0] not in g[1], (q['id'], g)
    if q['t'] == 'order':
        assert len(set(q['steps'])) == len(q['steps'])
used = {q['fig'] for q in Q if q['t'] == 'img'}
print('unused figs:', set(figs) - used)
print('total', len(Q))
print(collections.Counter(q['t'] for q in Q))
print(collections.Counter(q['topic'] for q in Q))
print('levels', collections.Counter(q['lvl'] for q in Q))

out = sys.argv[1]
with open(out, 'w', encoding='utf-8') as f:
    f.write('/* Status 3 – Datenbasis. Generiert von build_data.py – Inhalte siehe Quellenangaben je Frage. */\n')
    f.write('window.S3DATA=' + json.dumps(dict(version=sys.argv[2] if len(sys.argv) > 2 else 'dev', topics=TOPICS, questions=Q,
                                                    figs=figs, memos=memos.MEMOS), ensure_ascii=False, separators=(',', ':')) + ';\n')
import os
print(os.path.getsize(out) // 1024, 'KB')
