# ─────────────────────────────────────────────────────────────
# glycine.py  —  88 BPM / G minor / lo-fi soul
#
# Core concept: tape warmth + ghost-note groove.
#   Every voice runs through tape saturation. h1 and h2 are
#   staggered 8th-note layers (on + off the beat) at very
#   different amps — together they read as 16th hats with ghosts.
#   Walking 16th bass and slow 1-bar chord changes.
#   pluck sus varies from short to long across sections for phrasing.
#
# Arc (bars):
#    0–16   intro      bass + kick only
#   16–48   verse      kit enters, pluck melody
#   48–64   chorus     chords swell, melody climbs
#   64–80   break      pluck + pad, reverb heavy
#   80–112  verse 2    full arrangement
#  112–128  outro      fade, bass last
# ─────────────────────────────────────────────────────────────

Clock.bpm = 88
Scale.default = "minor"
Root.default = "G"

secs = [64, 128, 64, 64, 128, 64]

k1 >> compkick(dur=1, oct=3,
               amp=var([0.85, 0.88, 0.9, 0.5, 0.88, 0.4], secs),
               drive=var([0.1, 0.18, 0.22, 0.05, 0.2, 0.05], secs),
               room=0.15, mix=0.2)

s1 >> play(". . . . o . . . ", dur=1/4,
           amp=var([0, 0.72, 0.78, 0, 0.72, 0.3], secs),
           delay=0.03,
           room=0.25, mix=0.35)

h1 >> play("- . - . - . - . ", dur=1/4,
           amp=var([0, 0.45, 0.5, 0.28, 0.48, 0.2], secs),
           sample=2)

h2 >> play(". - . - . - . - ", dur=1/4,
           amp=var([0, 0.12, 0.15, 0.08, 0.15, 0.06], secs),
           sample=2)

b1 >> dbass([0, 3, 5, 3, 0, -1, 3, 5,
             7, 5, 3, 5, 0, 5, 3, 0], dur=1/4, oct=5,
            amp=var([0.82, 0.85, 0.88, 0.58, 0.88, 0.35], secs),
            lpf=var([400, 500, 650, 300, 550, 200], secs),
            sus=var([0.5, 0.55, 0.6, 0.45, 0.58, 0.3], secs),
            tape=var([0.5, 0.55, 0.5, 0.3, 0.55, 0.2], secs),
            tapedrive=var([0.3, 0.35, 0.38, 0.2, 0.35, 0.1], secs))

n1 >> pluck([0, 3, 5, 7, 5, 3, 0, -1,
             0, 5, 7, 9, 7, 5, 3, 0], dur=1/4, oct=5,
            amp=var([0, 0.45, 0.52, 0.38, 0.48, 0.25], secs),
            sus=var([0.6, 0.7, 1.2, 2.0, 0.8, 1.5], secs),
            tape=0.4, tapedrive=0.25,
            room=0.3, mix=0.35,
            lpf=linvar([1500, 5000], 64))

m1 >> juno([(0,2,4), (3,5,7), (2,4,6), (3,5,7)], dur=4, oct=4,
           amp=var([0, 0.38, 0.52, 0.28, 0.42, 0.15], secs),
           sus=3.5,
           tape=0.45, tapedrive=0.3,
           cheapverb=0.6, cvdecay=3.0,
           lpf=linvar([600, 2500], 96))

p1 >> plaitsX([0, 5, 3, 7], dur=[4, 4, 4, 4], oct=5, preset=4,
              amp=var([0, 0.22, 0.35, 0.4, 0.25, 0.12], secs),
              cheapverb=0.8, cvdecay=6.0,
              lpf=linvar([400, 1800], 112))
