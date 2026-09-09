# unprobable 125
Clock.bpm = 125;
x_all.hpf=40
f5 >> sinepad(PArp([0,2,5],4), oct=7,dur=1/4, vol=0.3, fx2=1, fx1=1, root=var(P[1:12]), sus=1, pan=-1).unison(4)
f4 >> pluck(PArp([0,2,5],4), dur=1/4, lpf=3200, vol=0.3, fx2=1, fx1=1, root=var(P[1:12]), sus=1, pan=1).unison(4)
f5 >> pluck(PArp([0,2,5],4), dur=1/4, lpf=3200, vol=0.3, fx2=1, fx1=1, root=var(P[1:12]), sus=1, pan=1).unison(4)
f0 >> sinepad(PArp([0,2,5],4), oct=PStep([4,5,6],5, 4) ,dur=P[1/2, 1/2, 1/4, 1/4], vol=0.3, fx2=1, fx1=1, root=var(P[1:12]), sus=1).unison(4)
f5.oct=lininf(6, 4, 32)

b8 >> fbass(oct=(4,PStep(16,6,5)), lpf=linvar([800,8800],[32,0]), hpf=40, dur=PDur(5,8), fdist=linvar([2, 6], 128), vol=1)

b1 >> rsin(5 +var([IV, VI, III, VI]), octafuz=0, fx1=0, dur=1/4, sus=1/4)
