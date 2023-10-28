# D2_92
Clock.bpm=92
Scale.default="minor"

d1 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=1, drive=P*[0,expvar([0.01,0.9],26)], lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1))
d2 >> dbass(var([0,[-4,2,-2]],[14,2]), dur=P*[2,6],amp=(d1.degree!="v")*0.8, lpf=linvar([1800,3500],19), lpr=expvar([1,0.2],17), sus=b1.dur*PWhite(0.8,2),fx1=1, fx2=0.0, rate=linvar([0.1,15],23), oct=(PStep(7,6,5),4,PStep(4,6,5))).unison(3)
d3 >> play("<X ><(-[--]-[::])><..|*2|.><..C.>", bits=16, amp=1, dur=2, crush=3, room1=1, mix=PWhite(0,0.5)).rarely("amen").sometimes("stutter", PRand(1,6), rate=PRand([1,6]))
d4 >> sitar(P[0,5,P*[7,8,4],3], oct=P*[5,[6,4,3]], vib=PWhite(6,32), slide=0.01, slidedelay=PWhite(0.2,0.9), sus=s1.dur*PWhite(0.3,0.8), dur=1/4, room=1, mix=PWhite(0,0.2), amp=var([(d1.degree=="@"), (d1.degree!="@")],[28,4]), drive=(0,0.1), fx2=1).spread() + [0,0,P*[2,4],0]
