# tpl melody arpeggios
# template

# Setup
Clock.bpm = 128
Scale.default = Scale.minor
Root.default = "E"

# ===== SIMPLE TRIADS =====
# Basic triad arpeggio
m1 >> pluck([0, 2, 4], dur=1/4, oct=5, amp=0.6)

# Triad up and down
m2 >> pluck([0, 2, 4, 2], dur=1/4, oct=5, amp=0.6, lpf=2000)

# ===== SEVENTH CHORDS =====
# Minor 7th arpeggio
m3 >> pluck([0, 2, 4, 6], dur=1/4, oct=5, amp=0.6)

# Extended arpeggio
m4 >> pluck([0, 2, 4, 6, 9], dur=1/4, oct=5, amp=0.5, lpf=2400)

# ===== CHORD PROGRESSIONS =====
# Arpeggiating chord progression
m5 >> pluck(P[(0,2,4), (1,3,5), (2,4,6)], dur=1/4, oct=5, amp=0.6)

# Different inversions
m6 >> pluck(P[(0,2,4), (2,4,7), (4,7,9), (7,9,12)], dur=1/4, oct=5, amp=0.6)

# ===== VARIABLE SPEED =====
# Fast arpeggio
m7 >> pluck([0, 2, 4, 7], dur=1/8, oct=5, amp=0.5, lpf=3000)

# Variable duration
m8 >> pluck([0, 2, 4, 7],dur=var([1/4, 1/8], [8, 4]),oct=5,amp=0.6)

# Mixed durations
m9 >> pluck([0, 2, 4, 7, 9, 7, 4, 2],dur=[1/4, 1/8, 1/8, 1/4, 1/8, 1/8, 1/4, 1/4],oct=5,amp=0.6)

# ===== OCTAVE VARIATIONS =====
# Octave jumps in arpeggio
m10 >> pluck([0, 2, 4, 7],dur=1/4,oct=[5, 5, 6, 5],amp=0.6)

# Two octave spread
m11 >> pluck([0, 2, 4, 7],dur=1/4,oct=(5, 6),amp=0.5)

# ===== WITH FILTER MOVEMENT =====
# Moving low-pass filter
m12 >> pluck([0, 2, 4, 7],dur=1/4,oct=5,lpf=linvar([800, 3200], 32),lpr=0.2,amp=0.6)

# Pulsing filter
m13 >> pluck([0, 2, 4, 7],dur=1/4,oct=5,lpf=var([1200, 2400], 4),amp=0.6)

# ===== BELL-STYLE ARPEGGIOS =====
# Bright bell arpeggio
m14 >> bell([0, 2, 4, 7, 9], dur=1/4, oct=6, amp=0.5, mverb=0.3)

# Delayed bell arpeggio
m15 >> bell([0, 2, 4, 7],dur=1/4,oct=6,delay=0.25,amp=0.5,mverb=0.4)

# ===== EUCLIDEAN ARPEGGIOS =====
# Euclidean rhythm arpeggio
m16 >> pluck([0, 2, 4, 7],dur=PDur(5, 8),oct=5,amp=0.6)

# Complex euclidean
m17 >> pluck([0, 2, 4, 7, 9],dur=PDur(7, 16),oct=5,amp=0.5,lpf=2400)

# ===== RANDOM VARIATIONS =====
# Random note selection
m18 >> pluck(PRand([0, 2, 4, 7]),dur=1/4,oct=5,amp=0.6)

# Random octave
m19 >> pluck([0, 2, 4, 7],dur=1/4,oct=PRand([4, 5, 6]),amp=0.5)

# ===== WITH PANNING =====
# Stereo arpeggio
m20 >> pluck([0, 2, 4, 7],dur=1/4,oct=5,pan=[-0.5, -0.2, 0.2, 0.5],amp=0.6)

# Moving pan
m21 >> pluck([0, 2, 4, 7],dur=1/4,oct=5,pan=linvar([-1, 1], 16),amp=0.6)

# ===== DELAYED ARPEGGIOS =====
# Echo effect
m22 >> pluck([0, 2, 4, 7],dur=1/4,oct=5,echo=0.25,delay=0.5,amp=0.6)

# Long delay
m23 >> pluck([0, 2, 4],dur=1/2,oct=5,delay=[0, 0.5, 1, 1.5],feed=0.3,amp=0.6)

# ===== VIBRATO =====
# Vibrato on arpeggio
m24 >> pluck([0, 2, 4, 7],dur=1/4,oct=5,vib=4,vibdepth=0.1,amp=0.6)

# Variable vibrato
m25 >> pluck([0, 2, 4, 7],dur=1/4,oct=5,vib=linvar([0, 8], 16),vibdepth=0.2,amp=0.6)

# ===== PLAITS ARPEGGIOS =====
# Plaits engine arpeggio
m26 >> plaits([0, 2, 4, 7],dur=1/4,oct=5,engine=5,timbre=0.6,morph=0.5,amp=0.5)

# Moving timbre
m27 >> plaits([0, 2, 4, 7],dur=1/4,oct=5,engine=7,timbre=linvar([0.2, 0.9], 32),morph=0.7,amp=0.5)

# ===== WALKING ARPEGGIOS =====
# Walking pattern
m28 >> pluck(PWalk(8, 1, 1),dur=1/4,oct=5,amp=0.6)

# ===== LAYERED ARPEGGIOS =====
# Multiple octaves
m29 >> pluck([0, 2, 4, 7],dur=1/4,oct=(4, 5, 6),amp=0.4,lpf=2000).unison(2)

# ===== CONTROL TIPS =====
# Gradually speed up
# m1.dur = linvar([1/4, 1/16], 64)

# Add reverb
# m1.mverb = 0.5

# Change pattern
# m1.degree = [0, 2, 4, 6, 9]

# Shuffle pattern
# m1.every(4, "shuffle")
