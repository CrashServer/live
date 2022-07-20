#scan
scene1
Clock.bpm = 70;

c0 >> play("v", dur=1/2, lpf=PGauss(2000, 200), hpf=100, hpr=var([0.5, 0.2], 4),mverb=0.5, mverbdamp=0.1, mverbdiff=0.8, bpf=(1000, 1500), bpr=0.8, dist2=0.5, dist2mix=linvar([0.2, 1], [4, 2, 8]), dist2shape=1)
c1 >> latoo(dur=1, amp=1, cut=1/4, mverb=PWhite(0, 0.5), mverbdamp=0.8, mverbfreeze=0, mverbdiff=0.8, hpf=50, bpf=(1000, 500), bpr=0.8, mpf=1200, lpf=(200, 600),dist2=1, dist2mix=1, dist2shape=1).unison(2)
c2 >> pink(dur=1/2, cut=1/4, hpf=1200, hpr=PWhite(0.1,1), leg=8, a=PWhite(0, 0.2), pan=PWhite(-1, 1), amp=PWhite(0, 0.5))
~c3 >> play("<q><k>", sample=(3,P[0:5]), delay=(0,(0,[0,0.25])), dur=c0.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=0, hpf=0)
c4 >> bass(amp=[1, 0, 1, 0, 1, 1, 0, 0], sus=[2, 0, 0, 0, 1/2, 1/2, 0, 0], dur=1/4, leg=4, dist2=0.4).unison(4)
c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)
~c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=1000, scale=Scale.minor, dist2=1).unison(6) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, PStep(4, 4, 3), 3], [16, 8, 8])
