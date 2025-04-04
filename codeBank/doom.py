# doom
Clock.bpm = 170
g1 >> faim(P[-5,-5,7,-5, -5,5,-5,-5, 3,-5,-5,1, -5,-5,2,3, -5,-5,7,-5, -5, 5,-5,-5, 3,-5,-5, P(-5,1)], dur=P[1/2].stutter(27) | 2.5, lpf=[PRand(400,2280),0,0], lpr=PWhite(0.1,0.5), dist2=1, fx1=0, shape=0.3, vol=0.5).gtr(2)
g2 >> faim(Pvar([P[21,19,18,21, 24,22,21,18, 21,22,24,26, 24,22,21,18], P[26,22,19,22, 26,22,26,31, 26,22,26,22, 26,31,34,38]],32), dur=1/4, amp=var([0,1],[28,4]), dist2=1).gtr(2)
g3 >> superbass(var([0,P*[3,5,7,0]],[14,2]), oct=5, dur=1/2, lpf=1700, cutoff=4000, lpr=0.5, beef=2).gtr(1)
g5 >> pluck(var([0,P*[3,5,7,0]],[14,2]), oct=3, dur=1/2, lpf=1700, cutoff=4000, lpr=0.4).gtr(1)
g4 >> play("<k(.k)u.><->", sample=(9,5), amp=2).human(40,0).every(14, "stutter", 8, cycle=16, degree="u", amp=PWhite(0.3,1))
