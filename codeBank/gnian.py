# gnian 120
# interlude

Scale.default = "major"
Clock.bpm = 120;
a1 >> cbass([(-2, P[0, -2, 4] * P[6, 1, 1]), -2.01], hpf=40, oct=(PStep(3, 5, 6),5), follow=(12, 4), lpf=[0, linvar([4000, 16000], 32)], dur=4, sus=a1.dur + PWhite(0.01, 0.05), mid=1, amp=1.1).unison(2) + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])
a1 >> cbass([(-2, P[0, -2, 4] * P[6, 1, 1]), -2.01], hpf=40, oct=(PStep(3, 5, 6),5), follow=(12, 4), lpf=[0, linvar([4000, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), mid=1, amp=1.1).unison(2) + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])
a2 >> cbass([(-2, P[0, -2, 4] * P[6, 1, 1]), -2.01], oct=(PStep(5, 5, 6),6), lpf=[0, linvar([400, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), amp=1, beef=0, follow=4).unison(2) + var([0, 3], [12, 4]) + var([0, 6, 5], [24, 4, 4])
a7 >> cbass(    a1.degree + var([P[0, 5, 7, 5], P[3, 7, 10, 7]], [4, 4]),  dur=PDur(5, 8) * var([1, 1, 1/2], [5, 2, 1]), mverb=0.5,   oct=var([6, 7], [3, 1]),    slide=0,    lpf=linvar([8000, 16000], 32),    sus=PDur(5, 8) + PWhite(0, 0.2), tanh=0.0, amp=var([0, 1, 0.7, 1.2, 0.8], [1, 3, 1, 1, 2]),    delay=0.25).unison(2, 0.08)
b1 >> dbass([(-2, P[0, -2, 4] * P[6, 1, 1]), -2.01], hpf=40, oct=(PStep(3, 5, 6),5), follow=(12, 4), lpf=[0, linvar([4000, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), mid=1, amp=1.1).unison(2) + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])
p1 >> pluck([(-2, P[0, -2, 4] * P[3, 1, 0]), -2.01], hpf=40, oct=(PStep(3, 5, 6),5), follow=(12, 4), lpf=[0, linvar([4000, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), mid=linvar([1, 4], 32), amp=1.1).unison(2) + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])
a1 >> cbass( [(-2, P[0, -2, 4] * P[6, 1, 1]), -2.01] + var([0, 5, 7, 3], [4, 2, 1, 1]) + P[0, 2, 4, 7, 5, 3, 2].stutter(2),    dur=PDur(var([5, 7, 3], [8, 4, 4]), 8),    oct=var([7, 8], [6, 2]),    slide=PWhite(0, 0.3) * PRand([0, 1]),    lpf=linvar([6000, 12000], 16),     sus=PDur(5, 8) * PWhite(0.8, 1.2),     amp=var([0, 1, 0.7, 1.2], [1, 5, 1, 1]),    pan=PSine(16) * 0.3).unison(2, 0.05)
a3 >> cbass([-2, -2.01], hpf=40, oct=(PStep(3, 5, 6),5), dist2=0.4, follow=(12, 4), lpf=[0, linvar([4000, 16000], 32)], dur=var([1/2, 1/2, 1/4, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), mid=1, amp=1.1).unison(2) + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])
~a1 >> cbass([(-2, P*[0, -2, 4] * P[6, 1, 1]), -2.01], hpf=40, oct=(PStep(3, 5, 6),5), follow=(12, 4), lpf=[0, linvar([4000, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), mid=1, amp=1.1).unison(2) + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])
a2 >> cbass([-2, -2.01] + var([0, 7], 2), dur=PDur(var([3, 5, 7], [4, 2, 2]), 8), oct=5, sus=0.05, amp=P[0, 1.4, 0, 1.2, 0.8, 0, 1.6, 0.6], hpf=200, lpf=2000, chop=16)
a7 >> cbass([-2, -2.01], dur=1/4, oct=var([5, 6], [7, 1]), sus=0.08, amp=P*[1.2, 0.4, 0.6, 0.3, 1.4, 0.5, 0.4, 0.7, 1.1, 0.4, 0.5, 0.3, 1.5, 0.6, 0.4, 0.8], hpf=400, lpf=4000, room=0.1)
b5 >> cbass([-2, -2.01] + P*[0, 0, 7, 0, 5, 0, 3, 0], dur=1/4, oct=var([5, 6], PRand([3, 5, 7])), sus=P[0.05, 0.05, 0.2, 0.05, 0.05, 0.15, 0.05, 0.25], amp=var([1.2, 0.8, 1.5, 0.6], [2, 1, 2, 3]), hpf=350, lpf=2500, chop=var([0, 8], [6, 2]))
a2 >> cbass([-2, -2.01] + var([0, 5, 7], 2), dur=PDur(3, 8), oct=var([5, 6, 5], [2, 1, 1]), sus=0.1, amp=var([1.3, 1.5, 1.1], [2, 1, 1]), slide=PRand([-0.2, 0, 0.2]), hpf=300, lpf=3000).unison(2)
a1 >> cbass([(-2, P*[0, -2, 4] * P[6, 1, 1]), -2.01], hpf=40, oct=(PStep(3, 5, 6),5), follow=(12, 4), lpf=[0, linvar([4000, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), mid=1, amp=1.1).unison(2) + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])
a2 >> cbass([(-2, P*[0, -2, 4] * P[6, 1, 1]), -2.01], oct=(PStep(5, 5, 6),6), lpf=[0, linvar([400, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), amp=1, beef=0, follow=4).unison(2) + var([0, 3], [12, 4]) + var([0, 6, 5], [24, 4, 4])
a1.degree=0
a2.degree=0
a3 >> cbass(a1.degree + P[0, 2, 4, 7], dur=1/2, oct=7, amp=0.8, lpf=8000, sus=0.1)
a7.degree=0
a2 >> cbass(a1.degree + var([0, 5], 4), dur=PDur(5, 8), oct=7, amp=var([0, 1], [1, 7])).unison(4)
a_all.follow=0
a_all.dur=4
a_all.lpf=1600
a_all.dur=8
b_all.lpf=200
p_all.lpf=700
a1 >> cbass([-2, -2.01], dur=P[1/4, 1/4, 1/8, 1/8], oct=5, sus=0.06, amp=P[1.3, 0.8, 1.5, 0.7], hpf=280, lpf=3500, shape=0.4).every(4, 'stutter', 2)

