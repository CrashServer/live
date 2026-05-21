# ─────────────────────────────────────────────────────────────
# ferment.py  —  170 BPM / D minor / drum & bass
#
# Core concept: delays AS rhythm, not decoration.
#   fbdelay fbtime=0.75 on reese  → dotted-8th ghost hits create
#     syncopated 16th subdivisions from a simple 16th bassline
#   echoBoy eb=0.75 on lead       → phrase trails overlap the bar,
#     melodic smear over the break
#   dubdelay on sub fill          → stereo ping-pong thickens drop 2
#
# Arc (bars):
#    0–16   intro      kick + sub only, bare
#   16–48   build      reese enters, fbdelay ghosts emerge
#   48–80   drop 1     full arrangement, echoBoy on lead
#   80–96   breakdown  strip to bass + delay tails, atmosphere
#   96–128  drop 2     harder feedback, dubdelay fill, dense
#  128–144  outro      fade, delays decay to silence
# ─────────────────────────────────────────────────────────────

Clock.bpm = 170
Scale.default = "minor"
Root.default = "D"

# 1 bar = 4 beats at 170 BPM
# secs[i] = beat-count of each section
secs = [64, 128, 128, 64, 128, 64]

# ─── DRUMS ──────────────────────────────────────────────────

# Kick — compkick, straight 4/4 anchor
k1 >> compkick(dur=1, oct=3,
               amp=var([0.9, 0.85, 0.9, 0.75, 0.95, 0.5], secs),
               drive=var([0.2, 0.2, 0.3, 0.1, 0.4, 0.1], secs),
               room=0.1, mix=0.15)

# Snare — backbeat 2 & 4; echoBoy eb=0.75 adds a
# dotted-8th ghost snare that bleeds across the bar
s1 >> play(". . . . o . . . ", dur=1/4, sample=0,
           amp=var([0.85, 0.85, 0.9, 0.8, 0.95, 0.4], secs),
           eb=var([0, 0.75, 0.75, 0.75, 0.75, 0.5], secs),
           ebfeed=0.35,
           ebmix=var([0, 0.35, 0.45, 0.5, 0.5, 0.25], secs))

# Break loop — Amen-style, enters at drop 1
l1 >> play("X . x . X x . X . x X . x . X . ", dur=1/2, sample=1,
           amp=var([0, 0, 0.75, 0.6, 0.85, 0], secs),
           shape=0.12)

# Tight 16th perc — adds rhythmic density in drops
t1 >> play("t . ", dur=1/4,
           amp=var([0, 0, 0.28, 0.2, 0.32, 0], secs),
           eb=var([0, 0, 0.25, 0.25, 0.25, 0], secs),
           ebfeed=0.2, ebmix=0.3)

# ─── BASS ───────────────────────────────────────────────────

# Sub — slow root motion, heavy and low
b1 >> dbass([0, 0, -2, 0], dur=[2, 1, 1, 2], oct=5,
            amp=var([0.85, 0.85, 0.9, 0.8, 0.9, 0.3], secs),
            lpf=var([350, 400, 500, 350, 500, 200], secs),
            sus=var([1.8, 1.8, 2.0, 1.5, 2.0, 1.0], secs),
            room=0.2, mix=0.25)

# Reese — fast 16th cut line, the rhythmic heart of the track.
# fbtime=0.75 (dotted 8th) means every note spawns a ghost
# exactly 3/4 of a beat later — lands between the next two 16ths,
# turning a straight 16th line into a syncopated DnB roll.
# fbfeed ramps up through sections for increasing density.
b2 >> reese([0, 0, -2, 0, 3, 0, -2, 3,
             0, 3, 5, 3, 0, -2, 0, 5], dur=1/4, oct=4,
            amp=var([0, 0.7, 0.75, 0.6, 0.82, 0], secs),
            fbdelay=var([0, 0.65, 0.72, 0.65, 0.8, 0], secs),
            fbtime=0.75,
            fbfeed=var([0, 0.4, 0.48, 0.42, 0.62, 0], secs),
            fbcutoff=var([2000, 2000, 3000, 1500, 4000, 1000], secs),
            fbspread=0.25,
            lpf=linvar([800, 3500], 96),
            cutoff=var([1000, 1200, 2500, 800, 3200, 500], secs),
            shape=0.2, drive=0.25,
            sus=0.08)

# Sub fill — 8th note stabs in drop 2 only;
# dubdelay dublen=0.5 creates a tight stereo echo
# that doubles the attack and widens the low end
b3 >> bass([0, -2, 0, 3, 0, -2, 3, 5], dur=1/2, oct=5,
           amp=var([0, 0, 0, 0, 0.65, 0], secs),
           dubd=var([0, 0, 0, 0, 0.65, 0], secs),
           dublen=0.5, dubfeed=0.4, dubwidth=0.2,
           lpf=2500, sus=0.1)

# ─── HARMONY ────────────────────────────────────────────────

# Atmospheric pad — washes in at breakdown, threads through
p1 >> plaitsX([0, 3, 7], dur=[4, 4, 8], oct=5, preset=4,
              amp=var([0, 0, 0.22, 0.35, 0.18, 0.1], secs),
              cheapverb=0.8, cvdecay=5.0,
              lpf=linvar([600, 2500], 128))

# Hoover stab — half-note chord hits with the same
# dotted-8th fbdelay as the reese; the two fbdelays
# interlock rhythmically, the stab echo answers the bass ghost
m1 >> juno([(0,4,7), rest(0), (-2,3,7), rest(0)], dur=1/2, oct=4,
           amp=var([0, 0, 0.58, 0.5, 0.65, 0], secs),
           fbdelay=var([0, 0, 0.68, 0.62, 0.75, 0], secs),
           fbtime=0.75,
           fbfeed=var([0, 0, 0.38, 0.32, 0.52, 0], secs),
           fbcutoff=var([600, 600, 2000, 1000, 2800, 600], secs),
           cutoff=var([500, 500, 1800, 800, 2600, 400], secs),
           shape=0.3,
           cheapverb=0.5, cvdecay=1.5)

# ─── LEAD ───────────────────────────────────────────────────

# Lead — 8th note melody; echoBoy eb=0.75 at 170 BPM
# = 265ms delay, phrases overlap by a dotted 8th so
# notes trail over the bar line and blend with incoming hits
n1 >> saw([0, 3, 5, 7, 5, 3, 0, -2,
           0, 5, 7, 10, 7, 5, 3, 0], dur=1/8, oct=5,
          amp=var([0, 0, 0.5, 0.42, 0.55, 0], secs),
          eb=0.75,
          ebfeed=var([0, 0, 0.38, 0.4, 0.45, 0], secs),
          ebmix=var([0, 0, 0.38, 0.42, 0.48, 0], secs),
          ebsat=0.2,
          lpf=linvar([1200, 6000], 64),
          sus=[0.15, 0.1, 0.2, 0.1, 0.15, 0.1, 0.3, 0.2,
               0.15, 0.1, 0.2, 0.1, 0.15, 0.1, 0.25, 0.15],
          shape=0.15)

# Delay texture — sparse pluck pings, fbdelay=0.8 + fbfeed=0.65
# makes each note self-sustain into a rhythmic echo pattern.
# fbtime modulates between quarter and dotted-8th across sections,
# shifting the echo grid and creating polyrhythmic interference
n2 >> pluck([0, 5, 7, 3], dur=[2, 2, 2, 2], oct=6,
            amp=var([0, 0, 0.28, 0.32, 0.32, 0.1], secs),
            fbdelay=0.8,
            fbtime=var([1, 0.75, 0.5], [64, 192, 192]),
            fbfeed=0.65, fbcutoff=4000, fbspread=0.5,
            cheapverb=0.7, cvdecay=3.5)
