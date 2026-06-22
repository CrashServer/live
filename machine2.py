# machine2 — peak violence, continues from machine.py state
# RATM: maximum density, everything saturated, feedback chaos
Clock.bpm = 112

# double kick — stomp layer under the existing groove
d2 >> play("X.X.X...X.X.X...", dur=0.25, amp=0.75, sample=4, hpf=60)

# industrial snare doubles the backbeat — harder crack
ns >> industrialsnare([rest(0),rest(0),rest(0),rest(0),0,rest(0),rest(0),rest(0),rest(0),rest(0),rest(0),rest(0),0,rest(0),rest(0),rest(0)], dur=0.25, oct=4, amp=0.9, dynfuzz=0.35, hpf=300)

# doom sub — infrasonic floor under the jbass
dm >> subbass([0,-7,0,-5,0,-7,-12,-7], oct=2, dur=0.5, sus=0.45, amp=0.95, dist2=0.5, lpf=sinvar([80,400],8))

# crunch — mid grit, euclidean offset
cr >> crunch([0,-5,0,-7,-5,-7,0,-5], oct=5, dur=0.25, sus=0.15, amp=sinvar([0.35,0.8],8), multicrush=0.6, hpf=600, lpf=sinvar([1500,6000],8))

# hoover — screaming high lead, filter modulated
hv >> hoover([7,5,0,7,5,7,rest(0),0], oct=6, dur=0.5, sus=PRand([0.2,0.4,0.6],4), amp=sinvar([0.3,0.85],8), lpf=sinvar([800,8000],4), dynfuzz=0.6, dfgain=1.5, pitchShift=var([0,1,0,-1],8), fbdelay=0.5, fbtime=0.5, fbfeed=0.6, fbcutoff=5000, beat_dur=1)

# hnoise — noise bursts between every hit, chaotic
hn >> hnoise(0, oct=5, dur=PFDur((7,8),(5,16)), amp=sinvar([0,0.55],4), lpf=sinvar([2000,14000],4), hpf=1200, dynfuzz=0.75, dfgain=2)

# war pushed to maximum — beef=16, feedback near clipping
wr >> war([0,0,-5,-5,-7,-7,0,0], oct=5, dur=0.5, sus=0.4, amp=1, beef=16, cutoff=sinvar([300,14000],8), rq=0.45, fbdelay=0.5, fbtime=0.25, fbfeed=0.85, fbcutoff=6000, fbspread=0.05, beat_dur=1)
~wr >> war([0,0,-5,-5,-7,-7,0,0], oct=5, dur=0.5, sus=0.4, amp=1, beef=16, cutoff=sinvar([300,14000],8), rq=0.45, fbdelay=0.5, fbtime=0.25, fbfeed=0.85, fbcutoff=6000, fbspread=0.05, beat_dur=1)

# angst — full scream, oct=7, no mercy
ag >> angst([7,5,0,7,5,0,7,rest(0)], oct=7, dur=0.25, sus=0.1, amp=0.85, cutoff=sinvar([4000,20000],2), rq=0.2, rate=sinvar([0.6,1.0],4))

# brass — all the way up, growl maxed
br >> brass2([0,-5,-7,-5,0,rest(0),0,rest(0)], oct=5, dur=0.5, sus=PRand([0.15,0.2,0.1],4), amp=1.1, bright=1.0, growl=sinvar([0.6,1.0],4), tight=0.8, room=0.25, mix=0.2)

# scratch — continuous whammy dive, never stops
sc >> scratch([7,12,7,5,0,7,12,5], oct=5, dur=0.25, sus=0.2, amp=sinvar([0.4,0.8],4), rate=sinvar([0.2,0.6],2), depth=sinvar([0.5,1.0],4), pitchShift=linvar([0,3],32), dynfuzz=0.7)

# ba now has resonbank metallic overtones
ba.resonbank = sinvar([0,0.5],8)
ba.rbfreq = [47,62,73,100]
ba.rbdecay = [0.4,0.3,0.4,0.3]

# ht goes full chaos
ht >> play("i", dur=0.25, amp=PLife(0.8), hpf=8000, pan=PRand([-0.4,0,0.4],4), amplify=PFDur((7,16),(5,8)))

# sudden drop — silence everything except kick and doom
# sn.amp=0; wr.amp=0; ~wr.amp=0; ag.amp=0; hv.amp=0; cr.amp=0; hn.amp=0; sc.amp=0; br.amp=0

# rebuild — one by one
# wr.amp=1; ~wr.amp=1; ba.amp=1; ag.amp=0.85; br.amp=1.1; hv.amp=linvar([0,0.85],8); sc.amp=sinvar([0.4,0.8],4); hn.amp=sinvar([0,0.55],4); sn.amp=0.85; cr.amp=sinvar([0.35,0.8],8)
