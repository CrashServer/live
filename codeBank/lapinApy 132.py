# lapinApy 132
# banger

Clock.bpm=132
Scale.default="major"
Root.default=0

# lapinApy
q1 >> angst(PTime(), dur=8,cutoff=PFr(40, 18000),rq=PWhite(.1, 0.8), a=.2, wshape=5,wmix=PWhite(.1, 1.0), blur=2, amp=0.4,mverb=.7, slide=P*[1, 0,-1],slidefrom=P*[0,1,-1] ,slidedelay=PWhite(.25,0.75), lpf=0, hpf=100)

o2 >> lapin(var(P*[-2,2,4,6],8), dur=4, oct=4, lpf=4100).unison(2)

o3 >> dirt([P*[-2,0,1,2],P* [4,6,5,7,9]], dur=2, oct=(5,P*[6,7]), blur=2, atk=.02,decay=.001,  leg=PWhite(.0, 2.0), rate=PFr(0.1, 2.1),hpf=40, valad=linvar([500,2500],[55,27]), valadr=0.3, valadd=5, valadt=0, valadc=0.1, amp=.7 ).unison(3)

# variation + speed
o3 >> dirt([P*[-2,0,1,2],P* [4,6,5,7,9]], dur=1/2, oct=(5,P*[6,7]), blur=1, atk=.02,decay=.001,  leg=PWhite(.0, 2.0), rate=PFr(0.1, 2.1),hpf=40, valad=linvar([500,2500],[55,27]), valadr=0.3, valadd=5, valadt=0, valadc=0.2, amp=.7, pong=0.75 ).unison(3)

q8 >> pbass(var([0,-2],8)  + var([0, PGauss()], [7,1]),  dur=1/2, oct=(4,5),rate=expvar([0,8],[64,0]), hpf=30, amp=1.0).unison(3) + var([0,6, 7,9,0],[16, 8,4,2,2])
q8.oct=[4,5]
q8.degree=var([0,-2], 16)

c3 >> loop("electrodrum16", dur=16, sample=4)
d9 >> play("..o.", sample=2).sometimes("stutter", PRand(4))
y5 >> play("X.", amp=1)

z1 >> loop("breakcore160_16", dur=16, sample=var(PRand(808), 32))

