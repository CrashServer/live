
rec()

#@intro(16)
v6 >> play("x ", dur=1/2, amp=Pacc(2), rgate=0.5, csweep=0.1, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@build(4)
v6 >> play("x ", dur=1/2, lpf=linvar([1700, 3700, 2800], [3, 2]))

#@peak(16)
v6 >> play("x ", dur=1/2, lpr=0.1, lpf=linvar([500, 1800, 1500], [4, 1]), echo=0.5, gdel=0.3, gdeltime=0.8, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.5)

#@break(4)
v6 >> play("x ", dur=1/2, lpf=linvar([500, 1800, 1500], [4, 1]), shape=0.6)

#@drop(8)
v6 >> play("x ", dur=1/2, lpf=linvar([500, 1800, 1500], [4, 1]), shape=0.3)

#@outro(16)
v6 >> play("x ", dur=1/2, lpf=linvar([500, 1800, 1500], [4, 1]), shape=linvar([0.3, 0.7, 0.6, 0.7, 0.3, 0.5, 0.3], [1.5, 0.5, 0.5, 1.5, 1, 1]))

#@part7(8)
p6 >> dbass(dur=1/2)

#@part8(8)
p6 >> dbass(dur=1/2, lpf=200)

#@part9(4)
p6 >> dbass(dur=1/2, lpf=400, lpr=0.1)

#@part10(4)
~p6 >> dbass(dur=1/2, lpf=400, lpr=0.1)

#@part11(16)
p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2))
~p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2))

#@part12(16)
f5 >> play("..-.")

#@part13(4)
f5 >> play("..-.").every(4, "stutter")

#@part14(16)
f5 >> play("..[----].").every(4, "stutter", 8)

#@part15(4)
f5 >> play("..{-[---]}.").every(4, "stutter", 8)

#@part16(16)
f5 >> play("..{-[---]}.").every(4, "stutter", 8)

#@part17(4)
f5 >> play("..{-[---]}.", hpf=2000).every(4, "stutter", 8)

#@part18(4)
f5 >> play("..{-[---]}.", hpf=2100).every(4, "stutter", 8)

#@part19(4)
f5 >> play("..{-[---]}.", hpf=4700).every(4, "stutter", 8)

#@part20(16)
f5 >> play("..{-[---]}.", hpf=linvar([2100, 4700], 3)).every(4, "stutter", 8)

#@part21(16)
m9 >> superbass(rate=0.5, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1)

#@part22(32)
m9 >> superbass(rate=0.5, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5)

#@part23(8)
m9 >> superbass(rate=0.5, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part24(8)
m9 >> superbass(rate=0.5, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part25(8)
b1 >> play("X ")

#@part26(8)
b1 >> play("X[xx]")

#@part27(8)
m9 >> superbass(rate=2.0, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

m9.slide=0.5

#@part28(8)
m9 >> superbass(rate=2.0, cutoff=1000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part29(8)
m9 >> superbass(rate=2.0, cutoff=1000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, tstretch=1, tstretchsize=0.2, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part30(16)
f5.stop()

#@part31(4)
p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2)).unison(4)

#@part32(8)
p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2)).unison(6)


m9.dur=16
#@part33(4)
p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2)).unison(6)

#@part34(4)
p6 >> dbass(dur=1/2, lpf=500, lpr=sinvar([0.2, 0.5], 2)).unison(6)

#@part35(4)
p6 >> dbass(dur=1/2, lpf=4300, lpr=sinvar([0.2, 0.5], 2)).unison(6)

#@part36(16)
p6 >> dbass(dur=1/2, lpf=linvar([500, 4500, 3300], [4, 3]), lpr=sinvar([0.2, 0.5], 2)).unison(6)

#@part37(32)
m9 >> ews()

#@part38(4)
attack("R_Jazz2")

#@part39(16)
g8 >> play("<k(...[--])><-:><..*.>", sample=1, amp=1, bank=1, dur=1/2, rate=1, cut=1.2).sometimes("stutter")


m9.oct=6

#@part40(8)
e4 >> play("a", bank=2, dur=PDur([4,3,5],8), sample=PFr(0,88,1664,4), rate=.4, valad=1000, valadr=0.5, valadd=25, valadt=ê*4, valadc=0.2)

#@part41(4)
e4 >> play("a", bank=2, dur=PDur([4,3,5],8), sample=PFr(0,88,1664,4), rate=.4, valad=1000, valadr=0.5, valadd=25, valadt=ê*4, valadc=0.4)

#@part42(4)
e4 >> play("a", bank=2, dur=PDur([4,3,5],8), sample=PFr(0,88,1664,4), rate=.4, valad=1000, valadr=0.5, valadd=25, valadt=ê*4, valadc=0.2)

#@part43(16)
e4.stop()

#@part44(4)
attack("bells2 120")

#@part45(16)
p1 >> bell2([0,4,7], dur=16, oct=5, amp=0.8, atk=4, sus=14, lpf=linvar([400,2500],64), room=0.6, mix=0.4, multicrush=2, mclowdrive=2, tube=1, tubegain=1, tubewarm=1, mcmiddrive=1, mchighdrive=4, mclofreq=1200, mchifreq=1200)

p6.stop()


#@part46(4)
p1 >> bell2([0,4,7], dur=16, oct=5, amp=0.8, atk=4, sus=14, lpf=linvar([400,2500],64), room=0.6, mix=0.8, multicrush=2, mclowdrive=2, tube=1, tubegain=1, tubewarm=1, mcmiddrive=1, mchighdrive=4, mclofreq=1200, mchifreq=1200)

#@part47(4)
s1 >> bell2([0,0,4,0,7,0,4,0], rgate=0.4, fbdelay=linvar([0.1, 0.7], 128), dur=1/4, oct=4.01, amp=0.56,lpf=linvar([600,3000],32), lpr=0.2, sus=0.3, tube=0.2, tubewarm=1, tubegain=0.9, multicrush=0, hpf=200, apan=0, awidth=0.6).unison(2,0.01)

#@part48(32)
s2 >> bell2([0,0,4,0,7,0,4,0], gate=0.0, fbdelay=0.78, dur=2, oct=5, amp=0.56,lpf=linvar([600,3000],32), lpr=0.3, sus=0.5, tube=0, tubewarm=0, tubegain=1, multicrush=0, apan=0, awidth=0.5, hard=var([0, 1, 2, 4, 8, 4, 2, 16, 4, 2]), round=0.2,nharm=2, fmamt=[0, 0,1, 1, 2, 4, 4], fmratio=12,strike=1, shimmer=2.0).unison(2,0.01)

#@part49(4)
s1.only()

#@part50(8)
s2 >> bell2([0,0,4,0,7,0,4,0], gate=0.0, fbdelay=0.78, dur=2, oct=5, amp=0.56,lpf=linvar([600,3000],32), lpr=0.3, sus=0.5, tube=0, tubewarm=0, tubegain=1, multicrush=0, apan=0, awidth=0.5, hard=var([0, 1, 2, 4, 8, 4, 2, 16, 4, 2]), round=0.2,nharm=2, fmamt=[0, 0,1, 1, 2, 4, 4], fmratio=12,strike=1, shimmer=2.0).unison(2,0.01)

#@part51(16)
s3 >> bell2([0,4,7,4], dur=1/4, oct=5, amp=var([0,0.65],[16,16]), lpf=linvar([1000,4000],32), room=0, sus=0.15, eb=0.5, leg=4, tube=0.5, tubewarm=4, mverb=0.1, a=0, bright=0.5, damp=0.5, hard=12, round=1,inharm=0.01, fmamt=1, fmratio=2.4,	strike=0.3, shimmer=0.31)

#@part52(4)
attack("spacesounds  120")

#@part53(4)
s1 >> loop("sundrone16", dur=8, amp=linvar([0.4, 0.6], 32), shimmer=0.4, shimmix=0.3)

#@part54(4)
q1 >> loop("quake8", dur=8, amp=0.8, lpf=1200, tape=0.6, echo=0.5, tapedrive=0.6)

#@part55(16)
s3 >> loop("whitedwarf16", dur=16, amp=0.9, hpf=1200, rgate=0.2, chop=4, mverb=0.0).lclip(4)

#@part56(16)
rec_stop()
# recorded_030146
# recorded

#@intro(32)
v6 >> play("x ", dur=1/2, amp=Pacc(2))

#@build(8)
v6 >> play("x ", dur=1/2, amp=Pacc(2), rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@peak(4)
v6 >> play("x ", dur=1/2, amp=Pacc(2), rgate=0.5, csweep=0, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@break(4)
v6 >> play("x ", dur=1/2, amp=Pacc(2), rgate=0.5, csweep=0.1, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@drop(16)
v6 >> play("x ", dur=1/2, lpf=400)

#@outro(16)
v6 >> play("x ", dur=1/2, lpf=linvar([1700, 3700, 2800], [3, 2]))

#@part7(8)
v6 >> play("x ", dur=1/2, lpf=linvar([500, 1800, 1500], [4, 1]))

#@part8(8)
v6 >> play("x ", dur=1/2, lpr=0.1, lpf=linvar([500, 1800, 1500], [4, 1]))

#@part9(64)
v6 >> play("x ", dur=1/2, lpr=0.1, lpf=linvar([500, 1800, 1500], [4, 1]), echo=0.5)

#@part10(16)
v6 >> play("x ", dur=1/2, lpr=0.1, lpf=linvar([500, 1800, 1500], [4, 1]), echo=0.5, gdel=0.3, gdeltime=0.8, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3)

#@part11(16)
v6 >> play("x ", dur=1/2, lpf=linvar([500, 1800, 1500], [4, 1]), shape=0.2)

#@part12(16)
v6 >> play("x ", dur=1/2, lpf=linvar([500, 1800, 1500], [4, 1]), shape=linvar([0.3, 0.7, 0.6, 0.7, 0.3, 0.5, 0.3], [1.5, 0.5, 0.5, 1.5, 1, 1]))

#@part13(4)
p6 >> dbass(dur=1/2)

#@part14(4)
p6 >> dbass(dur=1/2, lpf=400)

#@part15(8)
p6 >> dbass(dur=1/2, lpf=200)

#@part16(8)
~p6 >> dbass(dur=1/2, lpf=200)
p6 >> dbass(dur=1/2, lpf=200)

#@part17(16)
~p6 >> dbass(dur=1/2)
p6 >> dbass(dur=1/2)

#@part18(8)
p6 >> dbass(dur=1/2, lpf=400, lpr=0.1)
~p6 >> dbass(dur=1/2, lpf=400, lpr=0.1)

#@part19(8)
p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2))
~p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2))

#@part20(16)
f5 >> play("..-.").every(4, "stutter", 8)

#@part21(8)
f5 >> play("..{-[---].").every(4, "stutter", 8)

#@part22(4)
f5 >> play("..{-[---]}.").every(4, "stutter", 8)

#@part23(4)
f5 >> play("..{-[---]}.", hpf=2000).every(4, "stutter", 8)

#@part24(4)
f5 >> play("..{-[---]}.", hpf=2100).every(4, "stutter", 8)

#@part25(4)
f5 >> play("..{-[---]}.", hpf=linvar([2100, 4700], 3)).every(4, "stutter", 8)

#@part26(4)
m9 >> superbass(rate=0.5, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1)

#@part27(8)
m9 >> superbass(rate=0.5, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part28(4)
m9 >> superbass(rate=0.5, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part29(4)
b1 >> play("X ")

#@part30(8)
b1 >> play("X[xx]")

#@part31(8)
m9 >> superbass(rate=2.0, cutoff=5000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part32(4)
m9.slide=0.5

#@part33(4)
m9 >> superbass(rate=2.0, cutoff=1000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part34(4)
m9 >> superbass(rate=2.0, cutoff=1000, rq=0.0, rqd=0.0, fdecay=4, sub=1, dur=4, mverb=0.5, csweep=0.1, cswfreq=1200, tstretch=1, tstretchsize=0.2, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part35(4)
p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2)).unison(4)

#@part36(16)
p6 >> dbass(dur=1/2, lpf=400, lpr=sinvar([0.2, 0.5], 2)).unison(6)

#@part37(4)
m9.dur=8

#@part38(8)
p6 >> dbass(dur=1/2, lpf=500, lpr=sinvar([0.2, 0.5], 2)).unison(6)

#@part39(4)
m9.dur=16

#@part40(8)
p6 >> dbass(dur=1/2, lpf=linvar([500, 4500, 3300], [4, 3]), lpr=sinvar([0.2, 0.5], 2)).unison(6)
m9 >> ews()

#@part41(16)
g8 >> play("<k(...[--])><-:><..*.>", sample=1, amp=1, bank=1, dur=1/2, rate=1, cut=1.2).sometimes("stutter")

#@part42(8)
m9.oct=6

#@part43(8)
e4 >> play("a", bank=2, dur=PDur([4,3,5],8), sample=PFr(0,88,1664,4), rate=.4, valad=1000, valadr=0.5, valadd=25, valadt=ê*4, valadc=0.4)

#@part44(8)
e4 >> play("a", bank=2, dur=PDur([4,3,5],8), sample=PFr(0,88,1664,4), rate=.4, valad=1000, valadr=0.5, valadd=25, valadt=ê*4, valadc=0.4)

#@part45(8)
e4 >> play("a", bank=2, dur=PDur([4,3,5],8), sample=PFr(0,88,1664,4), rate=.4, valad=1000, valadr=0.5, valadd=25, valadt=ê*4, valadc=0.2)

#@part46(16)
p1 >> bell2([0,4,7], dur=16, oct=5, amp=0.8, atk=4, sus=14, lpf=linvar([400,2500],64), room=0.6, mix=0.4, multicrush=2, mclowdrive=2, tube=1, tubegain=1, tubewarm=1, mcmiddrive=1, mchighdrive=4, mclofreq=1200, mchifreq=1200)

#@part47(4)
p6.stop()

#@part48(4)
p1 >> bell2([0,4,7], dur=16, oct=5, amp=0.8, atk=4, sus=14, lpf=linvar([400,2500],64), room=0.6, mix=0.8, multicrush=2, mclowdrive=2, tube=1, tubegain=1, tubewarm=1, mcmiddrive=1, mchighdrive=4, mclofreq=1200, mchifreq=1200)

#@part49(8)
s1 >> bell2([0,0,4,0,7,0,4,0], rgate=0.4, fbdelay=linvar([0.1, 0.7], 128), dur=1/4, oct=4.01, amp=0.56,lpf=linvar([600,3000],32), lpr=0.2, sus=0.3, tube=0.2, tubewarm=1, tubegain=0.9, multicrush=0, hpf=200, apan=0, awidth=0.6).unison(2,0.01)

#@part50(16)
s2 >> bell2([0,0,4,0,7,0,4,0], gate=0.0, fbdelay=0.78, dur=2, oct=5, amp=0.56,lpf=linvar([600,3000],32), lpr=0.3, sus=0.5, tube=0, tubewarm=0, tubegain=1, multicrush=0, apan=0, awidth=0.5, hard=var([0, 1, 2, 4, 8, 4, 2, 16, 4, 2]), round=0.2,nharm=2, fmamt=[0, 0,1, 1, 2, 4, 4], fmratio=12,strike=1, shimmer=2.0).unison(2,0.01)

#@part51(8)
Clock.clear()
soff()
Server.clearFx()

#@part52(16)
rec_stop()

#@endfade(16)
