# attention 112
# Reisub

Root.default = linvar([0, 4, 2, PRand(2)], [PRand([4, 8, 12, 16])])
Clock.bpm = lininf(112, 132, 512)
r1 >> rsin((linvar([0,4],16),linvar([2,-2],24), linvar([-4,4],32)), dur=var(PRand([1,1/2,1/4,2]),8), hpf=linvar([30,180],23),oct=var([3, 4, 5], PRand(8)), para1=PWhite(200, 8000), fmod=8,lpf=linvar([3000,8000],19), amp=0.5, sus=r1.dur, fold=var([0.5, 0.1]), fx2=0.5, room2=1, revsus=r1.dur*PWhite(0,2), revatk=-1, damp2=PWhite(0.1,0.9))
r2 >> click(r1.degree, oct=[5,4,3,6], vib=P*[1, 2, 4, 8, 2, 16],echo=PStep([7,[3,6]],0,0.25), dur=[2,4,6,PRand([2, 4, 8])], mult=PRand(16), amp=0.7,shape=PWhite(0.2, 0.3), slide=0.3, pan=PWhite(-1,1), room2=1, damp2=0.1,  spf=8000, spfend=10, spfslide=4)
p1 >> play("<q ><p >", sample=1, dur=PDur([3, 5], 8), amp=PWhite(0.3,0.5), hpf=220, chop=1/2, leg=PWhite(150), pan=PWhite(-1,1))
p2 >> play("(qp) ", sample=2, dur=PDur([1, 6], 8), hpf=200, amp=PWhite(0.3, 0.5), leg=25, pan=PWhite(-0.5,0.5))
p3 >> play("//", sample=67, dur=16, hpf=140, spf=40, spfslide=5, spfend=8000, amp=0.3, rate=[PWhite(-0.5,-0.1), PWhite(2,8)], pan=(PWhite(-1,1),PWhite(-1,1))) # 
p4 >> play("p ", sample=2, dur=1/2, lpf=17000, lpr=0.1, amp=sinvar([0,0.3],37), leg=8, pan=PWhite(-0.25,0.75), hpf=200)
p5 >> play("p ", sample=1, dur=PDur([3, P*[5,7]], 8), lpf=8000, lpr=0.3, amp=sinvar([0,0.4],13), leg=8, pan=PWhite(0.5,-1), hpf=400)
p6 >> play("q ", sample=1, dur=PDur([3, P*[6,7]], 8), amp=0.4, spf=8800, spfend=340, spfslide=2, chop=1/2, leg=PWhite(150), hpf=240, pshift=0, pan=PWhite(-0.4,0.7))
p7 >> play("q ", sample=2, dur=PDur([[1, 6],8], 8), amp=0.5, leg=25, hpf=400, pan=PWhite(-1,1))
d1 >> play("<X(..{XxK.})X(..X)(X.)>", sample=2, lpf=linvar([500,1500],[32,7]), lpr=PWhite(0.3,1), amp=0.3).every(PRand(1,9), "stutter", PRand([6,8,12,16]), rate=PWhite(1,1.125), pan=[-1,1], bpf=1500, drive=0.2)
r3 >> dbass(linvar([0,0.6],[64,0]), root=0, mid=2, dur=PDur(8,14), amplify=0.8*(d1.degree!="X"), leg=PRand(4), a=0, sus=0.4, oct=4, lpf=13000, hpf=60).unison(3)
d1 >> play("<X(.....{X[XX]xv})><..O.><|x4|.>", amp=0.2, lpf=8000)
d2 >> play("<[-{---[--]|:4|}]><.:>", sample=7, amp=0.5, lpf=0 ,pan=PWhite(-0.5,0.5), rate=PWhite(0.99,1.01)).human(80,3,4).sometimes("stutter", PRand(4))
