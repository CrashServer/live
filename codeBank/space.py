# spacesounds # 120
# space

#workinprogress
Clock.bpm = 120
Scale.default = "minor"
Root.default = "C#"

s1 >> loop("sundrone16", dur=8, amp=linvar([0.4, 0.6], 32), shimmer=0.4, shimmix=0.3)
# Sun p-mode oscillations (SOHO/SDO helioseismology) ~C3
q1 >> loop("quake8", dur=8, amp=0.8, lpf=1200, tape=0.6, echo=0.5, tapedrive=0.6)
# Marsquake Mw3.3 (InSight SEIS seismometer Sol 235, sped up 100x) ~A1
s3 >> loop("whitedwarf16", dur=16, amp=0.9, hpf=1200, rgate=0.2, chop=4, mverb=0.0).lclip(4)
s1.dur=4
q1.dur=4
# GD358 white dwarf pulsation (g-modes) ~C#4 — forms natural C# minor triad
s4 >> loop("solrot16", dur=8, amp=1.0, lpf=800, bpf=800, hpf=2400, mverb=0.5)
# Solar rotation 2.2Hz beat (SOHO MDI l=20 m=±20) ~F#4

q1.dur=4
s3.dur=8

p1 >> sinepad(dur=PDur(3,8), degree=[0, 2, 4], oct=6, amp=linvar([0.5, 1], 16), sus=var([0.5, 1, 1], 8), atk=0.2, lpf=linvar([800, 3000], 64), mverb=0.2, hpf=1800).unison(3)

s1.hpf=1200
s2 >> loop("centauri16", dur=8, amp=0.7, cheapverb=0.6, fshift=2, hpf=1600)
# Alpha Centauri A oscillation (ESO CORALIE spectroscopy) ~G#3/A3

r3 >> loop("spherics16", dur=16, amp=0.8, lpf=linvar([400, 6000], 32)).unison(5)
# Atmospheric lightning crackles (Halley Station Antarctica VLF) ~C4

z6 >> ikea(hhat=0.1, sn=0.1, harm=0, mverb=0.5, a=0.5, dur=8, tape=0.5, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1)
s4 >> loop("sundrone16", dur=8, amp=1, shimmer=0.5, shimmix=0.4, fshift=1, hpf=1200)

b0 >> play("X ", dur=4, mverb=0.5, lpf=200)
s5 >> loop("sundrone16", dur=8, delay=4, echo=2, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, amp=1, shimmer=0.5, shimmix=0.4, fshift=1, hpf=1200)

# Sun p-mode oscillations 
t1 >> loop("carina16", dur=8, amp=var([0, 0.4, 0, 0.5], [8, 8, 12, 4]), clouds=0.3, csize=0.4, cdens=0.6)
# JWST Carina Nebula infrared sonification ~F4/F5
r2 >> loop("whistler16", dur=8, amp=1, echo=0.6, echotime=2, lpf=3000)

p2 >> organ(dur=PDur(3,8), degree=[0, 2, 4], oct=4, amp=linvar([0.5, 1], 16), sus=var([1, 0.5, 1], 8), atk=0.2, lpf=linvar([800, 3000], 64), mverb=0.7).only()

masterAll("dur", 8)
r1 >> loop("chorus16", dur=8, amp=var([0, 0.35, 0, 0.4], [8, 4, 12, 8]), high=4)
# Earth magnetosphere chorus — bird-like chirps (Halley VLF) ~F#3
s5 >> loop("solmodes16", dur=16, amp=0.3, mverb=0.7)

f1 >> loop("flares16", dur=16, amp=1, dist2=0.4, dist2mix=0.8, hpf=200, lpf=1600, mverb=0.5)
# X17/X28 solar flare Type III radio bursts (Cassini RPWS 2003) ~B4/C5
r4 >> loop("satlightning16", dur=16, amp=0.5, dist2=0.0, mverb=0.5, dist2mix=1, dist2shape=0.5)
# Saturn lightning radio (Cassini RPWS) — 10,000x more powerful than Earth ~D4
# 3 solar p-modes chord (224/253/280 Hz, SOHO MDI) ~C#4
t4 >> loop("ganymede16", dur=16, amp=0.3, mverb=0.5, lpf=linvar([600, 4000], 32))
# Ganymede magnetosphere flyby (Juno Waves 2021) — "dial-up from space" ~E6

x2 >> loop("exoplanet16", dur=16, amp=0.7, jpverb=0.4, jpmix=0.3)
# WASP-96b exoplanet atmosphere spectrum — descending melody with water drops (JWST NIRISS) ~C6

s1 >> loop("sundrone16", dur=8, amp=0.8, shimmer=0.6, shimmix=0.5, fshift=2)

b1 >> dbass(dur=PDur(3, 8), degree=[0, 0, 3, 0, 5, 0, 3, 7], oct=4, amp=0.9, sus=var([0.3, 0.6, 0.2, 1], 4), shape=var([0, 0.4, 0, 0.6], [8, 4, 12, 4]), lpf=linvar([400, 2000], 32)).unison(8)

f1.stop()
p2.stop()
x2.stop()
r4.stop()
s5.stop()
x3 >> loop("aurora16", dur=16, amp=0.35, cheapverb=0.5).unison(4)
# Jupiter auroral bKOM radio (Juno Waves 2016) ~B5

t3 >> loop("crab16", dur=16, amp=var([0, 0.4], [8, 8]), clouds=0.5, csize=0.6, cdens=0.3, cmode=1)
# Crab Nebula X-ray sweep with pulsar bell (Chandra + NuSTAR) ~C#6/F#4

j3 >> varsaw(dur=PDur(3, 8, 2), degree=[0, 4, 7, 9, 11, 7, 4, 0], oct=5, amp=0.2, sus=[1, 0.5, 2, 0.5, 1, 2, 0.5, 1], rq=linvar([0.1, 0.01], 16), mverb=0.6, shimmer=0.4)

m1 >> loop("mars16", dur=16, amp=0.6, lpf=linvar([300, 2000], 32), sample=1).only()
# Mars wind recorded by Perseverance SuperCam mic — actual sound from another planet

