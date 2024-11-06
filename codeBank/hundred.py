#gabbermayem
Clock.bpm = 150;
x1 >> play("W ", bank=var([1, 3], [24, [4, 2, 1, 1]]), lpf=1200, sample=6, lpr=[0.2, 0.4, 0.5, 0.1]).sometimes("stutter", 4)
x2 >> play("W ", bank=3, lpf=1200, dur=4, delay=0.5, sample=1, hpf=1600, echo=0.5, dafilter=0)
e3 >> play("W ", bank=3, dur=4, lpf=12000, mverb=0.5, hpf=400)
e4 >> play("[--].-[-.-]-.", bank=3, sample=8, rate=PWhite(1, 2))
e5 >> play("....O.o.", bank=3, sample=2)
e6 >> play("[--]", dur=PDur(3, 8),bank=3, sample=PRand(8), hpf=1000, rate=4, cut=1/9)
e7 >> play("w ", bank=3, sample=8, lpf=[400, 1200, 0, 0], hpf=var([0, 4000], [6, 2]))
x8 >> play("oo.:.", bank=3, amp=1, sample=4, hpf=100)
e9 >> loop("circlebreak16",dur=16, amp=4)

masterAll(0,"sample", var([1, 2], [3, 1]))
masterAll(0,"lpf", 1200)

masterAll(0,"rate", -4)
masterAll(0,"echo", 0.5)
masterAll(0,"a", 0.5)

h1 >> play("W ", bank=var([1, 3], [24, 8]), lpf=1200, sample=6)
h0 >> play("W ", bank=3, lpf=1200, dur=4, delay=0.5, sample=0, hpf=1600, echo=0.5, dafilter=0)
h2 >> play("W ", bank=3, dur=4, lpf=12000, mverb=0.5, hpf=400)
h3 >> play("[--]", bank=3, sample=8)
p3 >> play("....O.o.", bank=3, sample=2)
p4 >> play("[--]", dur=PDur(3, 8),bank=3, sample=PRand(8), hpf=1000, rate=2, cut=1/9)
x1 >> play("w ", bank=3, sample=8, lpf=[400, 1200, 0, 0], hpf=var([0, 4000], [6, 2]))
a2 >> play("oo.:.", bank=3, amp=1, sample=4, hpf=100)
masterAll(0,"sample", var([1, 2], [3, 1]))
masterAll("lpf", 400)
