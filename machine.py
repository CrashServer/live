# machine — 106 bpm, D minor, rage architecture
# Rage Against The Machine: locked groove, controlled fury, brass hits
Clock.bpm = 106
Scale.default = "minor"
Root.default = "D"

#@#@ machine

#@ intro

# kick — RATM tight groove (hits on 1, 2-and, 3, 3-and)
dk >> play("X...X.X.X...X...", dur=0.25, amp=var([1,0.9,1,0.88],4))

# snare on 2 and 4 — dry crack
sn >> play("....o.......o...", dur=0.25, amp=0.85, sample=2,
           hpf=200, dynfuzz=0.15, dfgain=1.4, dftone=3)

# bass — Commerford style: aggressive, almost lead
ba >> jbass([0,0,-5,0,-7,0,-5,-3], oct=4, dur=0.25,
            sus=var([0.3,0.2,0.35,0.25],[4,4,4,4]),
            amp=0.85, dynfuzz=0.3, dfgain=1.2,
            lpf=sinvar([400,2000],16))

# war riff — thick distorted power chord vibe
wr >> war([0,0,-5,-5,-7,-7,0,0], oct=4, dur=0.5,
          sus=0.4, amp=0.7, beef=10,
          cutoff=sinvar([600,3000],16), rq=0.6)

#@ groove

# hihat — 16th note pulse with life
ht >> play("i", dur=0.25, amp=PLife(0.5), hpf=8000,
           pan=PRand([-0.25,0,0.25],4))

# angst — Morello whammy effect (atonal, screeching)
ag >> angst([7,5,0,7,rest(0),5,7,rest(0)], oct=5, dur=0.5,
            sus=PRand([0.1,0.2,0.3],4), amp=sinvar([0,0.6],8),
            cutoff=sinvar([800,12000],4), rq=0.4,
            rate=sinvar([0.3,0.9],8),
            pitchShift=var([0,1,-1,0],4))

# brass2 stabs — horn punches
br >> brass2([0,-5,-7,-5,0,rest(0),0,rest(0)], oct=5, dur=0.5,
             sus=PRand([0.15,0.2,0.1],4), amp=0.6,
             bright=0.85, growl=0.4, tight=0.7,
             room=0.3, mix=0.25)

#@ rage

# clap — euclidean syncopation
cl >> play("..o.", dur=0.5, sample=3, amp=0.7,
           amplify=PEuclid(5,8), hpf=3500)

# war riff opens up, filter screams
wr.cutoff = sinvar([800, 8000], 8)
wr.beef = 14
wr.amp = sinvar([0.6, 0.9], 8)

# scratch burst — Tom Morello whammy moment
sc >> scratch([7,12,7,rest(0),5,rest(0)], oct=5,
              dur=PRand([0.5,0.25,1],4),
              sus=PRand([0.1,0.2,0.3],4), amp=sinvar([0,0.7],4),
              rate=sinvar([0.1,0.5],2), depth=sinvar([0.3,0.8],4),
              pitchShift=var([0,1,2,-1],4),
              dynfuzz=0.5)

# bass gets heavier
ba.dynfuzz = sinvar([0.3, 0.7], 8)
ba.amp = sinvar([0.8, 1.0], 8)

#@ breakdown

sc.stop()
wr.amp = linvar([0.7, 0], 8)

# war drops to single riff motif
wr >> war([0,rest(0),rest(0),rest(0),-5,rest(0),-7,rest(0)], oct=4,
          dur=0.5, sus=0.4, amp=0.65, beef=10,
          cutoff=sinvar([600,2000],8))

# brass hits harder on breakdown
br.amp = sinvar([0.5, 0.9], 8)
br.growl = sinvar([0.4, 0.8], 4)

#@ peak(64)

wr >> war([0,0,-5,-5,-7,-7,0,0], oct=4, dur=0.5, sus=0.4, amp=0.9, beef=14,
          cutoff=sinvar([400,10000],8), rq=0.5)
ag >> angst([7,5,0,7,5,0,7,rest(0)], oct=5, dur=0.25,
            sus=0.15, amp=0.7, cutoff=sinvar([2000,16000],4), rq=0.3)
sc >> scratch([0,7,12,7], oct=5, dur=0.5, sus=0.2, amp=0.6,
              rate=0.4, depth=0.7, pitchShift=linvar([0,2],16))
ba.amp = 1.0
dk.amp = var([1,0.95,1,0.92,1,0.9,1,1],8)

#@ end(32)
