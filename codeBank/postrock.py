# postrock
f1 >> faim([var([0,3,5],[24,4,4]),[12,10,8,7,8]], dur=[1/2], sus=[1,1/2], echo=0, dist2=(0,0.8)).gtr(1)

f2 >> faim(var(P*[2,3,5],PRand(16).rnd(4)), dur=1/2, mverb=0.5, atk=0.01, amp=0.7).gtr(3)
f3 >> faim(var(P*[4,5,7,12],PRand(16).rnd(4)), dur=1/2, mverb=0.5, atk=0.01, amp=0.7).gtr(4)

d4 >> play("x.",sample=(0,4), amp=1, lpf=900).sometimes("stutter", hpf=400)
d1 >> play("k(.k)..", sample=(0,9)).sometimes("stutter")
d2 >> play("<---{-[--]=:#}><.:>", sample=7, high=2).sometimes("stutter", PRand(8), rate=PWhite(1,8))
d3 >> play("..u(...{u[uu][.u]})", sample=(10,4))

t1 >> play("{tTmM}", sample=5, dur=PDur(5,8), low=2).fill()

d6 >> play("x.", dur=1/2, sample=4)

r1 >> rhodes(P[0,4,6,P*[-2, P*(0,4)]] + (0,2), dur=P[4,1/2,1/2,P*[1,rest(1)],P*[1,rest(1)],1/2,1/2], oct=(4), sus=r1.dur*PWhite(0.5,1), lpf=2400, mverb=0.4).sometimes("jump", 3) + var([0,7], [13,5])
f1 >> faim(var([0,2,-2,4],8), dur=PDur(5,8), oct=4, slide=var([0,1],[7,1])) + var([0,P*[1,-1]],[7,1])

Clock.bpm=90