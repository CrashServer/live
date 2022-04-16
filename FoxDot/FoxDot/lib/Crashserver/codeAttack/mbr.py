# mbr
Root.default ="C"
Scale.default="minor"
Clock.bpm = linvar([131, 134],[32,0]);

s1 >> dab((0,-2), dur=32,fx1=1, amp=0.9, fx2=1, lpf=PRand(800,8000), fmod=PRand(8).rnd(2), oct=PStep(3,6,5), cut=0).every(4, "rotate").unison(3,0.25,99)
b8 >> fbass(oct=(4,5,6), echo=0, lpf=PRand(800,10800), hpf=40, drive=linvar([0,0.7],[16,0]), dur=PDur(var([8,P*[5,7,6]],[6,2]),8), sus=1/6, vol=1)
v1 >> play("K", amp=[1,0,0,0], dur=1/4, output=8, sample=0, cut=0)
v3 >> play("@", amp=[[0,1,0,0],0,0,0], dur=1/4)
v4 >> play("N", amp=[0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0,  0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0,  0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0,  0,0,0,0, 0,0,0,0, 0,1,0,0, 1,0,0,0], dur=1/4, shape=1, sample=PRand(99)[:12], cut=1, lpf=200, amplify=1)
v5 >> play("[-]", amp=[0,[0,0,0,[0,1]],1,[0,0,0,[0,0,0,1]]], dur=1/4, sample=8, rate=PWhite(-0.5,3), hpf=180, vol=0.8, pan=PWhite(-1,1))
x3 >> play("s", amp=linvar([0.5, 1]), sample=0, dur=1/4, amplify=[0.76, 0.2, 0.4], lpf=PRand(8000,18000), pan=PWhite(-1,1)).human(40,.8)
x4 >> play("c", amp=[[0,1],0,0,0], dur=1/4, shape=PWhite(0.2,2), lpf=P*[200,linvar([40,18200],[32,0])])
x9 >> play("X ", sample=5, lpf=5800, amp=2)
v6 >> play("I", sample=4, hpf=PRand(2000,8000), rate=PWhite(-1,2), dur=P*[1,1/2], amp=[[0,1],0,0,0], pan=PWhite(-1,1))
v2 >> play("t", amp=[0,0,[0,1],[0,0,0,1]], lpf=P*[200,2000], dur=1/4)
z1 >> play("K", amp=[1,0,0,0], dur=1/4)
z2 >> play("o", amp=[[0,1],0,0,0], lpf=200, dur=1/4)
z3 >> play("-", amp=[0,0,[1,[1,0],1,1],0], dur=1/4, amplify=[0.76, 0.2, 0.4], rate=PWhite(1,4), pan=PWhite(-1,1))
z4 >> play("-", sample=1, amp=[[0,1],0,0,0], dur=1/4, shape=1, lpf=2200, rate=PWhite(1,4), pan=PWhite(-1,1))
z6 >> play("t", hpf=12000, dur=1/4, amp=[1,[0,1],1,[0,1]], sample=2, amplify=PGauss(4, 0.1), echo=0.125, echomix=var([0, 0.125], 4))
f2 >> pluck(linvar([0, 0.4], [4, 0]),oct=(linvar([6,6.2],[32,0]),5), dur=1/4, sus=linvar([1/8,1/4],[32,0]), vol=0.5).unison(4).human(80,0.5)
x1 >> play("K", amp=[1,0,0,0], dur=1/4)
x2 >> play("--", amp=[0,0,0,[1,1,1,[1,0]]], lpf=200, dur=1/4, pan=linvar([-1, 1], 16))
x5 >> play("o", amp=[[0,1],0,0,0], dur=1/4, sample=2)
x7 >> play("p", hpf=8000, dur=1/4, amp=[0,[0,1],0,[1,0]])
l1 >> play("V ", sample=3, cut=1, output=20)
f3 >> varsaw(linvar([1, 2.4], [8, 0]), leg=4,oct=(linvar([6,6.2],[64,0]),5), dur=1/2, sus=linvar([1/8,1/4],[32,0]), lpf=0, vol=0.5).unison(4).human(80,0.5)
Master().cut=0