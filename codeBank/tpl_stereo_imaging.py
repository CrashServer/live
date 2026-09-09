# tpl fx stereo
# template

# Setup
Clock.bpm = 128

# ============================================================================
# STEREO PARAMETER OVERVIEW
# ============================================================================

# FoxDot stereo imaging parameters:
# - unison: Number of layered voices
# - spread: Stereo width/detune amount (0.0-1.0)
# - pan: Left-right positioning (-1 to +1)
# - chop + pan: Rhythmic panning
# - delay + pan: Ping-pong delays

# ============================================================================
# UNISON - VOICE LAYERING
# ============================================================================

# ===== EXAMPLE 1: BASIC UNISON =====
# Layer multiple slightly detuned copies
p1 >> pluck([0, 2, 4, 7],dur=1,unison=4,amp=0.8)
# 4 layered voices

# ===== EXAMPLE 2: SUPER SAW =====
# Wide unison for big sound (EDM)
p2 >> saw((0, 4, 7),dur=4,sus=3.8,unison=8,amp=0.6)
# 8 voices = super wide
# Reduce amp (8 voices = loud!)

# ===== EXAMPLE 3: SUBTLE UNISON =====
# Small unison for thickening
p3 >> pluck([0, 2, 4, 7, 9],dur=0.5,unison=2,amp=0.85)
# Just double it

# ===== EXAMPLE 4: EXTREME UNISON =====
# Maximum width
p4 >> pads((0, 2, 4),dur=8,sus=7.5,unison=12,amp=0.5,lpf=2400)
# Very wide chorus
# Lower volume

# ===== EXAMPLE 5: VARYING UNISON =====
# Unison changes over time
p5 >> pluck([0, 3, 5, 7],dur=1,unison=var([2, 4, 8], [8, 4, 4]),amp=var([0.85, 0.7, 0.5], [8, 4, 4]),lpf=1600)
# Growing width
# Compensate volume

# ============================================================================
# SPREAD - STEREO WIDTH CONTROL
# ============================================================================

# ===== EXAMPLE 6: BASIC SPREAD =====
# Control how wide unison voices spread
p6 >> pluck([0, 2, 4, 7],dur=0.5,unison=4,spread=0.5,amp=0.8)
# 50% spread

# ===== EXAMPLE 7: MAXIMUM SPREAD =====
# Full stereo width
p7 >> pads((0, 4, 7),dur=4,sus=3.8,unison=6,spread=1.0,amp=0.7)
# 100% spread = full width

# ===== EXAMPLE 8: NARROW SPREAD =====
# Tight, centered sound
p8 >> pluck([0, 3, 5, 7, 10],dur=0.25,unison=4,spread=0.1,amp=0.9)
# Very narrow

# ===== EXAMPLE 9: EVOLVING SPREAD =====
# Spread changes over time
p9 >> saw([0, 2, 4, 7],dur=1,unison=6,spread=linvar([0.0, 1.0], 32),amp=0.7)
# Narrow → wide

# ===== EXAMPLE 10: OSCILLATING SPREAD =====
# Breathing stereo effect
p10 >> pads((0, 2, 4),dur=8,sus=7.5,unison=8,spread=sinvar([0.3, 0.9], 16),amp=0.6)
# Breathe in/out

# ============================================================================
# PAN - LEFT/RIGHT POSITIONING
# ============================================================================

# ===== EXAMPLE 11: STATIC PAN =====
# Position sound left or right
p11 >> pluck([0, 2, 4, 7],dur=0.5,pan=-0.5,amp=0.9)
# Left side (-1 = full left, 0 = center, +1 = full right)

# ===== EXAMPLE 12: PING-PONG PAN =====
# Alternate left/right
p12 >> pluck([0, 2, 4, 7, 9, 11],dur=0.25,pan=var([-1, 1], [0.5, 0.5]),amp=0.8)
# Bounce left/right

# ===== EXAMPLE 13: SMOOTH PAN SWEEP =====
# Sweep across stereo field
p13 >> pluck([0, 3, 5, 7],dur=1,pan=linvar([-1, 1], 16),amp=0.85)
# Left → right over 16 beats

# ===== EXAMPLE 14: SINE WAVE PANNING =====
# Smooth circular motion
p14 >> pluck([0, 2, 4, 7],dur=0.5,pan=PSine(8),amp=0.9)
# Sine wave panning (period = 8 beats)

# ===== EXAMPLE 15: STEPPED PANNING =====
# Jump between positions
p15 >> pluck([0, 2, 4, 7, 9],dur=0.5,pan=var([-0.7, 0, 0.7, -0.3, 0.3], [2, 1, 1, 1, 1]),amp=0.85)

# ============================================================================
# COMBINING UNISON + SPREAD + PAN
# ============================================================================

# ===== EXAMPLE 16: WIDE STEREO WITH PANNING =====
p16 >> saw([0, 4, 7],dur=2,unison=6,spread=0.8,pan=sinvar([-0.3, 0.3], 8),amp=0.7)
# Wide stereo
# Subtle movement

# ===== EXAMPLE 17: LAYERED WITH DIFFERENT PANS =====
# Multiple octaves with different positions
p17 >> pluck([0, 2, 4, 7],dur=0.5,oct=(5, 6, 7),pan=(-0.5, 0, 0.5),amp=(0.9, 0.7, 0.5))
# Low left, mid center, high right

# ===== EXAMPLE 18: UNISON WITH MOVING PAN =====
p18 >> pads((0, 4, 7),dur=4,sus=3.8,unison=8,spread=0.9,pan=linvar([-1, 1, -1], [32, 32, 32]),amp=0.6)
# Sweep both ways

# ============================================================================
# RHYTHMIC STEREO EFFECTS
# ============================================================================

# ===== EXAMPLE 19: EUCLIDEAN PANNING =====
# Pan follows rhythmic pattern
rhythm = PDur(5, 8)
p19 >> pluck([0, 2, 4, 7, 9],dur=0.25,pan=rhythm * 2 - 1,amp=0.85)
# Convert 0/1 to -1/+1

# ===== EXAMPLE 20: CALL AND RESPONSE PANNING =====
# Alternating phrases in stereo
p20 >> pluck([0, 2, 4, 7],dur=var([1, 1, 1, 1, 2], [1, 1, 1, 1, 4]),pan=var([-0.8, 0.8], [4, 4]),amp=0.9)
# 4 beats left, 4 beats right

# ===== EXAMPLE 21: SPREAD FOLLOWING RHYTHM =====
# Spread opens on accents
p21 >> pluck(PDur(7, 16) * [0, 2, 4, 7, 9, 11, 14],dur=0.25,unison=6,spread=PDur(7, 16) * 0.9 + 0.1,amp=0.8)
# Narrow base, wide on hits

# ============================================================================
# DELAY + PAN COMBINATIONS
# ============================================================================

# ===== EXAMPLE 22: PING-PONG DELAY (SIMULATED) =====
# Use pan with delay for ping-pong effect
p22 >> pluck([0, 3, 5, 7],dur=2,delay=0.375,pan=var([-0.5, 0.5], [0.375, 0.375]),amp=0.8)
# Alternate with delay

# ===== EXAMPLE 23: STEREO DELAY SPREAD =====
p23 >> pluck([0, 2, 4, 7],dur=1,delay=(0.25, 0.5),pan=(-0.7, 0.7),amp=0.7)
# Two delay times
# Delayed copies panned

# ============================================================================
# MULTI-LAYER STEREO ARRANGEMENTS
# ============================================================================

# ===== EXAMPLE 24: FULL STEREO MIX =====
# Bass - center
b1 >> bass([0, 0, 3, 7],dur=1,pan=0,amp=1.0)
# Dead center

# Melody - wide stereo
p24 >> pluck([0, 2, 4, 7, 9],dur=0.5,unison=6,spread=0.8,pan=PSine(16),amp=0.8,oct=6)
# Gentle movement

# Pads - maximum width
p25 >> pads((0, 4, 7),dur=8,sus=7.5,unison=10,spread=1.0,pan=sinvar([-0.2, 0.2], 32),amp=0.5,oct=5,lpf=1800)
# Full width
# Subtle drift

# Hi-hats - alternating
d1 >> play("-",dur=0.5,pan=var([-0.3, 0.3], [0.5, 0.5]),amp=0.6)
# Left/right

# ===== EXAMPLE 25: STEREO FIELD ZONING =====
# Assign instruments to stereo zones

# Zone 1: Far left
p26 >> pluck([0, 2, 4],dur=1,pan=-0.9,amp=0.7,oct=5)

# Zone 2: Center-left
p27 >> pluck([2, 4, 7],dur=1,pan=-0.4,amp=0.75,oct=6)

# Zone 3: Center
b2 >> bass([0, 3, 7],dur=2,pan=0,amp=0.9,oct=3)

# Zone 4: Center-right
p28 >> pluck([4, 7, 9],dur=1,pan=0.4,amp=0.75,oct=6)

# Zone 5: Far right
p29 >> pluck([7, 9, 11],dur=1,pan=0.9,amp=0.7,oct=5)

# ============================================================================
# HAAS EFFECT (STEREO WIDENING)
# ============================================================================

# ===== EXAMPLE 26: PSEUDO-HAAS EFFECT =====
# Very short delay for width
p30 >> pluck([0, 2, 4, 7],dur=1,unison=2,spread=0.1,delay=0.01,amp=0.85)
# Minimal spread
# Very short delay (10ms)

# ============================================================================
# MODULATION + STEREO
# ============================================================================

# ===== EXAMPLE 27: VIBRATO IN STEREO =====
p31 >> pluck([0, 2, 4, 7],dur=1,unison=4,spread=0.7,vib=12,vibdepth=0.02,amp=0.8)
# Vibrato rate
# Vibrato depth

# ===== EXAMPLE 28: SLIDE WITH STEREO =====
p32 >> pluck([0, 2, 4, 7, 9],dur=0.5,slide=2,unison=6,spread=0.8,pan=PSine(12),amp=0.75)
# Slide to next note

# ============================================================================
# EXTREME STEREO EFFECTS
# ============================================================================

# ===== EXAMPLE 29: CHAOTIC STEREO =====
# Random everything
p33 >> pluck([0, 2, 4, 7, 9, 11],dur=0.25,unison=PWhite(2, 10),spread=PWhite(0.3, 1.0),pan=PWhite(-1.0, 1.0),amp=0.7)
# Random voice count
# Random width
# Random position

# ===== EXAMPLE 30: STEREO WIDENING OVER TIME =====
# Gradually expand stereo field
p34 >> saw([0, 4, 7],dur=4,unison=lininf(2, 12, 64),spread=lininf(0.1, 1.0, 64),pan=sinvar([-0.5, 0.5], 8),amp=0.6)
# More voices over time
# Wider over time
# Movement

# ============================================================================
# MONO COMPATIBILITY TECHNIQUES
# ============================================================================

# ===== EXAMPLE 31: MONO-COMPATIBLE UNISON =====
# Wide but still works in mono
p35 >> pluck([0, 2, 4, 7],dur=0.5,unison=4,spread=0.5,amp=0.85)
# Moderate spread (not extreme)

# ===== EXAMPLE 32: MID-SIDE TECHNIQUE (SIMULATED) =====
# Bass in mono (mid), high freq in stereo (side)
b3 >> bass([0, 3, 7],dur=1,pan=0,lpf=300,amp=1.0)
# Mono bass

p36 >> pluck([0, 2, 4, 7],dur=0.5,unison=6,spread=0.9,hpf=800,amp=0.7)
# Wide treble

# ============================================================================
# PERFORMANCE TIPS
# ============================================================================

# Live stereo control:
# p1.unison = 8                        # More voices
# p1.spread = linvar([0, 1], 16)      # Open up
# p1.pan = PSine(8)                   # Add movement
# p1.pan = var([-1, 1], [2, 2])       # Ping-pong

# Common combinations:
# - unison=4-6, spread=0.7: Wide lead
# - unison=8-12, spread=1.0: Super saw
# - unison=2, spread=0.3: Subtle thickening
# - pan=PSine(n): Smooth movement
# - pan=var([-1,1], [n,n]): Hard panning

# ============================================================================
# STEREO WIDTH GUIDE
# ============================================================================

# Recommended unison + spread combinations:

# Subtle thickening:
# unison=2, spread=0.2

# Natural width (acoustic-like):
# unison=3-4, spread=0.4-0.6

# Wide synth (EDM lead):
# unison=6-8, spread=0.7-0.9

# Super wide (pad, atmosphere):
# unison=8-12, spread=1.0

# Extreme width (special effect):
# unison=12+, spread=1.0

# ============================================================================
# PAN VALUES REFERENCE
# ============================================================================

# -1.0  = Hard left
# -0.7  = Far left
# -0.5  = Left
# -0.3  = Center-left
#  0.0  = Center
#  0.3  = Center-right
#  0.5  = Right
#  0.7  = Far right
#  1.0  = Hard right

# ============================================================================
# FREQUENCY-DEPENDENT PANNING
# ============================================================================

# ===== EXAMPLE 33: LOW CENTERED, HIGHS WIDE =====
# Common mixing technique
b4 >> bass([0, 3, 7],dur=1,pan=0,lpf=300,amp=1.0)
# Bass always center

p37 >> pluck([0, 2, 4, 7],dur=0.5,oct=(5, 6, 7),pan=(0, -0.4, 0.4),hpf=400,amp=0.8)
# Mid center, highs spread
