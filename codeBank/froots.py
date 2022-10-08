# froots
Root.default=3
Clock.bpm = 76

b2 >> abass(var([0,P^(-4,P*[2,-2,3],[0.5,0.25])],16), dur=PDur(7,11) | rest(1.25), valad=460, valadr=0.59, oct=PStep(8,4,3), valadt=PFrac().lmap(0,3).int(), cutoff=8400, rel=PWhite(0.01,0.2))

c8 >> cs80([b2.degree,P*[4,2,1,0,-2,5,6]], dur=PDur(4,12)*PRand([8,4,2]), vibspeed=12, cutoff=12000, oct=PStep(8,P*[6,5],4), valad=PRand(260,860), valadr=0.4, fsus=0.2, fdec=0.2, fatk=0.2, ratio=PWhite(0.2,1.2), cglide=PWhite(0.01,0.285), vol=0.5).unison(3)

k1 >> play("<X.><..c.><{+pM}><[R]>", sample=4, dur=0.5, valad=PRand(160,3420), valadr=0.2, valadd=0.2, vol=0.7).sometimes("stutter")