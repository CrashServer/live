# H3
Clock.bpm = 120;
Root.default = 4
y0 >> subbass([2,3,[5,7]], dur=16, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=0.2, atk=PWhite(0.005,0.1), oct=(4,5), lpf=4000).unison(4)
y1 >> klank(y0.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 4), dur=P*[4, 8, 12], lpf=linvar([400,3800],128), lpr=0.1, amp=linvar([0.5, 0.7], 128), hpf=600, bpm = 80 + PWhite(-20, 20), fdist=1, fdistfreq=PWhite(1200, 2000)).unison(2)
y2 >> total(y0.degree[0],dur=32, chop=PRand([0, 0.5, 1, 0.35]), amp=[1,PWhite(0,1)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1), drive=0.01).slider().unison(2)
y3 >> jbass(var([PWalk(8, 1, 4),PWalk(15, [1, 4], 1)], [4, 4]) , dur=[15, 1/4, 1/4, 1/4, 1/4], sus=[2, 1/4, 1/4, 1/4, 1/4], oct=PStep(7, [3,5], 6), echo=P*[2, 1, 1, 1, 1], amp=0.5, rate=0.1, fx2=1, fx1=1, crush=P*[0,8]).unison(2).slider(0,PStep(8,1,0))
y3 >> bass(y0.degree[0], leg=0.2, oct=(4,6), dur=[15,1], amp=0.4, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6)
y4 >> ebass([ PWhite(-0.1, 0.1),PWhite(5, 3) ], slide=16, dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), spfslide=16, spfend=1600, spf=1).unison(4)
y5 >> pianovel(P*[y0.degree[0],y0.degree[1],y0.degree[2], (y0.degree[0], y4.degree[1]), (y0.degree[1], y0.degree[2]), (y0.degree[0], y0.degree[2]),P**(y0.degree[0], y0.degree[1], y0.degree[2]),P+(y0.degree[0], y0.degree[1], y0.degree[2]), P/(y0.degree[0], y0.degree[1], y0.degree[2])], dur=P*[5,1,1/2,8,3], sus = p1.dur, delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.2, 0.6), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000)).unison(3).penta()
y6 >> pasha(var([y4.degree, y0.degree, y0.degree + 5], [3, 5]), cut=var([0, 1/4], [8, 8]), oct=(3,6), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=var([0,0.1],PRand(4,16).rnd(2)), sus=y0.dur*PWhite(0.1,0.01), echo=var([0.5,[0.125,0.25,0.75]],[6,2]), pan=y4.dur*P[1,-1], lofi=expvar([0.1,1],[PRand(19),PRand(8)])) + var([0, var([0,PTrir(0,2,0)],[6,2])], [2, 8])
y7 >> zap(0, dur=8, hpf=40, drive=[PWhite(0.1,0.2),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,2)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.7).unison(4)
y8 >> sawbass(0, dur=8, sus=[8], echo=1/2, amp=(y7.amp==0), mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01), vol=0.6).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))
