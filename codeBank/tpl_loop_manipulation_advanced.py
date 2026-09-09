# tpl loops granular
# template

# Setup
Clock.bpm = 128

# ============================================================================
# LOOP PARAMETER OVERVIEW
# ============================================================================

# FoxDot has powerful loop manipulation parameters:
# - pos: Position in the loop (0.0-1.0)
# - chop: Number of chops/grains
# - chopwave: Chop waveform (0-6)
# - chopi: Chop interpolation
# - shift: Shift loop in time (beats)
# - beat_stretch: Auto time-stretch to tempo (0=off, 1=on)

# Common loops used in codebase:
# - losthighway8 (249 files) - atmospheric
# - lynchcrazy16 (243 files) - chaotic
# - davidlynch8 (209 files) - cinematic

# ============================================================================
# POSITION (POS) MANIPULATION
# ============================================================================

# ===== EXAMPLE 1: STATIC POSITION =====
# Play from specific point in loop
l1 >> loop("losthighway8",dur=4,pos=0.5,amp=1.0)
# Start from middle of loop

# ===== EXAMPLE 2: LINEAR POSITION SWEEP =====
# Scan through entire loop over time
l2 >> loop("lynchcrazy16",dur=4,pos=linvar([0.0, 1.0], 32),amp=0.8)
# 0% → 100% over 32 beats

# ===== EXAMPLE 3: RHYTHMIC POSITION JUMPS =====
# Jump between different sections
l3 >> loop("davidlynch8",dur=2,pos=var([0.0, 0.25, 0.5, 0.75], [8, 4, 2, 2]),amp=0.9)
# Jump around

# ===== EXAMPLE 4: RANDOM POSITION WANDERING =====
# Random walk through loop
l4 >> loop("losthighway8",dur=1,pos=PWhite(0.0, 1.0),amp=0.7)
# Random position each hit

# ===== EXAMPLE 5: COMPLEX POSITION MODULATION =====
# Multiple layers of position control
l5 >> loop("lynchcrazy16",dur=var([4, 2], 8),pos=linvar([0.0, PWhite(0.0, 1.0)], [8, 4]),chop=4,amp=0.85)
# Random target

# ============================================================================
# CHOP PARAMETER - GRANULAR/STUTTERING EFFECTS
# ============================================================================

# ===== EXAMPLE 6: BASIC CHOP =====
# Divide loop into equal segments
l6 >> loop("losthighway8",dur=4,chop=4,amp=1.0)
# Divide into 4 pieces

# ===== EXAMPLE 7: VARYING CHOP DENSITY =====
# Change number of chops over time
l7 >> loop("davidlynch8",dur=2,chop=var([2, 4, 8, 16], [8, 4, 2, 2]),amp=0.9)
# Increasing density

# ===== EXAMPLE 8: CHOPWAVE - DIFFERENT SHAPES =====
# Chopwave controls the envelope shape of each chop
l8 >> loop("lynchcrazy16",dur=4,chop=8,chopwave=var([0, 1, 2, 3, 4, 5, 6], 4),amp=0.8)
# Cycle through shapes
# 0=sine, 1=saw, 2=square, 3=triangle, 4=pulse, 5=noise, 6=custom

# ===== EXAMPLE 9: CHOPI - INTERPOLATION =====
# Smooth transitions between chops
l9 >> loop("losthighway8",dur=4,chop=16,chopi=0.8,chopwave=2,amp=0.85)
# High interpolation = smoother

# ===== EXAMPLE 10: RHYTHMIC CHOPPING =====
# Chop synced to rhythm
l10 >> loop("davidlynch8",dur=PDur(5, 8),chop=var([8, 16, 32], [8, 4, 4]),chopwave=1,chopi=var([0.2, 0.8], 4),amp=0.9)

# ============================================================================
# SHIFT PARAMETER - TIME SHIFTING
# ============================================================================

# ===== EXAMPLE 11: BASIC SHIFT =====
# Shift loop start by beats
l11 >> loop("lynchcrazy16",dur=4,shift=0.25,amp=1.0)
# Shift by 1/4 beat

# ===== EXAMPLE 12: MULTIPLE SHIFTED LAYERS =====
# Create polyrhythmic effect with shifts
l12 >> loop("losthighway8",dur=2,shift=(0, 0.25, 0.5, 0.75),amp=0.6)
# 4 layered shifts

# ===== EXAMPLE 13: DYNAMIC SHIFT =====
# Shift changes over time
l13 >> loop("davidlynch8",dur=4,shift=linvar([0, 1.5], 16),amp=0.85)
# Gradually shift

# ===== EXAMPLE 14: RHYTHMIC SHIFT PATTERN =====
# Shift creates rhythmic variation
l14 >> loop("lynchcrazy16",dur=1,shift=var([0, 0.25, 0.5, 0.125], [4, 2, 2, 1]),amp=0.9)

# ============================================================================
# BEAT_STRETCH - TIME STRETCHING CONTROL
# ============================================================================

# ===== EXAMPLE 15: BEAT_STRETCH ON (DEFAULT) =====
# Loop stretches to match tempo
l15 >> loop("losthighway8",dur=4,beat_stretch=1,amp=1.0)
# Auto-stretch to BPM (default)

# ===== EXAMPLE 16: BEAT_STRETCH OFF =====
# Play at original speed (grain effect)
l16 >> loop("davidlynch8",dur=4,beat_stretch=0,chop=16,amp=0.8)
# No stretching = raw grains
# Combine with chop for texture

# ===== EXAMPLE 17: GRAIN CLOUD TEXTURE =====
# beat_stretch=0 with high chop for granular synthesis
l17 >> loop("lynchcrazy16",dur=2,beat_stretch=0,chop=var([32, 64, 128], [8, 4, 4]),pos=PWhite(0.0, 0.3),chopwave=0,chopi=0.9,amp=0.7)
# High grain density
# Random position in small range

# ============================================================================
# COMBINED TECHNIQUES
# ============================================================================

# ===== EXAMPLE 18: POSITION + CHOP =====
# Chopped segments from specific position
l18 >> loop("losthighway8",dur=4,pos=var([0.0, 0.5], 8),chop=8,chopwave=2,amp=0.85)

# ===== EXAMPLE 19: SHIFT + CHOP POLYRHYTHM =====
# Multiple shifted chopped layers
l19 >> loop("davidlynch8",dur=2,shift=(0, 0.33, 0.66),chop=6,chopwave=1,amp=0.7)
# 3 layers

# ===== EXAMPLE 20: EVOLVING GRANULAR =====
# All parameters modulating together
l20 >> loop("lynchcrazy16",dur=var([4, 2, 1], [8, 4, 4]),pos=linvar([0.0, 0.5], 32),chop=linvar([4, 64], 64),chopwave=var([0, 2, 5], 8),chopi=sinvar([0.2, 0.95], 16),shift=var([0, 0.25], 4),beat_stretch=0,amp=0.75)

# ===== EXAMPLE 21: STUTTERING LOOP =====
# Rhythmic stuttering effect
l21 >> loop("losthighway8",dur=PDur(7, 16),pos=var([0.0, 0.1, 0.2, 0.3], [4, 2, 1, 1]),chop=16,chopwave=1,shift=0.125,amp=0.9).every(8, 'stutter', 4)

# ===== EXAMPLE 22: GLITCH EFFECT =====
# Extreme manipulation for glitch
l22 >> loop("davidlynch8",dur=var([0.25, 0.5, 1], [2, 2, 4]),pos=PWhite(0.0, 1.0),chop=var([16, 32, 64], [4, 2, 2]),chopwave=PRand([0, 2, 5, 6]),chopi=PWhite(0.0, 1.0),shift=var([0, 0.125, 0.25], [2, 1, 1]),beat_stretch=0,amp=0.8,lpf=var([400, 2000, 8000], 4))

# ===== EXAMPLE 23: AMBIENT PAD FROM LOOP =====
# Smooth granular texture
l23 >> loop("lynchcrazy16",dur=8,pos=linvar([0.2, 0.4], 64),chop=128,chopwave=0,chopi=0.98,beat_stretch=0,shift=sinvar([0, 0.5], 32),amp=0.6,mverb=0.9,lpf=1200)
# Small range
# Very high grain count
# Sine envelope
# Maximum smoothness

# ===== EXAMPLE 24: RHYTHMIC SLICE REARRANGEMENT =====
# Rearrange loop slices rhythmically
l24 >> loop("losthighway8",dur=0.5,pos=var([0.0, 0.25, 0.5, 0.75, 0.125, 0.625], [2, 2, 2, 2, 1, 1]),chop=4,chopwave=3,shift=0,beat_stretch=1,amp=1.0)

# ===== EXAMPLE 25: DAVID LYNCH STYLE COMPOSITION =====
# Cinematic atmosphere with loop manipulation
l25 >> loop("davidlynch8",dur=var([8, 4, 2], [16, 8, 4]),pos=var([0.0, 0.33, 0.66], [32, 16, 16]),chop=var([2, 4, 8], [16, 8, 8]),chopwave=var([0, 2], 16),chopi=0.7,shift=linvar([0, 1.0], 64),beat_stretch=1,amp=linvar([0.5, 1.0], 128),lpf=expvar([800, 4000], 64),mverb=0.8)

# ============================================================================
# MULTI-LOOP LAYERING
# ============================================================================

# ===== EXAMPLE 26: THREE-LAYER TEXTURE =====
# Base layer
l26a >> loop("losthighway8",dur=8,pos=0.0,chop=2,amp=0.7,lpf=800)

# Mid layer - chopped
l26b >> loop("lynchcrazy16",dur=4,pos=linvar([0.0, 0.5], 32),chop=16,chopwave=2,chopi=0.6,shift=0.25,amp=0.5,bpf=1500,bpnoise=0.1)

# Top layer - glitchy
l26c >> loop("davidlynch8",dur=PDur(5, 8),pos=PWhite(0.0, 1.0),chop=32,chopwave=5,beat_stretch=0,amp=0.4,hpf=3000,mverb=0.6)

# ============================================================================
# PERFORMANCE TIPS
# ============================================================================

# Live manipulation examples:
# l1.pos = linvar([0, 1], 16)      # Scan through loop
# l1.chop = var([4, 8, 16], 4)     # Increase density
# l1.chopwave = 5                  # Change envelope
# l1.shift = 0.5                   # Offset timing
# l1.beat_stretch = 0              # Disable stretching

# Common combinations:
# - pos + chop: Navigate and slice
# - shift + layers: Polyrhythmic textures
# - chop + chopwave + chopi: Granular control
# - beat_stretch=0 + high chop: Granular synthesis
# - pos=PWhite + chop: Random slice playback

# ============================================================================
# PARAMETER RANGES & TIPS
# ============================================================================

# pos: 0.0 to 1.0 (0% to 100% through loop)
#   - Use linvar for sweeps
#   - Use var for jumps
#   - Use PWhite for randomness

# chop: 1 to 256+ (number of slices)
#   - Low (2-8): Rhythmic stutters
#   - Mid (8-32): Granular texture
#   - High (32-128+): Smooth grains

# chopwave: 0-6 (envelope shape)
#   - 0: Sine (smooth)
#   - 1: Saw (ramp)
#   - 2: Square (hard cut)
#   - 3: Triangle (medium)
#   - 4: Pulse (varied)
#   - 5: Noise (random)
#   - 6: Custom

# chopi: 0.0 to 1.0 (interpolation amount)
#   - 0.0: Hard cuts
#   - 0.5: Moderate smoothing
#   - 0.9+: Very smooth

# shift: beats (can be negative)
#   - Use multiples for layering
#   - Combine with dur for polyrhythms

# beat_stretch: 0 or 1
#   - 1: Auto-stretch to BPM (default)
#   - 0: Raw playback (for grains)
