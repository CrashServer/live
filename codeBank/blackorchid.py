
# blackorchid 88
# dark

Clock.bpm = 88;
b2 >> prodrums([0, 3, 7, 10, 12, 7], voice=4, dur=PDur(3, 8), layer1_amp=0.4, layer2_amp=0.3, layer3_amp=0.2, body_tone=var([3500, 3000], [6, 2]), harmonic=2.5, fm_amount=1, fm_ratio=4, waveform=var([3, 6], 12), texture=4, decay=0.5, echo=0.5, amp=0.3, oct=(6, 5), pan=PSine(8) * 0.3)
v1 >> viola([6, 3, P*[4, 2, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, mverb=0.8, blur=2, lpf=PRand(1200, 3000), hpf=300, amp=0.5).unison(2) + (-7, PStep(5, 7, 0))
p1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]), oct=3, amp=0.6, dark=0.7)
p3 >> ethpad([0, 7], dur=8, oct=6, attack=3, release=4, amp=0.35, room=0.9, mix=0.6)
a1 >> acidline(var([P[0, 0, 3, 0, 5, 0, 0, 3], P[0, 3, 5, 7, 10, 7, 5, 3]], [16, 16]), dur=var([0.25, 0.125], [24, 8]), cutoff=expvar([300, 4000], 8), res=linvar([0.4, 0.9], 16), drive=linvar([1.5, 0.2], 32), lpf=1200, accent=var([P[0, 0, 1, 0]*0.5, P[1, 0, 0, 1]*0.6], [12, 4]), tubedrive=linvar([0.2, 0.7], 48), amp=0.6)
b1 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)], voice=4, dur=0.25, layer1_amp=1, layer2_amp=1.2, layer3_amp=0.8, body_tone=linvar([500, 1400], 16), harmonic=0.7, fm_amount=3.1, fm_ratio=var([2, 2.5, 3], 4), waveform=6, texture=10, decay=0.3, mid_sat=1.6, amp=0.8, oct=4)
a1 >> acidline([0, 0, 3, 0, 5, 0, 0, 3], dur=0.25, cutoff=linvar([400, 2400], 8), res=linvar([0.5, 0.85], 4), drive=2.5, accent=P[0, 0, 1, 0]*0.5, tubedrive=0.4, amp=0.5, oct=5)

v1.stop()
j1 >> cs80([0, 0, 0.5, 3], dur=0.5, oct=(3, PStep(4, 3, 4)), amp=var([0.3, 0.5], [16, 16]), cutoff=linvar([400, 5000], 8), shape=0.1, shimmer=linvar([0, 0.5], 32), shimsize=0.8, shimmix=0.4)
x1 >> plaitsX([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dur=1/6, oct=5, cutoff=linvar([2000, 8000], 4), amp=var([0, 0.6, 0, 0.8], [16, 8, 8, 32]), leg=0, crush=4)
x2 >> vati([11, 10, 9, 8, 7, 4, 3, 0], dur=0.25, oct=6, cutoff=linvar([800, 4000], 8), amp=var([0, 0.8], [24, 8]), leg=0)
b3 >> dbass([0, 0, 0, 3, 0, 0, 5, 0], dur=0.25, oct=5, amp=P[0.8, 0.3, 0.5, 0.6], lpf=1300, envdist=0.8, envdistgain=2, leg=0)
h2 >> play("-", sample=5, dur=0.25, amp=P[0.4, 0.15, 0.3, 0.15], hpf=4000)
d2 >> play("..C.", sample=2, dur=0.5, amp=0.5)
h1 >> play("{---=}", rate=PWhite(1, 3), pan=PWhite(-1, 1), hpf=4000, amp=0.3).sometimes("stutter", PRand(15))
s1 >> play("..o.", sample=5, dur=0.5, amp=0.7, hpf=200)
p1 >> darkpad([0, 6], dur=8, oct=4, sus=6, atk=3, rel=3, cutoff=linvar([400, 1400], 32), dark=PWhite(0.5, 0.9), detune=0.04, amp=linvar([0, 0.35], 32), mverb=0.3)

p1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]), oct=3, amp=linvar([0.5, 0], 32), dark=0.9)
k2 >> play("X", amp=Pvar([P[1, 0], PTimebin()], [64, 64]), mid=2, sample=5).sometimes("stutter")
