# grind — 140 bpm, C phrygian, friction machine
Clock.bpm = 140
Scale.default = "phrygian"
Root.default = "C"

#@#@ grind

#@ intro

# kick — 4-on-floor, amp variation
dk >> play("X.", dur=0.5, amp=var([1,0.9,1,0.85],4))

# snare — 2 and 4
sn >> play("..o.", dur=0.5, amp=0.8,
           dynfuzz=0.2, dfgain=1.3, dftone=2)

# doom bass — heavy root
db >> doom([-7,-7,-5,-7,-12,-7,-5,-3], oct=3, dur=0.5,
           sus=var([0.4,0.3,0.5,0.35],[4,4,4,4]),
           amp=0.85, dist2=0.35,
           lpf=sinvar([200,900],16))

# tb303 acid line — filter sweep
tb >> tb303([0,-2,3,-2,0,5,-2,3], oct=4, dur=0.25,
            sus=PRand([0.1,0.2,0.3,0.5],8), amp=0.45,
            lpf=sinvar([400,3500],24), lpr=0.7,
            dist2=linvar([0,0.4],32))

#@ build

# hihat — PLife chaos pattern
ht >> play("i", dur=0.25, amp=PLife(0.45),
           hpf=8500, pan=PRand([-0.3,0,0.3],4))

# hoover — tension swell
hv >> hoover([-5,-3,0,-5], oct=4,
             dur=var([2,1,3,2],[4,4,8,4]),
             sus=var([1.5,1,2,1.5],[4,4,8,4]), amp=0.5,
             lpf=linvar([400,3000],32),
             dynfuzz=sinvar([0,0.65],16),
             room=0.35, mix=0.3)

# jbass low rumble layer
jb >> jbass([-7,-12,-7,-5], oct=3,
            dur=var([1,2,0.5,1],[4,8,4,4]),
            sus=sinvar([0.3,0.7],16), amp=0.6,
            dynfuzz=0.25,
            resonbank=sinvar([0,0.3],32))

#@ drop

# clap — euclidean syncopation
cl >> play("..o.", dur=0.5, sample=2, amp=0.75,
           amplify=PEuclid(5,8), hpf=3000)

# darklead stabs — sparse and brutal
dl >> darklead([0,3,5,rest(0),0,rest(0),3,rest(0)], oct=5, dur=0.5,
               sus=PRand([0.1,0.15,0.2],4), amp=0.4,
               tape=sinvar([0,0.55],32), tapedrive=0.35,
               room=0.5, mix=0.4)

# crunch glitch stabs — euclidean hit
cr >> crunch([5,3,0], oct=5, dur=PFDur((5,16),(3,8)),
             sus=0.12, amp=sinvar([0,0.55],16),
             multicrush=0.4, hpf=1000)

# hnoise industrial texture — breathes in and out
hn >> hnoise(0, oct=4, dur=var([4,8,2],[8,16,8]),
             amp=sinvar([0,0.2],32),
             lpf=sinvar([500,4000],16),
             room=0.3, mix=0.25)

# doom bass filter opens
db.lpf = linvar([200, 2000], 32)
db.amp = sinvar([0.8, 1.0], 16)

#@ peak

# kick doubled with synth thud
dk.amp = var([1,0.95,1,0.9,1,0.85,1,1],8)
db.dist2 = sinvar([0.3,0.7],16)
hv.amp = sinvar([0.4, 0.7], 16)
tb.lpf = sinvar([300, 6000], 16)

#@ end(32)
