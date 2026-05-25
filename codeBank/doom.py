# edge 93 — intro + refined sound design
Clock.bpm = 93
Root.default = "A#"

# === INTRO: fog — harmonic DNA emerges from nothing ===
p1 >> darkpad([0, 6], dur=8, oct=4, sus=8, atk=4, dark=0.7, detune=0.02, amp=linvar([0, 0.35], 32), lpf=linvar([300, 1200], 64), room=0.9, mix=0.7)
p2 >> ethpad([0, 1, 7], dur=8, oct=5, attack=4, release=4, amp=linvar([0, 0.3], 48), room=0.9, mix=0.6)

# === INTRO 2: c2 arpeggio barely audible, drowned in reverb ===
c2 >> cs80([0, 0, 0.5], cutoff=linvar([200, 1500], [16, 8, 16]), dec=1.0, leg=0, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5, 2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([200, 1200], 64), dur=1/6, shape=0, amp=var([0, 0.15], [24, 8]), room=0.7, mix=0.5).unison(2)

# === INTRO 3: c1 enters filtered, delay pulls it wide ===
c1 >> cs80(cutoff=linvar([400, 3000], [8, 4, 8]), dec=1.0, leg=var([0, 4], [31, 1]), lpr=0.1, oct=(4, PStep(4, 3, 4)), vibspeed=P[0.5, 2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 2000], 64), dur=1/6, shape=0, room=0.5, mix=0.3, amp=linvar([0, 0.5], 32), delay=PSine(128)*0.33)

# === MAIN: edge arrives — lo-fi bite but with space ===
c1.bits = 8
c1.crush = var([8, 5], [12, 4])
c1.shape = 0.2
c1.fx1 = 1
c1.glide = 1
c1.lpf = linvar([400, 4000], 128)

# c2 — tape warmth instead of raw dist2, shimmer for depth
c2 >> cs80([0, 0, 0.5], cutoff=linvar([400, 5300], [8, 4, 8]), dec=1.0, leg=0, lpr=0.1, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5, 2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.1, tape=var([0, 0.8], [8, 8]), tapedrive=var([1, 3], [12, 4]), shimmer=var([0, 0.5], [16, 16]), shimsize=0.6, shimpitch=var([1, 2], [8, 8]), shimmix=0.3, room=0.4, mix=0.25).unison(3)

# pad opens — shimmer bloom
p1.shimmer = 0.5
p1.shimsize = 0.6
p1.shimpitch = var([1, 2, 1.5], [8, 4, 4])
p1.shimmix = 0.4
p1.amp = 0.3

# === EVOLVE: harmonic shift, distortion breathes in and out ===
c2.degree = var([[0, 0, 0.5], [0, 1, 7]], [16, 16])
c2.dist2 = var([0, 0.6, 0, 1.2], [8, 4, 12, 4])
c2.shape = var([0.1, 0.3], [12, 4])

# c1 widens
c1.oct = (4, PStep(4, 3, 4))
c1.crush = var([8, 4, 8], [8, 4, 4])

# === PEAK: dist2 flares for 4 beats then pulls back ===
c2.degree = [7, 7, 14]
c2.dist2 = var([0, 4, 0], [8, 4, 12])
c2.glide = linvar([3, 20], 16)
c1.oct = (5, PStep(5, 6, 6))

# pads darken underneath the peak
p1.lpf = linvar([1200, 600], 32)
p2.amp = linvar([0.3, 0.5], 16)

# === DESCENT: everything filters down, reverb takes over ===
c2.dist2 = linvar([4, 0], 32)
c2.lpf = linvar([4000, 400], 48)
c2.shimmer = linvar([0.5, 0.9], 32)
c2.shimmix = linvar([0.3, 0.8], 32)
c1.lpf = linvar([4000, 400], 64)
c1.shape = linvar([0.2, 0], 48)
c1.room = linvar([0.5, 0.9], 32)
p1.amp = linvar([0.3, 0], 64)
p2.amp = linvar([0.5, 0], 64)
