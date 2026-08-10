# dive the dice - 92
Clock.bpm=92
Scale.default="mixolydian"

c1 >> dafbass(dur=PDur(var([1, 4,3,4,5,7],[1, 1, 1, .5]), 16), oct=(4,5), rate=P*[1,2] , valad=linvar([500,4000], [64]), valadr=linvar([.1, .9], [55]), valadd=PStep(16, PWhite(5, 55), 5), valadt=0, valadc=0.2,).unison(3)

x5 >> play("-", dur=PDur(var([1, 4,3,9, 4,5,7],P*[1, 1, .5, 1/4, 1/8]), 8, 1), amp=1, rate=1/x5.dur, cheapverb=0.2, cvdecay=1.5, cvdamp=0.5)

e7 >> play("x.", sample=3, fbdelay=expvar([0.1, .99], [64,0]), fbtime=0.25, fbfeed=0.8, fbcutoff=linvar([2000, 12000],[64,0]), fbspread=0.02, beat_dur=1, hpf=expvar([0, 0, 400],[32, 32, 0]) )
c1.hpf=var([140, 0],[.25])

a0 >> play(".(...{..c})c.", rate=[1, -.9,1, 1], sample=4, delay=[0, 0, PStep(PRand(2,8), PWhite(.01, .06),0), 0], mverb=0.2, mverbmix=0.2, mverbdamp=0.2, mverbdiff=0.625, mverbfreeze=0, hpf=400 )

n0 >> plaitsX([PTrir(-12, 7), PTrir(-3,3), PTrir(-7,7)], amp=[0, PCoin(), 1,1], dur=1/4, oct=P*[5,6], cutoff=7800, rq=0.1, trigger=0, bright=0.8, preset=10, porta=0.1, harm=0, timbre=0, morph=0, aux=1, fdecay=PFr(1,3), cheapverb=0.1, cvdecay=1.5, cvdamp=0.5)
