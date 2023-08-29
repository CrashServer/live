Clock.bpm = 135;

d7 >> loop("hiphop16", dur=16)
d6 >> play("C:.Cc.", sample=(5, 4), lpf=(1200, 4000), hpf=1200).sometimes("stutter")
d0 >> play("<X ><O.><-.>", dur=8, sample=4, echo=2).rarely("stutter", 4, fold=1)

d7 >> loop("nsbass16", dur=16, sample=1, hpf=400)
d1 >> loop("hiphop16", dur=16, sample=2)

d0.sample=4
d6.sample=1
d0.hpf=1700
d6.hpf=3200

d2 >> loop("hiphop16", dur=16, sample=4, hpr=0.9, hpf=1200)
d2.sample=3
d2.hpf=0

d7.sample=2
d1.sample=4

d7 >> loop("nsbass16", dur=16, sample=1, hpf=400, echo=4, mverb=0.5)
d7.shift=1
d7.chop=32
d7.chopmix=0.2

d7.shift=0
d9 >> loop("psych32", dur=32, sample=2, lpf=4000, mverb=0.5)
d0.hpf=0
d0.echo=(1, 2.25)

d0.dur=2
d9 >> play("X[::]", amp=1, sample=4)
d8 >> loop("psych32", dur=32, sample=3, lpf=4000)

d7 >> loop("core16", dur=16, sample=3, hpf=200)
d1 >> play("..U.")
d2 >> play("XK.V.", dist2=1)
d3 >> play("[--]", amp=4)

d9 >> loop("gab16_10sec_180", dur=32, sample=1, hpf=400)
d8 >> loop("ravebass8", dur=8, sample=5, drive=0.0, amp=1, hpf=4000)
d7.stop()
d8.stop()

k4 >> play("V ", amp=4)


d0.dur=2
d8.stop()
d9.stop()
d0.dur=1/2
d3.sample=1
d2.sample=2
d1.sample=0
d4 >> play(".cC.",dur=1/2, dist2=1)

d6 >> play("X ", amp=2)
d5 >> dbass((0, 2, var([4, 6], [8]))).unison(4)
d9.hpf=400


d0.dist2=0
d1.echo=0
d1.lpf=linvar([200, 1200], 32)
d6.dur=4


d1>> dbass()
d8 >> dbass(dur=1/2, oct=3)




