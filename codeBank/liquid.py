# Liquid 174

Clock.bpm = 174

## messy jam session
d1 >> play("x..x.x..x...x.x.", sample=var([0, 3, 8], [16, 8, 8]), amp=var([1.2, 1.4, 1.1], [8, 4, 4]), rate=var([1, 0.95, 1.05], [12, 2, 2]))
d2 >> play("....b.....s.....", sample=var([12, 18, 25], [8, 4, 4]), amp=var([0.9, 1.1, 0.8], [6, 5, 5]), chop=var([0, 2, 4], [12, 2, 2]), rate=var([1, 1.1, 0.9], [8, 4, 4]))
d3 >> play("..s...s.s.s...s.", sample=var([15, 20, 30], [8, 4, 4]), amp=var([0.4, 0.6, 0.3], [4, 6, 6]), dur=1/2, hpf=var([0, 6000], [7, 1]), pan=var([(-0.5, 0.5), 0], [8, 8]))
d4 >> play("h.h.h.h.h.h.h.h.", sample=var([1, 1, 2], [6, 5, 5]), amp=var([0.5, 0.7, 0.4], [4, 4, 8]), dur=1/2, hpf=4000, pan=var([(-0.3, 0.3), 0], [4, 12])).after(8, "stop")
d5 >> play("c...............c...............", sample=var([5, 8, 12], [8, 4, 4]), amp=1.0, dur=1, mverb=0.6, pan=var([(-0.8, 0.8), 0], [16, 16]))
d6 >> play("....r.......r...", sample=var([18, 22, 28], [8, 4, 4]), amp=0.6, dur=1, hpf=4000, echo=var([0, 0.125], [7, 1]), pan=0.6)
d2 >> play("bb..s......bb..ss...sb", rate=PWhite(1, 1.04), dist2=PWhite(0, 0.8))

d7 >> play("........u.......u.......+.......+.......", sample=var([25, 30, 35], [6, 5, 5]), dur=var([1, 1/2], [12, 4]), amp=var([0.7, 0.9], [8, 8]), lpf=var([0, 5000], [15, 1]))
b1 >> dbass(var([0, -12, -5, -7], 4), dur=var([1/2, 1/4, 3/4], [8, 4, 4]), oct=6, amp=var([1.2, 1.5, 1.0], [4, 6, 6]), lpf=var([200, 400], [8, 8]), slide=var([0, 1], [25, 1]), dist2=0.5).unison(4)
p1 >> ethpad(var([0, 4, 7, 5], [8, 8, 8, 8]), dur=8, oct=(6, 4), amp=0.5, mverb=0.8, lpf=var([2000, 3000], [16, 16]), attack=2, decay=4, pan=var([(-0.6, 0.6)], [32]))
l4 >> loop("break32", dur=32).lclip(4)

d1 >> play("x..x..x.", sample=0, amp=1.2)
d2 >> play("..s...s.", sample=1, amp=0.9)
d3 >> play("-.--.--.", sample=2, hpf=8000)

d1 >> play("x..x.x..", sample=3, amp=1.1)
d2 >> play("..:.:..:", sample=4, amp=0.9, rate=1.1)
d3 >> play("--.--.--", sample=5, pan=PWhite(-0.5, 0.5))

b1.dur=1/2

d2 >> play("..s...s.", sample=10, amp=0.6, lpf=2000)
d3 >> play("-.-.-.--", sample=11, rate=(0.9, 1.1))
d1 >> play("x..x...x", sample=12, amp=1.2)

d2 >> play("....s...", sample=13, dur=2, amp=1.2, rate=-1.1)
d3 >> play("-.--.-.-", sample=14, dur=1/2, hpf=6000)
d1 >> play("x.", sample=9, amp=1.0)

b1 >> war(var([0, -12, -5, -7], [4, 4, 4, 4]), dur=var([1/2, 1/4, 3/4], [8, 4, 4]), oct=7, amp=var([1.2, 1.5, 1.0], [4, 6, 6]), lpf=var([200, 400], [8, 8]), slide=var([0, 1], [15, 1]), dist2=0.5).unison(4)
l4 >> loop("break4", dur=4,pos=0, room=0.1, ratelfo=0, ratelfoadd=0.5, ratelfomul=0.5, sample=0, beat_stretch=1, looping=1.0, clip=0)
b1 >> ikea()
p1 >> cluster(dur=8, oct=2)
b6 >> play("b ", sample=1, dur=2)

d_all.stop()
