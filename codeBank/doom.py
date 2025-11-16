# doom 170
# Cover
Clock.bpm = 170

g1 >> faim(P[-5,-5,7,-5, -5,5,-5,-5, 3,-5,-5,1, -5,-5,2,3, -5,-5,7,-5, -5, 5,-5,-5, 3,-5,-5, P(-5,1)], dur=P[1/2].stutter(27) | 2.5, lpf=[PRand(400,2280),0,0], leg=PRand(12,128), lpr=PWhite(0.1,0.5), beef=(0, 0.5), dist2=1, fx1=0, shape=0.3, vol=0.4).gtr(2)
g2 >> tb303(Pvar([P[21,19,18,21, 24,22,21,18, 21,22,24,26, 24,22,21,18], P[26,22,19,22, 26,22,26,31, 26,22,26,22, 26,31,34,38]],32), dur=1/4, amp=var([0,1],[28,4]), dist2=0.5, oct=4, rq=0.2, top=PRand(500,4000)).gtr(2)
n7 >> tb304(cutoff=100, rq=0.7, top=1500, fAtk=0.001, fDec=0.15, fSus=0.0, fRel=0.2, wave=0)
g3 >> lbass(var([0,P*[3,5,7,0]],[14,2]), oct=5, dur=1/2, lpf=1700, cutoff=4000, lpr=0.5, beef=2).gtr(1)
g4 >> play("<k(.k)u.><->", sample=(9,5), amp=2).human(40,0).every(14, "stutter", 8, cycle=16, degree="u", amp=PWhite(0.3,1))

j3 >> loop("ragedrum32", dur=32, drcomp=0.5, sample=1)
v8 >> loop("rock16", dur=16, drcomp=0.5)

n7 >> play("X.")
