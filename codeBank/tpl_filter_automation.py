# tpl fx filterauto
# template

# Setup
Clock.bpm = 128

# ============================================================================
# FILTER TYPES OVERVIEW
# ============================================================================

# FoxDot has 5 main filter types:
# - lpf: Low-pass filter (cuts highs)
# - hpf: High-pass filter (cuts lows)
# - bpf: Band-pass filter (keeps middle)
# - brf: Band-reject/notch filter (cuts middle)
# - formant: Formant filter (vowel sounds)

# Each filter has:
# - Cutoff frequency (Hz)
# - Resonance (lpr, hpr, bpr, etc.)

# Additional filter parameters:
# - bpnoise: Band-pass noise amount
# - bits: Bit reduction
# - crush: Sample rate reduction

# ============================================================================
# LOW-PASS FILTER (LPF) - MOST COMMON
# ============================================================================

# ===== EXAMPLE 1: STATIC LPF =====
b1 >> bass([0, 3, 7, 10],dur=1,lpf=800,lpr=0.2,amp=0.9)
# Fixed cutoff at 800 Hz
# Low resonance

# ===== EXAMPLE 2: LINEAR SWEEP =====
# Classic filter sweep
p1 >> pluck([0, 2, 4, 7],dur=0.5,lpf=linvar([400, 4000], 32),lpr=0.3,amp=0.8)
# Sweep over 32 beats

# ===== EXAMPLE 3: EXPONENTIAL SWEEP =====
# More natural sounding sweep (faster at start)
p2 >> pads((0, 2, 4),dur=8,sus=7.5,lpf=expvar([200, 8000], 64),lpr=0.5,amp=0.7)
# Exponential curve
# Higher resonance

# ===== EXAMPLE 4: OSCILLATING LPF =====
# Rhythmic filter movement
p3 >> pluck([0, 3, 5, 7, 10],dur=PDur(5, 8),lpf=sinvar([600, 2400], 16),lpr=0.4,amp=0.85)
# Sine wave modulation

# ===== EXAMPLE 5: STEPPED LPF =====
# Rhythmic jumps between frequencies
p4 >> bass([0, 0, 3, 3],dur=0.5,lpf=var([400, 800, 1600, 3200], [4, 2, 2, 1]),lpr=var([0.2, 0.6], 4),amp=0.9)
# Step through

# ===== EXAMPLE 6: HIGH RESONANCE "SCREAMING" LPF =====
# Extreme resonance for acid/techno
b2 >> tb303([0, 0, 3, 7, 10, 7],dur=0.25,lpf=linvar([400, 2400], 8),lpr=0.9,amp=0.85,oct=4)
# Very high resonance = screaming

# ============================================================================
# HIGH-PASS FILTER (HPF) - CUTS LOWS
# ============================================================================

# ===== EXAMPLE 7: STATIC HPF =====
# Remove low end
d1 >> play("-",dur=PDur(5, 8),hpf=3000,hpr=0.1,amp=0.8)
# Cut everything below 3kHz

# ===== EXAMPLE 8: SWEEPING HPF =====
# Reveal low end over time
p5 >> pluck([0, 2, 4, 7, 9],dur=0.5,hpf=linvar([4000, 100], 32),hpr=0.2,amp=0.9)
# Start thin, get full

# ===== EXAMPLE 9: RHYTHMIC HPF =====
# Pumping high-pass effect
l1 >> loop("losthighway8",dur=4,hpf=var([100, 2000], [3, 1]),hpr=0.3,amp=0.85)
# Pump between full/thin

# ===== EXAMPLE 10: HPF + LPF COMBINATION =====
# Band-pass effect using both filters
p6 >> pads((0, 4, 7),dur=4,sus=3.8,lpf=2400,lpr=0.3,hpf=800,hpr=0.3,amp=0.8)
# Cut highs
# Cut lows
# Result: only 800-2400 Hz

# ============================================================================
# BAND-PASS FILTER (BPF) - KEEPS MIDDLE
# ============================================================================

# ===== EXAMPLE 11: STATIC BPF =====
b3 >> bass([0, 3, 7],dur=1,bpf=1500,bpr=0.4,amp=0.9)
# Center frequency
# Width of band

# ===== EXAMPLE 12: SWEEPING BPF =====
# Telephone/radio effect moving through spectrum
p7 >> pluck([0, 2, 4, 7, 9, 11],dur=0.25,bpf=linvar([400, 4000], 16),bpr=0.6,amp=0.85)
# Sweep center frequency
# Narrow band

# ===== EXAMPLE 13: NARROW BPF - FORMANT EFFECT =====
# Very narrow for vowel-like sounds
p8 >> pads((0, 2, 4),dur=8,sus=7.5,bpf=var([800, 1200, 2400], [8, 4, 4]),bpr=0.9,amp=0.7)
# Jump between formants
# Very narrow

# ===== EXAMPLE 14: BPF WITH NOISE =====
# Add noise to band-passed signal
p9 >> pluck([0, 3, 5, 7],dur=0.5,bpf=linvar([600, 2400], 32),bpr=0.5,bpnoise=0.3,amp=0.8)
# Add noise component

# ============================================================================
# BAND-REJECT FILTER (BRF) - CUTS MIDDLE
# ============================================================================

# ===== EXAMPLE 15: STATIC NOTCH =====
# Remove specific frequency
p10 >> pluck([0, 2, 4, 7],dur=0.5,brf=1000,brr=0.8,amp=0.9)
# Cut 1kHz
# Narrow notch

# ===== EXAMPLE 16: SWEEPING NOTCH =====
# Moving notch filter (phaser-like)
p11 >> pads((0, 4, 7),dur=4,sus=3.8,brf=sinvar([400, 3200], 16),brr=0.7,amp=0.8)
# Sweep notch

# ============================================================================
# FORMANT FILTER - VOWEL SOUNDS
# ============================================================================

# ===== EXAMPLE 17: VOWEL MORPHING =====
p12 >> pluck([0, 2, 4, 7, 9],dur=0.25,formant=var([0, 1, 2, 3, 4], 4),amp=0.85)
# Different vowels
# 0=a, 1=e, 2=i, 3=o, 4=u

# ===== EXAMPLE 18: TALKING BASSLINE =====
b4 >> bass([0, 0, 3, 3, 7, 7, 10, 10],dur=0.5,formant=var([0, 1, 2, 1], [2, 1, 1, 1]),amp=1.0)

# ============================================================================
# MULTI-FILTER COMBINATIONS
# ============================================================================

# ===== EXAMPLE 19: PARALLEL FILTERS =====
# Multiple filters applied together
p13 >> pluck([0, 2, 4, 7],dur=0.5,lpf=linvar([800, 3200], 16),lpr=0.3,hpf=200,hpr=0.1,amp=0.9)
# Low-pass sweep
# Cut rumble

# ===== EXAMPLE 20: SERIAL FILTERS (SIMULATED) =====
# Stack multiple filters by layering
p14 >> pads((0, 4, 7),dur=4,sus=3.8,lpf=2400,lpr=0.4,bpf=1200,bpr=0.5,amp=0.7)
# First stage
# Second stage

# ===== EXAMPLE 21: FILTER MATRIX =====
# Different filters on different layers
p15 >> pluck([0, 2, 4, 7],dur=0.5,oct=(5, 6, 7),lpf=(800, 1600, 3200),lpr=0.3,amp=(0.7, 0.5, 0.3))
# Three octaves
# Different cutoff per octave
# Lower volumes for higher octaves

# ============================================================================
# RHYTHMIC FILTER MODULATION
# ============================================================================

# ===== EXAMPLE 22: FILTER FOLLOWING RHYTHM =====
# Filter opens on accents
p16 >> pluck(PDur(5, 8) * [0, 2, 4, 7, 9],dur=PDur(5, 8),lpf=var([600, 2400, 600, 600, 600], [1, 1, 1, 1, 1]),lpr=0.4,amp=0.9)
# Accent

# ===== EXAMPLE 23: PUMPING FILTER =====
# Sidechain-style filter pumping
p17 >> pads((0, 2, 4),dur=4,sus=3.8,lpf=var([400, 2000], [0.25, 0.75]),lpr=0.3,amp=0.8)
# Quick open, slow close

# ===== EXAMPLE 24: EUCLIDEAN FILTER TRIGGERS =====
# Filter modulation follows Euclidean pattern
rhythm = PDur(5, 8)
p18 >> pluck([0, 2, 4, 7, 9, 11],dur=0.25,lpf=rhythm * 3000 + 400,lpr=0.5,amp=0.85)
# Open on hits (400 + 3000, or 400 + 0)

# ============================================================================
# FILTER ENVELOPE MODULATION
# ============================================================================

# ===== EXAMPLE 25: ATTACK-SYNCED FILTER =====
# Filter opens with note attack
p19 >> pluck([0, 3, 5, 7],dur=1,attack=0.3,lpf=2400,lpr=0.5,amp=0.9)
# High cutoff
# Filter will follow amplitude envelope naturally

# ===== EXAMPLE 26: INDEPENDENT FILTER ENVELOPE =====
# Filter moves differently than amplitude
p20 >> bass([0, 0, 3, 7],dur=0.5,attack=0.01,lpf=linvar([400, 1600], 8),lpr=0.6,amp=1.0)
# Fast amplitude
# Slow filter

# ============================================================================
# BIT CRUSHING & SAMPLE RATE REDUCTION
# ============================================================================

# ===== EXAMPLE 27: BIT REDUCTION =====
# Reduce bit depth for lo-fi sound
p21 >> pluck([0, 2, 4, 7],dur=0.5,bits=var([16, 8, 4, 2], [4, 2, 1, 1]),lpf=1200,amp=0.85)
# Degrade quality
# Tame harsh aliasing

# ===== EXAMPLE 28: SAMPLE RATE REDUCTION =====
# Reduce sample rate for aliasing
p22 >> bass([0, 3, 7, 10],dur=1,crush=var([0, 4, 8, 16], [8, 4, 2, 2]),lpf=800,amp=0.9)
# More crush = lower SR
# Control aliasing

# ===== EXAMPLE 29: EXTREME DEGRADATION =====
# Combine bits + crush for extreme lo-fi
p23 >> pluck([0, 2, 4, 7, 9],dur=0.25,bits=var([12, 6, 3], [8, 4, 4]),crush=var([0, 8, 16], [8, 4, 4]),lpf=linvar([400, 1200], 16),lpr=0.4,amp=0.8)

# ============================================================================
# COMPLEX FILTER AUTOMATION
# ============================================================================

# ===== EXAMPLE 30: MULTI-STAGE FILTER JOURNEY =====
# Filter changes dramatically over long time
p24 >> pads((0, 4, 7),dur=8,sus=7.5,lpf=expvar([200, 8000, 400], [32, 32, 32]),lpr=sinvar([0.2, 0.8], 16),hpf=linvar([50, 400], 96),amp=0.7)
# 3-stage journey
# Resonance evolves
# HPF creeps up

# ===== EXAMPLE 31: CHAOTIC FILTER MODULATION =====
# Multiple random modulation sources
p25 >> pluck([0, 2, 4, 7, 9, 11],dur=0.25,lpf=PWhite(400, 4000),lpr=PWhite(0.1, 0.7),bpf=var([1000, 2000], 4),bpr=0.4,amp=0.8)
# Random cutoff
# Random resonance
# Additional BPF

# ===== EXAMPLE 32: INTERLOCKING FILTERS =====
# Two filters move in opposite directions
p26 >> pads((0, 2, 4),dur=4,sus=3.8,lpf=linvar([2000, 500], 32),lpr=0.3,hpf=linvar([100, 800], 32),hpr=0.2,amp=0.7)
# Closing
# Opening
# Band narrows over time

# ============================================================================
# FILTER ON DIFFERENT ELEMENTS
# ============================================================================

# ===== EXAMPLE 33: DRUM FILTERING =====
# Filter drums for texture
d2 >> play("x-o-",dur=0.5,lpf=var([20000, 1200], [7, 1]),lpr=0.5,amp=1.0)
# Occasional filter

# ===== EXAMPLE 34: LOOP FILTERING =====
# Filter loop for evolution
l2 >> loop("lynchcrazy16",dur=4,lpf=lininf(8000, 400, 128),lpr=0.4,hpf=var([50, 200], 32),amp=0.85)
# Infinite descent

# ===== EXAMPLE 35: LAYERED FILTER FREQUENCIES =====
# Multiple players with different filter zones
b5 >> bass([0, 0, 3, 7],dur=0.5,lpf=600,lpr=0.3,amp=1.0,oct=3)

p27 >> pluck([0, 2, 4, 7],dur=0.5,hpf=400,lpf=2400,lpr=0.2,amp=0.8,oct=5)
# Don't interfere with bass

p28 >> pads((0, 4, 7),dur=8,sus=7.5,hpf=1200,amp=0.6,oct=6,mverb=0.8)
# Only high atmosphere

# ============================================================================
# PERFORMANCE TECHNIQUES
# ============================================================================

# Live filter control examples:
# p1.lpf = linvar([400, 4000], 16)     # Start sweep
# p1.lpr = 0.8                          # Increase resonance
# p1.hpf = 200                          # Add high-pass
# p1.bpf = sinvar([800, 2400], 8)      # Add moving band-pass
# p1.bits = var([16, 4], 4)            # Add bit crush

# Common filter techniques:
# - lpf + lpr: Classic acid filter
# - hpf rising: Build tension
# - bpf sweeping: Telephone/radio effect
# - lpf + hpf: Manual band-pass
# - formant cycling: Vowel sounds
# - bits + crush + lpf: Lo-fi texture

# ============================================================================
# FILTER FREQUENCY RANGES
# ============================================================================

# Typical frequency ranges (Hz):
# - Sub bass: 20-60 Hz
# - Bass: 60-250 Hz
# - Low mids: 250-500 Hz
# - Mids: 500-2000 Hz
# - High mids: 2000-4000 Hz
# - Presence: 4000-6000 Hz
# - Brilliance: 6000-20000 Hz

# Common LPF settings:
# - Dark/warm: 400-800 Hz
# - Natural: 1200-2400 Hz
# - Bright: 3200-8000 Hz
# - Open: 10000+ Hz

# Common HPF settings:
# - Remove rumble: 20-60 Hz
# - Thin bass: 100-200 Hz
# - Telephone: 800-1200 Hz
# - Air only: 4000+ Hz

# Resonance (lpr/hpr/bpr) values:
# - Subtle: 0.1-0.3
# - Moderate: 0.4-0.6
# - Aggressive: 0.7-0.9
# - Extreme: 0.95+ (can self-oscillate)
