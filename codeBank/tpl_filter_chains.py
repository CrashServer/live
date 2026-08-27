# tpl fx filterchains
# template

# Setup
Clock.bpm = 128

# ===== LOW-PASS FILTER SWEEPS =====
# Basic LPF sweep
f1 >> lbass([0], dur=1, oct=4, lpf=linvar([400, 2400], 32), lpr=0.2, amp=0.8)

# Slow sweep
f2 >> lbass([0, 2], dur=1/2, oct=4, lpf=linvar([300, 3200], 64), lpr=0.3, amp=0.8)

# Pulsing LPF
f3 >> lbass([0], dur=1, oct=4, lpf=var([600, 1800], 4), lpr=0.2, amp=0.8)

# Exponential sweep
f4 >> lbass([0, 2, 4], dur=1/2, oct=4, lpf=expvar([400, 3200], 32), lpr=0.3, amp=0.8)

# ===== HIGH-PASS FILTER =====
# Basic HPF sweep
f5 >> play("-", dur=1/4, hpf=linvar([2000, 8000], 32), hpr=0.3, amp=0.6)

# Removing lows gradually
f6 >> lbass([0], dur=1, oct=4, hpf=linvar([0, 1200], 64), hpr=0.4, amp=0.8)

# Pulsing HPF
f7 >> play("-", dur=1/4, hpf=var([4000, 8000], 4), hpr=0.3, amp=0.6)

# ===== BAND-PASS FILTER =====
# Sweeping band-pass
f8 >> lbass([0, 2], dur=1/2, oct=4, bpf=linvar([400, 2400], 32), bpr=0.5, amp=0.8)

# Narrow band-pass
f9 >> play("-", dur=1/4, bpf=linvar([800, 4000], 32), bpr=0.8, amp=0.6)

# ===== COMBINED FILTERS =====
# LPF + HPF (band-pass effect)
f10 >> lbass([0], dur=1, oct=4,lpf=linvar([1200, 2400], 32),lpr=0.2,hpf=linvar([200, 800], 32),hpr=0.3,amp=0.8)

# Moving both filters
f11 >> play("-", dur=1/4,lpf=linvar([2000, 8000], 64),lpr=0.2,hpf=linvar([200, 2000], 64),hpr=0.3,amp=0.6)

# ===== RESONANCE SWEEPS =====
# High resonance LPF
f12 >> lbass([0], dur=1, oct=4, lpf=linvar([600, 2400], 32), lpr=0.8, amp=0.7)

# Moving resonance
f13 >> lbass([0, 2], dur=1/2, oct=4,lpf=linvar([800, 2400], 32),lpr=linvar([0.1, 0.9], 16),amp=0.8)

# Self-oscillating filter
f14 >> lbass([0], dur=1, oct=4, lpf=linvar([400, 1600], 32), lpr=0.95, amp=0.6)

# ===== MULTI-MODE FILTER =====
# MPF (multi-mode filter)
f15 >> lbass([0, 2], dur=1/2, oct=4,mpf=linvar([800, 3200], 32),mpr=0.3,amp=0.8)

# ===== FILTER WITH DISTORTION =====
# Filter before distortion
f16 >> lbass([0], dur=1, oct=4,lpf=linvar([600, 2400], 32),lpr=0.4,shape=0.4,shape=0.3,amp=0.7)

# Distortion before filter
f17 >> lbass([0, 2], dur=1/2, oct=4,shape=0.5,shape=0.4,lpf=linvar([800, 2000], 32),lpr=0.2,amp=0.7)

# ===== STEPPED FILTERS =====
# Step-wise filter movement
f18 >> lbass([0], dur=1, oct=4,lpf=PStep(8, 2400, 400),lpr=0.2,amp=0.8)

# Random filter steps
f19 >> lbass([0, 2], dur=1/2, oct=4,lpf=PRand([600, 1200, 1800, 2400]),lpr=0.3,amp=0.8)

# ===== FILTER ENVELOPE FOLLOWERS =====
# Following another player's amplitude
# Define a1 first
# a1 >> play("x.x.x..x", sample=0, amp=1)
# f20 >> lbass([0], dur=1, oct=4, lpf=400 + (a1.amp * 2000), amp=0.8)

# ===== FORMANT-STYLE FILTERS =====
# Vowel-like filter movement
f21 >> lbass([0], dur=1, oct=4,bpf=var([300, 800, 2200], [8, 4, 4]),bpr=0.6,amp=0.8)

# ===== CUTOFF MODULATION =====
# Cutoff parameter (alternative to lpf)
f22 >> plaits([0, 2, 4], dur=1/4, oct=5,cutoff=linvar([1000, 6000], 32),bright=linvar([0.3, 0.9], 16),engine=5,amp=0.6)

# ===== FILTER WITH TREMOLO =====
# Pulsing filter amplitude
f23 >> lbass([0], dur=1, oct=4,lpf=linvar([600, 2400], 32),lpr=0.3,tremolo=4,tremolo_=0.5,amp=0.8)

# ===== NOTCH FILTER EFFECT =====
# Using HPF + LPF with gap
f24 >> play("-", dur=1/4,lpf=1000,lpr=0.5,hpf=900,hpr=0.5,amp=0.6)

# ===== FILTER WITH ECHO =====
# Filtered echo
f25 >> lbass([0, 2], dur=1/2, oct=4,lpf=linvar([800, 2400], 32),lpr=0.2,echo=0.5,delay=0.25,amp=0.8)

# ===== CONTROL TIPS =====
# Open filter over time
# f1.lpf = linvar([400, 3200], 64)

# Increase resonance
# f1.lpr = linvar([0.1, 0.8], 32)

# Switch to high-pass
# f1.hpf = linvar([200, 4000], 64)

# Add filter modulation
# f1.lpf = var([800, 1600, 2400], [4, 8, 4])
