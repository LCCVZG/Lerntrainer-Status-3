"""Generate synthetic ECG (strip + 12-lead) and capnography SVGs for Status 3.
All curves are drawn from simple parametric models (sum of Gaussians) — teaching
illustrations, not real patient recordings."""
import math, random, json, copy

PX = 4.0          # px per mm
MV = 10 * PX      # px per mV (10 mm/mV)
SPS = 200         # samples per second
SEC = 25 * PX     # px per second (25 mm/s)


def g(t, mu, s):
    return math.exp(-0.5 * ((t - mu) / s) ** 2)


def sig(x, k=0.006):
    x = max(-60, min(60, x / k))
    return 1 / (1 + math.exp(-x))


NORMAL = {
    'I':   dict(P=.10, Q=.05, R=.75, S=.10, T=.25),
    'II':  dict(P=.15, Q=.05, R=1.10, S=.15, T=.32),
    'III': dict(P=.05, Q=.05, R=.40, S=.20, T=.10),
    'aVR': dict(P=-.12, Q=0, R=.12, S=.80, T=-.25),
    'aVL': dict(P=.05, Q=.03, R=.45, S=.20, T=.10),
    'aVF': dict(P=.10, Q=.04, R=.75, S=.15, T=.22),
    'V1':  dict(P=.08, Q=0, R=.20, S=1.00, T=.08, ST=.02),
    'V2':  dict(P=.08, Q=0, R=.40, S=1.40, T=.50, ST=.10),
    'V3':  dict(P=.08, Q=0, R=.80, S=1.00, T=.50, ST=.08),
    'V4':  dict(P=.08, Q=.03, R=1.30, S=.60, T=.45, ST=.03),
    'V5':  dict(P=.08, Q=.08, R=1.40, S=.30, T=.35),
    'V6':  dict(P=.08, Q=.08, R=1.10, S=.20, T=.30),
}
LEADS = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']


def beat(t, p):
    """One PQRST complex; t relative to R peak (s)."""
    qrsd = p.get('qrsd', .08)
    on = -qrsd / 2
    pr = p.get('PR', .16)
    v = 0.0
    if p.get('P'):
        pc = on - pr + .05
        v += p['P'] * g(t, pc, .022)
    sc = qrsd / .08
    if p.get('Q'):
        v -= p['Q'] * g(t, on + .010 * sc, .006 * sc)
    rw = p.get('Rw', .010 * sc)
    v += p.get('R', 0) * g(t, p.get('Rt', 0), rw)
    if p.get('R2'):
        v += p['R2'] * g(t, p.get('R2t', .045 * sc), p.get('R2w', .010 * sc))
    if p.get('S'):
        v -= p['S'] * g(t, p.get('St', .022 * sc), p.get('Sw', .009 * sc))
    if p.get('delta'):
        v += p['delta'] * g(t, on - .012, .018)
    J = on + qrsd
    tc = J + p.get('Toff', .17)
    tw = p.get('Tw', .045)
    st = p.get('ST', 0)
    if st:
        if p.get('coved'):
            v += st * sig(t - J + .004) * math.exp(-max(0, t - J) / .10)
        else:
            v += st * sig(t - J + .004) * (1 - sig(t - tc - .02, .03))
    T = p.get('T', 0)
    if T:
        left, right = tw * 1.25, tw * .85
        if p.get('Tsym'):
            left = right = tw
        s = left if t < tc else right
        v += T * g(t, tc, s)
    if p.get('T2'):  # terminal negative part (biphasic)
        v -= p['T2'] * g(t, tc + p.get('T2off', .06), .035)
    if p.get('U'):
        v += p['U'] * g(t, tc + .16, .03)
    return v


def series(dur, beats, params, extra=None):
    n = int(dur * SPS)
    out = []
    for i in range(n):
        t = i / SPS
        v = 0.0
        for tb in beats:
            if -0.6 < t - tb < 0.7:
                v += beat(t - tb, params)
        if extra:
            v += extra(t)
        out.append(v)
    return out


def regular(dur, rate, start=.35):
    rr = 60 / rate
    out, t = [], start
    while t < dur + .5:
        out.append(t)
        t += rr
    return out


# ---------------- SVG helpers ----------------

def grid(w, h, gid):
    return (f'<defs><pattern id="s{gid}" width="{PX}" height="{PX}" patternUnits="userSpaceOnUse">'
            f'<path d="M{PX} 0H0V{PX}" fill="none" stroke="var(--ecg-grid)" stroke-width=".4"/></pattern>'
            f'<pattern id="b{gid}" width="{PX*5}" height="{PX*5}" patternUnits="userSpaceOnUse">'
            f'<rect width="{PX*5}" height="{PX*5}" fill="url(#s{gid})"/>'
            f'<path d="M{PX*5} 0H0V{PX*5}" fill="none" stroke="var(--ecg-grid2)" stroke-width=".9"/></pattern></defs>'
            f'<rect width="{w}" height="{h}" fill="var(--ecg-paper)"/><rect width="{w}" height="{h}" fill="url(#b{gid})"/>')


def poly(vals, x0, y0, step=None):
    step = step or SEC / SPS
    pts = ' '.join(f'{x0 + i*step:.1f},{y0 - v*MV:.1f}' for i, v in enumerate(vals))
    return f'<polyline points="{pts}" fill="none" stroke="var(--ecg-ink)" stroke-width="1.5" stroke-linejoin="round"/>'


def calib(x, y):
    return (f'<path d="M{x} {y} h{PX} v{-MV} h{PX*2} v{MV} h{PX}" fill="none" '
            f'stroke="var(--ecg-ink)" stroke-width="1.5"/>')


def label(x, y, s, size=13):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="700" fill="var(--ecg-ink)" '
            f'font-family="system-ui,sans-serif">{s}</text>')


def strip_svg(key, vals, lead='II', dur=None, note=None):
    dur = dur or len(vals) / SPS
    w = int(dur * SEC + 40)
    h = 30 * PX
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" class="ecg">', grid(w, h, key)]
    base = h * .55
    s.append(calib(4, base))
    s.append(poly(vals, 24, base))
    s.append(label(30, 16, f'{lead}  ·  25 mm/s  ·  10 mm/mV'))
    if note:
        s.append(label(w - 8 - len(note) * 6.6, 16, note))
    s.append('</svg>')
    return ''.join(s)


def twelve_svg(key, rate, params, rhythm_beats=None):
    """params: dict lead -> param dict (full)."""
    dur = 10.0
    beats = rhythm_beats or regular(dur, rate, .3)
    data = {ld: series(dur, beats, params[ld]) for ld in LEADS}
    colw = 2.5 * SEC
    rowh = 26 * PX
    x0 = 24
    w = int(x0 + 4 * colw + 8)
    h = int(rowh * 4 + 10)
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" class="ecg ecg12">', grid(w, h, key)]
    layout = [['I', 'aVR', 'V1', 'V4'], ['II', 'aVL', 'V2', 'V5'], ['III', 'aVF', 'V3', 'V6']]
    seg = int(2.5 * SPS)
    for r, row in enumerate(layout):
        yb = rowh * r + rowh * .62
        s.append(calib(4, yb))
        for c, ld in enumerate(row):
            vals = data[ld][c * seg:(c + 1) * seg + 1]
            xs = x0 + c * colw
            s.append(poly(vals, xs, yb))
            s.append(label(xs + 4, rowh * r + 16, ld))
            if c:
                s.append(f'<line x1="{xs}" y1="{yb-14}" x2="{xs}" y2="{yb+14}" stroke="var(--ecg-ink)" stroke-width="1.2"/>')
    yb = rowh * 3 + rowh * .62
    s.append(calib(4, yb))
    s.append(poly(data['II'], x0, yb))
    s.append(label(x0 + 4, rowh * 3 + 16, 'II'))
    s.append('</svg>')
    return ''.join(s)


def leadset(over=None, common=None):
    p = copy.deepcopy(NORMAL)
    for ld in p:
        if common:
            p[ld].update(common)
    for ld, d in (over or {}).items():
        p[ld].update(d)
    return p


FIGS = {}
random.seed(7)

# ---------- Rhythm strips ----------

def noise(a=.015, f=(.3, .9)):
    ph = random.random() * 6
    return lambda t: a * math.sin(2 * math.pi * f[0] * t + ph) + a * .6 * math.sin(2 * math.pi * f[1] * t)


# VF (coarse)
comps = [(random.uniform(3.8, 6.5), random.uniform(.15, .35), random.random() * 6) for _ in range(6)]
FIGS['vf'] = strip_svg('vf', [sum(a * math.sin(2 * math.pi * f * t + p + .6 * math.sin(.7 * t * f)) for f, a, p in comps)
                              * (0.8 + .3 * math.sin(2 * math.pi * .35 * t)) for t in [i / SPS for i in range(int(8 * SPS))]])

# Monomorphic VT ~180/min
vt = dict(P=0, Q=0, R=1.05, Rw=.035, S=.75, St=.085, Sw=.035, qrsd=.16, T=-.35, Tw=.05, Toff=.08, Tsym=1)
FIGS['vt'] = strip_svg('vt', series(8, regular(8, 182, .2), vt), note='HF ≈ 180/min')

# Torsade de pointes
FIGS['tdp'] = strip_svg('tdp', [(.25 + .9 * abs(math.sin(math.pi * t / 2.4))) * math.sin(2 * math.pi * 4.2 * t)
                                for t in [i / SPS for i in range(int(8 * SPS))]])

# P-wave asystole: P at 70/min, no QRS
pw = dict(P=.16, Q=0, R=0, S=0, T=0)
FIGS['pasys'] = strip_svg('pasys', series(8, regular(8, 70, .5), pw, noise(.01)))

# AV block III: P 85/min, wide escape 36/min
pf = dict(P=.22, PR=.1, Q=0, R=0, S=0, T=0)
esc = dict(P=0, Q=0, R=.9, Rw=.025, S=.45, St=.06, Sw=.025, qrsd=.15, T=-.35, Tw=.07)
pt = regular(10, 85, .25)
qt = regular(10, 36, .9)
FIGS['avb3'] = strip_svg('avb3', [a + b for a, b in zip(series(10, [x + .2 for x in pt], pf), series(10, qt, esc))])

# Mobitz II 3:2 — P every 0.75 s, PR constant, every third P blocked
pp = .75
ps, qs = [], []
t = .3
k = 0
while t < 10.5:
    ps.append(t)
    if k % 3 != 2:
        qs.append(t + .18)
    k += 1
    t += pp
pm = dict(P=.15, Q=0, R=0, S=0, T=0, PR=.0001)
qm = dict(P=0, Q=.05, R=1.0, S=.2, T=.3, qrsd=.10)
FIGS['mob2'] = strip_svg('mob2', [a + b for a, b in zip(series(10, [x + .16 for x in ps], dict(P=.15, R=0, S=0, Q=0, T=0, PR=.16)),
                                                        series(10, qs, qm))])

# Atrial fibrillation ~ 140/min irregular
t = .3
bs = []
while t < 10.5:
    bs.append(t)
    t += random.choice([.32, .36, .41, .47, .38, .55, .34, .44, .62, .39])
fibc = [(random.uniform(5, 8), random.uniform(.02, .05), random.random() * 6) for _ in range(5)]
FIGS['afib'] = strip_svg('afib', series(10, bs, dict(P=0, Q=.04, R=1.1, S=.15, T=.25),
                                         lambda t: sum(a * math.sin(2 * math.pi * f * t + p) for f, a, p in fibc)),
                         note='unregelmäßig, HF ≈ 140/min')

# AVNRT ~190/min
FIGS['svt'] = strip_svg('svt', series(8, regular(8, 190, .2), dict(P=0, Q=.03, R=1.1, S=.25, T=.22, Toff=.11, Tw=.035)),
                        note='regelmäßig, HF ≈ 190/min')

# Atrial flutter 2:1 (sawtooth 300/min, ventricle 150)
def saw(t):
    ph = (t * 5.0) % 1.0
    return -.32 * (ph if ph < .82 else (1 - ph) * 4.5) + .12
FIGS['flutter'] = strip_svg('flutter', [a + saw(i / SPS) for i, a in enumerate(series(10, regular(10, 150, .27),
                                                                                         dict(P=0, Q=.03, R=1.0, S=.2, T=.05)))],
                            note='regelmäßig, HF 150/min')

# ---------- 12-lead ECGs ----------

# Inferior OMI with reciprocal STD in aVL and I; mild STE in V1 (RV)
FIGS['inf_omi'] = twelve_svg('inf_omi', 72, leadset({
    'II': dict(ST=.20, T=.55, Tw=.06),
    'III': dict(ST=.30, T=.65, Tw=.06, R=.55),
    'aVF': dict(ST=.25, T=.58, Tw=.06),
    'aVL': dict(ST=-.18, T=-.25),
    'I': dict(ST=-.06, T=.05),
    'aVR': dict(ST=-.05),
    'V1': dict(ST=.10, T=.20),
    'V2': dict(ST=.0, T=.35),
    'V5': dict(ST=-.05), 'V6': dict(ST=-.05),
}))

# Proximal LAD occlusion, hyperacute T waves V2-V4 with early STE, STE aVL, reciprocal III
FIGS['ant_hyper'] = twelve_svg('ant_hyper', 88, leadset({
    'V1': dict(ST=.12, T=.35, Tw=.06),
    'V2': dict(ST=.25, T=1.20, Tw=.07, Tsym=1),
    'V3': dict(ST=.30, T=1.35, Tw=.07, Tsym=1),
    'V4': dict(ST=.20, T=1.10, Tw=.07, Tsym=1),
    'V5': dict(ST=.08, T=.60),
    'I': dict(ST=.08, T=.35),
    'aVL': dict(ST=.10, T=.30),
    'III': dict(ST=-.10, T=-.10),
    'aVF': dict(ST=-.05, T=.05),
}))

# De Winter: upsloping STD at J point + tall symmetric T V1-V6, STE aVR
dw = dict(ST=-.15, T=1.05, Tw=.055, Tsym=1)
FIGS['dewinter'] = twelve_svg('dewinter', 84, leadset({
    'V2': dict(ST=-.25, T=1.0, Tw=.055, Tsym=1),
    'V3': dict(ST=-.32, T=1.20, Tw=.055, Tsym=1),
    'V4': dict(ST=-.32, T=1.15, Tw=.055, Tsym=1),
    'V5': dict(ST=-.25, T=.85, Tw=.055, Tsym=1),
    'V6': dict(ST=-.10, T=.60, Tw=.055, Tsym=1),
    'aVR': dict(ST=.10, T=-.15),
    'I': dict(ST=-.05), 'II': dict(ST=-.05),
}))

# Wellens A: biphasic T V2-V3 (up then terminal down), preserved R, no Q, pain-free
FIGS['wellens'] = twelve_svg('wellens', 68, leadset({
    'V2': dict(ST=.06, T=.35, T2=.45, Toff=.14, T2off=.07),
    'V3': dict(ST=.06, T=.35, T2=.40, Toff=.14, T2off=.07),
    'V4': dict(T=.25, T2=.18, Toff=.15, T2off=.07),
}))

# Posterior OMI: STD max V2-V4 with upright T, tall R in V2
FIGS['post_omi'] = twelve_svg('post_omi', 78, leadset({
    'V1': dict(R=.45, S=.6, ST=-.12, T=.25),
    'V2': dict(R=.9, S=.7, ST=-.30, T=.30, Toff=.19),
    'V3': dict(R=1.1, S=.6, ST=-.32, T=.25, Toff=.19),
    'V4': dict(ST=-.22, T=.25),
    'V5': dict(ST=-.05),
    'III': dict(ST=.06, T=.25),
    'aVF': dict(ST=.04),
}))

# LBBB with excessive discordant STE in V2/V3 (Smith-modified Sgarbossa positive)
lb_common = dict(qrsd=.15)
lbbb = {
    'I': dict(Q=0, R=1.0, Rw=.032, R2=.25, R2t=.05, R2w=.015, S=0, ST=-.12, T=-.30, Toff=.18),
    'aVL': dict(Q=0, R=.8, Rw=.032, S=0, ST=-.10, T=-.25, Toff=.18),
    'V5': dict(Q=0, R=1.5, Rw=.032, R2=.3, R2t=.05, S=0, ST=-.15, T=-.40, Toff=.18),
    'V6': dict(Q=0, R=1.3, Rw=.032, S=0, ST=-.12, T=-.35, Toff=.18),
    'V1': dict(R=.08, S=1.4, St=.03, Sw=.03, ST=.25, T=.45, Toff=.18),
    'V2': dict(R=.10, S=1.6, St=.03, Sw=.03, ST=.55, T=.75, Toff=.18),
    'V3': dict(R=.15, S=1.4, St=.03, Sw=.03, ST=.50, T=.70, Toff=.18),
    'V4': dict(R=.5, S=1.0, St=.03, Sw=.03, ST=.20, T=.40, Toff=.18),
    'II': dict(R=.9, Rw=.03, S=.1, ST=-.05, T=-.1, Toff=.18),
    'III': dict(R=.2, Rw=.025, S=.5, Sw=.03, ST=.05, T=.15, Toff=.18),
    'aVF': dict(R=.5, Rw=.03, S=.3, T=.05, Toff=.18),
    'aVR': dict(R=.1, S=.9, Sw=.03, ST=.08, T=.2, Toff=.18),
}
FIGS['lbbb_sgarb'] = twelve_svg('lbbb_sgarb', 92, leadset(lbbb, lb_common))

# Hyperkalaemia: flat P, wide QRS, tall peaked narrow T
FIGS['hyperk'] = twelve_svg('hyperk', 64, leadset({
    'V2': dict(T=1.30, Tw=.030, Tsym=1), 'V3': dict(T=1.35, Tw=.030, Tsym=1), 'V4': dict(T=1.10, Tw=.030, Tsym=1),
    'V5': dict(T=.75, Tw=.03, Tsym=1), 'II': dict(T=.70, Tw=.03, Tsym=1), 'aVF': dict(T=.55, Tw=.03, Tsym=1),
    'I': dict(T=.45, Tw=.03, Tsym=1),
}, dict(qrsd=.15, P=.02, Toff=.13, R=.6)))

# Brugada type 1: coved STE >=2 mm V1-V2 with negative T
FIGS['brugada'] = twelve_svg('brugada', 70, leadset({
    'V1': dict(R=.25, S=.7, ST=.40, coved=1, T=-.25, Toff=.20, R2=.35, R2t=.04),
    'V2': dict(R=.35, S=1.0, ST=.45, coved=1, T=-.20, Toff=.21, R2=.30, R2t=.045),
}))

# LV aneurysm: QS V1-V4 with modest STE and small T (T/QRS low)
FIGS['lv_aneurysm'] = twelve_svg('lv_aneurysm', 76, leadset({
    'V1': dict(R=0, Q=0, S=1.2, ST=.12, T=.10),
    'V2': dict(R=0, Q=0, S=1.8, ST=.22, T=.15),
    'V3': dict(R=0, Q=0, S=1.4, ST=.25, T=.15),
    'V4': dict(R=.25, Q=.6, S=.5, ST=.15, T=.12),
    'I': dict(T=.12), 'aVL': dict(T=.05),
}))

# WPW: short PR, delta wave, wide QRS
FIGS['wpw'] = twelve_svg('wpw', 74, leadset({
    'V1': dict(delta=.25, R=.7, S=.3),
    'V2': dict(delta=.3, R=1.0, S=.5),
    'III': dict(delta=-.15, R=.2, S=.4),
    'aVF': dict(delta=-.05),
}, dict(PR=.10, delta=.22, qrsd=.12)))

# ---------- Capnography ----------

def capno_svg(key, fn, dur=30, ymax=60, note=None):
    w, h = 720, 230
    x0, y0, y1 = 44, 196, 20
    sx = (w - x0 - 12) / dur
    sy = (y0 - y1) / ymax
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" class="capno">',
         f'<rect width="{w}" height="{h}" rx="10" fill="var(--mon-bg)"/>']
    for mm in range(0, ymax + 1, 10):
        y = y0 - mm * sy
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{w-12}" y2="{y:.1f}" stroke="var(--mon-grid)" stroke-width="1"/>')
        s.append(f'<text x="{x0-8}" y="{y+4:.1f}" font-size="12" text-anchor="end" fill="var(--mon-txt)" font-family="system-ui,sans-serif">{mm}</text>')
    for sec in range(0, dur + 1, 5):
        x = x0 + sec * sx
        s.append(f'<text x="{x:.1f}" y="{h-12}" font-size="11" text-anchor="middle" fill="var(--mon-txt)" font-family="system-ui,sans-serif">{sec} s</text>')
    pts = []
    n = int(dur * 50)
    for i in range(n + 1):
        t = i / 50
        pts.append(f'{x0 + t*sx:.1f},{y0 - max(0, fn(t))*sy:.1f}')
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="var(--mon-co2)" stroke-width="2.4" stroke-linejoin="round"/>')
    s.append(f'<text x="{x0+6}" y="{y1+2}" font-size="13" font-weight="700" fill="var(--mon-co2)" font-family="system-ui,sans-serif">CO₂ (mmHg)</text>')
    if note:
        s.append(f'<text x="{w-16}" y="{y1+2}" font-size="13" font-weight="700" text-anchor="end" fill="var(--mon-txt)" font-family="system-ui,sans-serif">{note}</text>')
    s.append('</svg>')
    return ''.join(s)


def breath(t, period, insp_frac, plateau, up=.08, slope=0.0, base=0.0, cleft=False):
    """single capnogram cycle; expiration first then inspiration drop"""
    ph = (t % period)
    exp_d = period * (1 - insp_frac)
    if ph < exp_d:
        rise = 1 - math.exp(-ph / up)
        val = base + (plateau - base) * rise + slope * ph
        if cleft and exp_d * .55 < ph < exp_d * .7:
            val -= plateau * .28 * math.sin(math.pi * (ph - exp_d * .55) / (exp_d * .15))
        return val
    d = ph - exp_d
    peak = base + (plateau - base) + slope * exp_d
    return base + (peak - base) * math.exp(-d / .08)


FIGS['capno_shark'] = capno_svg('capno_shark', lambda t: breath(t, 4.0, .35, 30, up=.9, slope=4.0), note='AF 15/min')
FIGS['capno_eso'] = capno_svg('capno_eso', lambda t: (breath(t, 5, .4, 14 * math.exp(-t / 4)) if t < 12 else 0) + .3,
                              note='nach Intubation')
FIGS['capno_rosc'] = capno_svg('capno_rosc', lambda t: breath(t, 6, .5, 14 if t < 17 else 46, up=.15)
                               + (1.5 * math.sin(2 * math.pi * 1.8 * t) if t < 17 else 0), dur=36,
                               note='laufende CPR')
FIGS['capno_cleft'] = capno_svg('capno_cleft', lambda t: breath(t, 5, .35, 38, up=.12, slope=.6, cleft=True),
                                note='kontrollierte Beatmung')
FIGS['capno_hypervent'] = capno_svg('capno_hypervent', lambda t: breath(t, 2.0, .45, 21, up=.06), note='AF 30/min')

if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    json.dump(FIGS, open(out, 'w'), ensure_ascii=False)
    print(len(FIGS), sum(len(v) for v in FIGS.values()) // 1024, 'KB')
