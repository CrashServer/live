
# Server.addFx(jpverb=.4, jpvermix=0.5)

# Server.addFx(echo=0.025)


Clock.

soloRnd()
a4 >> blip(0, dur=8, oct=5, sus=8, wshape=0, fx1=0, slide=PRand(1, 12), slidedelay=PWhite(0.3,0.7)).unison(4, .5)
y1 >> plaitsX([0,[P+[7,5], P+[1,2,PRand(8),7]]], preset=(11,12), dur=16, oct=(2,3,PStep(5,5,4)), dfm=PRand(900,5200)*1, dfmd=1, tremolo=PStep(8,4,0), tremolo_=0.5, dfmr=0.79, fdecay=1, mverb=0.8, amp=1, fx2=0.5)
p1 >> plaits(P[0,5,6,10], dur=1/4, oct=(3,5), harm=0.7, timbre=0.8, morph=0.94, engine=2, fdecay=1.8, cutoff=9000, bright=PFr(0.9,0.99), aux=0, porta=0.09, dist2=0.5) + var([0,7],11)
p2 >> plaits(P[-2,4,6,7], dur=1/2, oct=(3,5), harm=0.7, timbre=0.8, morph=0.24, engine=1, fdecay=1.8, cutoff=9000, bright=PFr(0.9,0.99), aux=0, porta=0.09, dist2=0.4) + var([0,[PWalk(8, 1, 1)]],7)
# p3 >> a_daftlead(4, dur=1/2, oct=3, harm=0.0, timbre=0.6, morph=0.94, engine=1, fdecay=1.8, cutoff=9000, bright=PFr(0.9,0.99), aux=0, porta=0.09, dist2=0.5) + var([0,7],11)


i0 >> bellmod(PWhite(-4,4), mverb=.8, dur=PWhite(1/4, 1/8), lag = 10, s1=1, s2=PWhite(0,.3), s3=PWhite(0,.3), pong=0.25, beat_dur=1, pongtime=2).end(16,PRand(0,4))

p6 >> loop("junglecool16", dur=16, sample=PRand(909), sbrk=P*[0, PWhite(.2, 2)])