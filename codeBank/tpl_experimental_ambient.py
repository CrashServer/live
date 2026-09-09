# tpl ambient 88
# template

# ===== SETUP =====
Clock.bpm = 88
Scale.default = Scale.locrian
Root.default = "D"

# ===== SECTION 1: INTRO - DRONE =====
# Deep drone bass
r1 >> organ((0),dur=32,oct=(2, 3),lpf=linvar([400, 800], 128),lpr=0.1,amp=0.5,sus=32,mverb=0.9)

# (Let evolve - 32 beats)

# ===== SECTION 2: ADD TEXTURE =====
# Granular cloud texture
t1 >> play("*",dur=8,sample=PRand(16),rate=PWhite(0.5, 2),amp=0.3,hpf=6000,mverb=0.8,pan=PWhite(-1, 1))

# (Build atmosphere - 32 beats)

# ===== SECTION 3: ADD SPARSE MELODY =====
# Slow, evolving plaits melody
m1 >> plaits(var([0, [2, 4], 7, [9, 11]], [16, 8, 16, 8]),dur=8,oct=var([4, 5], [32, 16]),engine=var([8, 11], 64),timbre=linvar([0.3, 0.9], 128),morph=linvar([0.5, 0.9], 96),harm=0.3,amp=0.5,mverb=0.8,delay=[0, 2, 4],feed=0.3)

# (Develop - 64 beats)

# ===== SECTION 4: ADD RHYTHM =====
# Subtle, irregular rhythm
p1 >> play("-",dur=PDur(var([3, 5, 7], [16, 8, 8]), 16),sample=PRand(8),rate=PWhite(0.8, 1.5),amp=PWhite(0.2, 0.6),hpf=8000,pan=PWhite(-0.8, 0.8),mverb=0.6).human(80, 8, 8)

# (Add movement - 32 beats)

# ===== SECTION 5: ADD HARMONIC LAYER =====
# Evolving chord pad
q1 >> organ(var([((0, 2, 4)), ((0, 2, 4, 6, 9))], [32, 16]),dur=16,oct=(3, 4, 5),lpf=linvar([600, 2400], 128),lpr=0.2,crush=0.3,bits=var([8, 12], 16),amp=0.4,sus=16,mverb=0.8).unison(4)

# (Peak complexity - 64 beats)

# ===== SECTION 6: ADD GLITCH ELEMENTS =====
# Stuttering texture
g1 >> play("v",dur=var([1/4, 1/2, 1], [4, 2, 2]),sample=PRand(16),rate=PWhite(-2, 2),amp=var([0, 0.5], [7, 1]),hpf=4000,pan=PWhite(-1, 1)).sometimes("stutter", PRand([4, 8, 16]))

# Random bass hits
b1 >> lbass(var([0, [_, 0, 7]], [8, 4]),dur=var([4, 2], [12, 4]),oct=var([2, 3], [16, 8]),lpf=var([400, 800], 8),amp=var([0, 0.7], [7, 1]),mverb=0.6)

# (Chaotic middle - 64 beats)

# ===== SECTION 7: BREAKDOWN =====
# Stop rhythm and glitches
# p1.stop()
# g1.stop()
# b1.stop()

# Just pads and melody
# m1.dur = 16
# m1.amp = 0.4

# Add second drone
r2 >> organ((7),dur=32,oct=(2, 3, 4),lpf=linvar([300, 1200], 128),amp=0.4,sus=32,mverb=0.9)

# (Sparse section - 64 beats)

# ===== SECTION 8: REBUILD =====
# Bring back texture slowly
# t1.amp = linvar([0, 0.4], 32)

# Add filtered noise sweep
w1 >> play("*",dur=16,sample=5,hpf=linvar([1000, 12000], 64),amp=linvar([0.2, 0.6], 64),mverb=0.8)

# (Build - 32 beats)

# ===== SECTION 9: CLIMAX =====
# Everything together
# p1.start()
# b1.start()

# Add moving filter to drone
r1.lpf = linvar([200, 1600], 64)
q1.lpf = linvar([400, 3200], 64)

# Intensify melody
m1.amp = 0.7
m1.delay = [0, 1, 2, 3, 4]
m1.feed = 0.5

# (Climax - 64 beats)

# ===== SECTION 10: OUTRO - DECAY =====
# Gradually remove elements
# g1.stop()
# (wait 16 beats)
# b1.amp = linvar([0.7, 0], 32)
# (wait 32 beats)
# p1.amp = linvar([0.4, 0], 32)
# (wait 32 beats)
# m1.amp = linvar([0.7, 0], 64)
# (wait 64 beats)
# q1.amp = linvar([0.4, 0], 64)
# (wait 64 beats)
# r1.amp = linvar([0.5, 0], 128)
# r2.amp = linvar([0.4, 0], 128)

# ===== ALTERNATIVE VARIATIONS =====

# Variation 1: Add reverb-heavy bell hits
# bell1 >> bell(PRand([0, 2, 4, 7, 9, 11]), dur=var([8, 16], 32), oct=7,
#              amp=0.4, mverb=0.95, delay=[0, 4, 8], feed=0.4)

# Variation 2: Add field recording loop
# field1 >> loop("ambient64", dur=64, sample=2, amp=0.3, lpf=1200, mverb=0.7)

# Variation 3: Add detuned supersaw pad
# saw1 >> supersaw((0, 4, 7), dur=16, oct=(3, 4), cutoff=linvar([600, 1800], 128),
#                 amp=0.3, mverb=0.8, sub=2).unison(8)

# Variation 4: Add granular synthesis
# grain1 >> plaits(var([0, 7], 32), dur=16, engine=13, timbre=linvar([0.2, 0.8], 64),
#                 morph=0.9, oct=4, amp=0.4, mverb=0.9)

# ===== CONTROL TIPS =====
# Create evolving drone
# r1.lpf = linvar([200, 1200], 256)

# Add random pitch variation
# m1.degree = m1.degree + PWhite(-0.1, 0.1)

# Increase harmonic complexity
# q1.degree = var([((0,2,4)), ((0,2,4,6,9,11))], [32, 16])

# Modulate reverb amount
# Master().mverb = linvar([0.5, 0.9], 128)
