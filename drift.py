# drift — 72 bpm, Bb minor, still water
Clock.bpm = 72
Scale.default = "minor"
Root.default = "Bb"

#@#@ drift

#@ intro

# pad foundation — long attack, sinvar breathing
p1 >> pad2([-7,-5,0,2], oct=5, dur=8,
           sus=sinvar([5,9],64), amp=sinvar([0.2,0.4],32),
           room=0.95, mix=0.85,
           lpf=sinvar([500,1800],48))

# FM chord swell
p2 >> omi([(0,4),(2,5),(-2,2),(0,3)], oct=5,
          dur=var([6,8,4,12],[8,16,8,16]),
          sus=sinvar([5,10],32), amp=0.18,
          room=0.99, mix=0.9,
          lpf=linvar([400,1600],64))

# sub breath — slow root movement
ba >> subbass([-7,-5,0,-7], oct=3,
              dur=var([8,12,4,8],[16,16,8,16]),
              sus=sinvar([6,10],32), amp=sinvar([0.2,0.45],48),
              lpf=sinvar([80,350],32), room=0.7, mix=0.6)

#@ bloom

# bell texture — sparse, panned
b1 >> bell2([0,4,7,5,2], oct=6,
            dur=PRand([1,2,3,0.5],5),
            sus=PRand([0.5,1,2],5),
            amp=sinvar([0.12,0.3],16),
            cheapverb=0.7, cvdecay=sinvar([2,4],16),
            pan=PRand([-0.5,0,0.5],5))

# gong punctuation — very sparse
g1 >> gong([0,rest(0),rest(0),7,rest(0),rest(0),rest(0),2], oct=4,
           dur=4, sus=sinvar([5,10],24),
           amp=sinvar([0.1,0.35],32),
           shimmer=0.4, room=0.99, mix=0.95)

# plaitsX morphing granular cloud
px >> plaitsX([0,2,4,7,9], oct=5,
              preset=var([4,5,8,11],[16,16,16,16]),
              dur=var([4,6,8],[16,24,16]),
              sus=sinvar([3,7],24), amp=sinvar([0.08,0.22],32),
              room=0.9, mix=0.8,
              lpf=linvar([500,2000],64))

#@ swell

# choir swells — disappears and reappears
ch >> choir([-7,-5,0,4], oct=4,
            dur=var([8,12,16],[32,16,32]),
            sus=sinvar([6,12],24), amp=sinvar([0,0.28],48),
            room=0.99, mix=0.95,
            lpf=linvar([300,1000],128))

# sinepad top layer — shimmering dots
sp >> sinepad([12,9,7,4,7,9,12], oct=5,
              dur=PRand([0.5,1,2],7),
              sus=PRand([0.3,0.5,1],7),
              amp=sinvar([0.06,0.15],12),
              cheapverb=0.65, cvdecay=3.5,
              pan=sinvar([-0.6,0.6],7))

# space texture — mid-range pad shimmer
sx >> space([2,0,-2,4], oct=5,
            dur=var([6,8,4],[12,16,8]),
            sus=sinvar([4,8],24), amp=sinvar([0.1,0.25],32),
            room=0.9, mix=0.85,
            lpf=sinvar([600,2500],48))

# bass deepens
ba.oct = 3
ba.amp = sinvar([0.3, 0.55], 48)
ba.lpf = sinvar([120, 500], 32)

#@ end(64)
