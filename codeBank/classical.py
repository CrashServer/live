#classicshit
Clock.bpm = 78

e0 >> play("m ", dur=2, rate=(0.5, 1), bank=2, sample=P[0:80], mverb=0.5, chop=0, sbrk=0, pan=PWhite(-1, 1)).unison(4)
a2 >> play("B", bank=2,sample=(P[0:10], PRand(852)), dur=4, mverb=0.5, hpf=40, leg=0.5)
v1 >> play("x", bank=2, sample=var([ [41, 45, 48, 24], P[1:100]]),rate=1, dur=1, lpf=0, amp=linvar([0.5, 1,1.5], PRand(16)[:4]), dist2=0.7)
a2.stop()

v1 >> play("v ", dur=var([2, 4, PDur(5, 8)]), bank=2, sample=PRand(1500), mverb=0.5, chop=0, shift=(0.5, 1)).unison(4).solo(0)
v1 >> play("B", bank=2,sample=(P[0:10], P[0:850]), dur=4, mverb=0.5, hpf=40, leg=0.5)

~v1 >> play("x", bank=2, sample=var([ [41, 45, 48, 24], P[1:100]]),rate=1, dur=1, lpf=0, amp=linvar([0.5, 0.7,1], PRand(16)[:4]), dist2=0.7)

~v1 >> play("v ", dur=var([2, 4, PDur(5, 8)]), bank=2, sample=P[0:70], mverb=0.5, chop=0, shift=(0.5, 1)).unison(4)

v2 >> play("v ", bank=2, dur=2, sample=14, amp=2)
v3 >> play("v ", bank=2, sample=PRand(128), dur=1/2, rate=(0.5,1,2), echo=0.5)

k1 >> loop("rageambi32", dur=32, a=2, amp=0.5, sample=1, mverb=0.5)


v_all.sample=PRand(125)
v_all.dur=4
v_all.echo=0.5
v_all.rate=0.3
e_all.rate=0.3


v_all.feed=0.5
v_all.hpf=400
e0.stop()
a2.stop()
