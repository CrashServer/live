Clock.bpm = 78

e0 >> play("m ", dur=2, rate=(0.5, 1), bank=2, sample=P[0:80], mverb=0.5, chop=0, sbrk=0).unison(4)
a2 >> play("B", bank=2,sample=(P[0:10], PRand(852)), dur=4, mverb=0.5, hpf=40, leg=0.5)

v1 >> play("x", bank=2, sample=var([ [41, 45, 48, 24], P[1:100]]),rate=1, dur=1, lpf=0, amp=linvar([0.5, 1,1.5], PRand(16)[:4]), dist2=0.7)
a2.stop()

v1 >> play("v ", dur=var([2, 4, PDur(5, 8)]), bank=2, sample=PRand(1500), mverb=0.5, chop=0, shift=(0.5, 1)).unison(4).solo(0)
v1 >> play("B", bank=2,sample=(P[0:10], P[0:850]), dur=4, mverb=0.5, hpf=40, leg=0.5)

~v1 >> play("x", bank=2, sample=var([ [41, 45, 48, 24], P[1:100]]),rate=1, dur=1, lpf=0, amp=linvar([0.5, 0.7,1], PRand(16)[:4]), dist2=0.7)

~v1 >> play("v ", dur=var([2, 4, PDur(5, 8)]), bank=2, sample=P[0:70], mverb=0.5, chop=0, shift=(0.5, 1)).unison(4)

v2 >> play("v ", bank=2, dur=2, sample=14, amp=2)
v3 >> play("v ", bank=2, sample=PRand(128), dur=1/2, rate=(0.5,1,2), echo=0.5)


v_all.feed=0.5
v_all.hpf=400
e0.stop()
a2.stop()

v_all.hpr=.8
v_all.hpf=400

v3.rate=0.25
v2.rate=0.5

masterAll(0, "lofi", 1)
k1 >> loop("rageambi32", dur=32, a=2, amp=0.5, sample=1, mverb=0.5)
x1 >> loop("rytm64", dur=32)

k4 >> loop("long64", dur=64, amp=1, sample=2)
masterAll(0,"rate", 0.25)
masterAll(0,"hpf", 1600)

v2 >> loop("dnbfx16", dur=16, amp=0.5, sample=1)
v4 >> loop("dnbfx16", dur=(16, 32, 64), delay=16, amp=0.5, sample=1)


masterAll("rate", 0.25)
masterAll("hpf", 1600)


v1 >> play(".C..", rate=0.5, hpf=400)
l1 >> loop("ragedrum32", dur=32, sample=4, amp=1)
e1 >> play("[--]", bank=3, hpf=12000)
v1 >> loop("indus32", dur=32, sample=PRand(17))


masterAll("cut", 1/2)

v_all.solo(1)
v_all.solo(0)

masterAll(0,"cut", 1/2)


x4 >> loop("xxsbass16",dur=16, lpf=400, amp=0.5, sample=1, lpr=0.2)
x5 >> loop("xxsbass16",dur=16, lpf=800, amp=0.5, sample=1, lpr=0.1)

v2 >> loop("xbassphase16", dur=16).stop()

v3.stop()

v_all.only()
k_all.only()
v0 >> play("c ", bank=2, sample=PRand(8), dur=1/4, lpf=400, lpr=0.1, leg=4)
k4.stop()


x1 >> play("x ", bank=3)
v2 >> play("c ", dur=2)
v3 >> play("o", bank=2, dur=2, rate=1, echo=0)
v1 >> play("v", dur=2, bank=2, sample=4)

v2 >> play("L ", bank=3, dur=2, hpf=400)

~v3 >> play("X", bank=3, sample=4, amp=0.2)
v2.amp=0.5

v3.every(4, "stutter", sample=12, degree="O")

k1 >> plaitsX(oct=7, dist2=1).unison(4)

l1 >> loop("gbuild16", dur=16, sample=3)

l2 >> play("Oxo.", sample=4)

masterAll(0, "lpf", 200)


v3.solo(1)
c1 >> cluster(dur=4, hpf=400, hpr=0.1)

i1 >> ikea(dur=1, hh=20)








