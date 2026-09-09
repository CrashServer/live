# dive the dice - 92
# intro, superxstatic

Clock.bpm=92
Scale.default="minor"
Root.default=1

x8 >> lfnoise(rate=PWhite(0,1), cutoff=PRand(400, 4800), rq=0.8, vol=.2, dur=8, blur=2, mverb=.2)

o8 >> faim([var([0, -1, -2],8), var([7, 9], 13), var([9, 8, 7, 5],6)], dur=P[1/2,1/2].exp(2), beef=2,  wshape=0, wgain=1, wmix=0.5, mverb=0.7, oct=(5,PStep(9, 7,6)), vol=.8, resonz=0.8, rfreq=410).unison(3)

c1 >> dafbass(dur=PDur(var([1, 4,3,4,5,7],[1, 1, 1, .5]), 16), oct=(4,5), rate=P*[1,2] , valad=linvar([500,4000], [64]), valadr=linvar([.1, .9], [55]), valadd=PStep(16, PWhite(5, 55), 5), valadt=0, valadc=0.2,).unison(3)
o8.resonz=0

x5 >> play("-", dur=PDur(var([1, 4,3,9, 4,5,7],P*[1, 1, .5, 1/4, 1/8]), 8, 1), amp=1, rate=1/x5.dur, mverb=.2)

e7 >> play("x.", sample=3, fbdelay=expvar([0.1, .99], [64,0]), fbtime=0.25, fbfeed=0.8, fbcutoff=linvar([2000, 12000],[64,0]), fbspread=0.02, beat_dur=1, hpf=expvar([0, 0, 400],[32, 32, 0]) )
c1.hpf=var([140, 0],[.25])

a0 >> play(".(...{..c})c.", rate=[1, -.9,1, 1], sample=4, delay=[0, 0, PStep(PRand(2,8), PWhite(.01, .06),0), 0], mverb=0.2, mverbmix=0.2, mverbdamp=0.2, mverbdiff=0.625, hpf=400 )

## More creepy
o8 >> faim([var([0, -1, -2],8), var([7, 9], 13), var([9, 8, 7, 5],6)], dur=P[1/2,1/2].exp(1), beef=2,  wshape=3, wgain=1, wmix=0.5, mverb=0.7, oct=(5,PStep(9, 7,6)), vol=0.6).unison(3)
o8 >> faim([var([0, -1, -2],8), var([7, 9], 13), var([9, 8, 7, 5],6)], dur=P[1/2,1/2].exp(1), beef=PFr(-1,2),  wshape=3, wgain=1.5, wmix=0.5, mverb=0.7, oct=(5,PStep(9, 7,6)), vol=0.6).unison(3)
x2 >> play("X.", sample=0, amp=2)

d6 >> play("G", dur=PRand(4,8), sample=PRand(808), wshape=3, wgain=2, wmix=0.5, rate=1, mverb=.2, sbrk=PRand([0, PWhite(0, 2)]), t_reset=0, sbrkdur=PWhite(0, 2), sbrkmix=1.0, hpf=400, crunch=0.6).unison(3)
o8 >> svdk([var([0, -1, -2],8), var([7, 9], 13), var([9, 8, 7, 5],6)], dur=P[1/2,1/2].exp(2),  wshape=0, wgain=1, wmix=0.5, mverb=0.7, oct=(5,PStep(9, 7,6)), vol=0.3, r=0).unison(3).trim(0)

Clock.bpm=linbpm(132, 32)
o8 >> svdk([var([0, -1, -2],8), var([7, 9], 13), var([9, 8, 7, 5],6)], dur=P[1/2,1/2].exp(4),  wshape=0, wgain=1, wmix=0.5, mverb=0.7, oct=(5,PStep(9, 7,6)), vol=0.3, r=1.0).unison(3).trim(2)

l0 >> loop("breakcore160_16", dur=var([16, 8],[48, 16]), sample=5, crunch=.8,  sbrk=0, t_reset=0, sbrkdur=0.5, sbrkmix=1.0)

## Possible sortie plus calme (mais à voir, pas au point encore)
c1.stop()
x5.stop()
e7.stop()
a0.stop()
x2.stop()
o8.stop()
y9 >> play("8", dur=[1, 1.75], wshape=PWhite(0, 8), wgain=1, wmix=0.5, idist=PWhite(.1, .5))

g7 >> play("-", dur=PStep(11, .25, .5), sample=2, rate=PTrir(.5, 2.0)).sometimes("stutter", PRand(6))
l0.stop()

e4 >> play("r", dur=PDur(2,11), sample=6, clouds=(0.0, 0.8), cpos=PWhite(0.1, .7), csize=0.5, cdens=0.5, ctex=0.3, cpitch=6, cgain=2, cfb=0.6, cmode=2)
o2 >> wavetable("WT_Analog", oct=4, dur=P[.5, 0.25, .75, 1].exp(var(P*[8,4,2],8)), rate=0, degree=[0, 0, 2, 1, -2], sample=8,detune=0.4, wtpos=0, cutoff=5800, rq=0.8, wtdist=0.3, wshape=4, wgain=1, wmix=0.5, r=0.7, tanh=.2)

z8 >> play("x.", sample=3)
