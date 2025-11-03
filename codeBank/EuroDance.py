# EuroDance
# Banger
Root.default="E"
Scale.default="minor"
p1 >> pluck((var([0, -2], 32),var([[3,5], 4, 2], 8)), dur=PDur(5, 8), sus=2, blur=2, chop=4, rate=1, mverb=.2, hpf=10, oct=PStep(8,P+(6,4),5)).unison(3)
q1 >> cbass(var([0, -2], 8), dur=8, cutoff=10, rq=0.2, boost=1.5, detune=0.01, follow=2, tanh=0).unison(3)
j3 >> dbass(var([0, -2], 8), dur=1/2, oct=(4,5), rate=.2, valad=800, valadr=0.3, valadd=15, valadt=0, valadc=0.2).unison(3)
q2 >> play("k.", sample=0, amp=2)
s1 >> play("<x(...x)><-><..u.>", sample=7).sometimes("stutter")
z8 >> play(".(...[U.])..(..(.([U.])))", sample=6).sometimes("stutter")
