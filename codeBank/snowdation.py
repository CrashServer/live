# snowdation 133
# interlude

Clock.bpm = 133;

a2 >> sine((0, 2), sinefb=linvar([0, 1.0], 128), amp=0.5, delay=0.5, oct=3, sus=2, hpf=200, pan=linvar([-1, 1], 128))
a4 >> sine((0, 2), sinefb=linvar([0, 0.5], 196), amp=0.3, delay=1, oct=3, sus=1, hpf=400, pan=linvar([1, -1], 128))
a1 >> play("U", dur=16, rate=[0.9, 1.1], sample=PRand([4, 5, 6, 7, 8, 9]), shape=0.1, feed=0.4).unison(2)
d8 >> play("p ", sample=4, rate=0.25, dur=16, delay=2, amp=4, echo=0.25, echotime=4)
d6 >> play("  c ", dur=8, amp=0.7, echo=0.5, room=1, mix=0.5)
