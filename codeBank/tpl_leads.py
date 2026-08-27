# tpl melody leads
# template

# Setup
Clock.bpm = 128
Scale.default = Scale.minor
Root.default = "E"

# ===== SIMPLE MELODIES =====
# Basic melody
l1 >> bell([0, 2, 4, 7, 9, 7, 4, 2], dur=1/2, oct=5, amp=0.7, mverb=0.3)

# Short hook
l2 >> bell([0, 4, 7, 4], dur=1, oct=5, amp=0.8, mverb=0.4)

# ===== LONG SUSTAINED NOTES =====
# Sustained lead
l3 >> bell([0, 2, 4], dur=4, oct=5, amp=0.7, sus=4, mverb=0.5)

# With filter movement
l4 >> bell([0, 2, 4, 7],dur=4,oct=5,sus=4,lpf=linvar([1200, 4000], 64),lpr=0.2,amp=0.7,mverb=0.5)

# ===== FAST RUNS =====
# Quick melodic run
l5 >> bell([0, 2, 4, 5, 7, 9, 11, 12], dur=1/4, oct=5, amp=0.6)

# Descending run
l6 >> bell([12, 11, 9, 7, 5, 4, 2, 0], dur=1/4, oct=5, amp=0.6, lpf=2400)

# ===== WITH VIBRATO =====
# Vibrato lead
l7 >> bell([0, 2, 4, 7],dur=2,oct=5,vib=6,vibdepth=0.2,amp=0.7,mverb=0.4)

# Variable vibrato
l8 >> bell([0, 2, 4, 7],dur=2,oct=5,vib=linvar([0, 8], 16),vibdepth=linvar([0, 0.3], 16),amp=0.7)

# ===== PLAITS LEAD =====
# Classic plaits lead
l9 >> plaits([0, 2, 4, 7, 9],dur=1/2,oct=5,engine=5,timbre=0.7,morph=0.6,harm=0.5,amp=0.6,mverb=0.4)

# Moving parameters
l10 >> plaits([0, 2, 4, 7],dur=1,oct=5,engine=var([5, 7], 16),timbre=linvar([0.3, 0.9], 32),morph=linvar([0.4, 0.8], 24),amp=0.6,mverb=0.5)

# ===== PORTAMENTO/GLIDE =====
# Sliding between notes
l11 >> bell([0, 4, 7, 12],dur=1,oct=5,slide=0.2,amp=0.7,mverb=0.4)

# Variable glide
l12 >> plaits([0, 2, 4, 7],dur=1,oct=5,porta=linvar([0, 0.5], 32),engine=5,amp=0.6)

# ===== OCTAVE JUMPS =====
# Jumping melody
l13 >> bell([0, 7, 0, 4],dur=1,oct=[5, 6, 5, 6],amp=0.7,mverb=0.4)

# ===== DELAYED LEAD =====
# Echo lead
l14 >> bell([0, 4, 7],dur=1,oct=5,echo=0.5,delay=0.25,feed=0.3,amp=0.6,mverb=0.3)

# Ping-pong delay
l15 >> bell([0, 2, 4, 7],dur=2,oct=5,delay=[0, 0.25, 0.5, 0.75],feed=0.2,pan=linvar([-1, 1], 8),amp=0.6)

# ===== DISTORTED LEAD =====
# Overdriven lead
l16 >> bell([0, 2, 4, 7],dur=1,oct=5,shape=0.4,shape=0.3,amp=0.7,mverb=0.3)

# ===== STEREO LEAD =====
# Wide stereo lead
l17 >> bell([0, 2, 4, 7],dur=1,oct=5,amp=0.6,mverb=0.5).unison(4)

# Panning lead
l18 >> bell([0, 2, 4, 7],dur=1,oct=5,pan=linvar([-1, 1], 16),amp=0.7)

# ===== CHOPPY LEAD =====
# Staccato lead
l19 >> bell([0, 2, 4, 7, 9, 7, 4, 2],dur=1/4,oct=5,sus=0.1,amp=0.8,lpf=2400)

# ===== FILTERED LEAD =====
# Moving filter
l20 >> bell([0, 2, 4, 7],dur=2,oct=5,lpf=linvar([800, 4000], 32),lpr=0.3,amp=0.7,mverb=0.4)

# Band-pass lead
l21 >> bell([0, 2, 4, 7],dur=1,oct=5,bpf=linvar([800, 3200], 32),bpr=0.5,amp=0.7)

# ===== PLUCKY LEAD =====
# Short attack lead
l22 >> pluck([0, 2, 4, 7, 9],dur=1/2,oct=5,amp=0.7,lpf=2000,leg=0)

# ===== SAWBASS AS LEAD =====
# Sawtooth lead
l23 >> sawbass([0, 2, 4, 7],dur=1/2,oct=6,amp=0.6,lpf=linvar([1200, 3200], 32),lpr=0.2,mverb=0.3)

# ===== CS80 LEAD =====
# Classic synth lead
l24 >> cs80([0, 2, 4, 7],dur=2,oct=5,cutoff=linvar([800, 3200], 32),detune=0.3,vibspeed=6,vibdepth=0.15,amp=0.7)

# ===== CONTROL TIPS =====
# Add vibrato
# l1.vib = 6
# l1.vibdepth = 0.2

# Open filter
# l1.lpf = linvar([1200, 4000], 32)

# Add echo
# l1.echo = 0.5
# l1.delay = 0.25

# Distort
# l1.drive = 0.4
