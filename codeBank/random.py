# IDEAS, random 

b1 >> dbass([0,0,0,3,0,0,2,0], dur=0.25, sus=0.08, amp=[1,0.7,0.9,1,0.8,0.6,1,0.7], lpf=var([400,800,400,1200],[4,2,4,8]), res=0.8, drive=linvar([0.2,0.8],16), vol=4, vadiod=1500, vadiodr=0.5, vadiodd=0.5, vadiodc=0.3)
d2 >> play("<X ><(-[--]-[::])><..|*2|.><..C.>", bits=var([16,8,4],[8,4,4]), amp=var([1,2],[8,8]), dur=var([2,1,1/2],[16,8,8]), crush=var([3,8],[8,8]), room1=1, mix=PWhite(0,0.5), sample=var([2,4,8],[16,8,8])).rarely("amen").sometimes("stutter", PRand(1,6), rate=PRand([1,6]))
d1 >> play(PEuclid2(var([3,4,5],[24,8,8]),8,"(vv{v@})","(-|=2|)"), dur=var([1,1/2,1/4],[16,8,8]), drive=P*[0,expvar([0.01,0.9],26)], lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61), amp=var([0.8,1.2],[4,4]), sample=var([2,4,8],[16,8,8])).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1))
gesa = SynthDef("gesa")
d1 >> play("X---X-o-K---", dur=0.25, sample=6)
b1 >> gesa([0,0,0,3,0,0,2,0], dur=0.25, sus=0.2, bits=12, crush=4, distortion=8, cutoff=4000, resonance=0.5, attack=0.01,amp=[1,0.7,0.9,1,0.8,0.6,1,0.7], lpf=var([400,800,400,1200],[4,2,4,8]), res=0.9,drive=linvar([0.2,0.8],16), vol=4)
b9 >> gesa(var([0,-2], 8), dur=1/2, oct=(4,5), rate=.2, valad=800, valadr=0.3, valadd=15, valadt=0, valadc=0.2, crush=var([0,8],[4,4]), fold=var([0,0.5],[8,8])).unison(3)

x5 >> play("X ")
e2 >> ebass([1,0,0,0,0] + var([0,PTrir(-2,2,0)],[8,8]), dur=[1/2,1/2,1,1], oct=(4), pick=[0.8, 0.2, 0.2], cutoff=linvar([850, 1250],32), decay=0.6, rel=e2.dur*0.5, amp=1, fold=(0, 0.14), vol=1, tanh=0.2, scale=Scale.chromatic).penta()
e1 >> ebass([1,0,0,0,0], dur=PDur(var([5,7],[8,8]),16), oct=(4), pick=[0.8, 0.2, 0.2], cutoff=linvar([850, 1250],32), decay=0.6, rel=e1.dur*0.5, amp=var([1,0.7],[4,4]), fold=(0, 0.14), vol=1, tanh=0.2, delay=var([0,0.25],[8,8])).penta()
d1 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=1, drive=P*[0,expvar([0.01,0.9],26)], lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61), amp=var([0.8,1.2],[4,4])).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1))

b7 >> dbass([0,1,0,-1,0], dur=0.5, oct=5, slide=var([0,0.1],[4,4]), lpf=var([800,3200],[8,8])).unison(4)
b9 >> faim(P[-5,-5,7,-5, -5,5,-5,-5, 3,-5,-5,1, -5,-5,2,3], dur=P[1/2].stutter(16) | 1, lpf=[PRand(400,2280),0,0], lpr=PWhite(0.1,0.5), dist2=1, shape=0.0, vol=0.5).unison(4)

d2 >> play("<X ><(-[--]-[::])><..|*2|.><..C.>", bits=16, amp=1, dur=2, crush=3, room1=1, mix=PWhite(0,0.5), sample=var([2,4],[8,8])).rarely("amen").sometimes("stutter", PRand(1,6), rate=PRand([1,6]))

d3 >> play("<kk.Kkkkkk.kk><u.(...C).><~.><X...>", dur=1/2, valad=0, sample=P[0], valadr=0.3, valadd=139, valadt=0, valadc=0.1, amp=var([0.8,1.2],[8,8])).sometimes("stutter")
d1 >> play("XoXX-o-oX-o-XoX-", dur=0.25, sample=9, hpr=0.1, hpf=1200)

t2 >> ebass([0,0,0,3,0,0,0,7], dur=[0.25,0.25,0.25,0.5,0.25,0.25,0.25,1], sus=0.5, pick=[0.9,0.8,0.9,0.7,0.9,0.8,0.9,0.6], cutoff=1500, amp=[1,0.7,0.9,0.8,1,0.7,0.9,0.9], oct=7, drive=0.0)


x5 >> play("b ")
Clock.bpm = 130;
t5 >> dbass([0,0,3,3,5,5,0,0], dur=[0.25,0.25,0.25,0.25,0.25,0.25,0.5,0.5], sus=0.5, pick=0.95, cutoff=1200, amp=[1,0.8,1,0.8,1,0.8,1,0.9], oct=5, drive=0.8, fold=0.0, rate=0.5)
r9 >> vati([-5,-3,-5,0,-5,-3,0,3], dur=[0.5,0.25,0.25,0.5,0.5,0.25,0.25,1], sus=0.2, pick=[0.9,0.8,0.9,0.7,0.9,0.8,0.7,0.8], cutoff=12500, amp=1, oct=7, drive=0.0, fold=0.0)

t8 >> ebass([0,2,3,5,3,2,0,5], dur=[0.5,0.25,0.25,0.5,0.25,0.25,0.5,0.5], sus=0.5, pick=[0.7,0.8,0.7,0.6,0.7,0.8,0.7,0.6], cutoff=var([700,1100],[8,8]), amp=[0.9,0.7,0.8,1,0.8,0.7,0.9,0.9], oct=6, vol=4)
t6 >> ebass([0,3,0,3,0,5,0,3], dur=0.25, sus=0.5, pick=[0.9,0.7,0.9,0.7,0.9,0.8,0.9,0.7], cutoff=var([600,900],[4,4]), amp=[1,0.7,0.9,0.7,1,0.8,0.9,0.7], oct=6,shape=0.5)

s7 >> ebass([0,2,0,2], dur=var([0.25,0.5],[6,2]), sus=0.5, rate=P[1,-1,1,-1], pick=0.8, cutoff=var([200,500],[2,2]), amp=P[1,0.6,0.8,0.7], oct=6, crush=6).sometimes("stutter", PRand(8))
s8 >> ebass([0,0,0,0,0,0,5,0], dur=0.25, sus=0.2, pick=0.95, cutoff=350, amp=[1,0.6,0.7,0.5,0.8,0.6,1,0.7], oct=6, drive=0.5, leg=0.1)
t5 >> dbass([0,0,3,3,5,5,0,0], dur=[0.25,0.25,0.25,0.25,0.25,0.25,0.5,0.5], sus=0.5, pick=0.95, cutoff=1200, amp=[1,0.8,1,0.8,1,0.8,1,0.9], oct=5, drive=0.0, fold=0.4)

r9 >> vati([-5,-3,-5,0,-5,-3,0,3], dur=[0.5,0.25,0.25,0.5,0.5,0.25,0.25,1], sus=0.2, pick=[0.9,0.8,0.9,0.7,0.9,0.8,0.7,0.8], cutoff=12500, amp=1, oct=7, drive=0.0, fold=0.0)

t8 >> ebass([0,2,3,5,3,2,0,5], dur=[0.5,0.25,0.25,0.5,0.25,0.25,0.5,0.5], sus=0.5, pick=[0.7,0.8,0.7,0.6,0.7,0.8,0.7,0.6], cutoff=var([700,1100],[8,8]), amp=[0.9,0.7,0.8,1,0.8,0.7,0.9,0.9], oct=8, vol=4)

t6 >> ebass([0,3,0,3,0,5,0,3], dur=0.25, sus=0.5, pick=[0.9,0.7,0.9,0.7,0.9,0.8,0.9,0.7], cutoff=var([600,900],[4,4]), amp=[1,0.7,0.9,0.7,1,0.8,0.9,0.7], oct=6, shape=0.5)

s7 >> ebass([0,2,0,2], dur=var([0.25,0.5],[6,2]), sus=0.5, rate=P[1,-1,1,-1], pick=0.8, cutoff=var([200,500],[2,2]), amp=P[1,0.6,0.8,0.7], oct=6, crush=6).sometimes("stutter", PRand(8))
s8 >> ebass([0,0,0,0,0,0,5,0], dur=0.25, sus=0.2, pick=0.95, cutoff=350, amp=[1,0.6,0.7,0.5,0.8,0.6,1,0.7], oct=6, drive=0.5)
g4 >> dbass([0,3,5,0], dur=[1,1,1,1], sus=2, amp=2, oct=6, cutoff=2000, drive=0.0, fold=0)
