# NotFTL 1024
# trance, chaosbits
Clock.bpm=1024

w4 >> play("x", valad=PFr(500,800,1664, 128), amp=PStep(16, 0, 1), rate=PWhite(0.98, 1.02), valadr=PWhite(.1, 0.9), valadd=5, valadt=0, valadc=0.2, mverb=.2, wshape=linvar([0, 12],[333,222]), hpf=120)

g3 >> play("X", sample=0, dur=var([8, PRand(1,8)], [120,12]), amp=3, lpf=0)
e5 >> play("l", bank=1, sample=2, dur=[8, 4, 2, 1,1/2,1/2],  hpf=linvar([50,600],[147,33]), cut=PFr(0.5, 2), valad=linvar([400,4000],256), valadr=linvar([.2, 0.9], [356, 156]), valadd=15, valadt=0, valadc=0.2)
w5 >> play("-", pan=PWhite(-1,1), cut=1, rate=PWhite(1,1.04), amp=1, dur=var([1/2, 8], 4)).human(40)
s3 >> play(":", sample=9, amp=PStep(32, 4,0), rate=(-.5,.5), mverb=.7, eb=0.25, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=150, ebsat=0.3)

e3 >> hoover((linvar([0, 7], [128,0]),linvar([7,0], [128,0])),leg=0.0, dur=1/2, oct=PStep(16,6,5), mverb=.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.8, fbcutoff=3000, fbspread=0.2, beat_dur=.5, formant=PRand(5), amp=var([0.6,0],16), ).unison(2)

m2 >> rsin(rate=0.1, para1=4, rsing=7,dur=8, valad=var([900,PRand(2000,8000)], 32), valadr=0.1, valadd=100, valadt=0, valadc=0.2, octafuz=2, octamix=0.5)

Server.addFx(lpf=0, hpf=0, mverb=0,glitch=0.7, glitchrate=6, glitchdepth=0.9, glitchcrush=0.7, glitchchance=0.8, beat_dur=1)

u2 >> loop("breakcore160_16", dur=128, drcomp=.5, sample=var(PRand(808), [256]), amp=2, hpf=300)

u2.stop()
Clock.bpm=linbpm(40, 512)
