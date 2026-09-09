# tpl bass simple
# template

# Setup
Clock.bpm = 128
Scale.default = Scale.minor
Root.default = "E"

# ===== ROOT NOTE BASS =====
# Simple quarter note root bass
b1 >> bass([0], dur=1, oct=4, amp=0.8, lpf=1200, sus=0.8)

# Root with octave layer
b2 >> bass([0], dur=1, oct=(3, 4), amp=0.8, lpf=1600, lpr=0.1)

# ===== WALKING BASS =====
# Classic walking bass pattern
b3 >> bass([0, 2, 4, 7], dur=1, oct=4, amp=0.8, lpf=1400, sus=0.7)

# Walking with variation
b4 >> bass([0, -2, -3, -1], dur=1, oct=4, amp=0.9, lpf=1600, lpr=0.2)

# ===== RHYTHMIC BASS =====
# Eighth note pattern
b5 >> lbass([0, 0, 2, 0], dur=1/2, oct=4, amp=0.7, lpf=1200, cutoff=1000)

# Syncopated rhythm
b6 >> lbass([0, _, 0, 2], dur=1/2, oct=4, amp=0.8, lpf=1400)

# Fast rhythmic bass
b7 >> lbass([0, 0, 0, 2, 0, 0, 4, 2], dur=1/4, oct=4, amp=0.7, lpf=1000)

# ===== BASS WITH VARIATION =====
# Alternating pattern
b8 >> bass(var([0, [0, 2, 4]], [8, 4]), dur=1, oct=4, amp=0.8, lpf=1400)

# Pattern with rests
b9 >> bass([0, _, 0, _, 2, _, 0, _], dur=1/2, oct=4, amp=0.9, lpf=1600)

# ===== OCTAVE LAYERS =====
# Sub bass + mid bass
b10 >> bass([0], dur=1, oct=(3, 4), amp=[1.0, 0.6], lpf=1400, lpr=0.1)

# Three octave layer
b11 >> bass([0, 2], dur=1, oct=(3, 4, 5), amp=[1.0, 0.7, 0.4], lpf=1800)

# ===== BASS WITH FILTER MOVEMENT =====
# Moving low-pass filter
b12 >> lbass([0], dur=1, oct=4, amp=0.8, lpf=linvar([400, 1600], 32), lpr=0.2)

# Pulsing filter
b13 >> lbass([0, 2], dur=1/2, oct=4, amp=0.8, lpf=var([800, 1600], 4), lpr=0.3)

# ===== BASS WITH EFFECTS =====
# Bass with reverb
b14 >> bass([0, -2], dur=1, oct=4, amp=0.8, lpf=1400, mverb=0.2)

# Bass with distortion
b15 >> lbass([0], dur=1, oct=4, amp=0.7, lpf=1200, shape=0.3, shape=0.5)

# Bass with echo
b16 >> bass([0, 2, 4], dur=1, oct=4, amp=0.8, lpf=1400, echo=0.5, delay=0.25)

# ===== FOLLOWING PATTERNS =====
# Bass follows another player (define a1 first)
# a1 >> pluck([0, 2, 4, 7], dur=1/2)
# b17 >> bass(dur=1, oct=4).follow(a1, 4) + [0, -12]

# ===== SUB BASS LAYER =====
# Deep m2 bass (low octave, minimal filtering)
m2 >> bass([0], dur=4, oct=2, amp=1.0, lpf=200, sus=4)

# Main bass on top
m1 >> lbass([0, 2, 0, 4], dur=1/2, oct=4, amp=0.7, lpf=1400)

# ===== BASS WITH SLIDES =====
# Slide between notes
b18 >> lbass([0, 2, 4, 7], dur=1, oct=4, slide=0.1, amp=0.8, lpf=1400)

# Variable slide
b19 >> lbass([0, 2, 4], dur=1, oct=4, slide=var([0, 0.2], [7, 1]), amp=0.8)

# ===== ELECTRIC BASS =====
# Plucky electric bass sound
e1 >> ebass([0, 2, 4, 2], dur=1/2, oct=4, amp=0.8, cutoff=1200, pick=0.8)

# Picked bass with variation
e2 >> ebass([0, 0, 2, 0], dur=1/2, oct=4, pick=[0.8, 0.3, 0.5, 0.3], cutoff=1400)

# ===== CONTROL TIPS =====
# Gradually open filter
# b1.lpf = linvar([400, 2000], 64)

# Add occasional slide
# b1.slide = var([0, 0.2], [15, 1])

# Layer with unison
# b1.unison(2)

# Stop bass
# b_all.stop()
