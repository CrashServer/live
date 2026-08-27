# attacks scan collection
# snippets

#70 > SCAN
c0 >> play("v", dur=1/2, lpf=PGauss(2000, 200), hpf=100, hpr=var([0.5, 0.2], 4),mverb=0.5, mverbdamp=0.1, mverbdiff=0.8, bpf=(1000, 1500), bpr=0.8, dist2=0.5, dist2mix=linvar([0.2, 1], [4, 2, 8]), dist2shape=1)
c1 >> latoo(dur=1, amp=1, cut=1/4, mverb=PWhite(0, 0.5), mverbdamp=0.8,lpr=0.2, mverbfreeze=0, mverbdiff=0.8, hpf=50, bpf=(1000, 500), bpr=0.8, mpf=1200, lpf=(200, 600),dist2=1, dist2mix=1, dist2shape=1).unison(2)
c2 >> pink(dur=1/2, cut=1/4, hpf=1200, hpr=PWhite(0.1,1), leg=8, a=PWhite(0, 0.2), pan=PWhite(-1, 1), amp=PWhite(0, 0.5))
c3 >> play("<q><k>", sample=(3,P[0:5]), delay=(0,(0,[0,0.25])), dur=c0.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=0, hpf=0)
# --------------------------------------------------------------------
#70 > SCAN 2
c0 >> play("<q><k>", sample=(3,P[0:5]), delay=(0,(0,[0,0.25])), dur=a6.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=0, hpf=0, valad=600)
c1 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)
c2 >> dbass(valad=var([1000, 1200, 2000]), lpf=600, amp=0.5, dist2=5, hpf=400, hpr=0.95, valadt=1, valadd=1, valadr=1,     mverb=0.6, mverbdiff=1, leg=4, dur=[1/4, 1/2, 1/2, 1/2, 1/4, 1/4, 1/4])
c3 >> play("(X-)([x-].).([X---]..O.)")
# --------------------------------------------------------------------
#133 > NEWBEAT
Clock.bpm = 133;
Root.default = "D#"
d1 >> dbass([3, 4, 4, 8, 4, 7,  4, 4], scale=Scale.chromatic, dur=1/2).unison(2)
d2 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], oct=P[5, 6], scale=Scale.chromatic, dur=1/2, echo=0.25)
d3 >> ssaw(P*[3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/2, amp=PWhite(0, 1), oct=6)
d4 >> zap([3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/4, oct=PWalk(4, 1, 1) + 2, dist2=1).unison(2)
d5 >> play("x ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1), hpr=[0.1, 0.5])
d6 >> play("pM", lpf=1200, hpf=1200, dur=var([2, PDur(3, 8)]), lpr=linvar([0.1, 0.8], [8, 16]), rate=(1, 0.5, 0.25), delay=(0, 0.25, 1), amp=1)
d1 >> ebass([0, 0, 0.1, 0, 2], dur=1/2, hpr=0.1, oct=7, hpf=400, mverb=0.01).slider().unison(4) + var([0, 14], [15, 1])
d2.dur=1/2
d2.dist2=1
d2.mverb=0.5
d3 >> play("p", amp=P[1, 1, 1, 1, 0.1, 0.1].stutter(2), sample=5, shape=var([0, 0.5, 1]), vol=2)
d4 >> play("+", amp=P[1, 1, 1, 1, 0.1, 1].stutter(2), dur=PDur([3, 3, 5, 8], 8) * 4, sample=d3.dur, shape=0, rate=P*[1, 2, -1, 1, 1, 2, 4])
d5 >> dbass([0, 0, 11, [11, 14]], dist2=4, oct=6, dur=1/2, lpf=linvar([100, 6400], [32, 8, 8, 16]), mpf=linvar([2000, 320], 32), bpf=linvar([200, 3200], 16), bpr=linvar([1, 0.1], 8), echo=var([0.5, 0.25, 1], 8), mpr=var([0.1, 0.5, 0.8, 0.3], [4, 8, 2, 16]), lpr=var([0.1, 0.5, 0.8, 0.3], [4, 8, 2, 16]))

d5 >> play("-", lpf=0, hpf=100, dur=1/2, delay=0.5, mverb=0.5, amp=1)
d8 >> play("V ", sample=1, hpf=200, shift=1, cut=1/2)
d7 >> play("X ", hpf=400, sample=5, dur=var([1, 1/2], [3, 4])).often("stutter")

d4.lpf=400
d2.lpf=400

d1 >> dbass(P[-65, -65, -65, -65, 11, 12].stutter(2), dur=1/2, dist2=1, shape=1, revsus=1, mverb=0.5, amp=2, oct=(6, 5))
d3 >> faim(P[  P[-2, -4], P[-4, -3]].stutter(4),oct=4, dur=1/2, dist2=1, tanh=linvar([0.5, 0.7], 32))

d4 >> play("X ")
~d4 >> play("X ")

# [broken in source] >> 95 #
Clock.bpm = 95;

d0 >> dbass([0, 0, [0.5, 0, 4]], dur=1/4, oct=PStep(4, 5, 6), feed=0.1).unison(4).sometimes("offadd", 4)
d1 >> dbass([0, 0, [0.5, 0, 4]], dur=PDur(3, [8, 4]), oct=PStep(4, 5, [3, 4, 5, 6, 7]), feed=0.1).unison(4).sometimes("offadd", 7)
d2 >> dbass([0, 0, [0.5, 0, 4]], dur=1/4, oct=PStep(4, 5, 6), feed=0.1, shape=(0.1, 0)).unison(4).sometimes("offadd", 4)
d0 >> dbass([0, 0, [0.5, 0, 4]], hpf=var([400, 600]), dur=1/4, oct=PStep(4, 5, 6), feed=0.2, lpf=linvar([200, 1200], 32), hpr=0.3).unison(2).sometimes("offadd", 4)
d1 >> tb303([0, 0, [4, 0, 4]], amp=1, dur=PDur(3, [8, 4]), oct=PStep(4, 5, [3, 4, 5, 6, 7]), feed=0.2, hpf=1000, dist2=1, hpr=0.08, cutoff=120, ctf=12, res=0.1, top=400).unison(2).sometimes("offadd", 7)
d2 >> faim([0, 0, [0.5, 0, 4]], dur=var([1/4, P*[2, 1/2, 1]]), beef=1, oct=PStep(4, 4, 5), feed=0.0, dist2=1, shape=(0.1, 0)).unison(2).sometimes("offadd", 4)
d3 >> faim([0, 0, [0.5, 0, 4]], dur=4, oct=PStep(4, 5, 7), feed=0, dist2=0.2).unison(4).sometimes("offadd", 4)
Root.default = var([12, 0.1, 0, 0, 0.1, 2, 0, 0, 1], 1)

# -----------------------------------------------
Clock.bpm=92
Scale.default="minor"

d0 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{vU})","(-ux)"), dur=var([1/2, 1], [8, 4]), dist2=P*[0,expvar([0.01,0.9],26)], oct=(3, PStep(9,5,4)), rate=var([1, PWalk(8, 1, 1)], [7, 1]),octer=1, octersub=1, valad=1200, valadd=0.5, octersubsub=var([2, PRand(15,2222)], [15, 1]), triode=0, lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), sample=4, valadr=0.9,valad=2000, valadd=PWhite(0, 4), pan=PWhite(-1,1), amp=0.5, rate=PRand([1, 4]))
d1 >> play(PEuclid2(var([3,4, 12],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=[2, 4, 2], delay=0.5, dist2=P*[0,expvar([0.01,0.9],26)], oct=(3, PStep(9,5,4)), octer=0, octersub=0, octersubsub=var([2, PRand(15,2222)], [15, 1]), triode=0, lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), sample=4, valadr=0.9,valad=2000, valadd=PWhite(0, 4), pan=PWhite(-1,1), amp=0.25, rate=2)
d2 >> play("P", amp=0.2, sample=var([3, 4], 4), dur=2, cut=1/2, mverb=1, bpf=0, bpr=0, pan=PWhite(-1, 1), mverbdamp=[0.1, 0.5, 0.9], mverbdiff=[1, 0.5], lpr=(0.1, [0, PWalk(8, 1, 1)/10]), lpf=(PRand(4000), linvar([200, 800], 16)))
d3 >> play("k[--]{[cc][.C][[[mT]--]*][o.]}", sample=PwRand([5, 7], [2, 7]), dur=[[1/2, [1/4, [3/4]]], 1/4, 1/2, [2, P*[2, 4, 1/4]]], delay=(0, 0.5, 0.125, 0.5), shape=[a1.dur==2] * PWhite(0, 1), rate=var([1, linvar([4, 1], 16)]), mverb=(1, 0.5), leg=([12, 0], [4, 2, 4]), mverbdamp=[0.8, linvar([1, 0.8])], amp=[0.5, 0, 0.25, 0.25, 0.75, 0.5, 3/4, 1]).unison(0)
d0.stop()
d3 >> play("<X ><(-[--]-[::])><..|*2|.><..C.>", bits=16, amp=1, dur=2, crush=3, room1=0, mix=PWhite(0,0.5)).rarely("amen").sometimes("stutter", PRand(1,6), rate=PRand([1,6]))
d1 >> soprano([III, VII], amp=0.5, mverb=0.1, slide=0.1, cut=1, dur=8, oct=(3, 4), root=[0, PStep(4, 0, 4)], shape=0.5)
b3 >> dbass(dur=1/4, oct=5, spf=2400, spfslide=var([0.5, [4, linvar([2, 2], 32)]]), spfend=var([200, 400, 2000, 800, 3200], PRand(8)), dist2=var([0, 1], [24, 8]), lpf=4000, sus=b2.dur, tanh=1, mverb=(0.05, 0.2), spr=PWhite(0.01, 0.1)).slider()

d2 >> blip(P[0,5,P*[7,8,4],3], oct=P*[5,[6,4,7]], vib=0, slide=0, slidedelay=0, sus=s1.dur*PWhite(0.3,0.8), dur=1/4, room=0, mix=0, amp=d1.degree=="v", dist2=1, fx2=1).spread().after(4, "stop") + P[0,0,P*[2,4],0]

d0 >> soprano((0, [0, 0.5, ]), amp=0.10, mverb=1, slide=1, cut=(1/4, 1), dur=8, shift=0.5, oct=(2, 4), root=[0, PStep(4, 0, 4)], shape=0.1)

d1 >> play("X ")

d1.amp=0.1

d2 >> donk(var([0,[-4,2,-2]],[14,2]), dur=P*[2,6, 1/4, 1/4, 1/4, 1/4],amp=(d1.degree!="v")*0.8, lpf=linvar([1800,3500],19), lpr=expvar([1,0.2],17), sus=b1.dur*PWhite(0.8,2),fx1=1, fx2=0.0, rate=linvar([0.1,15],23), oct=(PStep(7,6,8),4,PStep(4,6,7)), salad=4000, saladd=1, shape=0, dist2=1).unison(3)

d4.amp=PFrac(0.62, 0.12)
d2.amp=PFrac(0.52, 0.21)

# ---------------------------
# tabation 2

d2 >> ebass([0, var([21, 0], [5, 7])], dist2=1, dur=P*[1/2, 1, 1/4, 1/4], oct=PStep(5, 4, (6, 4)), valad=linvar([500, 2000])).unison(4)
b1 >> dbass(P[0, 4, P[6, 0]], dur=P*[2, 1/2, 1/4, 1, 1/4], spf=1200, spfslide=var([0.2, [0.02, linvar([0.02, 0.01], 32)]]), spfend=200, dist2=1, lpf=1200, tanh=[0, 0.1], mverb=(0.05, 0), spr=0.4)
d3 >> fbass(dur=P*[8,2, 2, 1, 1/4, 1/4, 1/4, 1/4, 1/4, 1/4], oct=P*[4, 5,6], spf=2400, spfslide=var([0.5, [4, linvar([2, 2], 32)]]), spfend=var([200, 400, 2000, 800, 3200], PRand(8)), dist2=var([0, 1], [24, 8]), lpf=linvar([200, 4000], 32), sus=b2.dur, tanh=0.5, mverb=(0.05, 0.2), spr=PWhite(0.01, 0.1)).slider()
c0 >> play("v", dur=P[1, 1/3, 1/3, 1/3, 1/2,1/2, 1/4, 1/4, 1/4, 1/4], cut=2-0.95, lpf=PGauss(2000, 200), hpf=2000, hpr=var([0.5, 0.2], 4),mverb=c0.dur/4, mverbdamp=1-c0.dur, mverbdiff=0.8, mverbdist=1, delay=0.5, bpf=(1000, 1500), bpr=0.8, dist2=0.5, dist2mix=linvar([0.2, 1], [4, 2, 8]), dist2shape=0)
c1 >> play("xx").stop()
