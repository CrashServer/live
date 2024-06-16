# tabamix
Clock.link()
Root.default="E"
Scale.default="minor"
Master().reset()
Clock.bpm = 135;

c1 >> plaitsX(0,dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), preset=P*[2,11], mverb=0.5, leg=4, hpf=P*[4000, 800])

c1 >> click(0, dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), hpf=linvar([40, 400], 128), drive=[PWhite(0.4,0.8),0.2], oct=(PwRand([3, 4, 5], [8, 1, 1]), PStep(9,5,4)), octer=1, mverb=0, leg=0,  octersub=2, octersubsub=var([2, PRand(15,2222)], [15, 1]), triode=4, amp=0.3, amplify=1).unison(3).rarely("stutter",PRand(6), oct=6, pan=[-1,1], mpf=2860, hpf=400).gtr(1)
c1.oct=var([1, 2, 0])
c1.unison(1)

c1 >> varsaw(linvar([-5, 4, 8, -12, 12],[4, 2, 1, 8]),oct=5, dur=1/8, amp=0.1).unison(4).slider().solo(-8)

c2 >> play("x", sample=4, dur=[1,c1.dur], hpf=40, drive=[PWhite(0.4,0.8),0.2], triode=4, amp=0.5, amplify=1).unison(3).rarely("stutter",PRand(6), pan=[-1,1], mpf=2860, hpf=400).sometimes("stutter", degree="V ")

c1 >> faim(dist2=0.1, dist2_=1, cut=1/2)
c3 >> bass(0, dur=c1.dur, leg=12, amp=var([0.5, 0], [12, 4]), rate=PWhite(0.01, 0.2), sus=c1.dur*1.5).unison(2)

d4 >> play("<u><t>", amp=1, sample=(2,P[0:5]), delay=(0,(0,[0,0.25])), dur=c1.dur*2, crush=[0,0,0,PRand(8)], bits=4, lpf=c1.crush*1500)

p1 >> play("PTptpPTtp", amp=1, sample=0)

c2.dur=1

a1 >> play("-.--[--]-(.-){:.}", dist2=PwRand([0, 1], [15, 1]), fold=(1, 0), dur=(1/2, 1), sample=(4,2), hpf=(10000, linvar([200, 4000])), tanh=a1.dist2, mverb=a1.dist2, echo=a1.dist2, rate=(a1.dist2 + 1))

g0 >> tb303(0, dur=1/4, cut=1/2, amp=PBin(), cutoff=var([200, 3200, 4000, 8000], [8, 12, 4, 8]), top=PRand(1200)[:8], rq=0.1, dec=var([0.1, 0.2, 0.5, 12], [4]))

g1 >> tb303(0, dur=var([1/2, 1/4], [4, 8]), cut=1/2, amp=1, oct=var([4, 5], [24, 8]), dist2=0, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:16], rq=[0.3, 0.3, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

g2 >> abass(var([([7, 0], 0), [(12, 0), ([6, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2], leg=linvar([0, 4], 32), scale=Scale.chromatic, drive=PWhite(0.0, 0.1), hpf=50, hpr=(0.1, 0.9))


