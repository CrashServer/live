# epicdevo 66
# torecord
Scale.default = "chromatic"
Clock.bpm = 66
d1 >> industrialdrone([0], dur=16, oct=4, sus=16,  cutoff=linvar([300, 800], 32),  feedback=0.4, noise=0.1, amp=0.4)
p1 >> darkpad([0, 6], dur=8, oct=4, sus=4.5, atk=2, rel=3, cutoff=linvar([600, 2000], 16), dark=0.6,  detune=0.02, amp=0.35, mverb=0.2)
p2 >> ethpad([0, 1, 7], dur=8, oct=5, attack=3, release=4,  amp=0.57, mverb=0.2)
a1 >> darkpad([0, 6, 7], dur=4, oct=6, rq=0.2,  amp=linvar([0, 0.3], 16))
c5 >> faim([0, 1, 6], dur=4, oct=3, beef=1, amp=0.9, fshift=linvar([-20, 20], 16), fmix=0.3)
p1 >> ethpad(r1.degree, dur=8, oct=3, attack=2, amp=0.2, mverb=0.2)
t1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]),oct=3, amp=0.8, dark=0.3)
c3 >> faim(([0, 1, 7], 0), dur=1/2, oct=4, beef=2, amp=0.9, chorus2=1, chorus2rate=0.7, hpf=100, chorus2depth=0, chorus2mode=1).often("stutter", oct=P*[4, 4,5, 6])
c1 >> cs80([0, 0, 0.5], dur=1/2, oct=(3, PStep(4, 3, 4)), amp=0.3, cutoff=linvar([400, 5000], 8), shape=0.1, vakorg=500, vakorgr=0.5, vakorgd=0.5, vakorgt=0, vakorgc=0.3, shimmer=0.8, shimsize=0.8, shimpitch=var([0.0, 0.5, 1, 2, 1, 1, 2, 4, 4, 6, 6, 8, 8]), shimmix=0.5)
c4 >> organ(linvar([17, 1], [8, 1]), dur=[1/2, 1/4], oct=6, beef=1,dist2=0.4, amp=0.3, leg=0, fbdelay=0.5, sus=1/4)
d1.stop()
c4 >> ssaw(linvar([8, 1], [8, 1]), dur=[1/2, 1/4], oct=6, beef=1,dist2=0.5, amp=0.3, leg=0, rgate=0.5, sus=1/4)
c3 >> faim([0, 1, 7], dur=1/2, oct=7, beef=1,         dist2=0.2, amp=0.8, leg=0)
c5.stop()
c4.stop()
b1 >> dbass([0, 0, 0, 3, 0, 0, 5, 0], dur=0.25, oct=6,amp=P[0.8, 0.3, 0.5, 0.6], lpf=1300, envdist=0.8, envdistgain=2, leg=4, envdistsens=1, envdistattack=0.070)
r1 >> vati([12, 11, 10, 9, 7, 4, 3, 0], dur=1/4, oct=6,cutoff=linvar([800, 4000], 8), amp=1.7, leg=0)
prophet = SynthDef("prophet")
r1 >> prophet([12, 11, 10, 9, 7, 4, 3, 0], dur=1/4, oct=5,cutoff=linvar([800, 4000], 8), amp=0.7, leg=0)
s1 >> play("..o...o.", dur=0.25, sample=5, amp=1.0, hpf=200, fbdelay=0.5)
r1 >> prophet([0, _, 0, 2, 3, _, 5, 3], dur=0.25, oct=5,    cutoff=3500, amp=0.93, leg=0.5)
Root.default = 0
d1.stop()
a1.stop()
c5.stop()
s1 >> play("..o...o.", dur=0.25, sample=5, amp=var([0.8, 0.9, 0], [16, 14, 2]), hpf=200, fbdelay=0.5, rgate=0.2)
s2 >> play("e", dur=0.25, sample=3, amp=var([0, 0.5], [30, 2]))
s2.degree = var(["e", "oooo[oo]oo"], [30, 2])
Scale.default = "chromatic"
p1 >> darkpad([0, 6], dur=8, oct=5, sus=8, atk=2, rel=3, cutoff=linvar([600, 2000], 16), dark=0.6,  detune=0.02, amp=0.81, mverb=0.2)
p2 >> ethpad([0, 1, 7], dur=8, oct=6, attack=3, release=4,  amp=0.71, room=0.9, mix=0.6)
c3 >> faim([0, 1, 6, 7], dur=var([1/2, 1/4], [7, 1]), oct=5, beef=1, dist2=0.5, amp=var([0.9, 0.5, 0], [8, 8, 2]), leg=0)
t1.stop()
c1 >> cs80([0, 0, 0.5], dur=1/2, oct=(3, PStep(4, 3, 4)),   amp=var([0.3, 0.5], [16, 16]),          cutoff=linvar([400, 5000], 8), shape=0.1)
r1 >> plaits([0, _, 11, _, 6, 1, _, 7], dur=var([0.25, 1/6], [14, 2]), oct=5, cutoff=linvar([800, 5000], 8), amp=var([0.48, 2.0], [16, 16]), leg=0).unison(4)

d1 >> industrialdrone([0], dur=16, oct=4, sus=16,  cutoff=linvar([300, 800], 32),  feedback=0.4, noise=0.1, amp=0.4)
p1 >> darkpad([0, 6], dur=8, oct=3, sus=8, atk=2, rel=3, cutoff=linvar([600, 2000], 16), dark=0.6,  detune=0.02, amp=0.35, room=0.7, mix=0.5)
r1.stop()

p2 >> ethpad([0, 1, 7], dur=8, oct=5, attack=3, release=4,  amp=0.57, room=0.9, mix=0.6)
a1 >> darkpad([0, 6, 7], dur=4, oct=6, rq=0.3,  amp=linvar([0, 0.3], 16))

Clock.bpm = 132
c5 >> faim([0, 1, 6], dur=4, oct=6, beef=1, amp=0.9,   fshift=linvar([-20, 20], 16), fmix=0.3)
c4.stop()
d1 >> industrialdrone([0], dur=16, oct=6, feedback=0.5, amp=0.3)
p1 >> ethpad(r1.degree, dur=8, oct=5, attack=2, amp=0.2, room=0.9)
t1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]),oct=3, amp=1, dark=0.7)
r2 >> vati([0, 1, 3, 6, 7, 11, 12, 6], dur=0.25, oct=var([5, 6], [16, 16]), cutoff=3000, amp=var([0, 1.0], [16, 16]), leg=0)
b1 >> plaitsX(var([[0,0,0,3,0,0,5,0], [0,1,2,3,4,5,6,7]], [16, 16]),  dur=0.25, oct=6, amp=P[0.8, 0.3, 0.5, 0.6], lpf=900, shape=0)

x1 >> play("X", dur=var([rest(32), 0.5], [30, 2]), sample=8, amp=4, crush=4)
l5 >> compkick(punch=1.2, comp=8, release=0.35, click=3,drive=0.5, sub=1, oct=4, body=0.6, tone=4)

k4 >> play("....C.", amp=2, fbdelay=0.5, lpf=12000, glitch=0.5)

l5 >> compkick(punch=1, comp=8, release=0.35, click=4,drive=0.5, sub=1, oct=4, body=1, tone=12)

l5 >> a_bd()
t1.stop()
p1.stop()


drop()
# Server.addFx(hpf=400)

c4.stop()
r1.stop()
r3.stop()
b1.stop()

Group(k1, s1, s2, h1).solo()
s1.stop()
# a1 >> acidline([0, 0, 3, 0, 5, 0, 3, -2], dur=0.25, oct=6, beef=122, cutoff=linvar([400, 2000], 8), rq=0.8, amp=1.8)

c5 >> faim([0, 6, 12, 1, 7], dur=2, oct=3, beef=2,  dist2=0.8, amp=1.2, leg=2, room=0.6, mix=0.4)
b1 >> dbass([0, 0, 0, 0, 0, 0, 0, 0], dur=1/8, oct=5, amp=P[1, 0.4, 0.7, 0.4], lpf=1200, shape=0)
r1 >> prophet([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dur=1/6, oct=5,  cutoff=linvar([2000, 8000], 4), amp=0.8, leg=0, crush=4)
r2 >> vati([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], dur=1/6, oct=6,  cutoff=5000, amp=0.9, leg=0)


c6 >> cs80([0, 1, 6], dur=var([1, 1/4], [3, 1]), oct=6, cutoff=6000, amp=0.7, crush=3, dist2=0.5, leg=0)
n1 >> noise(dur=8, amp=linvar([0, 0.4], 8), hpf=2000, lpf=8000)

Clock.bpm = 66
c5 >> faim([0, 3, 6, 9], dur=2, oct=3, beef=2, dist2=0.6, amp=1.0, leg=1, room=0.5)
k1 >> play("X...", dur=0.5, sample=4, amp=1.3, shape=0.8)
s1 >> play("..o.", dur=0.5, sample=5, amp=1.0, crush=3)

Clock.bpm = 132
r1 >> prophet([0, 1, 3, 4, 6, 7, 9, 10], dur=0.5, oct=4,cutoff=linvar([500, 6000], 16), amp=0.9, leg=0.3)
r7 >> prophet([0, 1, 3, 4, 6, 7, 9, 10], dur=0.5, oct=5,cutoff=linvar([500, 6000], 16), amp=0.9, leg=0.3).slider()

c5.oct=3


