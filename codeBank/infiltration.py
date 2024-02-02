#infiltration
Scale.default="minor"
Clock.bpm = 123;
Root.default = 0;

d9 >> play("<.3>", amp=1, dur=4, sample=(0), rate=(-0.5,1))

l1 >> loop("cindrum8", dur=8, sample=0, sbrk=0.2, sbrkdur=P*[4,0.5,1,2])
l1 >> loop("cindrum8", dur=8, sample=2, sbrk=0.2, sbrkdur=P*[4,0.5,1,2])
l2 >> loop("cindrum16", dur=16, sample=6, sbrk=0.2, sbrkdur=P*[4,0.5,1,2])
l6 >> loop("rbot4", dur=8, delay=4, cut=PWhite(0.1,0.5), sample=2, leg=0)
l7 >> play("{UMTmt[UU]}", rate=1, delay=7.5, dur=8, hpf=200, amp=2, fx2=0, pan=PWhite(-1,1))

i1 >> plaitsX(preset=10, porta=PWhite(-2,2), oct=(5,6,7), dur=8, glide=PWhite(0.01,1), glidedur=PWhite(0,2), rel=0, chop=P*[0,8], chopwave=(PRand(2,5),PRand(2,5),PRand(2,5)), bright=1, pan=(PWhite(-1,1),PWhite(-1,1),PWhite(-1,1)), spin=0.5, chopmix=PWhite(0, 1), dist2=1, vol=0.4, sus=PRand(1,9), hpf=PRand(500,4000)*1, high=2, mverb=PWhite(0,0.9)*1, lpf=PRand(400, 20000)*1, room2=PWhite(0, 1), damp2=PWhite(0.1, 0.9), revsus=PWhite(0.2, 8), revatk=PWhite(-1, 4))

s4 >> bass(var([0,linvar([0,PRand(-7,14)], [4,0])],[P*[4,12,28],4]), dur=1/4, cutoff=PFrac(0.6,0.3,16,1400, 8000), detune=0.5, krush=0.4, kutoff=PFrac(0.6,0.3,16,1400, 8000), oct=(6,4,5), rq=0.1, slide=0, compress=1, a=0, rate=0.1, mid=2, crush=PStep(16,PRand(2,8),0), bits=4, hpf=var([160,0], [1/4, 3/4]), amp=1)
s5 >> faim(s4.degree*-1, dur=1/4, oct=(4), detune=0.2, slide=0, compress=0, rate=0.9, mid=0, low=1, crush=PStep(8,PRand(2,8),0)*1, bits=4, ehpf=var([200,0],[1/4, 3/4]), ehpr=0.8, ehpfa=0.1, ehpc=PRand(-20,20), sus=PStep(16,1/8,1/4))

s4 >> superbass(lininf(21,-7, 4), dur=PDur([4,7,5],8), cutoff=PFrac(0.6,0.3,16,1200, 2000), detune=0.5, oct=6, rq=lininf(0.1, 0.8, 4), slide=0, a=0, crush=0, hpf=0, fdecay=6)

s6 >> pluck(var([0,linvar([0,PRand(-7,14)], [4,0])],[P*[4,12,28],4]), dur=1/4, cutoff=PFrac(0.3,0.6,16,800, var([1000,8000], [32,0])),slide=0, fdecay=linvar([4,5],[64,0]), decay=0.1, rel=0.5, oct=(4,5,[6,7]), rq=0.7, rqd=0.1, tanh=1, amp=1, vol=0.2, vib=40, hpf=1500)

d6 >> play("<x.><..C.><-><X.>", sample=(7), pan=(0,0,PWhite(-1,1),0), amp=(4,1,2,2), compress=1, lofi=0, dur=1/2).sometimes("stutter", PRand(2,16).rnd(2))
d6 >> play("<x.><..C.><-:><X.>", sample=(7), pan=(0,0,PWhite(-1,1),0), amp=(4,1,2,2), compress=1, lofi=0, dur=1/2).sometimes("stutter", PRand(2,16).rnd(2))
d6 >> play("<x.><..C.><[--]><X.>", sample=(7), pan=(0,0,PWhite(-1,1),0), amp=(4,1,2,2), compress=1, lofi=0, dur=1/2).sometimes("stutter", PRand(2,16).rnd(2))
d6 >> play("<x.><..C.><[--]:><X.>", sample=(7), pan=(0,0,PWhite(-1,1),0), amp=(4,1,2,2), compress=1, lofi=0, dur=1/2).sometimes("stutter", PRand(2,16).rnd(2))
d6 >> play("<.[xx]><....><[--]><X.>", sample=(7), pan=(0,0,PWhite(-1,1),0), amp=(4,1,2,2), compress=1, lofi=0, dur=1/2).sometimes("stutter", PRand(2,16).rnd(2))

d6.lofi=linmod(0,1,16)

v1 >> noloop("vocalinfi4", dur=8, sample=[1,0], trig=0, delay=0)

t1 >> plaitsX(P[-14:14], preset=9, oct=(4,5,6), dur=1/4, a=0, pan=PWhite(-1, 1), chopmix=0.3, chopwave=(2, 3), chop=1, mverb=0.2)
