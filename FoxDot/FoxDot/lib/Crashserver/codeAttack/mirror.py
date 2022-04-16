# mirror
p1 >> pianovel([11,11,9, 6,6,4, 9,9,2, 1,1,-1], dur=P[4,2,2], echo=1, echotime=1.5, velocity=PRand(48,68), echomix=0.5, mverb=0.5).gtr(6)
p2 >> varsaw((var([-11,-9,0,-4],16),6,6,p1.degree),oct=(3,4,5,6), sus=10, blur=2, shape=PWhite(0.0,0.1), dur=8, lpf=PRand(400,1200), lpr=PWhite(0.2,0.5), amp=0.6).unison(18,0.25).gtr(1)