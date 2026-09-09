# tpl bass acid
# template

# Setup
Clock.bpm = 128
Scale.default = Scale.minor

# ===== CLASSIC ACID =====
# Simple TB-303 pattern
a1 >> tb303([0, 3, 7, 12], dur=1/4, oct=4, cutoff=1000, sus=0.3, amp=0.8)

# With resonance
a2 >> tb303([0, 3, 7, 12], dur=1/4, oct=4, cutoff=1200, res=0.8, sus=0.3, amp=0.8)

# ===== MOVING FILTER =====
# Classic filter sweep
a3 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=linvar([400, 3200], 32),res=0.7,amp=0.8)

# Pulsing cutoff
a4 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=var([600, 2400], 4),res=0.8,amp=0.8)

# ===== COMPLEX PATTERNS =====
# Longer sequence with rests
a5 >> tb303([0, _, 7, 3, _, 12, 7, _],dur=1/4,oct=4,cutoff=linvar([800, 2800], 16),res=0.7,amp=0.8)

# Random note selection
a6 >> tb303(PRand([0, 3, 7, 12]),dur=1/4,oct=4,cutoff=linvar([600, 2400], 32),res=0.8,amp=0.7)

# ===== VARIABLE OCTAVES =====
# Octave jumps
a7 >> tb303([0, 7, 0, 12],dur=1/4,oct=var([4, 5], [8, 4]),cutoff=linvar([800, 2400], 24),res=0.7)

# Random octave variation
a8 >> tb303([0, 3, 7],dur=1/4,oct=PRand([3, 4, 5]),cutoff=linvar([600, 3200], 32),res=0.8)

# ===== RHYTHMIC VARIATIONS =====
# Euclidean rhythm
a9 >> tb303([0, 3, 7],dur=PDur(5, 8),oct=4,cutoff=linvar([800, 2800], 32),res=0.7)

# Variable duration
a10 >> tb303([0, 3, 7, 12],dur=var([1/4, 1/8], [7, 1]),oct=4,cutoff=linvar([1000, 2800], 24),res=0.8)

# ===== SLIDE/GLIDE =====
# Sliding between notes
a11 >> tb303([0, 7, 12, 7],dur=1/4,oct=4,slide=0.15,cutoff=linvar([800, 2400], 32),res=0.7)

# Variable slide
a12 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,slide=var([0, 0.2], [7, 1]),cutoff=linvar([1000, 2800], 32))

# ===== HIGH-PASS FILTER =====
# Combined filters for darker sound
a13 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=linvar([800, 2400], 32),res=0.7,hpf=linvar([200, 2400], 64),hpr=0.4)

# ===== DISTORTION/DRIVE =====
# Overdriven acid
a14 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=linvar([1000, 2800], 32),res=0.8,shape=0.4,shape=0.3)

# Heavy distortion
a15 >> tb303([0, 7, 12],dur=1/4,oct=4,cutoff=linvar([600, 2400], 24),res=0.7,dist2=0.6)

# ===== VARIABLE RESONANCE =====
# Moving resonance
a16 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=linvar([800, 2800], 32),res=linvar([0.3, 0.9], 16))

# ===== COMPLEX MODULATION =====
# Multiple parameters moving
a17 >> tb303(var([0, [0, 3, 7, 12]], [8, 4]),dur=1/4,oct=var([4, 5], [16, 8]),cutoff=linvar([600, 2800], 32),res=linvar([0.5, 0.9], 24),hpf=linvar([200, 2400], 64),hpr=0.4,shape=linvar([0, 0.5], 64))

# ===== LAYERED ACID =====
# Low acid
q2 >> tb303([0], dur=1, oct=3, cutoff=800, res=0.5, amp=0.8)

# High moving acid
q1 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=linvar([1000, 3200], 32),res=0.8,amp=0.6)

# ===== STEREO ACID =====
# Stereo spread acid
a18 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=linvar([800, 2800], 32),res=0.7,pan=linvar([-1, 1], 16)).unison(2)

# ===== STUTTERING ACID =====
# Random stutters
a19 >> tb303([0, 3, 7, 12],dur=1/4,oct=4,cutoff=linvar([1000, 2800], 32),res=0.8).sometimes("stutter", PRand([2, 4]))

# ===== CONTROL TIPS =====
# Gradually open filter
# a1.cutoff = linvar([400, 3200], 64)

# Increase resonance
# a1.res = linvar([0.3, 0.9], 32)

# Add drive gradually
# a1.drive = linvar([0, 0.6], 64)

# Random pattern variation
# a1.degree = PRand([0, 3, 7, 12])
