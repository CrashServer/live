# intropic 143
# mud
f0 >> loop("rageambi16", dur=16, a=0.2, sample=1).lclip(0)
f1 >> loop("rageambi16", dur=24, sample=3, delay=1, mverb=0.5).lclip([2, 2, 4, 2])
d0 >> play("<kk.Kkkkkk.kk><u.(...C).><~.><X...>", dur=1/4, valad=0, sample=1, valadr=0.3, valadd=139, valadt=4, valadc=0.1, amp=1, high=1).sometimes("stutter")
masterAll("amp", var([1,P*[0,1]], [12,4]))
p4 >> loop("dnbfx16", dur=16, dist2=0.5, sample=[1, 3, 0], amp=2)
m0 >> vati(I,off=(7, 3), dur=(4, 6), tremolo=0.1, leg=0.5, oct=3, tanh=1).unison(4)
d0.trim(0)
w9 >> loop("ragegtr16", dur=16, lpf=3900, sample=4, chop=2, dafilter=300, dastart=1220).lclip(2)
h0 >> loop("gab16", dur=16, sample=9, high=8)
t1 >> loop("noizebeat16", dur=16, sample=5, lpf=3600).lclip(4)
w9.lclip(8)
a7 >> loop("gab8", dur=8, sample=5)
