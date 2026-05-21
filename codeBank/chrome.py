# ─────────────────────────────────────────────────────────────
# chrome.py  —  143 BPM / F# minor / UK drill
#
# Core concept: 808 pitch drops as melodic gesture.
#   b1 porta ramps from 0.08 → 0.25 across sections — early
#   sections have tight glides, drop 2 gets long dramatic drops.
#   Arrangement is intentionally sparse: hi-hat stays minimal
#   so the 808 motion sits in the open space.
#   n1 saw is soaked in reverb (mix=0.75) to smear into texture.
#
# Arc (bars):
#    0–16   intro      kick + 808 only
#   16–40   verse      hi-hat and lead enter filtered low
#   40–72   drop 1     chord stabs open up, lead filter climbs
#   72–88   drop 2     808 porta maxes, everything louder
# ─────────────────────────────────────────────────────────────

Clock.bpm = 143
Scale.default = "minor"
Root.default = "F#"

secs = [64, 96, 128, 64]

k1 >> compkick(dur=1, oct=3,
               amp=var([0.95, 0.95, 0.98, 0.98], secs),
               drive=var([0.3, 0.35, 0.42, 0.45], secs),
               room=0.1, mix=0.12)

s1 >> play(". . . . o . . . ", dur=1/4,
           amp=var([0, 0.7, 0.75, 0.78], secs),
           room=0.52, mix=0.65)

h1 >> play("- . ", dur=1/4,
           amp=var([0, 0.35, 0.4, 0.38], secs),
           sample=2)

b1 >> bass([0, -2, 0, 5, 3, -2, 0, 7], dur=[3, 1, 2, 2, 3, 1, 2, 2], oct=3,
           amp=var([0.88, 0.92, 0.95, 0.98], secs),
           sus=var([4.0, 5.0, 6.0, 7.0], secs),
           porta=var([0.08, 0.12, 0.18, 0.25], secs),
           lpf=var([200, 240, 280, 320], secs),
           room=0.18, mix=0.22)

n1 >> saw([0, 0, -2, 0, 3, 0, 5, 3], dur=2, oct=4,
          amp=var([0, 0.45, 0.52, 0.55], secs),
          sus=var([1.5, 2.0, 2.8, 3.2], secs),
          room=0.68, mix=0.75,
          lpf=linvar([600, 3500], 128),
          shape=var([0, 0.1, 0.15, 0.18], secs))

p1 >> juno([0, rest(0), -2, rest(0), 3, rest(0), 5, rest(0)], dur=2, oct=4,
           amp=var([0, 0.35, 0.42, 0.45], secs),
           sus=2.5,
           cheapverb=0.65, cvdecay=4.0,
           lpf=linvar([400, 2200], 96),
           shape=0.12)
