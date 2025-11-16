# EuroDance
# Banger
Root.default=2
Scale.default="minor"
~p1 >> pluck((var([0, -2], 32),var([[3,5], 4, 2], 8)), dur=PDur(5, 8), lpf=0, sus=2, blur=2, chop=4, fmod=2, rate=2, fx2=1, fx2mix=1, hpf=PFr(100,4000), oct=PStep(8,P+(6,4),5), cutoff=2300).unison(3)
j3 >> dbass(var([0,[2, -2]], 16), dur=1/2, oct=(4,5), rate=0.5, valad=800, valadr=0.3, valadd=15, valadt=0, valadc=0.2, hpf=expvar([55,PRand(200,500)],33)).unison(3) + var([0, PGauss(0, 4)], [14,2])
~q1 >> cbass(7, dur=ù5, cutoff=10, rq=0.2, boost=1.5, detune=0.01, follow=linvar([1, 8], 41), tanh=0.1, fx2=1, vol=0.6).unison(2)
h4 >> dbass([0,3,5,0,3,5,7,0], dur=[21,0.5,0.5,1,0.5,0.5,1,1], sus=2, amp=var([1,0.8],[8,8]), oct=var([6, (6, 7)], 8), cutoff=12200, vol=1, vib=2, pan=PWhite(-0.6, 0.6))

q2 >> play("k.", sample=0, amp=2)
s1 >> play("<x(...x)><..u.>", sample=(1,3), drcomp=0.5, delay=0, mverb=(0,.1), amp=(1,2)).sometimes("stutter")
s2 >> play("<-[--]>", sample=7, pan=PWhite(-1,1), mverb=(0)).sometimes("stutter", PRand(8))
z8 >> play(".(...[u.])..(..(.([u.])))", sample=3, drcomp=0.5).sometimes("stutter", PRand(2,6), amp=PWhite(0.5,1))

p1.dur=PDur(1,8)
