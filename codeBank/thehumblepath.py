# turbulence 120
# todo

Clock.bpm = 120
Root.default=var([0,[1,8]],[14,2])

d1.feed=0
d1 >> play("x.",  amp=0.1, feed=var(PRand([0,0.125,0.25,0.5,0.75]),16), feedfreq=[[0,PRand(500)],0], sample=4, tanh=[15], chop=var(PRand(8), 16), lpf=0, hpf=d1.feed.map({0:0, 0.125:75, 0.25: 100, 0.5:125, 0.75:255})).strum(8)

s1 >> abass(PWhite(-0.2,0.2), amp=0.2, fmod=[0,PRand(8)], oct=[4,[5,6]], dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], dfm=d1.feed.map({0:linvar([2800,4640],16), 0.125:linvar([1664,2400],16), 0.25:linvar([1180,1664],[16,0]), 0.5:linvar([808,1180],[16,0]), 0.75:linvar([606,808],[16,0])}, default=2600), dfmr=PWhite(0.2,1), dfmd=1, sus=PWhite(1/8,1),slide=PStep([12,4,3],PRand(8),0), slidedelay=PWhite(0.2,0.9)).unison(3).every(32, "dur.shuffle")

d2 >> play("<x ><..O.>", amp=var([0, 1], 32), sample=4)
o1 >> play("--C--{-[-c][---]}C", amp=1+d2.amp/2, sample=7, lpf=linvar([40,20000,20000],[32,32,0]), lpr=linvar([1,0.1,0.5],[32,32,0]), pan=[PWhite(-1,1),0,PWhite(-1,1)], room=PWhite(0,1), mix=PWhite(0,0.7))
o2 >> play("O", amp=1, rate=var([PWhite(0.5,3),1],32), pan=PWhite(0,0.4), sample=4, room=1, mix=.3).fill()

t1 >> tb303(s1.degree, amp=0.8, oct=PStep(16,[5,[4,6]],3), dur=PDur(var([8,[7,PRand(5,10)]],[6,2]),8), cutoff=5400*d1.feed + 500, top=linvar([400,5500],24), res=PWhite(0.1,0.3), sus=1/8).unison(2)
s2 >> star(amp=0.2,bend=PStep([2,4,8],PWhite(0,3),0), benddelay=PWhite(0.4,0.9), oct=(6,7), dur=d2.amp.map({0:8}, default=1), chop=16+16*d1.feed,  drive=0.2+(s2.bend*0.1), lpf=expvar([6800,1480],[48,16]), lpr=PWhite(0.2,0.8)).unison(3,0.25,99)
