# snares — 190 bpm, Eb phrygian, Venetian Snares style
# Breakcore: chopped amen chaos + piano/strings contrast (Rossz Csillag Alatt Született)
# 7-note piano phrase phases against 4/4 grid — constant metric displacement
Clock.bpm = 190
Scale.default = "phrygian"
Root.default = "Eb"

#@#@ snares

#@ prelude

# piano alone first — melancholic, phasing against 4/4 (7 notes × 0.25 = 1.75 beats)
pn >> piano([0,-2,3,5,-4,2,-7], oct=5, dur=0.25, sus=PRand([0.2,0.35,0.5],4), amp=0.55, cheapverb=0.45, cvdecay=2, pan=sinvar([-0.25,0.25],7))

# viola — slow sustained contrast
vi >> viola([0,-4,3,-7], oct=4, dur=var([2,3,4,2],[8,4,8,4]), sus=sinvar([1.5,3],16), amp=sinvar([0.1,0.3],24), room=0.85, mix=0.75, vibrato=sinvar([0,0.3],16))

#@ break

# kick layer 1 — main chopped amen
dk >> play("X.X.X...X.X.X.X.", dur=0.25, amp=PLife(0.75), hpf=50)

# kick layer 2 — phasing offset (7-beat cycle)
d2 >> play("..X...X...X...X.", dur=0.25, amp=0.7, sample=1)

# snare layer 1 — complex position
sn >> play("..o...o.o...o.o.", dur=0.25, amp=PRand([0.8,1,0.6,0.9],4), sample=2)

# snare layer 2 — another offset layer
t2 >> play(".o..o...o..o....", dur=0.25, amp=0.6, sample=3, hpf=2000, pitchShift=var([0,1,-1,0.5],4))

# hats — 32nd note chaos
ht >> play("i", dur=0.125, amp=PLife(0.7), hpf=9000, pan=PRand([-0.4,0,0.4],4))

# glitchbass — the brutal low end
gb >> glitchbass([0,-4,3,-4,0,-7,-4,0], oct=4, dur=0.25, sus=0.15, amp=0.8, cutoff=sinvar([600,8000],4), rq=0.4, rate=sinvar([0.5,2],4))

#@ chaos

# scatter — metallic noise spray between hits
sc >> scatter(0, oct=5, dur=PFDur((7,16),(5,8)), amp=sinvar([0,0.45],4), lpf=sinvar([3000,14000],4), hpf=2000, rate=sinvar([0.01,0.1],2))

# angst — shriek against the piano
ag >> angst([0,-4,3,-4], oct=7, dur=PRand([0.25,0.5,0.125],4), sus=0.1, amp=sinvar([0.3,0.7],4), cutoff=sinvar([6000,20000],2), rq=0.2, rate=sinvar([0.6,1.0],4))

# war — adds mid-range violence (brief stabs)
wr >> war([0,-4,rest(0),-4,0,rest(0),-7,rest(0)], oct=5, dur=0.25, sus=0.1, amp=sinvar([0,0.6],4), beef=12, cutoff=sinvar([1000,8000],4), rq=0.5)

# piano phrase goes higher — contrast intensifies
pn.oct = var([5,6],[14,7])
pn.amp = sinvar([0.45, 0.75], 8)

#@ peak

# all drums maxed with PLife
dk >> play("X.X.X...X.X.X.X.", dur=0.25, amp=PLife(0.9))
sn >> play("..o...o.o...o.o.", dur=0.25, amp=PRand([0.85,1,0.65,0.95],4), sample=2, pitchShift=var([0,-1,1,0],8))
t2 >> play(".o..o...o..o....", dur=0.25, amp=PRand([0.65,0.8,0.5,0.7],4), sample=3, pitchShift=var([0,1,-1,2],4))
ht >> play("i", dur=0.0625, amp=PLife(0.8), hpf=9000)

# piano drops to low octave — inversion of contrast
pn >> piano([0,-2,3,5,-4,2,-7], oct=3, dur=0.25, sus=PRand([0.15,0.25,0.4],4), amp=0.7, cheapverb=0.4, cvdecay=1.5)
vi.amp = sinvar([0.25, 0.5], 8)
gb.amp = sinvar([0.7, 1.0], 4)

#@ resolution(48)

d2.amp = linvar([0.7, 0], 16)
t2.amp = linvar([0.6, 0], 16)
ag.amp = linvar([0.6, 0], 16)
wr.amp = linvar([0.5, 0], 12)
sc.amp = linvar([0.4, 0], 12)
dk.amp = linvar([0.75, 0], 24)
sn.amp = linvar([0.85, 0], 24)
ht.amp = linvar([0.7, 0], 24)
gb.amp = linvar([0.7, 0], 24)
pn >> piano([0,-2,3,5,-4,2,-7], oct=5, dur=0.25, sus=PRand([0.2,0.35,0.5],4), amp=linvar([0.6, 0], 48), cheapverb=0.5, cvdecay=2.5)
vi.amp = linvar([0.4, 0], 48)
