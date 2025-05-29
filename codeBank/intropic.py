# intropic
Clock.bpm = 143
f0 >> loop("rageambi16", dur=16, sample=1)
# d0 >> play("<kk.Kkkkkk.kk><u.(...C).><~.><X...>", dur=1/4, valad=0, sample=1, valadr=0.3, valadd=139, valadt=4, valadc=0.1).sometimes("stutter")
masterAll("amp", var([1,P*[0,1]], [12,4]))
# p4 >> loop("dnbfx16", dur=16, dist2=0.5, sample=[1, 3, 0], amp=2)
# m0 >> vati(I,off=(7, 3), dur=(4, 6), tremolo=0.1, leg=0.5, oct=3, tanh=1).unison(4)
d0.trim(0)

w9 >> loop("ragegtr16", dur=16, lpf=3900, sample=4, chop=2, dafilter=300, dastart=1220).lclip(2)
h0 >> loop("gab16", dur=16, sample=6)
# t1 >> loop("noizebeat16", dur=16, sample=5, lpf=3600).lclip(4)
a7 >> loop("gab8", dur=8, sample=4)
p5 >> play("x.", sample=15, rate=1, dafilter=0)