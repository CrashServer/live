# tpl pads chords
# template

# Setup
Clock.bpm = 128
Scale.default = Scale.minor
Root.default = "E"

# ===== SIMPLE CHORD PADS =====
# Basic triad pad
p1 >> organ((0, 2, 4), dur=4, oct=4, amp=0.5, sus=4, mverb=0.5)

# Seventh chord pad
p2 >> organ((0, 2, 4, 6), dur=4, oct=4, amp=0.5, sus=4, mverb=0.6)

# ===== CHORD PROGRESSIONS =====
# Classic progression
p3 >> organ([(0, 2, 4), (1, 3, 5), (2, 4, 6), (3, 5, 7)],dur=4,oct=4,amp=0.5,sus=4,mverb=0.5)

# Extended chords
p4 >> organ([(0, 2, 4, 6), (1, 3, 5, 7), (2, 4, 6, 9)],dur=4,oct=4,amp=0.5,sus=4,mverb=0.6)

# ===== LAYERED OCTAVES =====
# Multi-octave pad
p5 >> organ((0, 2, 4),dur=4,oct=(3, 4, 5),amp=0.4,sus=4,mverb=0.6)

# ===== MOVING FILTER =====
# Filtered pad
p6 >> organ((0, 2, 4, 6),dur=4,oct=4,lpf=linvar([600, 2400], 64),lpr=0.2,amp=0.5,sus=4,mverb=0.5)

# Breathing filter
p7 >> organ((0, 2, 4),dur=4,oct=4,lpf=var([800, 2000], 8),amp=0.5,sus=4,mverb=0.6)

# ===== VARSAW PADS =====
# Detuned saw pad
p8 >> varsaw((0, 2, 4),dur=4,oct=4,detune=0.3,amp=0.4,sus=4,lpf=1200,mverb=0.6)

# Moving saw pad
p9 >> varsaw((0, 2, 4, 6),dur=8,oct=(3, 4, 5),lpf=linvar([600, 2400], 128),lpr=0.2,cut=2,cutmix=0.1,amp=0.4,sus=6)

# ===== SUPERSAW PADS =====
# Wide supersaw
p10 >> supersaw((0, 2, 4),dur=4,oct=(4, 5),cutoff=linvar([800, 2000], 64),sub=2,amp=0.3,sus=4,mverb=0.7).unison(4)

# ===== CS80 PADS =====
# Classic CS80 sound
p11 >> cs80((0, 2, 4, 6),dur=4,oct=4,cutoff=linvar([1000, 3000], 64),detune=0.5,dec=2,vibspeed=3,vibdepth=0.1,amp=0.5,mverb=0.6)

# ===== TREMOLO PADS =====
# Pulsing pad
p12 >> organ((0, 2, 4),dur=4,oct=4,tremolo=4,tremolo_=0.5,amp=0.5,sus=4,mverb=0.5)

# Variable tremolo
p13 >> organ((0, 2, 4, 6),dur=4,oct=4,tremolo=var([2, 4, 8], 16),tremolo_=0.6,amp=0.5,sus=4,mverb=0.6)

# ===== PLAITS PADS =====
# Plaits pad engine
p14 >> plaits((0, 2, 4),dur=4,oct=4,engine=8,timbre=0.7,morph=0.8,harm=0.3,amp=0.5,mverb=0.7)

# Moving plaits pad
p15 >> plaits((0, 2, 4, 6),dur=4,oct=4,engine=var([8, 11], 16),timbre=linvar([0.4, 0.9], 64),morph=linvar([0.5, 0.9], 48),amp=0.5,mverb=0.7)

# ===== STEREO PADS =====
# Wide stereo pad
p16 >> organ((0, 2, 4),dur=4,oct=4,amp=0.5,sus=4,mverb=0.6).unison(4)

# Panning pad
p17 >> organ((0, 2, 4, 6),dur=4,oct=4,pan=linvar([-0.5, 0.5], 32),amp=0.5,sus=4,mverb=0.6)

# ===== BITCRUSHED PADS =====
# Digital pad
p18 >> organ((0, 2, 4),dur=4,oct=4,crush=0.5,bits=var([8, 12], 8),amp=0.5,sus=4,mverb=0.5)

# ===== SUSTAINED STRING PADS =====
# String-like pad
p19 >> swell((0, 2, 4, 6),dur=8,oct=4,slide=-0.1,tremolo=var([2, 4], 32),amp=0.5,mverb=0.7)

# ===== SPARSE PADS =====
# Evolving sparse pad
p20 >> organ(var([((0, 2, 4)), ((0, 2, 4, 6, 9))], [16, 8]),dur=8,oct=4,lpf=linvar([800, 2400], 128),amp=0.4,sus=8,mverb=0.7)

# ===== DRONE PADS =====
# Single note drone
p21 >> organ((0),dur=16,oct=(3, 4, 5),lpf=linvar([600, 1800], 128),amp=0.4,sus=16,mverb=0.8)

# Two-note drone
p22 >> organ((0, 7),dur=16,oct=(3, 4),amp=0.4,sus=16,mverb=0.8)

# ===== RHYTHMIC PADS =====
# Pulsing chord pad
p23 >> organ((0, 2, 4),dur=1/2,oct=4,amp=var([0.6, 0], 4),sus=0.5,mverb=0.5)

# Gated pad
p24 >> organ((0, 2, 4, 6),dur=1/4,oct=4,amp=PBin(),sus=0.3,lpf=1600,mverb=0.5)

# ===== CONTROL TIPS =====
# Gradually open filter
# p1.lpf = linvar([600, 2400], 128)

# Add more reverb
# p1.mverb = 0.8

# Fade in
# p1.amp = linvar([0, 0.6], 64)

# Change chord
# p1.degree = (0, 2, 4, 6)

# Widen stereo
# p1.unison(4)
