# rage 91
# rock, groove, banger
# E minor, RATM-style nervous bass: 16-step riff drives sus/amp gating,
# kick syncopates with -k(...(...k))-, guitar stabs on offbeats with eb echoBoy.
# Chorus drops sub-octave, lapin wah lead screams in.

Clock.bpm = 91
Scale.default = "minor"
Root.default = "E"

# === I. POCKET — kick, snare, the riff ===

k1 >> play("<k(...(...k))..><..u.><-><.s.>", drcomp=0.5, amp=1.1).sometimes("stutter")
s1 >> play("<..o.><..o(.o)>", sample=3, bank=0, amp=0.95, hpf=200, room=0.15).human(40, 4)
b1 >> ebass([0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.4, 0, 0, 1.3, 1.5, 0, 1.4, 0, 1.4, 1.3, 1.4, 1.3, 1.5, 0, 1.3, 1.4], oct=PStep(8, 4, 3), pick=0.45, cutoff=fb(8, 800, 2400), decay=1.0, rel=0.18, fold=fperlin(16, 0.1, 0.35), hpf=80, tanh=0.15).penta()

# === II. LOCK — hihat, guitar stab on offbeats, sub-octave layer ===

h1 >> play("-(--)-(--)-(--)-([--])", dur=1/2, sample=PStep(16, 1, 3), rate=PWhite(0.95, 1.08), amp=PWhite(0.25, 0.5), pan=PWhite(-0.4, 0.4)).degrade(0.15)
g1 >> guit((P*[0, -2], P*[2, 10, 12, 3], P*[5, 7]), dur=var(P*[1, 1/2, 8], 8), oct=(5, 6), rate=0.4, mod=0.4, shape=0.45, amp=0.32, echo=0, eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3, hpf=180, lpf=fb(24, 1200, 4800))
b2 >> cbass([-2, -2.01] + P*[0, 0, 0, 0], dur=1, oct=4, sus=P[0.4, 0.4], amp=P[1.0, 0.7], hpf=40, lpf=600, shape=0.3).unison(2, 0.04)

# === III. VERSE RIFF — bass alternates phrases, snare ghosts, faim atmosphere ===

b1 >> ebass(var([P[0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], P[0, 0, 7, 0, 5, 3, 0, 0, 0, 5, 7, 5, 3, 0, -2, -2]], [16, 16]), dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.4, 0, 0, 1.3, 1.5, 0, 1.4, 0, 1.4, 1.3, 1.4, 1.3, 1.5, 0, 1.3, 1.4], oct=PStep(8, 4, 3), pick=fperlin(32, 0.3, 0.65), cutoff=fb(8, 800, 2400), decay=1.0, rel=0.18, fold=fperlin(16, 0.1, 0.4), hpf=80, tanh=0.2).penta()
n1 >> play("..(.s)(s.)..", sample=4, dur=1/2, amp=P[0.45, 0.25, 0.4, 0.25], hpf=400, delay=PSwing(0.04)).sometimes("stutter", 3)
f1 >> faim(var([0, 2, -2], [16, 8, 8]), dur=1/2, oct=PStep(8, 5, 4), beef=(0, 2), shape=0.3, amp=0.3) + PStep(5, melody(), 0)

# === IV. BUILD — riser, bass adds chromatic walk, drum fill swells ===

l1 >> sinepad((P*[0, 5, 7], 4), dur=8, oct=(4, 5), atk=4, sus=8, rel=4, amp=linvar([0, 0.45], 16), lpf=linvar([400, 4200], 16))
b1 >> ebass(var([P[0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], P[0, -2, -1, 0, 3, 5, 7, 8, 7, 5, 3, 0, -1, -2, 0, 0]], [16, 16]), dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.5, 0, 0, 1.4, 1.6, 0, 1.5, 0, 1.5, 1.4, 1.5, 1.4, 1.6, 0, 1.4, 1.5], oct=PStep(8, 4, 3), pick=0.55, cutoff=fb(8, 800, 3200), decay=1.0, rel=0.18, fold=fperlin(16, 0.15, 0.5), hpf=80, tanh=0.25, lofi=fi(16, 0, 0.4)).penta()
k1 >> play("<k(...(...k))..><..u.><-><.s(s.)>", drcomp=0.5, amp=1.15, fbdelay=fi(16, 0, 0.25), fbtime=0.25, fbfeed=0.5, fbcutoff=2200, beat_dur=1).often("stutter", PRand(2, 5))

# === V. DROP / CHORUS — full force, lapin wah lead, octave-up scream ===

l1.stop()
b1 >> ebass(var([P[0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], P[0, 0, 7, 0, 5, 3, 0, 0, 0, 5, 7, 5, 3, 0, -2, -2]], [16, 16]), dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.6, 0, 0, 1.5, 1.7, 0, 1.5, 0, 1.5, 1.4, 1.5, 1.4, 1.7, 0, 1.4, 1.5], oct=PStep(8, 4, 3), pick=0.6, cutoff=fb(8, 1000, 3600), decay=1.0, rel=0.18, fold=fb(24, 0.2, 0.55), hpf=80, tanh=0.3, octclean=0.4, ocsub=0.3, ocup=0.5).penta()
g1 >> guit((P*[0, -2, 5], P*[2, 10, 12, 3, 7], P*[5, 7, 10]), dur=var(P*[1/2, 1/4, 4], 8), oct=(5, 6), rate=0.4, mod=0.55, shape=0.6, amp=0.42, eb=0.6, ebfeed=0.65, ebmix=0.4, ebmode=2, ebwow=0.15, ebflutter=0.2, ebsat=0.45, hpf=180, lpf=fb(24, 1200, 5800), tubedrive=fperlin(32, 0.4, 1.2), tubewarm=0.5)
w1 >> lapin(([0, 7, 5, 12, 7, 10, 7, 5], 4), amp=var([0, 0.55], [PRand(8, 16), PRand(2, 6)]), dur=PDur(var([5, 7, 4], [8, 4, 4]), 8), sus=fperlin(16, 0.1, 0.4), oct=(5, 6), rate=0.85, shape=0.3, fx1=0, fx2=1, tanh=0.25, fold=fperlin(32, 0.2, 0.5), lpf=fb([8, 4], 1500, 6000)).unison(3, 0.2, 90)
n1 >> play("..(.s)(s.)..(s.)", sample=4, dur=1/2, amp=P[0.55, 0.3, 0.5, 0.3, 0.4], hpf=400, delay=PSwing(0.05)).often("stutter", 3)
k1 >> play("<k(...(...k))..><..u.><-><.s(s.)>", drcomp=0.55, amp=1.2, shape=0.2).sometimes("stutter")

# === VI. BREAKDOWN — strip to bass + kick, half-time feel, tension ===

g1.stop()
w1.stop()
n1.stop()
h1.stop()
f1.stop()
s1.stop()
b2.stop()
b1 >> ebass([0, 0, 0, 12, 0, 0, 7, 0], dur=1/2, sus=P[0.8, 0.1, 0.5, 0.15, 0.6, 0.1, 0.4, 0.4], amp=P[1.4, 0, 0, 1.3, 1.5, 0, 1.3, 0], oct=PStep(8, 4, 3), pick=0.55, cutoff=linvar([600, 1800], 16), decay=1.4, rel=0.3, fold=0.25, hpf=80, tanh=0.2).penta()
k1 >> play("<k...><..u.>", drcomp=0.5, amp=1.05)

# === VII. RE-EXPLODE — full chorus return, drop everything back in ===

s1 >> play("<..o.><..o(.o)>", sample=3, bank=0, amp=0.95, hpf=200, room=0.15).human(40, 4)
h1 >> play("-(--)-(--)-(--)-([--])", dur=1/2, sample=PStep(16, 1, 3), rate=PWhite(0.95, 1.08), amp=PWhite(0.3, 0.55), pan=PWhite(-0.4, 0.4)).degrade(0.1)
b2 >> cbass([-2, -2.01] + P*[0, 0, 0, 0], dur=1, oct=4, sus=P[0.4, 0.4], amp=P[1.0, 0.7], hpf=40, lpf=600, shape=0.3).unison(2, 0.04)
b1 >> ebass(var([P[0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], P[0, 0, 7, 0, 5, 3, 0, 0, 0, 5, 7, 5, 3, 0, -2, -2]], [16, 16]), dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.6, 0, 0, 1.5, 1.7, 0, 1.5, 0, 1.5, 1.4, 1.5, 1.4, 1.7, 0, 1.4, 1.5], oct=PStep(8, 4, 3), pick=0.6, cutoff=fb(8, 1000, 3800), decay=1.0, rel=0.18, fold=fb(24, 0.2, 0.6), hpf=80, tanh=0.3, octclean=0.4, ocsub=0.3, ocup=0.5).penta()
g1 >> guit((P*[0, -2, 5], P*[2, 10, 12, 3, 7], P*[5, 7, 10]), dur=var(P*[1/2, 1/4, 4], 8), oct=(5, 6), rate=0.4, mod=0.55, shape=0.6, amp=0.42, eb=0.6, ebfeed=0.65, ebmix=0.4, ebmode=2, ebwow=0.15, ebflutter=0.2, ebsat=0.45, hpf=180, lpf=fb(24, 1200, 5800), tubedrive=fperlin(32, 0.4, 1.2), tubewarm=0.5)
w1 >> lapin(([0, 7, 12, 10, 7, 5, 7, 0], 4), amp=var([0, 0.6], [PRand(6, 12), PRand(3, 8)]), dur=PDur(var([3, 5, 7], [8, 4, 4]), 8), sus=fperlin(16, 0.1, 0.5), oct=(5, 6, 7), rate=0.85, shape=0.4, fx1=0, fx2=1, tanh=0.3, fold=fperlin(32, 0.2, 0.6), lpf=fb([8, 4], 2000, 7000), octclean=0.3, ocup=0.6).unison(3, 0.2, 90)
k1 >> play("<k(...(...k))..><..u.><-><.s(s.)>", drcomp=0.55, amp=1.2, shape=0.2).sometimes("stutter")
n1 >> play("..(.s)(s.)..(s.)", sample=4, dur=1/2, amp=P[0.55, 0.3, 0.5, 0.3, 0.4], hpf=400, delay=PSwing(0.05)).often("stutter", 3)

# === VIII. OUTRO — cut everything but the riff, sub-octave fade ===

s1.stop()
h1.stop()
g1.stop()
w1.stop()
n1.stop()
b2.stop()
k1.stop()
b1 >> ebass([0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=linvar([1.4, 0], 32) * P[1, 0, 0, 0.9, 1, 0, 0.9, 0, 0.9, 0.85, 0.9, 0.85, 1, 0, 0.85, 0.9], oct=PStep(8, 4, 3), pick=0.45, cutoff=linvar([2400, 600], 32), decay=1.0, rel=0.18, fold=linvar([0.3, 0], 32), hpf=80, tanh=linvar([0.2, 0], 32)).penta()

b1.stop()
