# ─────────────────────────────────────────────────────────────
# splinter.py  —  163 BPM / F minor / jungle
#
# Core concept: sample banks as texture layers.
#   l1 and l2 are two break loops running different patterns.
#   sample=var() shifts l1 through banks each section — the break
#   character changes without the pattern changing. reese fbdelay
#   same dotted-8th technique as ferment but with crush added in
#   drop 2, turning ghost hits into bitcrushed splinters.
#   b2 lays a slower root underneath the fast reese cut.
#
# Arc (bars):
#    0–16   intro      kick + b2 only, bare
#   16–48   drop 1     l1 and reese enter, saw lead
#   48–72   drop 2     l2 layers in, sample banks shift, crush
#   72–88   outro      l2 drops, decay
# ─────────────────────────────────────────────────────────────

Clock.bpm = 163
Scale.default = "minor"
Root.default = "F"

secs = [64, 128, 96, 64]

k1 >> compkick(dur=1, oct=3,
               amp=var([0.92, 0.95, 0.98, 0.85], secs),
               drive=var([0.2, 0.3, 0.42, 0.3], secs),
               room=0.08, mix=0.1)

l1 >> play("X . x . X x . X . x X . . x . . ", dur=1/2,
           sample=var([0, 1, 2, 1], secs),
           amp=var([0, 0.85, 0.9, 0.75], secs),
           shape=var([0, 0.12, 0.2, 0.14], secs))

l2 >> play("X x . X . x . X x . . X . x X . ", dur=1/2,
           sample=var([1, 1, 2, 2], secs),
           amp=var([0, 0, 0.72, 0], secs),
           shape=var([0, 0, 0.18, 0], secs))

b1 >> reese([0, 0, 3, 0, -2, 0, 5, 3,
             0, -2, 0, 5, 3, 0, 5, 7], dur=1/4, oct=4,
            amp=var([0, 0.85, 0.9, 0.75], secs),
            fbdelay=var([0, 0.62, 0.72, 0.65], secs),
            fbtime=0.75,
            fbfeed=var([0, 0.4, 0.55, 0.45], secs),
            fbcutoff=var([1500, 2500, 4500, 3000], secs),
            drive=var([0.2, 0.3, 0.42, 0.35], secs),
            cutoff=var([800, 1500, 3500, 2000], secs),
            sus=0.08, shape=0.15)

b2 >> bass([0, 0, -2, 3], dur=[3, 1, 2, 2], oct=5,
           amp=var([0.78, 0.8, 0.82, 0.65], secs),
           lpf=linvar([500, 3000], 128),
           sus=var([2.5, 2.8, 2.0, 1.5], secs),
           shape=var([0.12, 0.15, 0.22, 0.18], secs))

n1 >> saw([0, 7, 3, 10, 5, 12, 0, -2,
           7, 3, 5, -3, 0, 8, 5, 3], dur=1/8, oct=5,
          amp=var([0, 0.5, 0.58, 0.45], secs),
          shape=var([0.12, 0.2, 0.32, 0.25], secs),
          crush=var([0, 0, 0.45, 0.25], secs),
          lpf=linvar([1200, 8000], 64),
          sus=var([0.1, 0.08, 0.06, 0.1], secs))

p1 >> plaitsX([0, 5, 7, 3], dur=[4, 4, 4, 4], oct=5, preset=8,
              amp=var([0.3, 0.25, 0.18, 0.22], secs),
              cheapverb=0.65, cvdecay=3.0,
              lpf=linvar([600, 3000], 96))
