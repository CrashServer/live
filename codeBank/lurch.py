# ─────────────────────────────────────────────────────────────
# lurch.py  —  140 BPM / Bb minor / classic trap
#
# Core concept: 808 as the lead instrument.
#   b1 sus > dur so notes overlap and pitch-slide into each other
#   via porta — the 808 smear. h1.every(16, "stutter", 3) fires
#   a triplet roll every 4 bars without needing a separate player.
#   Melody uses P[] with PRand so the hook shifts slightly each
#   cycle — never quite the same twice.
#
# Arc (bars):
#    0–16   intro      808 + kick, bare
#   16–48   hook       hats, bells, pad enter
#   48–64   break      808 + snare only
#   64–96   drop       full, roll hats active
# ─────────────────────────────────────────────────────────────

Clock.bpm = 140
Scale.default = "minor"
Root.default = "Bb"

secs = [64, 128, 64, 128]

k1 >> compkick(dur=1, oct=3,
               amp=var([0.92, 0.95, 0.5, 0.95], secs),
               drive=var([0.28, 0.32, 0.15, 0.35], secs),
               room=0.12, mix=0.18)

s1 >> play(". . . . o . . . ", dur=1/4,
           amp=var([0, 0.75, 0.65, 0.78], secs),
           room=0.6, mix=0.72)

h1 >> play("- . - . - . - . - - - . - . - . ", dur=1/4,
           amp=var([0, 0.42, 0, 0.45], secs),
           sample=1)
h1.every(16, "stutter", 3)

b1 >> bass([0, 0, -2, 0, 3, 0, -2, 5], dur=2, oct=3,
           amp=var([0.9, 0.92, 0.88, 0.95], secs),
           sus=var([3.5, 4.0, 3.0, 4.5], secs),
           porta=var([0, 0.12, 0, 0.15], secs),
           lpf=var([250, 280, 220, 300], secs),
           room=0.2, mix=0.28)

n1 >> pluck(P[0, 3, PRand([5, 7]), 7, 5, PRand([3, 5]), 0, -2,
              0, 5, PRand([7, 9]), 5, 3, 5, PRand([0, 3]), -2], dur=1/4, oct=6,
            amp=var([0, 0.5, 0.32, 0.55], secs),
            sus=[0.1, 0.08, 0.12, 0.08, 0.15, 0.08, 0.1, 0.12,
                 0.1, 0.08, 0.12, 0.1, 0.08, 0.12, 0.15, 0.08],
            room=0.45, mix=0.55)

p1 >> supersaw([0, 3, 0, 5], dur=8, oct=4,
               amp=var([0, 0.18, 0.25, 0.2], secs),
               sus=linvar([4, 7], 64),
               cheapverb=0.78, cvdecay=5.0,
               lpf=linvar([500, 2000], 96),
               shape=0.08)
