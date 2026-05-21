# ─────────────────────────────────────────────────────────────
# redline.py  —  87 BPM / A minor / boom bap
#
# Core concept: sample= variation as drum texture.
#   s1 and h1/h2 use sample=var() so the same pattern character
#   hits different sample banks per section — the kit evolves
#   without the pattern changing.
#   m1 has delay=0.5: chord stabs land on the 8th-note off-beat,
#   classic hip-hop placement. Sus is short so they chop and decay.
#   b1 walks in 16th notes for jazz-inflected motion.
#
# Arc (bars):
#    0–16   intro      kick + bass only
#   16–40   verse 1    kit enters, sample bank 0
#   40–56   hook       chords and melody in, sample bank 1
#   56–88   verse 2    sample bank shifts again, denser bass walk
#   88–104  outro      melody drops, bass trails
# ─────────────────────────────────────────────────────────────

Clock.bpm = 87
Scale.default = "minor"
Root.default = "A"

secs = [64, 96, 64, 128, 64]

k1 >> compkick(dur=1, oct=3,
               amp=var([0.88, 0.9, 0.88, 0.92, 0.5], secs),
               drive=var([0.18, 0.22, 0.2, 0.25, 0.08], secs),
               room=0.2, mix=0.25)

s1 >> play(". . . . o . . . ", dur=1/4,
           amp=var([0, 0.72, 0.68, 0.75, 0.35], secs),
           sample=var([0, 0, 1, 2, 0], secs),
           room=0.35, mix=0.45)

h1 >> play("- . ", dur=1/4,
           amp=var([0, 0.32, 0.35, 0.35, 0.15], secs),
           sample=var([0, 1, 1, 2, 0], secs))

h2 >> play(". . . . - . . . ", dur=1/4,
           amp=var([0, 0.38, 0.42, 0.4, 0.2], secs),
           sample=var([0, 1, 2, 2, 0], secs))

b1 >> dbass([0, 3, 5, 3, 0, -2, 3, 0,
             5, 3, 0, 5, 7, 5, 3, 0], dur=1/4, oct=5,
            amp=var([0.82, 0.85, 0.82, 0.88, 0.4], secs),
            sus=var([0.5, 0.55, 0.5, 0.58, 0.3], secs),
            lpf=var([500, 600, 500, 700, 300], secs),
            room=0.2, mix=0.28)

m1 >> juno([(0,2,4), rest(0), (3,5,7), rest(0),
            (2,4,6), rest(0), (6,1,3), rest(0)], dur=1, oct=4,
           amp=var([0, 0.38, 0.42, 0.42, 0.18], secs),
           delay=0.5,
           sus=0.4,
           room=0.4, mix=0.5,
           lpf=linvar([800, 3000], 64))

n1 >> pluck([0, 3, 5, 7, 5, 3, 0, 3], dur=1/2, oct=5,
            amp=var([0, 0, 0.38, 0.42, 0.22], secs),
            sus=var([0.6, 0.6, 0.8, 1.0, 0.5], secs),
            room=0.3, mix=0.4,
            lpf=linvar([2000, 5000], 64))
