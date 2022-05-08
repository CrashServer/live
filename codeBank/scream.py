# scream
s1 >> jbass(1, oct=4, dur=var([1/2,1/4],[6,2]), amp=2, sus=s1.dur*0.7, hpf=40).sometimes("stutter") + var([0,[2,-1,6],[1,2,-1,3]],[6,1,1])

d2 >> play("..I.", drive=(0,0.1), dur=P*[0.5,1,2], sample=1, room2=linvar([0,1],24), mix2=linvar([0,0.9],37), rate=(PWhite(-0.5,1)), amp=1, pan=linvar([-1,1],24))

Master().lpf=linvar([250,12000],[64,inf], start=now)

p1 >> prof(PSine(64)*0.2, oct=(var([(3,4),5],[6,2])), dur=1/4, sus=p1.dur*0.9, cutoff=[linvar([290,12800],[36]),linvar([5800,490],[36])], lpf=0, lforate=.1, lfowidth=0.5, pan=[linvar([-1,0,1],[36,36]),linvar([1,0,-1],[36,36])])

r1 >> pasha(var([0,2,1],[12,2,2]), oct=PwRand([5,4,6],[34,2,2]), dur=PDur([4,5],8), chop=PRand([7,9,5]), drive=0.4, drivemix=0.4,room=1, mix=0.4, sus=1, lpf=3500, lpr=0.2, amp=PBern(64,0.9)*0.8).sometimes("shuffle") + PwRand([0,2],[36,2])
