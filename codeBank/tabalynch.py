#tabalynch
Scale.default="minor"
Root.defaul = 4
Clock.bpm=108
v4 >> noloop("lynchvoice8", dur=16, sample=6, comp=1, fx2=0, trig=0, sus=16, amp=1)
f8 >> play("<x.><.><....>", sample=0, amp=3).sometimes("stutter")
e4 >> play("...(...z)", sample=2)
c1 >> click(0, dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), hpf=linvar([40, 400], 128), drive=[PWhite(0.4,0.8),0.2], oct=(PwRand([3, 4, 5], [8, 1, 1]), PStep(9,5,4)), octer=1, mverb=0, leg=0,  octersub=2, octersubsub=var([2, PRand(15,22)], [15, 1]), triode=4, amp=0.5, amplify=1).unison(3).rarely("stutter",PRand(6), oct=6, pan=[-1,1], mpf=2860, hpf=400).gtr(1)
c1 >> plaitsX(0,dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), preset=P*[2,11], mverb=0.5, leg=4, hpf=P*[4000, 800])

g0 >> tb303(0, dur=1/4, cut=1/2, amp=PBin(), cutoff=var([200, 3200, 4000, 8000], [8, 12, 4, 8]), top=PRand(1200)[:8], rq=0.1, dec=var([-0.9, 0.2, 0.5, 12], [4]))
g1 >> tb303(0, dur=var([1/2, 1/4], [4, 8]), cut=1/2, amp=1, oct=var([4, 5], [24, 8]), dist2=0, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:16], rq=[0.3, 0.3, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))
g2 >> superbass(var([([7, 0], 0), [(12, 0), ([6, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2], leg=linvar([0, 4], 32), scale=Scale.chromatic, drive=PWhite(0.0, 0.1), hpf=50, hpr=(0.1, 0.9))

u6 >> loop("lynchcrazy16", dur=16, sample=4) # stone electro
c5 >> loop("jazzguitar8", dur=8) # edgy/touchy
c7 >> play("<k.><..><..u.>", sample=0, amp=2, drcomp=.51, lpf=0).sometimes("stutter")
