# A2
Scale.default = "minorPentatonic"
Root.default=4
Clock.bpm = 120;

a1 >> sos(dur=8, lpf=linvar([60,4800],[PRand(8,64), PRand(8,64)]), hpf=expvar([0,200],[PRand(8,64), PRand(8,64)]), fx1=1, vib=PWhite(0,16), vol=0.3).unison(3,0.5,90)
a2 >> ews(PTrir(0,8), dur=2, sus=2, squiz=0.8, rel=0.2, fx2=1, oct=PWhite(2,3), amp=0.8, vol=1)
a3 >> ews([2, (3, 5), (2, 3), [(3, 5), (5, 8)]], dur=2, sus=2, squiz=0.8, rel=0.2, oct=2, fx2=1, amp=1).sometimes("degree.shuffle")
a4 >> ews(linvar([2, 3.1], 4), dur=6, sus=6, rel=0.2, oct=2, amp=1, formant=1, fx2=1).unison(2)
a5 >> play("{{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{n[yyyN][xxxx]}} ", dur=PRand([1/2, 1/4]), sample=PRand(128), pan=PWhite(-1,1), lpf=PWhite(800, 8000), fx2=1, rate=PwRand([[-1, 0.2, 0.5, 1, 2],linvar([1, 4], 8),linvar([4, 1], 8),linvar([0.25, 4],8)],[16, 8, 4, 4]), echotime=PRand([0, 1, 2, 3, 4]),echo=PRand([0.25, 0, 0, 1, 2, 0.125, 0]), hpf=PWhite(40, 2000), amp=var([0, PWhite(0.0, 0.4)], [PRand([8, 16]), PRand([2, 4, 6])]))
a6 >> ebass(PWhite(-0.1, 0.1),dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), fx1=0, spfslide=16, spfend=1600, spf=1).unison(4)
a7 >> radio(dur=32, hpf=PWhite(1000, 2000), formant=PWhite(1, 2), amp=PMorse("kakaaop"), fx2=1)
a8 >> ews(PTrir(0,8), dur=2, sus=4, squiz=0, vib=PWhite(0,32), fmod=PWhite(0,4), hpf=80, rel=0.8, oct=PWhite(2,3), amp=0.5, vol=0.2, cutoff=PRand(400,3800), spin=PWhite(-2,2))
a9 >> play("W ", dur=4, feed=linvar([0.1, 0.5],16), rate=var([1, -1], [7, 1]))
a7.stop()
a9 >> play("W ", dur=4, delay=1, feed=linvar([0.1, 0.5],16), shape=0.1,rate=var([1, -1], [7, 1]))
a1 >> play("W ", dur=4, delay=3, feed=linvar([0.1, 0.5],16), shape=0.4, rate=var([ PWhite(1.5, 2.5), -1], [7, 1]),hpf=200, hpr=PWhite(0.1, 0.5))
a2 >> play("W ", dur=4, delay=4, feed=linvar([0.1, 0.5],16), shape=0.6, rate=var([r2.degree, -1], [7, 1]), formant=P*[0,1], echotime=4, echo=1, echomix=PRand([0.25, 0, 0, 0, 0.5]), hpf=200, hpr=PRand([0.1,  0.2]))
a3 >> play("d ", dur=4, delay=4, hpf=1600, echo=0.25, echotime=2, feed=0.5, amp=PRand([0, 1]), chop=4)
a1.stop()
a_all.dur=8
a_all.rate=[2,4,8]
a_all.cut=1/2
a_all.hpr=0.05
a_all.vol=0.5
a_all.rate=var([-2, 1])
Root.default = var([4.02, 4.0, 4.12])
