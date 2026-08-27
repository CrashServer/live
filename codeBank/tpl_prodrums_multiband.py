# tpl drums prodrums
# template

# Setup
Clock.bpm = 128

# ============================================================================
# PRODRUMS ARCHITECTURE EXPLAINED
# ============================================================================

# prodrums uses 3 independent layers that mix together:
# - Layer 1: Sub/Low frequencies (kick fundamentals)
# - Layer 2: Body/Mid frequencies (punch, tonality)
# - Layer 3: Transient/High frequencies (click, snap)

# Each layer has its own:
# - Amplitude control (layer1_amp, layer2_amp, layer3_amp)
# - Waveform selection
# - FM synthesis
# - Attack/decay envelope

# Plus multi-band EQ with saturation:
# - low_gain, mid_gain, high_gain (EQ)
# - low_sat, mid_sat, high_sat (saturation per band)

# ============================================================================
# BASIC PRODRUMS PATTERNS
# ============================================================================

# ===== EXAMPLE 1: BALANCED KICK =====
b1 >> prodrums([0, 3, 5],voice=4,dur=0.5,layer1_amp=0.9,layer2_amp=1.0,layer3_amp=1.0,body_tone=1901,harmonic=2.0,fm_amount=0.5,fm_ratio=1,waveform=1,decay=0.4,attack=0.01,low_gain=0.4,mid_gain=0.5,high_gain=0.2,low_sat=1.2,mid_sat=0.8,high_sat=1.0,amp=0.8)
# Voice selection (0-15)
# Layer amplitudes
# Sub/low
# Body/mid
# Transient/high
# Tone shaping
# Body resonance frequency
# Harmonic content
# FM synthesis
# FM modulation depth
# FM ratio
# Waveform
# Waveform type (0-6)
# Envelope
# Decay time
# Attack time
# Multi-band EQ
# Multi-band saturation

# ===== EXAMPLE 2: SUB-HEAVY KICK =====
# Emphasis on low end
b2 >> prodrums([0, 0, 0, PRand([5, 7, 10])],voice=4,dur=var([0.5, 0.25], [3, 1]),layer1_amp=2.5,layer2_amp=2.0,layer3_amp=1.0,body_tone=var([800, 400, 1200], 2),harmonic=0.5,fm_amount=1.3,fm_ratio=var([1, 0.5], 1),waveform=2,decay=0.2,attack=0.001,low_gain=1.5,mid_gain=0.8,high_gain=0.1,low_sat=0.6,mid_sat=0.3,high_sat=0.1,amp=1.0)
# Boost sub layer
# VERY loud sub
# Moderate body
# Normal transient
# Lower body tone for weight
# Less harmonics = deeper
# Heavy FM for growl
# Sine wave for clean sub
# Shorter decay for tightness
# Boost lows, reduce highs
# Saturate low end

# ===== EXAMPLE 3: PUNCHY KICK =====
# Emphasis on mid transient
b3 >> prodrums([0, 3, 7, 10, 12, 7],voice=4,dur=PDur(3, 8),layer1_amp=0.5,layer2_amp=0.4,layer3_amp=0.4,body_tone=var([3500, 3000, 4200], [6, 1, 1]),harmonic=1.5,fm_amount=0.4,fm_ratio=2.5,waveform=var([1, 6], 12),decay=var([0.4, 0.2], 8),attack=0.1,low_gain=0.4,mid_gain=0.8,high_gain=0.5,low_sat=0.5,mid_sat=0.8,high_sat=1.0,amp=0.55,echo=0.5,pan=PSine(8) * 0.3)
# Boost transient layer
# Moderate sub
# Moderate body
# Reduced transient
# Higher body tone for punch
# More harmonics
# Less FM for clarity
# Varying waveforms
# Medium decay
# Slower attack = less click
# Boost mids
# Emphasized
# Saturate mids
# Punchy saturation
# Additional effects
# Subtle pan modulation

# ===== EXAMPLE 4: CLICKY/TRANSIENT KICK =====
# Emphasis on attack
b4 >> prodrums([0, 3, 5, 7],voice=4,dur=PDur(var([3, 5], 8), 8),layer1_amp=linvar([0.9, 1.5], 16),layer2_amp=var([1.0, 1.8, 0.6], [4, 2, 2]),layer3_amp=1.0,body_tone=var([1901, 1200, 2400], [6, 1, 1]),harmonic=sinvar([0.9, 0.5, 1.3], 12),fm_amount=linvar([0.5, 1.8, 0.3], 16),fm_ratio=var([1.5, 2], 4),waveform=var([1, 2], 12),decay=var([0.4, 0.2, 0.7], [4, 2, 2]),attack=0.01,low_gain=linvar([0.4, 0.9], 8),mid_gain=0.5,high_gain=0.8,low_sat=var([1.2, 2.0], 4),mid_sat=0.8,high_sat=1.5,amp=0.8,oct=(4, 5))
# Boost transient
# Variable body tone
# Varying FM
# Variable decay
# Fast attack = clicky
# Boost highs
# Emphasized
# Saturate highs
# Crispy
# Octave layering

# ============================================================================
# ADVANCED TECHNIQUES
# ============================================================================

# ===== EXAMPLE 5: TEXTURE PARAMETER =====
# Texture adds noise/grain
b5 >> prodrums([0, 3, 7, 10, 12, var([7, 12, 13], [12, 1, 1])],voice=4,dur=PDur(3, 8),layer1_amp=0.5,layer2_amp=0.4,layer3_amp=0.4,body_tone=var([3500, 3000, 4200], [6, 1, 1]),harmonic=1.7,fm_amount=var([3, 24], [7, 3]),fm_ratio=0.5,waveform=var([1, 6], 12),texture=17,decay=var([0.4, 0.2], 8),attack=0.1,low_gain=0.4,mid_gain=0.8,high_gain=0.5,mid_sat=0.8,high_sat=1.0,echo=0.5,amp=0.55,oct=(6, 5),pan=PSine(8) * 0.3)
# FM modulation
# Wide variation
# TEXTURE - adds noise (0-42 range)
# Moderate noise

# ===== EXAMPLE 6: EVOLVING TEXTURE =====
# Texture grows over time
b6 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)],voice=4,dur=0.25,layer1_amp=1,layer2_amp=0.5,layer3_amp=0.3,body_tone=linvar([500, 900, 1400], 16),harmonic=2,fm_amount=1.2,fm_ratio=var([2, 2.5, 3], 4),waveform=6,texture=lininf(0, 42, 128),decay=0.2,attack=0.01,low_gain=0.5,mid_gain=0.6,high_gain=0.8,mid_sat=var([0.6, 2.5], [16, 4]),amp=0.75,oct=4,fshift=0,leg=0)
# Texture grows infinitely
# 0 → 42 over 128 beats
# Frequency shift
# No legato

# ===== EXAMPLE 7: MELODIC PRODRUMS =====
# Using prodrums for melodic patterns
b7 >> prodrums([0, 0, 0, 0, PRand([5, 7, 10])],voice=4,dur=var([0.5, 0.25], [3, 1]),layer1_amp=2.5,layer2_amp=2.0,layer3_amp=1.0,body_tone=var([800, 400, 1200], 2),harmonic=0.5,fm_amount=1.3,fm_ratio=var([1, 0.5], 1),waveform=1,decay=0.2,attack=0.001,low_gain=1.5,mid_gain=0.8,high_gain=0.1,low_sat=0.6,mid_sat=0.3,high_sat=0.1,scale=Scale.minor,oct=4,amp=1.0)
# Lower tone for melody
# Follow scale

# ===== EXAMPLE 8: STUTTERING DRUMS =====
b8 >> prodrums(P[0, 0, 0, PRand([5, 7, 10, 12])],voice=4,dur=var([0.5, 0.25, 1.0], [3, 1, 0.5]),layer1_amp=linvar([2.5, 3.5], 8),layer2_amp=var([2.0, 3.0], 2),layer3_amp=1.0,body_tone=var([800, 400, 1200, 600], [2, 1, 1, 0.5]),harmonic=var([0.5, 0.3], 4),fm_amount=linvar([1.3, 1.0, 2.5], 8),fm_ratio=var([1, 12, 1.5], [2, 1, 1]),waveform=var([2, 0], 4),decay=var([0.2, 0.1, 0.4], [4, 1, 1]),attack=0.001,low_sat=var([1.0, 1.5], 2),mid_sat=1.3,oct=4,low_gain=0.5,mid_gain=0.8,texture=var([0, 2], 8),high_gain=0.2,amp=1.0).every(16, 'stutter', 4)
# Modulating layer amps
# Evolving texture

# ============================================================================
# COMPARISON WITH REGULAR DRUMS
# ============================================================================

# Regular drum pattern
d1 >> play("x ", sample=0, amp=1.2)

# ProDrums equivalent - much more control
b9 >> prodrums([0],voice=4,dur=1,layer1_amp=1.5,layer2_amp=1.2,layer3_amp=1.0,body_tone=1200,harmonic=1.5,fm_amount=0.8,waveform=1,decay=0.3,low_gain=1.2,mid_gain=0.9,high_gain=0.7,low_sat=0.8,mid_sat=1.5,high_sat=1.2,amp=1.2)
# Sub layer
# Body
# Transient

# ============================================================================
# CONTROL TIPS
# ============================================================================

# Adjust layer balance
# b1.layer1_amp = 2.0      # Boost sub
# b1.layer3_amp = 0.5      # Reduce transient

# Change body tone
# b1.body_tone = linvar([800, 2400], 32)

# Modulate FM
# b1.fm_amount = var([0.5, 2.0], 8)

# Evolve texture
# b1.texture = lininf(0, 30, 64)

# Multi-band tweaking
# b1.low_gain = 1.5        # Boost lows
# b1.mid_sat = 2.0         # Saturate mids

# Change waveform
# b1.waveform = var([0, 1, 2, 6], 8)
