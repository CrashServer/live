# gta
Root.default = "C"
Clock.bpm=144
Scale.default="dorian"

t1 >> mpluck([[0, 1, 2, 1, 0, 1 ,0, -1],-3], mverb=lininf(0,0.8,32), amp=0.5, oct=(PStep(8, 5, 6), 5, 7), pan=PWhite(-1,1), cut=1/2, dur=2, delay=0, hpf=400).unison(4)
t2 >> pianovel([[0, 1, 2, 1, 0, 1 ,0, -1],-3], dur=1/2, velocity=PRand(40,60), hpf=100, velhard=0.2, amp=PGauss(0.4, 0.1), oct=PStep(7,6,5), rate=linvar([0.1,1.8],24), sus=PWhite(0.2,0.3)).unison(3).sometimes("stutter", oct=[6, 8], mverb=0).stop()
t3 >> pianovel(t2.degree + 5, oct=PStep(4, 5, [6, 7]),velhard=[PGauss(0.2, 0.2), 0], hpf=120, velocity=PRand(40,88), delay=var([0,(0.125, 0)], [5, 3]), amp=linvar([0.3, 0.6], [16]), mverb=0.1).accompany(p0).unison(4).human()

t4 >> ssaw([[0, 1, 2, 1, 0, 1 ,0, -1],-3], amp=0.3, hpf=linvar([200, 400]), hpr=0.39, dur=1/2, phase=0, sus=linvar([0.6, 1], 16)).unison(8)

t5 >> ssaw([0,2,P+(3,4),P+(6,7,8,14)], oct=(5.01, 3.99, 7), sawtype=P*[0,1], sawmix=0.5,  lpr=0.7, amp=(0.2, 0.1, 0.2), lpf=7800, dur=8).unison(8)
t6 >> ssaw([0,2,3,(4.5,7)], oct=(4,5), dur=8, lpf=800, slide=0.2, slidedelay=0.8, hpf=90).unison(3)

t7 >> bass([0,0,-1,7,7,-1], dur=[1/2,1/2,[rest(3)]], amp=1, oct=5, echo=0.25, sus=1)
t8 >> jbass(4, dur=1/2, amplify=var([0,1],[3.5,0.5]), amp=1, echo=0.5, oct=4)
t9 >> dbass(P[3, 4, 4.5, [4, 3]].stutter(2), dur=1/4, oct=(4,5), amplify=var([0, 1], [6, 2]))
t0 >> bass([(0, [7, 3]), (0, [4, -1])], drive=linvar([0, 1], 32), oct=P(3, [4, [5, 6]])+1, room2=0, dur=[1/2, 1/2, [rest(1)]]).unison(2)