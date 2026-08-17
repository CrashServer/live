# Space proto

# Sun p-mode oscillations (SOHO/SDO helioseismology) ~C3
~s1 >> loop("sundrone16", dur=8, amp=linvar([0.4, 0.6], 32), shimmer=0.4, shimmix=0.3)

 # GD358 white dwarf pulsation (g-modes) ~C#4 — forms natural C# minor triad
s3 >> loop("whitedwarf16", dur=8, amp=0.9, hpf=2400, rgate=0.6, chop=4, mverb=0.0).lclip(0)



q1.dur=4
s3.dur=8

s1.hpf=1200
# Alpha Centauri A oscillation (ESO CORALIE spectroscopy) ~G#3/A3
s2 >> loop("centauri16", dur=8, amp=0.7, cheapverb=0.6, fshift=2, hpf=1600)

# Atmospheric lightning crackles (Halley Station Antarctica VLF) ~C4
# r3 >> loop("spherics16", dur=16, amp=0.8, lpf=linvar([400, 6000], 32)).unison(5)

# s4 >> loop("sundrone16", dur=8, amp=1, shimmer=0.5, shimmix=0.4, fshift=1, hpf=1200)

s5 >> loop("sundrone16", dur=8, delay=4, echo=2, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, amp=1, shimmer=0.5, shimmix=0.4, fshift=1, hpf=1200)

# Sun p-mode oscillations 

# JWST Carina Nebula infrared sonification ~F4/F5
# t1 >> loop("carina16", dur=8, amp=var([0.2, 0.4, 0.3, 0.5], [8, 8, 12, 4]), clouds=0.5, csize=PWhite(0.1,.8), cdens=0.6, ctex=PWhite(.4, .8),cmode=2, blur=2, resonbank=0.2, rbfreq=PFr(20, 1200), rbdecay=0.5, rbspread=1.0, wshape=4, wgain=1, wmix=0.5)

r2 >> loop("whistler16", dur=8, amp=1, echo=0.6, echotime=2, lpf=3000)
# r1 >> loop("chorus16", dur=8, amp=var([0, 0.35, 0, 0.4], [8, 4, 12, 8]), high=4)
# Earth magnetosphere chorus — bird-like chirps (Halley VLF) ~F#3
s5 >> loop("solmodes16", dur=16, amp=0.3, mverb=0.7)


# Saturn lightning radio (Cassini RPWS) — 10,000x more powerful than Earth ~D4
# r5 >> loop("satlightning16", dur=64, hpf=1200, amp=1, dist2=0.8, cheapverb=0.2, cvdecay=1.5, cvdamp=0.5,  mverb=0.2, dist2mix=1, dist2shape=0.05)

# 3 solar p-modes chord (224/253/280 Hz, SOHO MDI) ~C#4


# Ganymede magnetosphere flyby (Juno Waves 2021) — "dial-up from space" ~E6
t4 >> loop("ganymede16", dur=16, amp=0.6, mverb=0.5, lpf=linvar([600, 4000], 32))

# d8 >> loop("xtech8", dur=8, sample=4)

# WASP-96b exoplanet atmosphere spectrum — descending melody with water drops (JWST NIRISS) ~C6
# x2 >> loop("exoplanet16", dur=16, amp=0.7, jpverb=0.4, jpmix=0.3)





f1.stop()
p2.stop()
x2.stop()
r4.stop()
s5.stop()

# Jupiter auroral bKOM radio (Juno Waves 2016) ~B5
x3 >> loop("aurora16", dur=16, amp=0.35, cheapverb=0.2, hpf=2400, shift=0.5).unison(4)

# Crab Nebula X-ray sweep with ulsar bell (Chandra + NuSTAR) ~C#6/F#4
t3 >> loop("crab16", dur=16, amp=var([0, 0.4], [8, 8]), clouds=0.25, csize=0.6, cdens=0.1, cmode=1)


#@#@CHANSON
##### MARS 
# Mars wind recorded by Perseverance SuperCam mic — actual sound from another planet
m1 >> loop("mars16", dur=16, amp=0.9, lpf=linvar([300, 2000], 32), sample=1)
m2 >> loop("mars16", dur=PRand(16,32), amp=0.9, lpf=linvar([3300, 6000], 32), sample=0, lofi=PWhite(.1, 0.7), hpf=300) 
# Marsquake Mw3.3 (InSight SEIS seismometer Sol 235, sped up 100x) ~A1 # rumble, noise
# q1 >> loop("quake8", dur=8, amp=0.8, lpf=PFr(1200, 4000), tape=0.6, echo=0.5, tapedrive=0.6 ,eb=4, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.5, ebflutter=15, ebsat=0.3)

#### SOL
# X17/X28 solar flare Type III radio bursts (Cassini RPWS 2003) ~B4/C5
f1 >> loop("flares16", dur=8, amp=PCoin(0, 1, .2), dist2=0.4, sample=PRand(9), dist2mix=0.8, hpf=200, lpf=1600, mverb=0.5, lpf_=12000)
s1 >> loop("sundrone16", dur=8, amp=0.8, shimmer=0.6, shimmix=0.5, sgate=.5, sgthresh=1, sgmode=0 )
# s4 >> loop("solrot16", dur=4, sample=1, amp=1.0, lpf=710, bpf=0, hpf=0, mverb=0.5, octer=1, octersub=5, octersubsub=5, leg=128,valad=500, valadr=0.6, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, valadd=5, valadt=0, valadc=0.2, rgate=0.5, rgaterate=4, rgatewave=.2, beat_dur=1, wshape=4, wgain=1, wmix=0.5)
# Solar rotation 2.2Hz beat (SOHO MDI l=20 m=±20) ~F#4
