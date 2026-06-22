# break — 128 bpm, A minor, breakbeat
# Amen-style syncopated groove, chunky stabs, swing bass
Clock.bpm = 128
Scale.default = "minor"
Root.default = "A"

#@#@ break

#@ intro

# kick — Amen-hybrid: X.x...X.X.x.X...
dk >> play("X.x...X.X.x.X...", dur=0.25, amp=var([1,0.65,1,0.65],4))

# snare — 2 and 4 with ghost hit before 4
sn >> play("....o.....oo....", dur=0.25, amp=var([0.85,0.5,0.9,0.55],4), sample=1, cheapverb=0.15, cvdecay=0.5)

# hats — swing shuffle with open hats
ht >> play("iIitIiItiIitIiIt", dur=0.25, amp=0.4, hpf=6000, pan=sinvar([-0.2,0.2],8))

# bass — jbass with swing delay, chunky 8th note line
ba >> jbass([0,0,-7,0,0,-5,0,-3], oct=4, dur=0.5, sus=var([0.3,0.4,0.25,0.35],[4,4,4,4]), amp=0.8, dynfuzz=0.25, lpf=sinvar([400,2000],16), delay=PSwing(0.04))

#@ groove

# dsaw stabs — offbeat chord hits
ds >> dsaw([0,-5,-7,-5], oct=5, dur=PBal("rumba"), sus=0.2, amp=0.55, dist2=0.2, lpf=sinvar([1000,4000],16), room=0.35, mix=0.3, pan=sinvar([-0.3,0.3],8))

# darklead riff — answering the bass
dl >> darklead([7,5,0,7,5,0,rest(0),5], oct=5, dur=0.5, sus=PRand([0.2,0.35,0.5],4), amp=0.45, lpf=sinvar([1000,5000],16), cheapverb=0.3, cvdecay=1, delay=PSwing(0.04))

#@ drop

# second snare layer — syncopated ghost hits
t2 >> play(".o..o.....o..o..", dur=0.25, amp=0.45, sample=3, hpf=2000)

# dub bass — octave below for sub weight
db >> dub([0,-7,0,-5], oct=3, dur=1, sus=0.85, amp=0.7, lpf=sinvar([80,300],16), room=0.4, mix=0.3)

# scatter texture — analog noise between hits
sc >> scatter(0, oct=5, dur=PFDur((5,8),(3,16)), amp=sinvar([0,0.3],8), lpf=sinvar([2000,8000],8), hpf=800, rate=sinvar([0.01,0.1],4))

# chord stabs — svdk on the and of 2
sv >> svdk([(0,4,7),(rest(0),rest(0),rest(0)),(-5,-2,2),(rest(0),rest(0),rest(0))], oct=4, dur=1, sus=0.3, amp=0.4, chorus=0.3, room=0.4, mix=0.3)

#@ peak

ba.dynfuzz = sinvar([0.25, 0.6], 8)
ds.amp = sinvar([0.45, 0.75], 8)
ds.lpf = sinvar([800, 6000], 8)
dl.oct = var([5,6],[16,8])
ht.amp = sinvar([0.35, 0.65], 8)

#@ end(32)
