# tpl bass rhythmic
# template

# Setup
Clock.bpm = 128
Scale.default = Scale.minor

# ===== FAST RHYTHMIC BASS =====
# 16th note pattern
b1 >> lbass([0, 0, 0, 2, 0, 0, 4, 2],dur=1/4,oct=4,amp=0.7,cutoff=1200,sus=0.2)

# Euclidean rhythm
b2 >> lbass([0, 2, 4],dur=PDur(5, 8),oct=4,amp=0.8,cutoff=1400,sus=0.3)

# ===== SYNCOPATED PATTERNS =====
# Off-beat bass
b3 >> lbass([_, 0, _, 2, _, 0, _, 4],dur=1/4,oct=4,amp=0.8,cutoff=1200)

# Syncopated with variation
b4 >> lbass([0, _, 0, 2, _, 2, _, 0],dur=1/4,oct=4,cutoff=var([1000, 1600], 4),amp=0.7)

# ===== VARIABLE DURATION =====
# Mixed note lengths
b5 >> lbass([0, 0, 2, 0, -2, 0, 4, 2],dur=var([1/4, 1/8], [7, 1]),oct=4,amp=0.8,cutoff=1400)

# Complex rhythm
b6 >> lbass([0, 2, 4, 2],dur=[1/2, 1/4, 1/4, 1/2],oct=4,amp=[0.9, 0.6, 0.7, 0.9],cutoff=1200)

# ===== ACCENTED PATTERNS =====
# Velocity/amp accents
b7 >> lbass([0, 0, 0, 2, 0, 0, 0, 4],dur=1/4,oct=4,amp=[1.0, 0.5, 0.6, 0.8, 0.5, 0.6, 0.5, 0.9],cutoff=1200)

# Filter accents
b8 >> lbass([0, 0, 2, 0],dur=1/4,oct=4,amp=0.8,cutoff=[1600, 800, 1200, 800],sus=0.3)

# ===== STACCATO BASS =====
# Short, punchy notes
b9 >> lbass([0, _, 2, _, 0, _, 4, _],dur=1/4,oct=4,sus=0.1,amp=0.9,cutoff=1400)

# Very short notes
b10 >> lbass([0, 2, 4, 2],dur=1/4,oct=4,sus=0.05,amp=1.0,cutoff=1600,leg=0)

# ===== BOUNCING BASS =====
# Bouncy rhythm
b11 >> lbass([0, 0, _, 2, _, 0, 2, _],dur=1/4,oct=4,amp=0.8,cutoff=linvar([1000, 1600], 16),sus=0.2)

# ===== OCTAVE JUMPS =====
# Jumping octaves rhythmically
b12 >> lbass([0, 0, 2, 2],dur=1/4,oct=[4, 5, 4, 5],amp=0.8,cutoff=1400)

# Variable octave pattern
b13 >> lbass([0, 2, 4],dur=1/4,oct=var([4, 5, 6], [8, 4, 4]),amp=0.7,cutoff=1200)

# ===== PERCUSSIVE BASS =====
# Very short, percussive
b14 >> lbass([0, _, _, 2, _, _, 0, _],dur=1/4,oct=5,sus=0.05,amp=0.9,cutoff=800,hpf=400)

# High-passed rhythmic bass
b15 >> lbass([0, 2, 0, 4],dur=1/4,oct=5,amp=0.8,hpf=linvar([400, 1200], 32),cutoff=1600)

# ===== FOLLOWING KICK =====
# Bass follows kick pattern (define k1 first)
# k1 >> play("x.x.x..x", sample=0)
# b16 >> lbass(dur=1/2, oct=4, amp=0.8, cutoff=1200).follow(k1, 2)

# ===== WITH SLIDES =====
# Sliding rhythmic bass
b17 >> lbass([0, 2, 4, 7],dur=1/4,oct=4,slide=0.1,amp=0.8,cutoff=1400,sus=0.3)

# Variable slide
b18 >> lbass([0, 2, 0, 4],dur=1/4,oct=4,slide=var([0, 0.15], [7, 1]),amp=0.8,cutoff=1200)

# ===== DISTORTED RHYTHMIC =====
# Distorted fast bass
b19 >> lbass([0, 0, 2, 0, 0, 4, 2, 0],dur=1/4,oct=4,amp=0.7,cutoff=1200,shape=0.4,shape=0.3,sus=0.2)

# ===== FILTERED RHYTHM =====
# Moving filter on rhythm
b20 >> lbass([0, 2, 4, 2],dur=1/4,oct=4,amp=0.8,cutoff=linvar([600, 2400], 32),lpr=linvar([0.1, 0.5], 16),sus=0.3)

# ===== STEREO RHYTHMIC =====
# Panned rhythmic bass
b21 >> lbass([0, 2, 0, 4],dur=1/4,oct=4,amp=0.8,cutoff=1400,pan=[-0.5, 0.5, -0.5, 0.5])

# ===== STUTTERING =====
# Random stutters
b22 >> lbass([0, 2, 4],dur=1/4,oct=4,amp=0.8,cutoff=1200).sometimes("stutter", PRand([2, 4, 8]))

# ===== CONTROL TIPS =====
# Speed up rhythm
# b1.dur = 1/8

# Add drive
# b1.drive = linvar([0, 0.5], 32)

# Vary cutoff
# b1.cutoff = linvar([800, 2000], 16)

# Make staccato
# b1.sus = 0.1
