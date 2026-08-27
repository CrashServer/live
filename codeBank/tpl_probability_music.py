# tpl comp probability
# template

# Setup
Clock.bpm = 128

# ============================================================================
# PROBABILITY PATTERNS OVERVIEW
# ============================================================================

# FoxDot probability-based patterns:
# - PRand(low, high): Random integers
# - PWhite(low, high): Random floats
# - PBern(n): Bernoulli (0 or value based on probability)
# - PwRand(values, weights): Weighted random choice
# - PWalk(max, step, start): Random walk
# - PShuf(list): Shuffle list

# ============================================================================
# PRAND - RANDOM INTEGERS
# ============================================================================

# ===== EXAMPLE 1: RANDOM NOTES =====
# Pick random notes from range
p1 >> pluck(PRand(0, 8),dur=0.5,amp=0.8)

# ===== EXAMPLE 2: RANDOM OCTAVES =====
# Random octave jumps
p2 >> pluck([0, 2, 4, 7],dur=1,oct=PRand(4, 7),amp=0.85)
# Random octave 4-6

# ===== EXAMPLE 3: RANDOM SAMPLES =====
# Random drum sample selection
d1 >> play("x",dur=0.5,sample=PRand(0, 5),amp=1.0)
# Random samples 0-4

# ===== EXAMPLE 4: RANDOM ACCENTS =====
# Random accent pattern
p3 >> pluck([0, 2, 4, 7, 9],dur=0.25,amp=PRand(0.5, 1.0) / 2)
# Random amp 0.25-0.5

# ===== EXAMPLE 5: RANDOM VOICE SELECTION =====
p4 >> prodrums(PRand([0, 3, 5, 7, 10]),voice=4,dur=0.5,amp=0.9)

# ============================================================================
# PWHITE - RANDOM FLOATS
# ============================================================================

# ===== EXAMPLE 6: RANDOM PITCH DEVIATION =====
# Subtle pitch randomness
p5 >> pluck([0, 2, 4, 7],dur=0.5,oct=5,degree=var([0, 2, 4, 7]) + PWhite(-0.1, 0.1),amp=0.8)
# Microtonal variation

# ===== EXAMPLE 7: RANDOM FILTER CUTOFF =====
p6 >> pluck([0, 2, 4, 7],dur=0.5,lpf=PWhite(400, 2400),lpr=0.3,amp=0.85)
# Random filter frequency

# ===== EXAMPLE 8: RANDOM PAN =====
# Scattered stereo field
p7 >> pluck([0, 2, 4, 7, 9],dur=0.25,pan=PWhite(-1.0, 1.0),amp=0.8)
# Random L/R position

# ===== EXAMPLE 9: RANDOM LOOP POSITION =====
l1 >> loop("losthighway8",dur=2,pos=PWhite(0.0, 1.0),chop=4,amp=0.7)
# Random position in loop

# ===== EXAMPLE 10: RANDOM DURATION =====
p8 >> pluck([0, 2, 4, 7],dur=PWhite(0.25, 1.0),amp=0.85)
# Random note lengths

# ============================================================================
# PBERN - BERNOULLI DISTRIBUTION (0 OR VALUE)
# ============================================================================

# ===== EXAMPLE 11: SPARSE PATTERN =====
# Notes play with 30% probability
p9 >> pluck(PBern(8, 0.3),dur=0.5,amp=0.9)

# ===== EXAMPLE 12: CONDITIONAL ACCENTS =====
# Random accents
p10 >> pluck([0, 2, 4, 7],dur=0.5,amp=0.6 + PBern(0.3, 0.5))
# Base 0.6, +0.3 randomly (50% chance)

# ===== EXAMPLE 13: RANDOM FILTER TRIGGER =====
# Filter opens randomly
p11 >> pluck([0, 2, 4, 7, 9],dur=0.25,lpf=800 + PBern(2400, 0.25),lpr=0.4,amp=0.85)
# 25% chance of high cutoff

# ===== EXAMPLE 14: RANDOM OCTAVE JUMPS =====
p12 >> pluck([0, 2, 4, 7],dur=0.5,oct=5 + PBern(1, 0.2),amp=0.8)
# 20% chance of octave up

# ===== EXAMPLE 15: SPARSE HITS =====
# Drum hits with probability
d2 >> play("o",dur=0.25,amp=PBern(1.0, 0.3))
# 30% probability of hit

# ============================================================================
# PWRAND - WEIGHTED RANDOM CHOICE
# ============================================================================

# ===== EXAMPLE 16: WEIGHTED NOTE SELECTION =====
# Some notes more likely than others
p13 >> pluck(PwRand([0, 2, 4, 7], [0.4, 0.3, 0.2, 0.1]),dur=0.5,amp=0.85)
# 0=40%, 2=30%, 4=20%, 7=10%

# ===== EXAMPLE 17: WEIGHTED RHYTHM =====
# Favor certain durations
p14 >> pluck([0, 2, 4, 7],dur=PwRand([0.25, 0.5, 1.0], [0.5, 0.3, 0.2]),amp=0.8)
# Fast notes more common

# ===== EXAMPLE 18: WEIGHTED FILTER =====
p15 >> pluck([0, 2, 4, 7, 9],dur=0.5,lpf=PwRand([400, 1200, 3200], [0.6, 0.3, 0.1]),lpr=0.4,amp=0.85)
# Usually dark, sometimes bright

# ============================================================================
# PWALK - RANDOM WALK
# ============================================================================

# ===== EXAMPLE 19: MELODIC WANDERING =====
# Melody walks randomly through scale
p16 >> pluck(PWalk(12, 2, 4),dur=0.5,amp=0.8)

# ===== EXAMPLE 20: FILTER WALK =====
p17 >> pluck([0, 2, 4, 7],dur=0.5,lpf=PWalk(4000, 400, 1200) + 400,lpr=0.3,amp=0.85)
# Walk between 400-4400 Hz

# ===== EXAMPLE 21: OCTAVE WALK =====
p18 >> pluck([0, 2, 4, 7],dur=1,oct=PWalk(3, 1, 4),amp=0.8)
# Walk octaves 4-7

# ============================================================================
# PSHUF - SHUFFLE/RANDOMIZE LIST
# ============================================================================

# ===== EXAMPLE 22: SHUFFLED MELODY =====
# Randomize order each cycle
p19 >> pluck(PShuf([0, 2, 4, 7, 9, 11]),dur=0.5,amp=0.85)

# ===== EXAMPLE 23: SHUFFLED RHYTHM =====
p20 >> pluck([0, 2, 4, 7],dur=PShuf([0.25, 0.5, 0.5, 1.0]),amp=0.8)

# ============================================================================
# COMBINING PROBABILITY FUNCTIONS
# ============================================================================

# ===== EXAMPLE 24: MULTI-PROBABILITY LAYERS =====
p21 >> pluck(PRand(0, 8) + PBern(5, 0.2),dur=PWhite(0.25, 0.75),oct=5 + PBern(1, 0.15),lpf=PWhite(600, 2400),pan=PWhite(-0.5, 0.5),amp=PWhite(0.6, 0.9))
# Random note + occasional jump
# Random duration
# Occasional octave up
# Random filter
# Random pan
# Random velocity

# ===== EXAMPLE 25: PROBABILITY MATRIX =====
# Different probabilities for different parameters
p22 >> pluck(PwRand([0, 2, 4, 7, 9], [0.3, 0.25, 0.2, 0.15, 0.1]),dur=PwRand([0.25, 0.5, 1.0], [0.5, 0.3, 0.2]),oct=PwRand([4, 5, 6], [0.2, 0.6, 0.2]),lpf=PWhite(800, 3200),amp=0.8)
# Weighted notes
# Weighted rhythm
# Favor oct 5

# ===== EXAMPLE 26: STRUCTURED RANDOMNESS =====
# Base pattern with random variations
base_melody = [0, 2, 4, 7]
p23 >> pluck(base_melody + PBern(PRand(-2, 2), 0.3),dur=0.5,oct=5,amp=0.85)
# 30% chance of variation

# ============================================================================
# GENERATIVE DRUMS
# ============================================================================

# ===== EXAMPLE 27: PROBABILITY DRUM PATTERNS =====
# Kick - regular
d3 >> play("x",dur=1,amp=1.0)

# Snare - some probability
d4 >> play("o",dur=0.5,amp=PBern(1.0, 0.4))
# 40% hits

# Hi-hat - mostly on, occasional gaps
d5 >> play("-",dur=0.25,amp=PBern(0.6, 0.85),pan=PWhite(-0.3, 0.3))
# 85% hits
# Random pan

# Percussion - sparse random
d6 >> play("*",dur=0.125,amp=PBern(0.8, 0.15),sample=PRand(0, 8))
# 15% hits
# Random samples

# ===== EXAMPLE 28: EUCLIDEAN + PROBABILITY =====
# Combine Euclidean rhythm with probability
p24 >> pluck(PRand([0, 3, 5, 7, 10]),dur=PDur(5, 8),oct=4 + PBern(1, 0.3),lpf=PWhite(400, 1600),amp=PWhite(0.7, 1.0))
# Euclidean structure
# Random octave jumps
# Random filter
# Random velocity

# ============================================================================
# EVOLVING PROBABILITY
# ============================================================================

# ===== EXAMPLE 29: INCREASING PROBABILITY =====
# Probability increases over time
p25 >> pluck(PBern(8, lininf(0.0, 1.0, 64)),dur=0.5,amp=0.9)
# Starts with 0% probability, reaches 100% at beat 64

# ===== EXAMPLE 30: OSCILLATING PROBABILITY =====
# Probability breathes in and out
p26 >> pluck(PBern([0, 2, 4, 7], sinvar([0.2, 0.8], 16)),dur=0.5,amp=0.85)

# ===== EXAMPLE 31: CONDITIONAL PROBABILITY =====
# Probability varies with pattern
p27 >> pluck([0, 2, 4, 7],dur=0.5,oct=5 + PBern(1, var([0.1, 0.5, 0.9], [8, 4, 4])),amp=0.8)
# Probability of octave jump varies

# ============================================================================
# MARKOV CHAIN (SIMULATED)
# ============================================================================

# ===== EXAMPLE 32: WEIGHTED STATE TRANSITIONS =====
# Simulate Markov chain with weighted choices
current_state = 0

# State 0 → mostly stay, sometimes → 1
p28 >> pluck(PwRand([0, 2, 4], [0.6, 0.3, 0.1]),dur=0.5,amp=0.85)

# ============================================================================
# CHAOS & CONTROL
# ============================================================================

# ===== EXAMPLE 33: CONTROLLED CHAOS =====
# Mix structured and random elements
p29 >> pluck(var([0, 2, 4, 7], 4) + PBern(PRand(-1, 1), 0.2),dur=var([0.5, 0.25], [3, 1]),lpf=linvar([600, 2400], 32) + PWhite(-200, 200),amp=0.85)
# Mostly structured
# Regular rhythm
# Structured + noise

# ===== EXAMPLE 34: INCREASING CHAOS =====
# Start structured, become chaotic
p30 >> pluck([0, 2, 4, 7] + PBern(PRand(-3, 3), lininf(0.0, 0.8, 128)),dur=0.5,lpf=linvar([800, 3200], 64),amp=0.8)
# Starts predictable, becomes random

# ============================================================================
# AMBIENT GENERATIVE
# ============================================================================

# ===== EXAMPLE 35: SPARSE AMBIENT TEXTURE =====
# Very sparse, random notes
p31 >> pads(PRand(0, 12),dur=PWhite(2, 8),sus=PWhite(4, 12),oct=PwRand([4, 5, 6], [0.2, 0.5, 0.3]),lpf=PWhite(800, 2400),amp=PBern(0.6, 0.3),mverb=0.9)
# Long, random durations
# Long sustain
# 30% probability of note

# ===== EXAMPLE 36: GLITCH TEXTURE =====
# High-density random grains
p32 >> pluck(PRand(0, 15),dur=PWhite(0.05, 0.2),oct=PRand(4, 8),lpf=PWhite(400, 8000),pan=PWhite(-1, 1),amp=PBern(0.3, 0.4),attack=0.001,decay=PWhite(0.05, 0.2))
# Very short notes
# Random octaves
# Sparse

# ============================================================================
# POLYRHYTHMIC PROBABILITY
# ============================================================================

# ===== EXAMPLE 37: INDEPENDENT PROBABILITY LAYERS =====
# Layer 1: Dense, low probability
p33 >> pluck(PBern([0, 2, 4], 0.3),dur=0.25,oct=4,amp=0.7)

# Layer 2: Medium density
p34 >> pluck(PBern([4, 7, 9], 0.5),dur=0.375,oct=5,amp=0.6)
# 3:2 polyrhythm

# Layer 3: Sparse, high probability
p35 >> pluck(PBern([7, 11, 14], 0.7),dur=0.5,oct=6,amp=0.5)

# ============================================================================
# PRACTICAL GENERATIVE TECHNIQUES
# ============================================================================

# ===== EXAMPLE 38: SELF-PLAYING BASS =====
# Bass that plays itself with variations
b1 >> bass(PwRand([0, 3, 7, 10], [0.4, 0.3, 0.2, 0.1]),dur=PwRand([0.5, 1.0, 2.0], [0.5, 0.4, 0.1]),oct=3,lpf=PWhite(300, 800),amp=PWhite(0.8, 1.0))
# Weighted root motion
# Varied rhythm

# ===== EXAMPLE 39: GENERATIVE MELODY =====
# Melody with constraints
p36 >> pluck(PWalk(7, 1, 0),dur=PwRand([0.25, 0.5, 1.0], [0.4, 0.4, 0.2]),oct=5 + PBern(1, 0.1),lpf=linvar([1200, 3200], 32),amp=PWhite(0.7, 0.9))
# Walk through scale
# Occasional jump

# ===== EXAMPLE 40: PROBABILITY-BASED ARRANGEMENT =====
# Different sections with different densities
section_density = var([0.3, 0.5, 0.8, 1.0], [32, 16, 16, 32])

p37 >> pluck(PBern(PRand([0, 2, 4, 7, 9]), section_density),dur=0.25,lpf=PWhite(800, 2400),amp=0.8)

# ============================================================================
# PERFORMANCE TIPS
# ============================================================================

# Live probability control:
# p1.degree = PRand(0, 12)             # More random
# p1.degree = PwRand([0,2,4,7], [0.4,0.3,0.2,0.1])  # Weighted
# p1.amp = PBern(1.0, 0.5)             # 50% sparse
# p1.lpf = PWhite(400, 4000)           # Random filter

# Common probability techniques:
# - PRand for discrete choices (notes, samples)
# - PWhite for continuous ranges (filter, pan, amp)
# - PBern for sparse patterns (0 or value)
# - PwRand for weighted choices (favor certain notes)
# - PWalk for bounded random walks
# - Combine with var/linvar for evolving probability

# ============================================================================
# PROBABILITY RANGES
# ============================================================================

# PBern probability values:
# - 0.1-0.2: Very sparse (10-20% hits)
# - 0.3-0.4: Sparse (30-40% hits)
# - 0.5: Half density
# - 0.6-0.7: Dense (60-70% hits)
# - 0.8-0.9: Very dense (80-90% hits)

# PwRand weights (must sum to 1.0):
# - [0.4, 0.3, 0.2, 0.1]: Decreasing probability
# - [0.1, 0.2, 0.4, 0.3]: Favor middle values
# - [0.5, 0.25, 0.25]: Favor first choice
