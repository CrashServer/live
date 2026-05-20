# spacesounds
# experimental

# ============================================================
# SPACE SOUNDS — Scientific Data Live Coding Set (v2)
# Key: C# minor → D → E → C# (harmonic movement)
# BPM: 120
# All loops from real NASA/ESA/LIGO/BAS scientific data
# Rewrite: f-family modulation, structured arc, Root shifts
# ============================================================

Clock.bpm = 120
Scale.default = "minor"
Root.default = "C#"

#@intro(32)
# -- Sun drone fades in with shimmer reverb --
s1 >> loop("sundrone16", dur=16, amp=fi(32, 0, 0.6), shimmer=fi(32, 0.1, 0.5), shimmix=fb(16, 0.2, 0.4))
# Sun p-mode oscillations (SOHO/SDO helioseismology) ~C3

# -- Marsquake sub-rumble --
q1 >> loop("quake8", dur=8, amp=0.4, lpf=fbn(32, 80, 250), tape=0.3, tapedrive=fb(16, 0.2, 0.5))
# Marsquake Mw3.3 (InSight SEIS seismometer Sol 235, sped up 100x) ~A1

#@build(32)
# -- White dwarf beating + solar rotation tremolo --
s3 >> loop("whitedwarf16", dur=16, amp=fi(16, 0.2, 0.45), mverb=0.3, mverbfreeze=fh(8, [0, 0, 0.4, 0.8]))
# GD358 white dwarf pulsation (g-modes) ~C#4

s4 >> loop("solrot16", dur=16, amp=fi(16, 0.15, 0.35), cheapverb=fb(24, 0.3, 0.7))
# Solar rotation 2.2Hz beat (SOHO MDI l=20 m=±20) ~F#4

# -- Pad follows the drones with Perlin movement --
p1 >> sinepad(dur=PDur(3,8), degree=[0, 2, 4], oct=5, amp=fi(16, 0, 0.25), sus=fperlin(8, 1, 4), atk=1, lpf=fb(32, 800, 3200), mverb=0.5)

# -- Spherics crackle rises --
r3 >> loop("spherics16", dur=16, amp=fi(16, 0.1, 0.35), lpf=fb(32, 400, 6000))
# Atmospheric lightning crackles (Halley Station Antarctica VLF) ~C4

#@peak(64)
# -- Full drone stack --
s1 >> loop("sundrone16", dur=16, amp=0.5, shimmer=fs(8, 0.3, 0.6), shimmix=0.4, fshift=fb(32, 1, 3))
s2 >> loop("centauri16", dur=16, amp=0.35, cheapverb=0.6, fshift=fb(32, -3, -1))
# Alpha Centauri A oscillation (ESO CORALIE spectroscopy) ~G#3/A3

s5 >> loop("solmodes16", dur=16, amp=0.3, mverb=fb(16, 0.2, 0.5))
# 3 solar p-modes chord (224/253/280 Hz, SOHO MDI) ~C#4

# -- Nebula textures with breathing --
t1 >> loop("carina16", dur=16, amp=fh(8, [0, 0.4, 0, 0.5]), clouds=fb(16, 0.2, 0.5), csize=0.4, cdens=fs(16, 0.3, 0.7))
# JWST Carina Nebula infrared sonification ~F4/F5

t4 >> loop("ganymede16", dur=16, amp=0.35, mverb=0.5, lpf=fb(32, 600, 4500))
# Ganymede magnetosphere flyby (Juno Waves 2021) ~E6

# -- cs80 melody with Perlin filter --
j1 >> cs80(dur=PDur(5, 8), degree=frot(P[0, 2, 4, 7, 9], 16), oct=fh(16, [5, 6, 5, 6]), amp=fh(16, [0, 0.2, 0.3, 0.15]), sus=fperlin(8, 0.3, 2), atk=0.2, cutoff=fb(32, 2000, 6000), detune=0.3, lpf=4000, mverb=0.4, shimmer=fh(12, [0, 0.3]))

# -- Magnetosphere chorus + whistler layers --
r1 >> loop("chorus16", dur=16, amp=fh(8, [0, 0.35, 0, 0.4]))
# Earth magnetosphere chorus — bird-like chirps (Halley VLF) ~F#3
r2 >> loop("whistler16", dur=16, amp=0.25, echo=fs(16, 0.3, 0.7), echotime=2, lpf=3000)
# Earth VLF whistlers — lightning along magnetic field lines ~C4

# -- Drums emerge from space noise --
d1 >> play("x  x  x   x    ", dur=0.5, amp=fi(48, 0, 0.5), lpf=200, shape=0.3)
d2 >> play(" h hh  h hh h h", dur=0.25, amp=PWhite(0.15, 0.35), hpf=6000, pan=PRand([-0.3, 0, 0.3]))

#@drop(64)
# -- Solar flare burst + saturn lightning --
Root.default = "D"
f1 >> loop("flares16", dur=16, amp=0.5, dist2=fb(16, 0.2, 0.5), dist2mix=0.8, hpf=200)
# X17/X28 solar flare Type III radio bursts (Cassini RPWS 2003) ~B4/C5
r4 >> loop("satlightning16", dur=16, amp=0.5, dist2=0.5, dist2mix=1, dist2shape=-0.9)
# Saturn lightning radio (Cassini RPWS) ~D4

# -- Bass kicks in with drunk walk degree --
b1 >> dbass(dur=PDur(3, 8), degree=fd(16, 1, 7), oct=5, amp=0.5, sus=fperlin(8, 0.2, 1), shape=fh(8, [0, 0.4, 0, 0.6]), lpf=fb(32, 400, 2200))

# -- plaitsX morphing lead --
j2 >> plaitsX(dur=PBal("clave")*0.5, degree=melody(), oct=fh(16, [5, 6]), amp=fh(8, [0, 0.3, 0.35, 0.15]), sus=fperlin(8, 0.3, 1), preset=fh(16, [0, 3, 5]), porta=fb(32, 0, 0.4), mverb=0.5, shimmer=fh(8, [0, 0.3]))

# -- Exoplanet floats --
x2 >> loop("exoplanet16", dur=16, amp=0.3, jpverb=fb(16, 0.2, 0.5), jpmix=0.3)
# WASP-96b exoplanet atmosphere spectrum (JWST NIRISS) ~C6

# -- Full drums with swing --
d1 >> play("X   x X   x X  x", dur=0.25+PSwing(0.02), amp=0.6, lpf=300, shape=0.4)
d2 >> play(".h.hh..h.hh.h.h", dur=0.25, amp=PWhite(0.15, 0.3), hpf=5000, pan=PRand([-0.3, 0, 0.3]))
d3 >> play("  o       s     ", dur=0.25, amp=Pacc("backbeat"), lpf=4000)

#@break(32)
# -- Strip to bells + aurora + crab, Root shift --
Root.default = "E"
s1 >> loop("sundrone16", dur=16, amp=0.3, shimmer=fb(16, 0.4, 0.8), shimmix=0.5, fshift=2)
x1 >> loop("solarbells16", dur=16, amp=0.5, echo=fs(8, 0.2, 0.6), echotime=1, mverb=0.4)
# Helios solar energetic particle flux sonified as bells ~A3/A4/A5

x3 >> loop("aurora16", dur=16, amp=0.35, cheapverb=fb(16, 0.3, 0.7)).unison(4)
# Jupiter auroral bKOM radio (Juno Waves 2016) ~B5

t3 >> loop("crab16", dur=16, amp=fh(8, [0, 0.4]), clouds=fb(12, 0.3, 0.6), csize=0.6, cdens=0.3, cmode=1)
# Crab Nebula X-ray sweep with pulsar bell (Chandra + NuSTAR) ~C#6/F#4

# -- angel melody with rotating degree --
j3 >> angel(dur=PDur(3, 8, 2), degree=frot(P[0, 4, 7, 9, 11], 8), oct=5, amp=0.2, sus=fperlin(8, 0.5, 2.5), rq=fb(16, 0.01, 0.1), mverb=0.6, shimmer=fs(16, 0.2, 0.5))

# -- Mars wind as texture --
m1 >> loop("mars16", dur=16, amp=0.25, lpf=fb(32, 300, 2000), sample=1)
# Mars wind — actual sound from another planet (Perseverance SuperCam)

# -- Minimal percussion --
d1 >> play("x       x       ", dur=0.25, amp=0.35, lpf=150)

#@peak2(64)
# -- Everything returns, Root to C# for final push --
Root.default = "C#"

s1 >> loop("sundrone16", dur=16, amp=0.5, shimmer=fs(8, 0.3, 0.6), shimmix=0.4, fshift=2)
s3 >> loop("whitedwarf16", dur=16, amp=0.4, mverb=fb(16, 0.2, 0.4))
t2 >> loop("nebula16", dur=16, amp=0.4, spectralfreeze=fh(12, [0, 0, 0, 1]), freezemix=0.5)
# Southern Ring Nebula MIRI mid-infrared — dying star (JWST) ~F2/C#4

t4 >> loop("ganymede16", dur=16, amp=0.35, mverb=0.5, lpf=fb(32, 800, 5000))

# -- Binary black hole chirp as riser --
g1 >> loop("space16", dur=16, amp=fh(16, [0, 0.5, 0, 0.6]), hpf=100, dist2=fb(16, 0.1, 0.4))
# Precessing binary black hole gravitational wave simulation (spin 0.99) ~A#1

# -- Acid bass with Perlin cutoff --
b2 >> tb303(dur=PDur(5, 8), degree=frot(P[0, 3, 5, 7], 8), oct=5, amp=0.45, sus=fperlin(8, 0.2, 0.8), rate=fb(32, 1, 4), cutoff=fperlin(32, 400, 3500), rq=0.2, shape=fh(6, [0, 0.3]))

# -- cs80 lead with fractal degree --
j1 >> cs80(dur=PBal("swing")*0.5, degree=ff(16, 0, 9), oct=fh(8, [5, 6]), amp=fh(24, [0.2, 0.3, 0]), sus=fperlin(8, 0.3, 2), cutoff=fs(32, 2000, 8000), detune=0.4, mverb=0.5, shimmer=fh(8, [0, 0.4]))

# -- Full drums with variation --
d1 >> play("X..X..X.X..X..X.", dur=0.25+PSwing(0.02), amp=0.6, shape=0.4)
d2 >> play(".h.hh.hh.h.hh.h", dur=0.25, amp=PWhite(0.15, 0.35), hpf=5000, pan=PRand([-0.3, 0, 0.3]))
d3 >> play("    s       s   ", dur=0.25, amp=Pacc("backbeat"), shape=0.2)
d4 >> play("  [--]    [--]  ", dur=0.25, amp=0.2, hpf=8000)

#@endfade(32)
# -- Dissolve to drones only --
s1 >> loop("sundrone16", dur=16, amp=fo(32, 0, 0.5), shimmer=fi(32, 0.3, 0.9), shimmix=0.5, fshift=2)
# Sun — still burning

s5 >> loop("solmodes16", dur=16, amp=fo(32, 0, 0.3), mverb=0.6)
# Solar harmonics fading

x1 >> loop("solarbells16", dur=16, amp=fo(32, 0, 0.4), echo=fi(32, 0.3, 0.8), echotime=2, mverb=0.6)
# Last bells from the Helios particle wind

q1 >> loop("quake8", dur=8, amp=fo(32, 0, 0.3), lpf=fo(32, 50, 150))
# Mars rumbles to silence
