# trone
a1.revatk=0
a1 >> angst((var([0,-2,-4,2],8),2,PRand(8)), dur=PDur(5,8)*8, oct=(3,4,[5,[6,2,6]]), room2=0.7, mix2=0.5, damp2=PWhite(0.1,0.8), revatk=PWhite(-3,3), revsus=a1.revatk + PRand(3), drive=0, rate=PWhite(0,16), high=2, mid=0.5, hpf=PStep(8,1400,40), lpf=PRand(500,12000)).slider()
b1 >> pbass(dur=PDur(var([4,P*[5,7,3]],[6,2]),8), rate=expvar([0,16],[64,0]), amp=0.8, oct=(4,PStep(32,6,5))).follow(a1, 8) + var([0,PGauss()],[7,1])

d1 >> play("<(xxx(x.))(...(.x))..><.(---.)><..o.><..(...*).><...{---[--]:=[.x][-o]}><|(XXX(X[.X]))0|.>",sample=((7,6),7,(7,2),7), dur=1/2, amp=0.5, room2=P(0,0.3,0.2,0.3,0.5,0), mix2=0.2, revatk=0.2, revsus=PWhite(0.2,1.7), lpf=0).sometimes("stutter", PRand(4).rnd(2)).rarely("trim",3, cycle=8)
d1.lpf=180

s1 >> abass(PArp([0,2,PGauss(4,2).rnd(2)],12), dur=PStrum(var(P*[8,4,2],8)), vib=0.5, rate=linvar([0.5,2.4],[64,0]), fmod=PRand(1,4), oct=5, amp=0.4, sus=s1.dur*PWhite(0.5,1.1), lpf=8080, room2=0.5, mix2=0.4).unison(3,0.1)
