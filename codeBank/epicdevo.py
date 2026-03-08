# epicdevo 66
# epic

#@intro(32)
d1 >> industrialdrone([0], dur=16, oct=4, sus=16,  cutoff=linvar([300, 800], 32),  feedback=0.4, noise=0.1, amp=0.4)

#@build(8)
p1 >> darkpad([0, 6], dur=8, oct=4, sus=4.5, atk=2, rel=3, cutoff=linvar([600, 2000], 16), dark=PWhite(0.5, 0.9),  detune=0.04, amp=0.35, mverb=0.2)

#@peak(8)
p2 >> ethpad([0, 1, 7], dur=8, oct=5, attack=3, release=4,  amp=0.57, mverb=0.0)

#@break(8)
d1 >> darkpad([0, 6, 7], dur=4, oct=6, rq=0.2,  amp=linvar([0, 0.3], 16))

#@drop(16)
c5 >> faim([0, 1, 6], dur=4, oct=3, beef=1, amp=0.9, fshift=linvar([-20, 20], 16), fmix=0.3)
p1 >> ethpad(r1.degree, dur=8, oct=3, attack=2, amp=0.2, mverb=0.2)

#@outro(16)
t1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]),oct=3, amp=0.8, dark=0.3)
c3 >> faim(([0, 1, 7], 0), dur=1/2, oct=4, beef=2, amp=0.9, chorus2=1, chorus2rate=0.7, hpf=100, chorus2depth=0, chorus2mode=1).often("stutter", oct=P*[4, 4,5, 6])

#@part7(32)
c1 >> cs80([0, 0, 0.5], dur=1/2, oct=(3, PStep(4, 3, 4)), amp=0.3, cutoff=linvar([400, 5000], 8), shape=0.1, vakorg=500, vakorgr=0.5, vakorgd=0.5, vakorgt=0, vakorgc=0.3, shimmer=lininf(0.8,0,32), shimsize=0.8, shimpitch=var([0.0, 0.5, 1, 2, 1, 1, 2, 4, 4, 6, 6, 8, 8]), shimmix=0.5)
c4 >> organ(linvar([17, 1], [8, 1]), dur=[1/2, 1/4], oct=6, beef=1,dist2=0.4, amp=0.3, leg=0, fbdelay=0.5, sus=1/4, resonbank=0.1, rbfreq=200, rbdecay=0.5, rbspread=1.0)

#@part8(16)
d1.stop()
p1.stop()
c4 >> ssaw(linvar([8, 1], [8, 1]), dur=[1/2, 1/4], oct=6, beef=1,dist2=0.5, amp=0.3, leg=0, rgate=0.5, sus=1/4)
c3 >> faim([0, 1, 7], dur=1/2, oct=7, beef=1,         dist2=0.2, amp=0.8, leg=0)

#@part9(8)
c5.stop()
c4.stop()
b1 >> dbass([0, 0, 0, 3, 0, 0, 5, 0], dur=0.25, oct=6,amp=P[0.8, 0.3, 0.5, 0.6], lpf=1300, envdist=0.8, envdistgain=2, leg=0, envdistsens=0.7, envdistattack=0.020)
r1 >> vati([12, 11, 10, 9, 7, 4, 3, 0], dur=1/4, oct=6,cutoff=linvar([800, 4000], 8), amp=1.7, leg=0)

#@part10(8)
c3.stop() #
c4.stop()
r1 >> plaitsX([12, 11, 10, 9, 7, 4, 3, 0], dur=1/4, oct=5,cutoff=linvar([800, 4000], 8), amp=1.2, leg=0)
s1 >> play("..o...o.", dur=0.25, sample=5, amp=1.0, hpf=200, fbdelay=0.5)
r1 >> plaitsX([0, _, 0, 2, 3, _, 5, 3], dur=0.25, oct=5,    cutoff=3500, amp=0.93, leg=0.5)
t1.stop()

#@part11(8)
Root.default = 0
d1.stop()
a1.stop()
p1.stop() #

#@part12(8)
c5.stop()
s1 >> play("..o...o.", dur=0.25, sample=5, amp=var([0.8, 0.9, 0], [16, 14, 2]), hpf=200, fbdelay=0.5, rgate=0.2)
p2.stop() #
s2 >> play("e", dur=0.25, sample=3, amp=var([0, 0.5], [30, 2]))

#@part13(16)
s2.degree = var(["e", "oooo[oo]oo"], [30, 2])
Scale.default = "chromatic"
p1 >> darkpad([0, 6], dur=8, oct=5, sus=8, atk=2, rel=3, cutoff=linvar([600, 2000], 16), dark=0.6,  detune=0.02, amp=0.81, mverb=0.2)
p2 >> ethpad([0, 1, 7], dur=8, oct=6, attack=3, release=4,  amp=0.71, room=0.9, mix=0.6)
c3 >> faim([0, 1, 6, 7], dur=var([1/2, 1/4], [7, 1]), oct=5, beef=1, dist2=0.5, amp=var([0.9, 0.5, 0], [8, 8, 2]), leg=0)

#@part14(8)
t1.stop()
c1 >> cs80([0, 0, 0.5], dur=1/2, oct=(3, PStep(4, 3, 4)),   amp=var([0.3, 0.5], [16, 16]),          cutoff=linvar([400, 5000], 8), shape=0.1)
r1 >> plaits([0, _, 11, _, 6, 1, _, 7], dur=var([0.25, 1/6], [14, 2]), oct=5, cutoff=linvar([800, 5000], 8), amp=var([0.48, 2.0], [16, 16]), leg=0).unison(4)

#@part15(8)
p1 >> darkpad([0, 6], dur=8, oct=3, sus=8, atk=2, rel=3, cutoff=linvar([600, 2000], 16), dark=0.6,  detune=0.02, amp=0.56, room=0.7, mix=0.5)
r1.stop()

#@part16(8)
p2 >> ethpad([0, 1, 7], dur=8, oct=5, attack=3, release=4,  amp=0.57, room=0.9, mix=0.6)
a1 >> darkpad([0, 6, 7], dur=4, oct=6, rq=0.3,  amp=linvar([0, 0.3], 16))

#@part17(8)
Clock.bpm = 132
c5 >> faim([0, 1, 6], dur=4, oct=6, beef=1, amp=0.9,   fshift=linvar([-20, 20], 16), fmix=0.3)

#@part18(8)
c4.stop()
d1 >> industrialdrone([0], dur=16, oct=6, feedback=0.5, amp=0.3)

#@part19(8)
p1 >> ethpad(r1.degree, dur=8, oct=5, attack=2, amp=0.2, room=0.9)
t1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]),oct=3, amp=1, dark=0.7)
r2 >> vati([0, 1, 3, 6, 7, 11, 12, 6], dur=0.25, oct=var([5, 6], [16, 16]), cutoff=3000, amp=var([0, 1.0], [16, 16]), leg=0)
b1 >> plaitsX(var([[0,0,0,3,0,0,5,0], [0,1,2,3,4,5,6,7]], [16, 16]),  dur=0.25, oct=6, amp=P[0.8, 0.3, 0.5, 0.6], lpf=900, shape=0)

#@part20(16)
x1 >> play("X", dur=var([rest(32), 0.5], [30, 2]), sample=8, amp=1, crush=4)
l5 >> compkick(punch=1.2, comp=8, release=0.35, click=3,drive=0.5, sub=1, oct=4, body=0.6, tone=4)

#@part21(8)
c1.stop()

#@part22(16)
c1 >> cs80([0, 0, 0.5], dur=1/2, oct=(3, PStep(4, 3, 4)),   amp=var([0.3, 0.5], [16, 16]),          cutoff=linvar([400, 5000], 8), shape=0.1)

#@part23(8)
b1.stop()
s1.stop()
p1.stop()
c4.stop()
r1.stop()
r3.stop()
b1.stop()

#@part24(8)
Group(k1, s1, s2, h1).solo()

#@part25(16)
c5 >> faim([0, 6, 12, 1, 7], dur=2, oct=3, beef=2,  dist2=0.8, amp=1.2, leg=2, room=0.6, mix=0.4)
b1 >> dbass([0, 0, 0, 0, 0, 0, 0, 0], dur=1/8, oct=5, amp=P[1, 0.4, 0.7, 0.4], lpf=1200, shape=0)
r1 >> plaitsX([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dur=1/6, oct=5,  cutoff=linvar([2000, 8000], 4), amp=0.8, leg=0, crush=4)
s2.stop()
r1 >> plaitsX([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dur=1/6, oct=5,  cutoff=linvar([2000, 8000], 4), amp=0.8, leg=0, crush=4)
r2 >> vati([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], dur=1/6, oct=6,  cutoff=5000, amp=0.9, leg=0)

#@part26(8)
c6 >> cs80([0, 1, 6], dur=var([1, 1/4], [3, 1]), oct=6, cutoff=6000, amp=0.7, crush=3, dist2=0.5, leg=0, lpf=1800)
n1 >> noise(dur=8, amp=linvar([0, 0.4], 8), hpf=2000, lpf=8000)

#@part27(4)
c6.oct=(4, 3)

#@part28(8)
b1.stop()
Clock.bpm = 66

#@part29(4)
c5 >> faim([0, 3, 6, 9], dur=2, oct=3, beef=2, dist2=0.6, amp=1.0, leg=1, room=0.5)
k1 >> play("X...", dur=0.5, sample=4, amp=1.3, shape=0.8)
s1 >> play("..o.", dur=0.5, sample=5, amp=1.0, crush=3)

#@part30(4)
c9 >> faim([7,6,1,0], dur=PDur(3,8), oct=5, beef=1, amp=var([0, 0.7], [16, 16]), dist2=0.1, leg=0.5)

#@part31(8)
p4 >> darkpad(0, dur=32, oct=2, sus=32, dark=0.95, amp=linvar([0, 0.6], 16), cheapverb=0.8, cvdecay=8, cvdamp=0.8).only()
c9 >> faim([7,6,1,0], dur=PDur(3,8), oct=5, beef=1, amp=var([0, 0.7], [16, 16]), dist2=0.1, leg=0.5)

#@part32(16)
c6 >> cs80([0, 1, 6], dur=var([1, 1/4], [3, 1]), oct=2, cutoff=6000, amp=0.7, crush=3, dist2=0.5, leg=0, lpf=1800)
p1 >> darkpad([0, 6], dur=8, oct=5, sus=8, atk=2, rel=3, cutoff=linvar([600, 2000], 16), dark=0.6,  detune=0.02, amp=0.81, mverb=0.2)
Clock.bpm = 132

#@part33(8)
c1 >> cs80([0, 0, 0.5], dur=1/2, oct=(3, PStep(4, 3, 4)), amp=0.3, cutoff=linvar([400, 5000], 8), shape=0.1, vakorg=500, vakorgr=0.5, vakorgd=0.5, vakorgt=0, vakorgc=0.3, shimmer=lininf(0.8,0,32), shimsize=0.8, shimpitch=var([0.0, 0.5, 1, 2, 1, 1, 2, 4, 4, 6, 6, 8, 8]), shimmix=0.5)

#@part34(4)
c4 >> organ(linvar([17, 1], [8, 1]), dur=[1/2, 1/4], oct=6, beef=1,dist2=0.4, amp=0.3, leg=0, fbdelay=0.5, sus=1/4, resonbank=0.1, rbfreq=200, rbdecay=0.5, rbspread=1.0)

#@part35(8)
b1 >> dbass([0, 0, 0, 3, 0, 0, 5, 0], dur=0.25, oct=6,amp=P[0.8, 0.3, 0.5, 0.6], lpf=4000, envdist=0.8, envdistgain=2, leg=4, envdistsens=1, envdistattack=0.020, resonbank=0.1, rbfreq=200, rbdecay=0.5, rbspread=1.0)

#@part36(8)
k1 >> play("X...", dur=0.5, sample=4, amp=1.3, shape=0.8)
s1 >> play("..o.", dur=0.5, sample=5, amp=1.0, crush=0)
g0 >> svdk(dur=8,lpf=800)

#@part37(4)
m7 >> loop("dubstepdrum32", dur=32)

#@part38(8)
c4.degree=0
c4.degree=2
c6 >> play("..C.")
l9 >> play("[--]")

#@part39(16)
l0 >> play("X ")

#@part40(16)
l9 >> play("[--]", hpf=1200)
l9 >> play("[--]", hpf=1300)
l9 >> play("[--]", hpf=2100)

#@part41(4)
~d8 >> loop("elephant16", dur=16, sample=4, tape=0, lpr=0, lpf=0)

#@part42(16)
p4.stop()
p1.stop()
c1.stop()
b1.stop()
c4.stop()
p4 >> loop("dnbfx16", dur=16, dist2=0.5, sample=[1, 3, 0], amp=0.5)
~d8 >> loop("elephant16", dur=16, sample=4, tape=0, lpr=0, lpf=0)

#@part43(4)
c6.stop()

#@part44(8)
k1.stop()
k1.stop()

#@part45(8)
s1.stop()

#@part46(8)
g0.lpf=400
d1 >> play("x", amp=Pacc(3, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 57, 50, 62, 69], rbdecay=[0.6, 0.2, 0.6, 0.6, 0.6, 0.7, 0.2], pong=0, rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.1, dftone=2, lpf=0, lpr=0.1).unison(4)

#@part47(4)
l9.stop()

#@part48(8)
d1 >> play("x", amp=Pacc(5, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, high=0.0, dftone=2, lpf=0, lpr=0.1).unison(4)

#@part49(8)
d8.stop()

#@part50(16)
c9.stop()
p1.stop()
c6.stop()
c1.stop()
c4.stop()
b1.stop()
g0.stop()
d1 >> play("x", amp=Pacc(4, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, dftone=2, lpf=linvar([2000, 4000], [32,0]), lpr=0.1).unison(4)

#@part51(8)
d1 >> play("x", amp=Pacc(4, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, dftone=2, lpf=0, lpr=0.1).unison(4)

#@part52(8)
d4 >> play("x", dur=0.5, mverb=1, rate=2, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0, cheapverb=PBin(8), cvdecay=1.5, cvdamp=0.5, amp=Pacc(6, 4), amplify=PLife(0.5), hpf=3200, echo=0.25, sample=6, resonbank=0.1, rbfreq=36, rbdecay=0.5, rbspread=1, glitch=0.5, glitchrate=8, glitchdepth=0.5, glitchcrush=0.3, glitchchance=0.5, beat_dur=1)
l0.stop()
d8 >> play(".-u-", dur=0.25, amp=Pacc(4))
d6 >> play("..U:", rfreq=8000, resonz=0.4, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=3000, fbspread=0.11, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@part53(8)
d1 >> play("x", amp=Pacc(3, 8), sample=5, dur=1/4, resonbank=0.8, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, dftone=3, lpf=linvar([2000, 4000], [32,0]), lpr=0.1).unison(4)

#@part54(16)
d4 >> play("x", dur=0.5, mverb=1, rate=2, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0, cheapverb=PBin(8), cvdecay=1.5, cvdamp=0.5, amp=Pacc(6, 4), amplify=PLife(0.5), hpf=3200, echo=0.25, sample=6, resonbank=0.1, rbfreq=36, rbdecay=0.5, rbspread=1, glitch=0.5, glitchrate=8, glitchdepth=0.5, glitchcrush=0.3, glitchchance=0.5, beat_dur=1)
d3 >> play("s", dur=0.5, sample=2, amp=0.56, amplify=PFDur((3,8),(5,16)), octclean=0.4, ocsub=0.7, ocup=0, hpf=100, lpf=4000, delay=PSwing(0.06))
d5 >> play("-", dur=0.25, sample=2, amp=0.9, amplify=PEuclid(7,16), hpf=6000, cheapverb=0.7, cvdecay=3, cvdamp=0.3, pan=0.3)

#@part55(8)
q3 >> compkick(0, punch=0.5, comp=16, release=0.35, click=1.0,drive=0.4, sub=1, tape=1, tapedrive=2, body=0.2, echo=0, tone=0.0, oct=3,)


