# hajnal 174
# breakcore, idm, banger, venetiansnares
# Tempo war: 174 -> 87 (half-time chamber) -> 174.
# 7/8 PDur over 4/4 frame. Heavy Amen chopping (.sometimes("amen")),
# classical viola/bell2 (Rossz Csillag DNA), stretch reverse-rate samples,
# multiband multicrush + dynfuzz + octafuz, Bernoulli amplitude gating.

Clock.bpm = 174
Scale.default = "minor"
Root.default = "C"

#@strings(32) — viola + bell2 chamber emerges from nothing

v1 >> viola([0, 3, 5, P*[7, 10, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, blur=2, lpf=PRand(1200, 3000), hpf=300, amp=linvar([0, 0.5], 24)).unison(2) + (-7, PStep(5, 7, 0))
b9 >> bell2([0, 7, 12], dur=16, oct=5, amp=linvar([0, 0.55], 24), atk=4, sus=14, lpf=linvar([400, 2500], 64), room=0.7, mix=0.5, multicrush=1.5, mclowdrive=1.5, mcmiddrive=1.5, mchighdrive=2.5, mclofreq=1200, mchifreq=2800, tube=0.5, tubegain=1.0, tubewarm=0.8, hard=var([0, 1, 2, 4], 8), nharm=2, fmamt=[0, 1, 2, 4], fmratio=12, strike=1, shimmer=2.0)
p1 >> ethpad([0, 1, 7], dur=8, oct=5, attack=4, release=4, amp=linvar([0, 0.32], 32), room=0.9, mix=0.6)

#@break(48) — Amen explodes, 7/8 dbass over 4/4, glitch hat with tremolo

l1 >> loop("breakcore160_16", dur=16, sample=PRand(64), sbrk=fperlin(32, 0.3, 0.9), sbrkdur=PWhite(-4, 30), sbrkmix=1.0, t_reset=PRand(9), decimate=fi(48, 0, 0.7), decbits=PRand(0, 6), decrate=4000, multicrush=2.5, mclowdrive=1.5, mcmiddrive=2, mchighdrive=2.5, mclofreq=2000, mchifreq=4000, octafuz=fi(32, 0, 1), amp=0.85)
b1 >> dbass([0, 0, 0, -5, 0, 7, 0, -7], dur=PDur(7, 8), oct=4, sus=PDur(7, 8)*0.6, hpf=80, cutoff=fb(8, 600, 2400), rq=0.3, dist2=fb(24, 0.4, 1.4), tubedrive=0.6, tubewarm=0.5, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.2, amp=1.1)
a1 >> play("x-", dur=1, sample=var(P[0:10], 64), crush=fb(16, 0, 6), amp=PBern(8)*0.6).sometimes("stutter", PRand(8), rate=4).unison(3).sometimes("amen")
h1 >> play("-(--)-(--)-", dur=1/4, sample=PStep(8, 1, 3), rate=PWhite(0.95, 1.6), amp=PWhite(0.3, 0.55), pan=PWhite(-0.5, 0.5), tremolo=PRand([0.3, 0.5, 0.7]), tremolomix=0.6, formant=PRand(4)).degrade(0.2)

#@polymeter(48) — second drum loop with bpf sweep, pitched compperc melody, stretch swells

l2 >> loop("electrodrum16", dur=16, sample=(6, 5), comp=1, multicrush=2, mclowdrive=1.5, mcmiddrive=2, mchighdrive=2, mclofreq=200, mchifreq=4000, csweep=0.1, cswfreq=20, cswdepth=0.3, cswrate=0.01, cswdecay=0.5, sbrk=PWhite(0.2, 0.8), bpf=fb(24, 200, 2400), bpr=0.3, amp=0.7)
m1 >> compperc(PRand([0, 3, 5, 7, 10, 12, -2, -5]), dur=PDur(var([5, 7, 11], [8, 4, 4]), 8), sus=0.08, amp=0.5, tone=0.4, noise=0.4, body=0.3, metal=0.55, ring=0.5, comp=0.55, hpf=900, cheapverb=0.5, cvdecay=2.5, pan=PRand([-0.6, -0.25, 0.25, 0.6]))
s1 >> stretch("breakcore160_16", sample=PRand(8), dur=P[16, 32], sus=[16, 32], rate=PWhite(-1, 1), lpf=2200, amp=0.4, formant=PRand(4))

#@chamber(32) — TEMPO HALVES: drums die, viola+bell2 cry through jpverb cathedral

Clock.bpm = lininf(174, 87, 16)
Root.default = "F"

l1.stop()
l2.stop()
a1.stop()
h1.stop()
m1.stop()
s1.stop()
b1.stop()

v1 >> viola([0, 3, 5, P*[7, 10, 5, 3]], dur=[P*[3, 5, 8], P*[2, 5], P*[8, 16]], beat_dur=1, rate=1, blur=4, lpf=PRand(1000, 2400), hpf=300, amp=0.55).unison(3) + (-7, PStep(5, 7, 0))
b9 >> bell2([0, 7, 12, 4, 11], dur=24, oct=5, amp=0.65, atk=6, sus=20, lpf=linvar([300, 2200], 96), room=0.85, mix=0.7, multicrush=2, mclowdrive=2, mcmiddrive=2, mchighdrive=3, mclofreq=1200, mchifreq=2800, tube=0.6, tubegain=1.2, tubewarm=1.0, hard=var([0, 1, 2, 4, 8, 4, 2], 4), nharm=2, fmamt=[0, 0, 1, 1, 2, 4], fmratio=12, strike=1, shimmer=2.0)
p1 >> ethpad([0, 1, 7, 3], dur=12, oct=5, attack=6, release=6, amp=linvar([0.32, 0.55], 24), room=0.95, mix=0.7)
c1 >> compperc([0, 7, 12, 5, 10, 7, 3], dur=4, sus=2, amp=0.45, tone=0.3, noise=0.2, body=0.4, metal=0.3, ring=0.5, comp=0.4, hpf=400, pan=PWhite(-0.4, 0.4))

#@reexplode(64) — tempo back, EVERYTHING denser, dynfuzz on bass, octafuz on loop

Clock.bpm = lininf(87, 174, 8)
Root.default = "C"

c1.stop()

v1 >> viola([0, 3, 5, P*[7, 10, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, blur=2, lpf=PRand(1200, 3000), hpf=300, amp=0.4).unison(2) + (-7, PStep(5, 7, 0))
b9 >> bell2([0, 7, 12, 4, 11], dur=12, oct=5, amp=0.55, atk=2, sus=10, lpf=linvar([400, 2800], 64), room=0.7, mix=0.5, multicrush=2, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=1200, mchifreq=2800, tube=0.5, tubegain=1.0, tubewarm=0.8)
l1 >> loop("breakcore160_16", dur=16, sample=PRand(64), sbrk=fperlin(32, 0.4, 1.0), sbrkdur=PWhite(-4, 40), sbrkmix=1.0, t_reset=PRand(9), decimate=fi(48, 0.2, 0.9), decbits=PRand(0, 8), decrate=fb(8, 2000, 8000), multicrush=3, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=2000, mchifreq=4000, octafuz=fi(32, 0.2, 1.5), chopwave=PRand(8), amp=1.0)
l2 >> loop("electrodrum16", dur=16, sample=(6, 6), comp=1, multicrush=3, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=200, mchifreq=4000, sbrk=PWhite(0.4, 1.0), bpf=fb(16, 200, 4000), bpr=0.5, spin=PRand([2, 4, 8, 16]), amp=0.85)
b1 >> dbass([0, 0, -5, 0, -7, 0, 7, 0, -3, 0, 0, -5], dur=PDur(7, 8), oct=4, sus=PDur(7, 8)*0.7, hpf=80, cutoff=fb(8, 800, 3000), rq=0.35, dist2=fb(24, 0.6, 1.8), tubedrive=0.8, tubewarm=0.5, hpr=0.2, subenh=0.7, subhfreq=80, subhgain=1.5, dynfuzz=0.18, dfgain=1, dfatk=0.015, dfdec=0.4, dftone=0.7, amp=1.2)
a1 >> play("x-(--)x", dur=1, sample=var(P[0:10], 64), crush=fb(8, 2, 8), amp=PBern(8)*0.8).often("stutter", PRand(8), rate=4).unison(3).often("amen")
m1 >> compperc(PRand([0, 3, 5, 7, 10, 12, -2, -5, 14]), dur=PDur(var([5, 7, 11, 13], [8, 4, 4, 4]), 8), sus=0.08, amp=0.6, tone=0.4, noise=0.5, body=0.3, metal=0.6, ring=0.5, comp=0.6, hpf=900, cheapverb=0.5, pan=PRand([-0.6, -0.25, 0.25, 0.6]))
h1 >> play("-(--)-(--)-([-=])-", dur=1/4, sample=PStep(8, 1, 3), rate=PWhite(0.95, 2.0), amp=PWhite(0.4, 0.65), pan=PWhite(-0.5, 0.5), tremolo=fb(16, 0.3, 0.8), tremolomix=0.7, formant=PRand(8)).degrade(0.15)
s1 >> stretch("breakcore160_16", sample=PRand(8), dur=P[8, 16, 32], sus=[8, 16, 32], rate=PWhite(-2, 2), lpf=fb(24, 800, 4400), amp=0.35, formant=PRand(8), spin=PRand([2, 4, 8]))

#@outro(48) — strings carry, bass tail, breakcore evaporates through formant filter

l1.stop()
l2.stop()
a1.stop()
m1.stop()
h1.stop()
b9.stop()

s1 >> stretch("breakcore160_16", sample=PRand(8), dur=P[16, 32], sus=[32, 64], rate=linvar([1, 0], 24), lpf=linvar([2200, 200], 24), amp=linvar([0.35, 0], 24), formant=linvar([0, 7], 24))
b1 >> dbass([0, 0, 0, -5], dur=PDur(7, 8), oct=4, sus=PDur(7, 8)*0.6, hpf=80, cutoff=linvar([2400, 200], 24), rq=0.3, dist2=linvar([1.4, 0], 24), tubedrive=0.5, tubewarm=0.7, hpr=0.2, subenh=0.5, subhfreq=80, subhgain=1.0, amp=linvar([1.0, 0], 24))
v1 >> viola([0, 3, 5, P*[7, 10, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, blur=4, lpf=linvar([1800, 400], 32), hpf=300, amp=linvar([0.45, 0], 32)).unison(2) + (-7, PStep(5, 7, 0))
p1 >> ethpad([0, 1, 7], dur=8, oct=5, attack=4, release=4, amp=linvar([0.4, 0], 32), room=0.95, mix=0.7)

#@endfade(16)

s1.stop()
b1.stop()
v1.stop()
p1.stop()
