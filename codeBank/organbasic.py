# organbasic
Root.default = "E"
Scale.default = Scale.minor;
r1 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([PDur(4,8),PDur(5,8)]), amp=1, crush=1, crush_=4, crush_d=2, bits=6, bits_=var([12, 16]), fmod=1, lpf=2800, lpr=0.4)
r2 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.7, crush=1, crush_=4, crush_d=2, fx2=0.2, bits=6, bits_=var([12, 8]), oct=(5, 7), fmod=1, lpf=2800, lpr=0.2).unison(2).every(4, "shuffle")
r3 >> bell(P[var([0,-2,-3,-4],8),4,PStep(4,6,8),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.6, crush=1, crush_=4, crush_d=2, mverb=0.2, bits=6, bits_=var([12, 8]), delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")
r4 >> bell(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.5, crush=1, crush_=4, crush_d=2, mverb=0.5, bits=6, bits_=var([12, 8]), r1=0.5, delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")
r2 >> varsaw(oct=(3, 4, 5), lpf=(800, linvar([400, 12000], 128)), dur=[6, 2], sus=[4, 8], lpr=0.1, a=0.5)
r1 >> karp()
s1 >> klank(dur=8, oct=(3, 4, 5)).unison(3) # progressif

s2 >> klank(oct=linvar([5, 6], 128), dur=PDur(3, 8)* 2)
r1 >> dbass()
r2 >> donk()
r3 >> donk()
r4 >> lbass()
q1 >> play("--")
x1 >> play("x.", sample=5, amp=4, lpf=400)
p1 >> play("<E ><p >", sample=1, dur=PDur([3, 5], 8), amp=PWhite(0.3,0.5), hpf=220, chop=1/2, leg=PWhite(15), pan=PWhite(-1,1), fx2=1)
g1 >> loop("gab32", dur=32, hpf=4000, sample=1)

r_all.dur=2
r_all.oct=3


r4 >> dab(dur=PDur(var([4,[5,3,8]],[6,2]),8), leg=([0, 5]), cutoff=400, dist2=0.4, hpf=1000, hpr=0.1)

s3 >> klank(oct=linvar([5, 6], 128), dur=PDur(3, 5)* 2, drive=linvar([0.02, 0.04], 32)).stop()
k4 >> lapin(([-4, -3], 4), oct=(3, 4), shape=0.1, fdistfreq=4000, dur=8, lpf=4000, fdist=1, hpf=200, bpf=0, lofi=1, amp=PCoin(0.2, 0, 0.25)).unison(2).slider()

x4 >> play("..o.")

r2.degree=r4.degree
r3 >> varsaw()

r1 >> varsaw(mverb=0, dur=PDur(var([4,[5,3,8]],[6,2]),8), oct=3)
r2 >> donk(mverb=0, dur=PDur(var([4,[5,3,8]],[6,2]),8), oct=4)




