# H2 120
# interlude
Clock.bpm = 120;
Scale.default = "minorPentatonic"
Root.default=4
a6 >> ebass(PWhite(-0.1, 0.1),dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), fx1=0, spfslide=16, spfend=1600, spf=1).unison(4)
a7 >> radio(dur=32, hpf=PWhite(1000, 2000), formant=PWhite(1, 2), amp=PMorse("kakaaop"), fx2=1)
a8 >> ews(PTrir(0,8), dur=2, sus=4, squiz=0, vib=PWhite(0,32), fmod=PWhite(0,4), hpf=80, rel=0.8, oct=PWhite(2,3), amp=0.5, vol=0.2, cutoff=PRand(400,3800), spin=PWhite(-2,2))
a9 >> play("W ", dur=4, feed=linvar([0.1, 0.5],16), rate=var([1, -1], [7, 1]))
a7.stop()
a9 >> play("W ", dur=4, delay=1, feed=linvar([0.1, 0.5],16), shape=0.1,rate=var([1, -1], [7, 1]))
a1 >> play("W ", dur=4, delay=3, feed=linvar([0.1, 0.5],16), shape=0.4, rate=var([ PWhite(1.5, 2.5), -1], [7, 1]),hpf=200, hpr=PWhite(0.1, 0.5))
a2 >> play("W ", dur=4, delay=4, feed=linvar([0.1, 0.5],16), shape=0.6, rate=var([r2.degree, -1], [7, 1]), formant=P*[0,1], echotime=4, echo=1, echomix=PRand([0.25, 0, 0, 0, 0.5]), hpf=200, hpr=PRand([0.1,  0.2]))
a3 >> play("d ", dur=4, delay=4, hpf=1600, echo=0.25, echotime=2, feed=0.5, amp=PRand([0, 1]), chop=4)

a_all.dur=8
a_all.rate=[2,4,8]
a_all.cut=1/2
a_all.hpr=0.1
a_all.vol=0.5
a_all.rate=var([-2, 1])
Root.default = var([4.02, 4.0, 4.12])
