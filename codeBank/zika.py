# zika
b2 >> dbass(p1.degree+PWhite(0,0.3), lpf=linvar([900,4500],24), dur=[1/2,1/4,1/2,1/4,1/2]).sometimes("dur.shuffle")
p1 >> prof(PSine(64)*0.2, oct=(var([(3,4),[5,6]],[6,2])), dur=PDur([5,7],8), sus=p1.dur*0.7, cutoff=7000, lforate=var([1,2,4],8), lfowidth=linvar([0.1,1],39), pan=[-1,1], amp=0.8)
n1 >> play("..I.", drive=(0,0.9), sample=1, rate=(PWhite(-1,4)), amp=PBern(16), pan=linvar([-1,1],24))
d4 >> play("x(---([::]:[::::]))", amp=1, sample=([0,1,2],[1,2,4])).sometimes("stutter")
d6 >> play("X ", amp=1)