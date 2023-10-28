# H1
Scale.default = "minorPentatonic"
Root.default=4
Clock.bpm = 120;
a1 >> sos(dur=8, lpf=linvar([60,4800],[PRand(8,64), PRand(8,64)]), hpf=expvar([0,200],[PRand(8,64), PRand(8,64)]), fx1=1, vib=PWhite(0,16), vol=0.3).unison(3,0.5,90)
a2 >> ews(PTrir(0,8), dur=2, sus=2, squiz=0.8, rel=0.2, fx2=1, oct=PWhite(2,3), amp=0.8, vol=1)
a3 >> ews([2, (3, 5), (2, 3), [(3, 5), (5, 8)]], dur=2, sus=2, squiz=0.8, rel=0.2, oct=2, fx2=1, amp=1).sometimes("degree.shuffle")
a4 >> ews(linvar([2, 3.1], 4), dur=6, sus=6, rel=0.2, oct=2, amp=1, formant=1, fx2=1).unison(2)
a5 >> play("{{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{n[yyyN][xxxx]}} ", dur=PRand([1/2, 1/4]), sample=PRand(128), pan=PWhite(-1,1), lpf=PWhite(800, 8000), fx2=1, rate=PwRand([[-1, 0.2, 0.5, 1, 2],linvar([1, 4], 8),linvar([4, 1], 8),linvar([0.25, 4],8)],[16, 8, 4, 4]), echotime=PRand([0, 1, 2, 3, 4]),echo=PRand([0.25, 0, 0, 1, 2, 0.125, 0]), hpf=PWhite(40, 2000), amp=var([0, PWhite(0.0, 0.4)], [PRand([8, 16]), PRand([2, 4, 6])]))

