# postGabber
Scale.default="minor"
Clock.bpm=163
l8 >> plaitsX([var([0,3,5], 8),7,14,[15,17]], shape=.3, dur=1/2, lpf=PFr(400,1800), preset=(3,12), oct=(4,5,6)).gtr()
a1 >> lbass(var([0,3,5], 8), dur=1/2, cutoff=PFr(400,3200)).gtr()
j5 >> loop("gbreak16", dur=16, sbrk=[0,.5], sbrkdur=.5, comp=0)
g2 >> play("x.", sample=4, lpf=PFr(400,2000), lpr=var([.5,.1],[6,2,5,1]), bank=1, vol=.6, hpf=0)
t2 >> loop("gscreecha16", dur=32, mverb=.2, sample=PRand(88))
