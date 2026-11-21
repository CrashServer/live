#@#@ afroDub
# 110 BPM — C dorian — polyrhythmic dub-techno / deep afro-house
# pkit layers, cross-genre merge, phase rotation, reese/arpy/eeri/supersaw/glitcher

Clock.bpm = 110
Root.default = "C"
Scale.default = "dorian"

#@ open — afro kick, spring-soaked hats, reese sub

_ka = pkit("afro", seed=5)

d1 >> play(_ka.kick, oct=3, amp=1.1,
    spring=0.4, sprdecay=1.3, sprtens=0.3, sprdamp=0.5)

d2 >> play(_ka.hat, amp=0.5, pan=PRand([-0.2, 0, 0.2]),
    spring=0.55, sprdecay=0.7, sprdamp=0.6)

b1 >> reese([0, rest(0), rest(0), rest(0), -1, rest(0), rest(0), rest(0)],
    oct=3, dur=1, sus=3.5,
    detune=0.04, cutoff=linvar([500, 1200], 32), rq=0.5,
    amp=0.95, tanh=0.55, tanhmix=0.7,
    low=1.4, lowfreq=80)

#@ pads — eeri floats in, supersaw filtered shut then opens

g1 >> eeri([0, 3, 7, 3], oct=5, dur=4, sus=7,
    rate=2, cutoff=sinvar([600, 1600], 24),
    amp=0.35, cheapverb=0.65, cvdecay=3.5, cvdamp=0.5,
    pan=sinvar([-0.3, 0.3], 20))

c1 >> supersaw([0, -1, 3, 4], oct=5, dur=8, sus=7,
    rate=0.2, cutoff=linvar([400, 2200], 64), rq=0.65,
    amp=0.28, cheapverb=0.5, cvdecay=2.0, pan=-0.25)

#@ melody — arpy dorian + glitcher texture + snare + perc

m1 >> arpy([0, 2, 3, 5, 7, 5, 3, 2, 0, -1, 0, 2, 3, 2, 0, 2],
    oct=5, dur=PBal(5, 16), sus=0.35,
    amp=0.45, vadiod=700, vadiodr=0.35,
    cheapverb=0.3, cvdecay=1.5, pan=0.2)

t1 >> glitcher([0, 2, 3], oct=5, dur=2, sus=0.5,
    henA=1.4, henB=0.3, len=8, rate=1,
    amp=0.18, spring=0.7, sprdecay=2.0, pan=PRand([0.3, 0.5, -0.4]))

d3 >> play(_ka.snare, amp=0.65,
    dubd=0.45, dublen=0.12, dubwidth=0.18, dubfeed=0.65, pan=0.1)

d4 >> play(_ka.perc, amp=0.38,
    spring=0.6, sprdecay=1.4, sprtens=0.5, pan=-0.3)

#@ full — hoover accent stabs, wobble texture, cross-genre hat merge

h1 >> hoover([0, rest(0), rest(0), rest(0), rest(0), rest(0), rest(0), rest(0),
              -1, rest(0), rest(0), rest(0), 0, rest(0), rest(0), rest(0)],
    oct=4, dur=1, sus=0.45,
    porta=1.5, portadur=0.18,
    amp=0.6, dafilter=700, dastart=200, darel=0.25, darq=0.4, pan=0.15)

w1 >> wob([0, rest(0), rest(0), rest(0), -1, rest(0), rest(0), rest(0)],
    oct=4, dur=1, sus=1.2,
    rate=2, depth=0.8, cutoff=320, res=2.4, shape=0,
    sub=0.5, drive=1.6, glide=0.08,
    amp=0.45, pan=0.35)

# afro body + house hats merged, phase-shifted 3 steps
_kh = pkit("house", seed=4)
d5 >> play((_ka | _kh)["hat","perc"], amp=0.42,
    pan=0.1, lofi=0.2, lofiwow=0.25)

#@ break — stripped, doom enters

d2.amp = 0
d3.amp = 0
d4.amp = 0
d5.amp = 0
m1.amp = 0
h1.amp = 0
w1.amp = 0
t1.amp = 0

z1 >> doom([0], oct=3, dur=8, sus=10,
    pw=sinvar([0.25, 0.65], 24),
    cutoff=linvar([150, 800], 32), rq=0.3,
    rate=0.4, wnoise=0.15,
    amp=0.35, cheapverb=0.55, cvdecay=6.0, pan=-0.35)

#@ build — a_gesa3 rhythmic bass engine + drums return

b2 >> a_gesa3([0, -2, 0, -4, 0, -1], oct=4, dur=2,
    distortion=5, cutoff=linvar([350, 1600], 48),
    complexity=0.6, probability=0.9, shuffle=0.25,
    amp=0.48, tanh=0.4)

d2.amp = 0.5
d3.amp = 0.7
d4.amp = 0.4
m1.amp = 0.45
t1.amp = 0.18

# fresh kit variation for second half
_k2 = pkit("afro", seed=9, density=0.85)
d1 >> play(_k2.kick, oct=3, amp=1.15,
    spring=0.4, sprdecay=1.3)
d2 >> play(_k2.hat, amp=0.55, pan=PRand([-0.2, 0, 0.2]),
    spring=0.5, sprdecay=0.6)

#@ peak — industrialdrone atmosphere, evolved arpy, sbrk pump

z2 >> industrialdrone([0, 0, -2], oct=3, dur=8, sus=10,
    cutoff=linvar([250, 1100], 64), res=0.3,
    drive=1.4, detune=0.02, feedback=0.35,
    noise=0.1, sub=0.6,
    amp=0.28, cheapverb=0.4, cvdecay=7.0)

m1.degree = [0, 2, 3, 5, 7, 9, 7, 5, 3, 2, 0, -1, 0, 2, 3, 5]
m1.dur = PFDur((3,8),(5,8))
m1.amp = 0.52

d1.sbrk = var([0, 0.4, 0, 0.25], [16, 4, 12, 4])

h1.amp = 0.6
w1.amp = 0.45
d5.amp = 0.42

# shimmer bloom on supersaw
c1.shimmer = var([0, 0.45], [32, 32])
c1.shimsize = 0.85
c1.shimmix = 0.55
c1.cutoff = sinvar([800, 2800], 32)

#@ outro — slow dissolve

b2.amp = linvar([0.48, 0], 32)
h1.amp = linvar([0.6, 0], 16)
w1.amp = linvar([0.45, 0], 16)
m1.amp = linvar([0.52, 0], 32)
t1.amp = linvar([0.18, 0], 24)
b1.amp = linvar([0.95, 0], 32)
z2.amp = linvar([0.28, 0], 48)

m1.cheapverb = 0.75
m1.cvdecay = 5.0

d1.amp = linvar([1.15, 0], 32)
d2.amp = linvar([0.55, 0], 32)
d3.amp = linvar([0.7, 0], 24)
d4.amp = linvar([0.4, 0], 24)

g1.amp = linvar([0.35, 0], 48)
c1.amp = linvar([0.28, 0], 48)
z1.amp = linvar([0.35, 0], 48)
