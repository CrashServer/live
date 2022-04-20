# mmxx
Master().reset()
Clock.bpm=113
Root.default = 1
Scale.default= Pvar([Scale.major, Scale.justMajor],PRand([4, 8, 16,32]))

b1 >> varsaw((var([0,-2,-4],16),[1,2,1],var(PRand([5,6,2,4,7],8))), sus=10, lpf=linvar([3000, 6700], 128), lpr=PWhite(0.2,0.9), blur=2, amp=0.4, dur=var([5,1,1], [6,1,1]), oct=PStep(6,6,4), fx2=1, fx2hpf=300, fx2lpf=7800).unison(3) + var([0, 4, 8], [6, 1, 1])

b2 >> varsaw((var([0,-2,-4],16),[1,2,1],var(PRand([5,6,2,4,7],8))), sus=1, spfslide=1, spfend=6000, spf=10, lpf=6000, lpr=PWhite(0.2,0.9), blur=2, amp=0.3, dur=var([4, 1/4, 8], [2, 2, 1]), oct=PStep(4,5,3), fx2=1, fold=0.5,bpm = 80 + PWhite(-20, 20)).unison(4) + var(PRand([0, 4, 8, -4, 6, -3]), [6, 1, 1])

e1 >> klank(b1.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 5), dur=P*[4, 8, 12], lpf=linvar([400,4800],128), lpr=0.05, amp=0.5,bpm = 80 + PWhite(-20, 20))

e2 >> klank(b1.degree[1] + var([0, -2, -4, 6]), dur=1, rate=4, oct=var([(5, 6), (4, 7)], 4), lpf=linvar([400,4800],128), hpf=2000, drive=0.0,lpr=0.7, chop=8, chopmix=0.25, lofi=linvar([0.1, 0.5], 32), amp=1,bpm = 80 + PWhite(-20, 20)).unison(2)

p1 >> pianovel(P*[b1.degree[0],b1.degree[1],b4.degree[2], (b1.degree[0], b1.degree[1]), (b1.degree[1], b1.degree[2]), (b1.degree[0], b1.degree[2]),P**(b1.degree[0], b1.degree[1], b1.degree[2]),P+(b1.degree[0], b1.degree[1], b1.degree[2]), P/(b1.degree[0], b1.degree[1], b1.degree[2])], dur=P*[5,1,1/2,8,3], sus = p1.dur*PWhite(1,1.5), delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.6,0.8), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000)).unison(3).penta()

z1 >> total(b1.degree[0],dur=16, amp=[1,PWhite(0,0.5)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1)).slider()

y4 >> subbass(p1.degree, dur=16, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=1, atk=PWhite(0.005,0.1), oct=(4,5)).unison(3)
y5 >> faim(y4.degree[0], oct=(4,5), dur=[15,1], amp=0.5, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6)

g1 >> play("G", dur=PRand(32), crush=PRand(16), bits=PRand(4,16), sample=PRand(2020), amp=0.8)

Scale.default= Pvar([Scale.major, Scale.justMajor, Scale.minor, Scale.justMinor],PRand([4, 8, 16,32]))
Clock.bpm = sinvar([113, 40], 128)