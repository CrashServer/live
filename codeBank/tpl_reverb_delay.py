# tpl fx reverbdelay
# template

# Setup
Clock.bpm = 128

# ===== BASIC REVERB =====
# Simple reverb
r1 >> bell([0, 2, 4, 7], dur=1/2, oct=5, mverb=0.4, amp=0.6)

# Heavy reverb
r2 >> bell([0, 2, 4], dur=2, oct=5, mverb=0.8, amp=0.5)

# Subtle reverb
r3 >> pluck([0, 2, 4, 7], dur=1/4, oct=5, mverb=0.2, amp=0.6)

# ===== REVERB PARAMETERS =====
# Custom reverb mix
r4 >> bell([0, 2, 4, 7], dur=1, oct=5,mverb=0.6,mverbmix=0.5,amp=0.6)

# Reverb with damping
r5 >> bell([0, 2, 4], dur=2, oct=5,mverb=0.7,mverbdamp=0.8,mverbmix=0.6,amp=0.5)

# Reverb with diffusion
r6 >> bell([0, 2, 4, 7], dur=1, oct=5,mverb=0.6,mverbdiff=0.8,amp=0.6)

# ===== ROOM REVERB =====
# Small room
r7 >> pluck([0, 2, 4, 7], dur=1/4, oct=5,room=0.3,mix=0.2,amp=0.6)

# Large hall
r8 >> bell([0, 2, 4], dur=2, oct=5,room=0.9,mix=0.6,amp=0.5)

# ===== ROOM2 REVERB (alternative) =====
# Room2 reverb
r9 >> play("s", dur=1, sample=1,room2=0.7,mix2=0.5,damp2=0.6,amp=0.8)

# ===== DELAY/ECHO =====
# Simple delay
d1 >> bell([0, 2, 4], dur=1, oct=5,delay=0.5,amp=0.6)

# Multiple delay taps
d2 >> bell([0, 2, 4, 7], dur=1, oct=5,delay=[0, 0.25, 0.5, 0.75],amp=0.5)

# Delay with feedback
d3 >> bell([0, 2, 4], dur=2, oct=5,delay=0.5,feed=0.4,amp=0.6)

# ===== ECHO PARAMETER =====
# Echo (time-synced delay)
e1 >> bell([0, 2, 4, 7], dur=1/2, oct=5,echo=0.25,amp=0.6)

# Echo with mix
e2 >> bell([0, 2, 4], dur=1, oct=5,echo=0.5,echomix=0.4,amp=0.6)

# Echo with time and mix
e3 >> bell([0, 2, 4, 7], dur=1/2, oct=5,echo=0.25,echotime=6,echomix=0.3,amp=0.6)

# ===== LONG DELAYS =====
# Long delay tail
d4 >> bell([0, 4, 7], dur=4, oct=5,delay=[0, 2, 4, 6],feed=0.3,amp=0.5)

# Evolving delay
d5 >> bell([0, 2, 4], dur=2, oct=5,delay=var([0.25, 0.5, 1], [8, 4, 4]),feed=0.4,amp=0.6)

# ===== PING-PONG DELAY =====
# Stereo ping-pong effect
p1 >> bell([0, 2, 4, 7], dur=1, oct=5,delay=[0, 0.25],pan=[-1, 1],feed=0.3,amp=0.6)

# ===== REVERB + DELAY =====
# Combined reverb and delay
rd1 >> bell([0, 2, 4], dur=1, oct=5,mverb=0.5,delay=0.5,feed=0.3,amp=0.6)

# Heavy space
rd2 >> bell([0, 4, 7], dur=2, oct=5,mverb=0.8,echo=0.5,feed=0.4,amp=0.5)

# ===== SLAPBACK DELAY =====
# Short slapback
s1 >> pluck([0, 2, 4, 7], dur=1/4, oct=5,delay=0.1,feed=0.1,amp=0.7)

# ===== RHYTHMIC DELAY =====
# Dotted eighth delay
rh1 >> bell([0, 2, 4], dur=1, oct=5,echo=0.375,feed=0.3,amp=0.6)

# Triplet delay
rh2 >> bell([0, 2, 4, 7], dur=1, oct=5,echo=1/3,feed=0.3,amp=0.6)

# ===== VARIABLE DELAY =====
# Random delay time
v1 >> bell([0, 2, 4, 7], dur=1/2, oct=5,delay=PWhite(0.1, 0.8),feed=0.2,amp=0.6)

# Modulating delay
v2 >> bell([0, 2, 4], dur=1, oct=5,delay=linvar([0.25, 1], 32),feed=0.3,amp=0.6)

# ===== DELAY ON DRUMS =====
# Delayed snare
ds1 >> play("..s.", sample=1,delay=0.25,feed=0.3,amp=0.8)

# Delayed hi-hat
dh1 >> play("-", dur=1/4, sample=2,echo=0.5,echomix=0.2,hpf=7000,amp=0.6)

# ===== FREEZE EFFECT =====
# Long reverb + feedback for freeze
f1 >> bell([0, 2, 4], dur=8, oct=5,mverb=0.9,delay=4,feed=0.7,amp=0.4)

# ===== GATED REVERB =====
# Short reverb on drums
g1 >> play("s", dur=1, sample=1,room=0.6,mix=0.4,damp2=0.9,amp=0.9)

# ===== CONTROL TIPS =====
# Add more reverb
# r1.mverb = 0.8

# Increase delay feedback
# d1.feed = 0.6

# Change delay time
# d1.delay = 0.75

# Sync echo to tempo
# e1.echo = 0.5  # half note
# e1.echo = 0.25  # quarter note
# e1.echo = 1/3  # triplet
