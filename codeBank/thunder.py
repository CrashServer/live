# thunder
f1 >> dafbass([Pvar([P[4,7], P[5,8]],8),0], dur=1/4, oct=6, dist2=[0.8,0.4], fmod=[0,0]).gtr(5)
d1 >> play("-", sample=0, comp=0.8, mverb=0.4)

f1 >> dafbass([P[12,10,9,10,9,7,9,5,7,4,5,4,5,4,5,4],0], dur=1/4, dist2=[0.8,0.4], oct=6).gtr(5)
d1 >> play("<k.k...k...k...k.><m.m.............><M.M.............><->", sample=(0,1,1,0), comp=0.8, mverb=0.8)

b1 >> dafbass(var(P*[2,-3,-1,-5],8), dur=1/4, dist2=0.8, fmod=[2,4]).gtr(2)

a1 >> play("x.", sample=4, dur=0.5).sometimes("stutter")
a2 >> play("k.").drummer()