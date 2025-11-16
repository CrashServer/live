# postrock 90
# interlude

Clock.bpm=90
f1 >> faim([var([0,3,5],[24,4,4]),[12,10,8,7,8]], dur=[1/2], sus=[1,1/2], echo=0, dist2=(0.8), oct=(4), slide=var([0,1],[7,1])).gtr(1)

f2 >> faim(var(P*[2,3,5],PRand(16).rnd(4)), dur=1/2, mverb=0.5, atk=0.01, amp=1.0, pan=-0.5).gtr(3).human(40, .8)
f3 >> faim(var(P*[4,5,7,12],PRand(16).rnd(4)), dur=1/2, mverb=0.5, atk=0.01, amp=1.0, pan=0.5).gtr(4).human(30,.7)

d4 >> play("x.",sample=(0,4), amp=1, lpf=2900).sometimes("stutter", hpf=400)
d1 >> play("k(.k)..", sample=(0,9)).sometimes("stutter")
d2 >> play("<---{-[--]=:#}><.:>", sample=7, high=2).sometimes("stutter", PRand(8), rate=PWhite(1,8))
d3 >> play("..u(...{u[uu][.u]})", sample=(10,4))

t1 >> play("{tTmM}", sample=5, dur=PDur(5,8), low=2).fill()
