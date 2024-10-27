# gruve
s1 >> play(".s", dur=1/2, echo=0.23, high=2)
d1 >> play("x.", sample=(4,0), amp=1)

# hmanize hihat
h3 >> play("-", dur=1/4, high=2).human(60,6,3)
h4 >> play("d", dur=PDur(3,12,0,1/3))

# little groove snare
n1 >> play("<..o.><..*.>", bank=0, rate=1, delay=PWhite(-0.05,.05)*0, sample=3)
n2 >> play("r", sample=4, dur=PDur(5,16,0,1/2), delay=0, dist2=PFr(0.5,1)).sometimes("stutter")

# play with pgroup, play with dur
y1 >> plaitsX([0,[P+[7,5], P+[1,2,PRand(8),7]]], preset=(11,12), dur=4, oct=(2,3,PStep(5,5,4)), dfm=PRand(900,5200)*1, dfmd=1, tremolo=PStep(8,4,0), tremolo_=0.5, dfmr=0.69, fdecay=1, mverb=0.8, amp=1)

# melodic bass with PGroup, play with fdecay
y2 >> superbass(P+(0,[7,5,3],2,[-2,1,4,6,9]), dur=2, oct=var([4, (4,5), (4,5,6)], [16,8,8]), hpf=0, cutoff=PFr(2800,6000), fdecay=PFr(1.0,2.0), sub=2, krush=1)

# plaits test
~p9 >> plaits(P[0,4,8,7], dur=1/2, oct=PStep(6,P*[5,4],3), harm=0.01, timbre=0.8, morph=0.99, engine=8, fdecay=3, cutoff=4000, bright=PFr(0.5,0.99), aux=1) + var([0,-2],8)

~p9 >> plaits(P[0,4,8,7], dur=1/4, oct=(3,4), harm=0.50, timbre=0.6, morph=0.94, engine=2, fdecay=1.8, cutoff=9000, bright=PFr(0.9,0.99), aux=0, porta=0.09, dist2=0.6) + var([0,0],8)

~p9 >> plaits(P[0,4,8,7], dur=1/4, oct=(3), harm=0.50, timbre=0.6, morph=0.84, engine=2, fdecay=2.8, cutoff=9000, bright=PFr(0.8,0.99), aux=0, porta=0.99, dist2=0.8) + var([0,2],8)

# Hard kick distored only
k1 >> play("X.", bank=1, sample=1, dfm=PFr(400,12000), dfmr=0.97, cut=PFr(1.79, 1.9), dfmd=2, drive=(0, 0.5), dist2=(0,0.8), crush=(0,4), bits=2, vol=0.8).often("stutter", PRand(4), hpf=100, cut=1).only()

