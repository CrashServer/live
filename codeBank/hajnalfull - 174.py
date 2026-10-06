# hajnalfull - 174
# superxstatic

Clock.bpm = 174
Scale.default = "minor"
Root.default = "C"

h4 >> plaitsX([0, 11, 4, 0, 2, 4, 5, 0], dur=P[21, 0.5, 0.5, 1, 0.5, 0.5, 1, 1]*1, sus=2, preset=8, amp=var([1, 0.8], [8, 8]), oct=var(P*[5, 6, (6, 7)], 8), cutoff=12200, vib=12, pan=PWhite(-0.6, 0.6), hpf=200, fbdelay=0.25, glide=0, rgate=0, a=0.3)
h4.slider()
v2 >> choir([0, 3, 5, P*[7, 10, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], vowel=2, vowelf=0, vowelq=1, beat_dur=1, rate=1, mverb=0.85, blur=0, lpf=PRand(1200, 3000), hpf=300, amp=linvar([1, 0.5], 24)).unison(2) + (-7, PStep(5, 7, 0))
b9 >> bell2([0, 7, 12], dur=16, oct=5, amp=linvar([0, 0.55], 24), atk=4, sus=14, lpf=linvar([400, 2500], 64), room=0.7, mix=0.5, multicrush=1.5, mclowdrive=1.5, mcmiddrive=1.5, mchighdrive=2.5, mclofreq=120, mchifreq=2800, tube=0.5, tubegain=1.0, tubewarm=0.8, hard=var([0, 1, 2, 4], 8), nharm=2, fmamt=[0, 1, 2, 4], fmratio=12, strike=1, shimmer=2.0)
g3 >> play("xXx--[---]", sample=3,fbdelay=2, fbtime=1, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, leg=4, echo=4, echomix=0.5, echotime=4, beat_dur=1, amp=PWhite(0, 1), dur=1/4, mverb=0.5).after(4,"stop")

x4.stop()
x5.stop()
g4 >> play("h", sample=4, rate=linvar([PRand([1, 2, 4, 8, 16]), 1], PRand([1, 2, 4, 8])), dur=var([PRand([4, 16, 32]), 1/4]), shift=PRand([2, 4, 8]))

e4 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), rate=2, amp=0.7, cut=PWhite(0.5, 1), sample=PRand(20), dur=1/4, lpf=0, leg=10, krush=0).sometimes("stutter").slider()
h4.oct=4

g4 >> play("h", sample=4, rate=linvar([PRand([1, 2, 4, 8, 16]), 1], PRand([1, 2, 4, 8])), dur=var([PRand([4, 16, 32]), 1/4]), shift=PRand([2, 4, 8]))
h4.fbdelay=0.5
h4.chop=4

g5 >> play(PRand("fff".replace("f", "{o--}")), rate=1, sample=PRand(20), dur=1/4, amp=0.6, lpf=0, leg=200, krush=P*[0,8]).sometimes("stutter").slider()
~g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.4, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
k6 >> play("c.{cC}.", sample=7, tanh=0.2, formant=1, dur=2, amp=2, leg=8, echo=0.456)

h4.stop()
rb >> play("<(X...)(v..(.//))(...(.v))(..v.)><(.r)...><-.><.+><...(.(.:))>",dur=1/2, amp=PBern(16), amplify=var([1,0],[14,1]), sample=6,pan=(0,-0.2,(-1,1),PWhite(-1,1),0.3)).human(20,5,0).often("stutter", PRand(16).rnd(2), delay=(0, 0.25), shape=0.2, mid=0, low=1.5, high=4).every(2, "shuffle")

b2 >> cbass([3, (3, [4, var([3, 14], [15, 1])])], slide=0.5,dur=[2, 1/2, 1, 1/2], oct=(7, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=0, lpf=0, bpf=linvar([2000, 6200, 32], [16, 8, 32]), shape=0, high=4, mid=0.1, low=0.1, vol=0.8, chop=0).unison(8).spread(2)

b2.stop()

g4 >> play("-", sample=7,  rate=linvar([PRand([1, 2, 4, 8, 16]), 1], PRand([1, 2, 4, 8])), dur=var([PRand([4, 16, 32]), 1/4]))
g5 >> play(PRand("fff".replace("f", "{o--}")), rate=1, sample=PRand(20), dur=1/4, amp=0.6, lpf=0, leg=200, krush=P*[0,8]).sometimes("stutter").slider()

soloRnd()

f6 >> play("o ", sample=4, dur=PDur([0, 0, 3], 8), rate=[2, 4], hpf=4000, shift=0.5)
d1 >> play("W ", drive=0, dur=4, bpf=80, bpr=0.9, amp=PMorse("thisiskickistooloud"),vol=0.5, slide=[0, -4], rate=var([1, linvar([1, 0.2], 4)])).unison(4)
b9.stop()
l2 >> noloop("vocalcrash8", dur=[16, 8, 4, 2], lofi=1, start=0.5, rate=1, sample=PRand(8)).after(8, "stop")

# Server.addFx(csweep=.1)
 
v2.stop()
b9.stop()

drop()

g5 >> play("b ", resonbank=0.0, rbfreq=200, rbdecay=0.5, rbspread=1.0)
e1 >> play("Xx{x.x{--}.}")

k5 >> play("C...", dur=2, amp=3, leg=4, echo=0.5)

~g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.4, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()

k6 >> play("c.{cC}.", sample=7, tanh=0.2, formant=1, dur=2, amp=2, leg=8, echo=0.456)
k7 >> play("X ", amp=1)

g3.shape=1
f8 >> play("g", dur=4).solo(8)
m4 >> play("j ", sample=6, formant=1, rate=3, dur=[2, 4, 8])
d1 >> play("W ", drive=0, dur=4, bpf=80, bpr=0.9, amp=PMorse("thisiskickistooloud"),vol=0.5, slide=[0, -4], rate=var([1, linvar([1, 0.2], 4)])).unison(4)

d8 >> play("@ ", dur=PDur(1, 15, 4), echo=0.25)
d2 >> brown(dur=8, cut=1/2, room2=0.2, chop=4, damp2=0.2, fold=0.5, lofi=0.5, hpf=4000)

#unsolo
k4 >> play("X ", amp=PBin(16), sample=6).often("stutter", 8, rate=PWhite(0.5, 4))
k7.stop()
l6 >> play("..U.", sample=4, amp=4)
m8 >> play("[--]{[--][-]}", sample=9)

soloRnd()

g4 >> loop("synth16", dur=16, delay=0, a=0, cut=0.125, leg=8)
g5 >> loop("synth16", dur=16, a=0, pos=PWhite(0, 1), beat_stretch=0, rate=-1)

b6 >> loop("ragegtr16", dur=16, delay=0, a=0, sample=PRand([0, 4]), cut=0.5, leg=8, hpf=200, mverb=0.5, amp=0.1).unison(3)

k6 >> loop("nsbass8", fbdelay=0.5, fbtime=0.25, fbfeed=0.7, amp=PBin(16)*0.3, fbcutoff=3000, fbspread=0.02, beat_dur=1, pos=linvar([0, PWhite(0.0, 1.0)], [8, 4]), sample=1, dur=4, beat_stretch=0, lpf=3200, lpr=0.1).lclip(1).after(32, "stop")

k7 >> loop("rock32", dist2=0.4, pos=linvar([0, PWhite(0.0, 1.0)], [16, 4]), sample=PRand(32)[:16], dur=1/2, beat_stretch=0).lclip(2)

soloRnd()

k7 >> loop("rock32", dist2=0.4, pos=linvar([0, PWhite(0.0, 1.0)], [16, 4]), sample=PRand(32)[:16], dur=8, beat_stretch=0).lclip(2)

Server.addFx(fbdelay=1, fshift=linvar([1, 12], 8))

# Server.addFx(fbdelay=1, fshift=12)

Server.addFx(lpf=3500, lpr=0.3)


l_all.only()
l5.stop()
l6.mverb=0.5
l6.amp=1.8
l6.rgate=1
g7 >> loop("synth16", dur=16, delay=0, a=0, cut=0.125, leg=8)
g4 >> loop("circlebreak16", dur=16, amp=2)
l4.sample=3
l3.stop()

Server.addFx(lpf=0)
l4.delay=(0, 4)
l4.shift=(0, 0.5)
l3 >> loop("drumglitch32", pos=0, cut=0, dur=32, sample=12)

g4 >> play("h", sample=4, rate=linvar([PRand([1, 2, 4, 8, 16]), 1], PRand([1, 2, 4, 8])), dur=var([PRand([4, 16, 32]), 1/4]), shift=PRand([2, 4, 8]))
g_all.rate=var([1, linvar([12, 1])], [28, 4])
g_all.only()
g5 >> play(PRand("fff".replace("f", "{o-}")), rate=1, sample=PRand(20), dur=1/4, amp=0.4, lpf=0, leg=200, krush=P*[0,8]).sometimes("stutter").slider()
g_all.dubd=var([0.2, 0.1, 0.3, 0])
g_all.shift=var([0,  linvar([PCoin(12, 1, 0.25), PCoin(1, 12, 0.25), 24])], [48, 4])
g_all.dur=var([1/4, linvar([PCoin(1, 1/8, 0.25), PCoin(1/8, 1, 0.25)], 16)], [24, 4])

#evaluate quickly 

g_all.hpf=1200
g_all.hpf=0
e1 >> play("%", dur=32, rate=-0.25)
g_all.lpr=0.2

#evaluate quickly 

g_all.rate=var([1, PWalk(8, 4, 1)], PRand(16))
g_all.dur=var([1/4, 4], PRand(16))
g_all.stop()

v2 >> viola([0, 3, 5, P*[7, 10, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, mverb=0.85, blur=0, lpf=PRand(1200, 3000), hpf=300, amp=linvar([0, 0.5], 24)).unison(2) + (-7, PStep(5, 7, 0))
b9 >> bell2([0, 7, 12], dur=16, oct=5, amp=linvar([0, 0.55], 24), atk=4, sus=14, lpf=linvar([400, 2500], 64), room=0.7, mix=0.5, multicrush=1.5, mclowdrive=1.5, mcmiddrive=1.5, mchighdrive=2.5, mclofreq=1200, mchifreq=2800, tube=0.5, tubegain=1.0, tubewarm=0.8, hard=var([0, 1, 2, 4], 8), nharm=2, fmamt=[0, 1, 2, 4], fmratio=12, strike=1, shimmer=2.0)
p1 >> ethpad([0, 1, 7], dur=8, oct=5, attack=4, release=4, amp=linvar([0, 0.32], 32), room=0.9, mix=0.6)

l1 >> loop("breakcore160_16", dur=16, sample=PRand(64), sbrk=fperlin(32, 0.3, 0.9), sbrkdur=PWhite(-4, 30), sbrkmix=1.0, t_reset=PRand(9), decimate=fi(48, 0, 0.7), decbits=PRand(0, 6), decrate=4000, multicrush=2.5, mclowdrive=1.5, mcmiddrive=2, mchighdrive=2.5, mclofreq=2000, mchifreq=4000, octafuz=fi(32, 0, 1), amp=0.85)

b1 >> dbass([0, 0, 0, -5, 0, 7, 0, -7], dur=PDur(7, 8), oct=5, sus=PDur(7, 8)*0.6, hpf=80, cutoff=fb(8, 600, 2400), rq=0.3, dist2=fb(24, 0.4, 1.4), tubedrive=0.6, tubewarm=0.5, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.2, amp=1.1)
a1 >> play("x-", dur=1, sample=var(P[0:10], 64), crush=fb(16, 0, 6), amp=PBern(8)*0.6).sometimes("stutter", PRand(8), rate=4).unison(3).sometimes("amen")
b1 >> dbass([0, 0, 0, -5, 0, 7, 0, -7], dur=PDur(7, 8), oct=6, bitrot=1.0, rotbits=6, rotrate=linvar([0.4, 0.8],16), rotjitter=0.1, sus=PDur(7, 8)*0.6, hpf=80, cutoff=fb(8, 600, 2400), rq=0.3, dist2=fb(24, 0.4, 1.4), tubedrive=0.6, tubewarm=0.5, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.2, amp=1.1, )
h1 >> play("-(--)-(--)-", dur=1/4, sample=PStep(8, 1, 3), rate=PWhite(0.95, 1.6), amp=PWhite(0.3, 0.55), pan=PWhite(-0.5, 0.5), tremolo=PRand([0.3, 0.5, 0.7]), tremolomix=0.6, formant=PRand(4)).degrade(0.2)
e1.stop()
k7 >> play("X ")


l2 >> loop("electrodrum16", dur=16, sample=(6, 5), comp=1, multicrush=2, mclowdrive=1.5, mcmiddrive=2, mchighdrive=2, mclofreq=200, mchifreq=4000, csweep=0.1, cswfreq=20, cswdepth=0.3, cswrate=0.01, cswdecay=0.5, sbrk=PWhite(0.2, 0.8), bpf=fb(24, 200, 2400), bpr=0.3, amp=0.7)
m1 >> compperc(PRand([0, 3, 5, 7, 10, 12, -2, -5]), dur=PDur(var([5, 7, 11], [8, 4, 4]), 8), sus=0.08, amp=0.5, tone=0.4, noise=0.4, body=0.3, metal=0.55, ring=0.5, comp=0.55, hpf=900, cheapverb=0.0, cvdecay=2.5, jpverb=0.4, jpsize=0.85, pan=PRand([-0.6, -0.25, 0.25, 0.6]))
s1 >> stretch("breakcore160_16", sample=PRand(8), dur=P[16, 32], sus=[16, 32], rate=PWhite(-1, 1), lpf=2200, amp=0.4, formant=PRand(4))

soloRnd()
# Server.addFx(decimate=var([0, 0.5], [14, 2]), decbits=4, decrate=4000, decsmooth=0)
# Server.addFx(decimate=var([0, 0.5], [14, 2]), decbits=4, decrate=4000, decsmooth=0)


b1 >> cbass([0, 0, -5, 0, -7, 0, 7, 0, -3, 0, 0, -5], dur=PDur(7, 8), oct=6, sus=PDur(7, 8)*0.7, hpf=80, cutoff=fb(8, 800, 3000), rq=0.35, dist2=fb(24, 0.6, 1.8), tubedrive=0.8, tubewarm=0.5, hpr=0.2, subenh=0.7, subhfreq=80, subhgain=1.5, dynfuzz=0.18, dfgain=1, dfatk=0.015, dfdec=0.4, dftone=0.7, amp=1.2)
~b1 >> dbass([0, 0, 0, -5, 0, 7, 0, -7], dur=PDur(7, 8), oct=6, bitrot=4.0, rotbits=12, rotrate=linvar([0.4, 0.8],16), rotjitter=0.1, sus=PDur(7, 8)*0.6, hpf=80, cutoff=fb(8, 600, 2400), rq=0.2, dist2=fb(24, 0.4, 1.4), tubedrive=0.6, tubewarm=0.5, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.2, amp=1.1, )
b1.dur=2

Clock.bpm = lininf(174, 87, 16)
Root.default = "F"
l1.stop()
l2.stop()
a1.stop()
h1.stop()
m1.stop()
s1.stop()
b1.stop()
k7.stop()

cx >> cs80([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=2, dur=4, sus=5, amp=sinvar([0.12,0.32],32), cutoff=sinvar([1000,3500],24), vibspeed=3.5, vibdepth=0.012, room=0.9, mix=0.8)
vc >> viola([0,-2,3,2,0,5,3,4], oct=5, dur=var([2,1,1,1,2,1,1,2],[2,1,1,1,2,1,1,2]), sus=var([1.8,0.8,0.8,0.8,1.8,0.8,0.8,1.8],[2,1,1,1,2,1,1,2]), amp=sinvar([0.15,0.35],24), room=0.9, mix=0.8, vibrato=sinvar([0,0.25],16))
br >> brass2([0,3,5,7,5,3,7,5, 0,3,5,7,9,7,5,3], oct=5, dur=var([1,0.5,0.5,1,0.5,0.5,1,2],[1,1,1,1,1,1,1,1]), sus=var([0.85,0.4,0.4,0.85,0.4,0.4,0.85,1.8],[1,1,1,1,1,1,1,1]), amp=sinvar([0.3,0.6],16), bright=0.75, growl=sinvar([0.1,0.45],16), vibrate=4.5, vibdepth=0.018, room=0.6, mix=0.5)

v1 >> viola([0, 3, 5, P*[7, 10, 5, 3]], dur=[P*[3, 5, 8], P*[2, 5], P*[8, 16]], oct=4, beat_dur=1, rate=1, mverb=0.95, blur=4, lpf=PRand(1000, 2400), hpf=300, amp=0.55).unison(3) + (-7, PStep(5, 7, 0))
b9 >> bell2([0, 7, 12, 4, 11], dur=24, oct=4, amp=0.65, atk=6, sus=20, lpf=linvar([300, 2200], 96), room=0.85, mix=0.7, multicrush=2, mclowdrive=2, mcmiddrive=2, mchighdrive=1, mclofreq=1200, mchifreq=2800, tube=0.6, tubegain=1.2, tubewarm=1.0, hard=var([0, 1, 2, 4, 8, 4, 2], 4), nharm=2, fmamt=[0, 0, 1, 1, 2, 4], fmratio=12, strike=1, shimmer=2.0)
p1 >> ethpad([0, 1, 7, 3], dur=12, oct=4, attack=6, release=6, amp=linvar([0.32, 0.55], 24), room=0.95, mix=0.7)
c1 >> compperc([0, 7, 12, 5, 10, 7, 3], dur=4, sus=1, amp=1, tone=0.3, noise=0.2, body=0.6, metal=1.0, ring=0.5, comp=0.6, hpf=100, jpverb=0.7, jpsize=0.95, jpdamp=0.3, pan=PWhite(-0.4, 0.4))

Clock.bpm = lininf(87, 174, 8)
Root.default = "C"
c1.stop()
br.stop()
vc.stop()
cx.stop()
v1 >> viola([0, 3, 5, P*[7, 10, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, mverb=0.85, blur=2, lpf=PRand(1200, 3000), hpf=300, amp=0.4).unison(2) + (-7, PStep(5, 7, 0))
b9 >> bell2([0, 7, 12, 4, 11], dur=12, oct=5, amp=0.55, atk=2, sus=10, lpf=linvar([400, 2800], 64), room=0.7, mix=0.5, multicrush=2, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=1200, mchifreq=2800, tube=0.5, tubegain=1.0, tubewarm=0.8)
l1 >> loop("breakcore160_16", dur=16, sample=PRand(64), sbrk=fperlin(32, 0.4, 1.0), sbrkdur=PWhite(-4, 40), sbrkmix=1.0, t_reset=PRand(9), decimate=fi(48, 0.2, 0.9), decbits=PRand(0, 8), decrate=fb(8, 2000, 8000), multicrush=3, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=2000, mchifreq=4000, octafuz=fi(32, 0.2, 1.5), chopwave=PRand(8), amp=1.0)

l2 >> loop("electrodrum16", dur=16, sample=(6, 6), comp=1, multicrush=3, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=200, mchifreq=4000, sbrk=PWhite(0.4, 1.0), bpf=fb(16, 200, 4000), bpr=0.5, spin=PRand([2, 4, 8, 16]), amp=0.85)
b1 >> cbass([0, 0, -5, 0, -7, 0, 7, 0, -3, 0, 0, -5], dur=PDur(7, 8), oct=6, sus=PDur(7, 8)*0.7, hpf=80, cutoff=fb(8, 800, 3000), rq=0.35, dist2=fb(24, 0.6, 1.8), tubedrive=0.8, tubewarm=0.5, hpr=0.2, subenh=0.7, subhfreq=80, subhgain=1.5, dynfuzz=0.18, dfgain=1, dfatk=0.015, dfdec=0.4, dftone=0.7, amp=1.2)
a1 >> play("x-(--)x", dur=1, sample=var(P[0:10], 64), crush=fb(8, 2, 8), amp=PBern(8)*0.8).often("stutter", PRand(8), rate=4).unison(3).often("amen")
m1 >> compperc(PRand([0, 3, 5, 7, 10, 12, -2, -5, 14]), dur=PDur(var([5, 7, 11, 13], [8, 4, 4, 4]), 8), sus=0.08, amp=0.6, tone=0.4, noise=0.5, body=0.3, metal=0.6, ring=0.5, comp=0.6, hpf=900, cheapverb=0.5, jpverb=0.5, jpsize=0.85, pan=PRand([-0.6, -0.25, 0.25, 0.6]))
h1 >> play("-(--)-(--)-([-=])-", dur=1/4, sample=PStep(8, 1, 3), rate=PWhite(0.95, 2.0), amp=PWhite(0.4, 0.65), pan=PWhite(-0.5, 0.5), tremolo=fb(16, 0.3, 0.8), tremolomix=0.7, formant=PRand(8)).degrade(0.15)
s1 >> stretch("breakcore160_16", sample=PRand(8), dur=P[8, 16, 32], sus=[8, 16, 32], rate=PWhite(-2, 2), lpf=fb(24, 800, 4400), amp=0.35, formant=PRand(8), spin=PRand([2, 4, 8]))

drop()

soloRnd()

u2 >> play("X ")
b1 >> dbass([0, 0, 0, -5, 0, 7, 0, -7], dur=PDur(7, 8), oct=6, bitrot=1.0, rotbits=6, rotrate=linvar([0.4, 0.8],16), rotjitter=0.1, sus=PDur(7, 8)*0.6, hpf=80, cutoff=fb(8, 600, 2400), rq=0.3, dist2=fb(24, 0.4, 1.4), tubedrive=0.6, tubewarm=0.5, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.2, amp=1.1, )

l1.stop()
l2.stop()
a1.stop()
m1.stop()
h1.stop()
b9.stop()

s1 >> stretch("breakcore160_16", sample=PRand(8), dur=P[16, 32], sus=[32, 64], rate=linvar([1, 0], 24), lpf=linvar([2200, 200], 24), amp=linvar([0.35, 0], 24), formant=linvar([0, 7], 24))
b1 >> dbass([0, 0, 0, -5], dur=PDur(7, 8), oct=4, sus=PDur(7, 8)*0.6, hpf=80, cutoff=linvar([2400, 200], 24), rq=0.3, dist2=linvar([1.4, 0], 24), tubedrive=0.5, tubewarm=0.7, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.0, amp=linvar([1.0, 0], 24))
v1 >> viola([0, 3, 5, P*[7, 10, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, mverb=linvar([0.85, 1], 32), blur=4, lpf=linvar([1800, 400], 32), hpf=300, amp=linvar([0.45, 0], 32)).unison(2) + (-7, PStep(5, 7, 0))
p1 >> ethpad([0, 1, 7], dur=8, oct=5, attack=4, release=4, amp=linvar([0.4, 0], 32), room=0.95, mix=0.7)
u2 >> play("X ")
b1 >> dbass([0, 0, 0, -5, 0, 7, 0, -7], dur=PDur(7, 8), oct=6, bitrot=1.0, rotbits=6, rotrate=linvar([0.4, 0.8],16), rotjitter=0.1, sus=PDur(7, 8)*0.6, hpf=80, cutoff=fb(8, 600, 2400), rq=0.3, dist2=fb(24, 0.4, 1.4), tubedrive=0.6, tubewarm=0.5, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.2, amp=1.1, )


~v2 >> loop("breakcore160_16", dur=16, sample=PRand(64), sbrk=fperlin(32, 0.3, 0.9), sbrkdur=PWhite(-4, 30), sbrkmix=1.0, t_reset=PRand(9), decimate=fi(48, 0, 0.7), decbits=PRand(0, 6), decrate=4000, multicrush=2.5, mclowdrive=1.5, mcmiddrive=2, mchighdrive=2.5, mclofreq=2000, mchifreq=4000, octafuz=fi(32, 0, 1), amp=0.85).only()

y7 >> loop("breakcore160_16", dur=16,sample=var(PRand(9009), [64, 64]), sbrk=0.0, sbrkdur=PWhite(-4, 30), sbrkmix=1.0,t_reset=PRand(9), decimate=0, decbits=PRand(0,6), decrate=4000, decsmooth=0, octclean=P*[0,PWhite()], ocsub=0.5, ocup=PWhite(0, 2))
y5 >> loop("breakcore155_16", dur=16,sample=var(PRand(9009), [64, 64]), sbrk=0.0, sbrkdur=PWhite(-4, 30), sbrkmix=1.0,t_reset=PRand(9), decimate=0, octclean=P*[0,PWhite()], ocsub=0.5, ocup=PWhite(0, 2))
h1 >> play("-(--)-(--)-", dur=1/4, sample=PStep(8, 1, 3), rate=PWhite(0.95, 1.6), amp=PWhite(0.3, 0.55), pan=PWhite(-0.5, 0.5), tremolo=PRand([0.3, 0.5, 0.7]), tremolomix=0.6, formant=PRand(4)).degrade(0.2)
d6 >> play("<x.><..o.><->", s=9, hpf=(50,0, PRand(400, 9500)), hpr=(0.4,0.5,0.5), amp=2).often("stutter", PRand(6), hpf=400)

# Server.addFx(glitch=4, glitchrate=8, glitchdepth=0.5, glitchcrush=0.3, glitchchance=0.5, beat_dur=1)
# Server.addFx(decimate=0.1)

b1.dur=1/2
l2 >> loop("electrodrum16", dur=16, sample=(6, 5), comp=1, multicrush=2, mclowdrive=1.5, mcmiddrive=2, mchighdrive=2, mclofreq=200, mchifreq=4000, csweep=0.1, cswfreq=20, cswdepth=0.3, cswrate=0.01, cswdecay=0.5, sbrk=PWhite(0.2, 0.8), bpf=fb(24, 200, 2400), bpr=0.3, amp=0.7)

s1 >> stretch("breakcore160_16", sample=PRand(8), dur=P[16, 32], sus=[16, 32], rate=PWhite(-1, 1), lpf=2200, amp=0.7, formant=PRand(4))
b9.stop()
p1.stop()
s1.stop()

m1 >> compperc(PRand([0, 3, 5, 7, 10, 12, -2, -5]), dur=PDur(var([5, 7, 11], [8, 4, 4]), 8), sus=0.08, amp=0.5, tone=0.4, noise=0.4, body=0.3, metal=0.55, ring=0.5, comp=0.55, hpf=900, cheapverb=0.0, cvdecay=2.5, jpverb=0.4, jpsize=0.85, pan=PRand([-0.6, -0.25, 0.25, 0.6]))

# Server.addFx(fshift=4)
y7 >> loop("breakcore160_16", dur=16,sample=var(PRand(9009), [64, 64]), sbrk=0.5, sbrkdur=PWhite(-4, 30), sbrkmix=1.0,t_reset=PRand(9), decimate=0, decbits=PRand(0,6), decrate=4000, decsmooth=0, octclean=P*[0,PWhite()], ocsub=0.5, ocup=PWhite(0, 2))

~y7 >> loop("breakcore160_16", dur=16, amp=2)

y5 >> loop("breakcore155_16", dur=16,sample=var(PRand(9009), [64, 64]), sbrk=0.5, sbrkdur=PWhite(-4, 30), sbrkmix=1.0,t_reset=PRand(9), decimate=0, octclean=P*[0,PWhite()], ocsub=0.5, ocup=PWhite(0, 2))
k5 >> loop("breakcore160_16", dur=16, sample=4, drcomp=0.5)

f0 >> play("X ", amp=2)
h1 >> play("-(--)-(--)-([-=])-", dur=1/4, sample=PStep(8, 1, 3), rate=PWhite(0.95, 2.0), amp=PWhite(0.4, 0.65), pan=PWhite(-0.5, 0.5), tremolo=fb(16, 0.3, 0.8), tremolomix=0.7, formant=PRand(8)).degrade(0.15)


drop()

v1.stop()
p1.stop()

v1.only()
l1.stop()
b9 >> bell2([0, 7, 12, 4, 11], dur=24, oct=5, amp=0.65, atk=6, sus=20, lpf=linvar([300, 2200], 96), room=0.85, mix=0.7, multicrush=2, mclowdrive=2, mcmiddrive=2, mchighdrive=3, mclofreq=1200, mchifreq=2800, tube=0.6, tubegain=1.2, tubewarm=1.0, hard=var([0, 1, 2, 4, 8, 4, 2], 4), nharm=2, fmamt=[0, 0, 1, 1, 2, 4], fmratio=12, strike=1, shimmer=2.0)
Server.addFx(fbdelay=1, fshift=12)

#
v1 >> viola([0, 3, 5, P*[7, 10, 5, 3]], dur=[P*[3, 5, 8], P*[2, 5], P*[8, 16]], beat_dur=1, rate=1, mverb=0.95, blur=4, lpf=PRand(1000, 2400), hpf=300, amp=0.55).unison(3) + (-7, PStep(5, 7, 0))

v1 >> viola([0, 3, 5, P*[7, 10, 5, 3]], dur=[P*[3, 5, 8], P*[2, 5], P*[8, 16]], beat_dur=1, rate=1, mverb=0.95, blur=4, lpf=PRand(1000, 2400), hpf=300, amp=0.55).unison(3).only() + (-7, PStep(5, 7, 0))
Server.addFx(fbdelay=1, fshift=12)
i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, dist2shape=0.0, dur=32,pos=0, amp=1, lpf=2000, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0).lclip(1)

# Server.addFx(fbdelay=1, fshift=12)
i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, lpf=3200, drcomp=0.1, mverb=0.0).lclip(2).only()
i1 >> loop("dubstepbass32", dist2=0.0, low=0, dist2mix=1, resonbank=0.2, rbfreq=72, rbdecay=0.5, rbspread=1.0, dist2shape=4.0, dur=32,pos=0, amp=1, room=0.0, sample=7, lpf=0, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0).lclip(8)
# Server.addFx(fbdelay=1, fshift=12)
i1 >> loop("dubstepbass32", dist2=0.0, low=0, dist2mix=1, resonbank=0.2, rbfreq=75, rbdecay=0.5, rbspread=1.0, dist2shape=4.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, shape=0.5, mverb=0.0).lclip(1)
~i1 >> loop("dubstepbass32", dist2=0.0, low=0, dist2mix=1, resonbank=0.2, rbfreq=75, rbdecay=0.5, rbspread=1.0, dist2shape=4.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, shape=0.5, mverb=0.0).lclip(1)

i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=.5, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0).lclip(var([2/3, 1, 1/3, 1]))
i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0).lclip(var([2/3, 1, 1/3, 1]))
i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, octclean=0.5, ocsub=0.5, ocup=0.3, mverb=0.0, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1).lclip(16)

e7 >> loop("psydrum16", dur=16, sample=7, amp=2)
~i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0, sbrk=0.0)
v2 >> play("X ", amp=2)

e7 >> loop("psydrum16", dur=16, sample=14)
c3 >> play("X ")
~i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, chop=4, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.1).lclip(var([2/3, 2, 1/3, 3]))
e7 >> loop("psydrum16", dur=16, sample=14).lclip(2)
# ~i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, chop=4, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.1, sample=6, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0).lclip(var([1/4, 1/2, 1/1, 3]))

e7 >> loop("psydrum16", dur=8, sample=23, high=4, hpf=400, sbrk=0.5).lclip(4)
c3.stop()
~i1 >> loop("dubstepbass32", dist2=0.0, low=2, dist2mix=1, chop=32, hpf=1200, dist2shape=0.0, dur=32,pos=0, amp=1, room=0.0, sample=7, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0).lclip(var([1/4, 1/2, 1/1, 3]))


a1.dur=1/2
a2.stop()
q5 >> subbass()
a1.oct=5
y9.stop()
a1.stop()
e7.stop()
i1.stop()
q5.stop()
a1.stop()
d1.stop()
d2.stop()
e9 >> loop("housebass24", dur=32, chop=0, sample=7, amp=0.5, hpf=0, fx1=0, a=0, octer=0, shift=0, octersub=à, octersubsub=1).unison(4).lclip(var([PRand([1,2,4,8])],32))

a1.oct=6
a1.stop()
~i1 >> loop("housebass24", dur=16, chop=0, sample=7, amp=0.5, hpf=0, fx1=0, a=0, octer=0, shift=0, octersub=à, octersubsub=1).unison(4).lclip(var([PRand([1,2,4,8])],32))
e9 >> loop("housebass24", dur=32, chop=0, sample=7, amp=0.5, hpf=0, fx1=0, a=0, octer=0, shift=0, octersub=à, octersubsub=1).unison(4).lclip(var([PRand([1,2,4,8])],32))
i1.stop()

b3 >> loop("noizebeat16", dur=16, sample=4)
h0 >> loop("gdrop8", pos=0, sample=0, dur=4)

z8 >> loop("gab16", dur=16)
z8 >> loop("gab8", dur=8, sample=4)

e9.lclip(0.5)
e9.fshift=2

e9.fshift=4

e9.fshift=[0, 4, 2]

b3.lclip(0.25)

e9.lpr=0.2
e9.lpf=linvar([400, 3200], 32)

b3.lpr=0.2
b3.lpf=linvar([400, 3200], 32)
x4 >> loop("ragedrum16", dur=32, sample=5, amp=1, comp=1, fx=1)
l2 >> noloop("vocalcrash8", dur=[16, 8, 4, 2], lofi=1, start=0.5, rate=1, sample=4)
e9.sample=var([4, 9], 8)
b3.sample=var([1, 2], 12)

b3.only()
b3.chop=4
b3.fbdelay=0.5
b3.dur=4
v2.lpf=400


6 >> play("<x.><.><..o.><k.>", sample=1, amp=1, bank=0).sometimes("stutter")
e9.sample=var([4, 5, 6, 7])
i1.stop()
e9.stop()
r9 >> loop("electrodrum16", dur=16, sample=3, comp=1)

p6.bank=1
~x4 >> play("x ", sample=3, amp=9)
e9 >> loop("housebass24", dur=32, chop=0, sample=7, amp=0.5, hpf=0, fx1=0).stop()

r4 >> play("X ", amp=4)

