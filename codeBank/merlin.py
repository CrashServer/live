# merlin 

# hardishstuff, approximative
Clock.bpm = 128
j1 >> play("<B.BBv.Bv><v.Bbv.Bv><(...:)>", sample=(6, 6, 4), hpf=(200, var([200, 0, 30, 20]), 0), cut=(0, 0, 0.1), leg=0)
j3 >> play("T..h hh4. Tbbb mbbb", sample=4, cut=1/8)
j2 >> play("b ", sample=8, dur=PDur(5, 8), cut=1/2, mverb=0.2, hpf=var([0, PWhite(0, 1200)[:4]]))
j2 >> play("b ", triode=1, octafuz=1, octamix=PWhite(0.2, 0.6), sample=8, dur=PDur(5, 8), cut=1/2, mverb=0.2, hpf=var([0, PWhite(0, 1200)[:4]]))
j1.octafuz=0.2 #+
x4 >> play("x ", amp=4, lpf=400)
~j2 >> play("b ", sample=8, dur=PDur(5, 8), mverb=0.02, hpf=var([0, PWhite(0, 1200)[:4]]))
~j1 >> play("<B.BBv.Bv><v.Bbv.Bv><(...:)>", sample=(6, 6, 4), hpf=(200, var([200, 0, 30, 20]), 0), cut=(0, 0, 0.1), dur=1/2, vadiod=500, vadiodr=0.5, vadiodd=4)
variation = Variation(8, 2)
x4.lpf=1200
j0 >> play("..//", dur=9, sample=2, delay=4, rate=0.35, mverb=0, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.125, mverbfreeze=0)
x1 >> loop("bsbass4", dur=4, shift=2, amp=1, sample=3, mring=2, rstruct=0.8, rbright=0.4, rdamp=1, rpos=0, rmodel=2, rpoly=1, regg=0, rsus=1)
x1.sample=PRand(8)
l4 >> loop("choir16", dur=16, sample=2, coarse=1, mring=1, amp=2, chop=4, rstruct=1, rbright=4, rdamp=0.4, rpos=0.5, rmodel=2, rpoly=1, regg=0.4, rsus=2).unison(2)
j1.octafuz=0.3
l4.chop=12
j0.stop()
j1 >> play("B.BB")
j1 >> play("BVBB")
j1 >> play("<BVBB><:>", echo=1)
d7 >> play("c ", dur=4, mverb=0.5, mverbmix=0.5, mverbdamp=0.2, mverbdiff=1.625, mverbfreeze=0)
x5 >> play("-.[--]", sample=8, hpf=4000)
x7 >> play("<[--]><{...}><- ><.>", hpf=12000)
h1 >> play("{ - -}{  -}[-. ]",  sample=2,  dur=1/4,   rate=PWhite(0.95, 1.05), amp=P[1, 0.8, 0.6, 0.9, 0.7, 0.85, 0.5, 0.8], pan=PWhite(-0.3, 0.3),  room=0.1,   lpf=expvar([4000, 8000], 16)).every(8, 'stutter', 3)  # Occasional stutter effect
j0.stop()
j1 >> play("b ", rate=linvar([1, 1.12], [4, 0]), dur=1/4)
l4.stop()
j1 >> play("<B.BBv.Bv><v.Bbv.Bv><(...:)>", sample=(6, 6, 4), hpf=(200, var([200, 0, 30, 20]), 0), cut=(0, 0, 0.1))
~j2 >> play("b ", sample=5, dur=PDur(5, 8), mverb=0.02, hpf=var([0, PWhite(0, 1200)[:4]]))
j1 >> play("<B.BBv.Bv><v.Bbv.Bv><(...:)>", sample=(6, 6, 4), hpf=(200, var([200, 0, 30, 20]), 0), cut=(0, 0, 0.1))
l4 >> play("X ", sample=8, amp=2)
h_all.hpf=12000
x_all.hpf=12000
masterAll("octafuz", 0)
masterAll("shape", 0)
j9 >> loop("housebass24", dur=24, sample=1, shape=1)
j_all.hpf=0
x_all.stop()
e9 >> loop("housebass24", dur=24, sample=4)
e8 >> loop("housebass24", dur=24, sample=1, valad=1200, valadr=0.5, valadd=2, valadt=1)
j_all.dur=4
l4.octafuz=4
l4 >> play("X ", vakorg=1200, vakorgr=0.1, vakorgd=0.5, vakorgt=0)
o1 >> loop("circledrum16", dur=16, amp=2)
x4 >> play("X ", sample=8)
e9.dur=16
e8.dur=16
~x4 >> play("X ", sample=8, amp=4)
e9 >> loop("housebass24", dur=24, octer=0, shift=2, octersub=4, octersubsub=0).unison(4)

