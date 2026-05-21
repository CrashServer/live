# ─────────────────────────────────────────────────────────────
# sediment.py  —  138 BPM / C minor / dark techno
#
# Core concept: sinvar as single metabolic rate.
#   lpf and dfamt both oscillate on a 64-beat sinvar so the
#   arrangement breathes as one organism. dynfuzz on svdk keys
#   to section amp — peaks gritty, breakdown clean.
#   plaitsX preset=11 (chord engine) for thick mid-pad.
#
# Arc (bars):
#    0–24   intro      kick + sub, static
#   24–56   groove     hats enter, lead barely audible
#   56–80   peak       dynfuzz opens, filter climbs
#   80–96   break      pad + sub only, long tails
#   96–128  return     groove resumes, tighter drive
# ─────────────────────────────────────────────────────────────

Clock.bpm = 138
Scale.default = "minor"
Root.default = "C"

secs = [96, 128, 96, 64, 128]

k1 >> compkick(dur=1, oct=3,
               amp=var([0.9, 0.92, 0.95, 0.5, 0.92], secs),
               drive=var([0.15, 0.28, 0.38, 0.08, 0.28], secs),
               room=0.1, mix=0.1)

s1 >> play(". . . . o . . . ", dur=1/4,
           amp=var([0, 0.7, 0.78, 0.5, 0.7], secs),
           room=0.18, mix=0.25)

h1 >> play("- . - . - - . - ", dur=1/4,
           amp=var([0, 0.48, 0.55, 0.28, 0.48], secs),
           sample=2)

h2 >> play("- . . . - . . - ", dur=1/4,
           amp=var([0, 0.32, 0.4, 0.2, 0.32], secs),
           sample=1)

b1 >> dbass([0, -2, 3, 0], dur=[2, 2, 2, 2], oct=5,
            amp=var([0.85, 0.88, 0.92, 0.65, 0.88], secs),
            lpf=sinvar([350, 1400], 64),
            sus=var([1.9, 2.0, 2.2, 1.6, 2.0], secs),
            room=0.2, mix=0.2)

n1 >> svdk([0, 3, 0, 5, 7, 5, 0, -2], dur=1/4, oct=4,
           amp=var([0, 0.52, 0.62, 0.38, 0.52], secs),
           dynfuzz=var([0, 0.5, 0.72, 0, 0.52], secs),
           dfmix=var([0, 0.38, 0.55, 0, 0.38], secs),
           dfamt=sinvar([0.2, 0.85], 32),
           lpf=linvar([700, 4500], 128),
           sus=var([0.1, 0.12, 0.08, 0.15, 0.12], secs),
           shape=0.18)

p1 >> plaitsX([0, -2, 3, 5], dur=[4, 4, 4, 4], oct=5, preset=11,
              amp=var([0, 0.28, 0.32, 0.48, 0.28], secs),
              cheapverb=0.72, cvdecay=4.5,
              lpf=linvar([500, 2200], 96))

m1 >> juno([(0,2,4), rest(0), (3,5,7), rest(0), (2,4,6), rest(0)], dur=2, oct=4,
           amp=var([0, 0.42, 0.5, 0.32, 0.42], secs),
           shape=sinvar([0, 0.28], 16),
           cheapverb=0.5, cvdecay=2.0,
           lpf=var([700, 1100, 2800, 500, 1100], secs))
