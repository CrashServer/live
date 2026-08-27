# tpl house groove 124
# template

# ===== SETUP =====
Clock.bpm = 124
Scale.default = Scale.minor
Root.default = "E"

# ===== SECTION 1: INTRO - DRUMS =====
# Four-on-the-floor kick
k1 >> play("x ", sample=0, amp=1.4, lpf=200, lpr=0.2)

# Classic house hi-hat
h1 >> play("-", dur=1/4, sample=2, amp=0.6, hpf=7000, pan=PWhite(-0.3, 0.3))

# (Build for 16 beats)

# ===== SECTION 2: ADD SNARE =====
# Snare on 2 and 4
s1 >> play("..s.", sample=1, amp=0.9, mverb=0.3)

# (Groove for 16 beats)

# ===== SECTION 3: ADD BASS =====
# House bass line
b1 >> lbass([0, _, 0, 2], dur=1/2, oct=4, amp=0.8, lpf=1400, cutoff=1200)

# (Let it groove - 32 beats)

# ===== SECTION 4: ADD CHORDS =====
# Piano-style organ chords
c1 >> organ([(0, 2, 4), (1, 3, 5), (2, 4, 6), (3, 5, 7)],dur=4,oct=4,amp=0.4,sus=3.5,lpf=2000,mverb=0.3)

# (Build energy - 32 beats)

# ===== SECTION 5: ADD MELODY =====
# Bell melody
m1 >> bell([0, 2, 4, 7, 9, 7, 4, 2],dur=1/2,oct=6,amp=0.6,delay=0.25,feed=0.2,mverb=0.4)

# (Main section - 64 beats)

# ===== SECTION 6: ADD TEXTURE =====
# Open hi-hat
h2 >> play("......o.", dur=1/2, sample=4, amp=0.5, hpf=6000)

# Percussion layer
p1 >> play("..p...p.", dur=1/4, sample=7, amp=0.5, pan=PWhite(-0.7, 0.7))

# Shaker
p2 >> play("v.v.v.v.", dur=1/4, sample=8, amp=0.4, hpf=5000)

# (Peak energy - 64 beats)

# ===== SECTION 7: BREAKDOWN =====
# Stop drums, keep pads
# k1.stop()
# s1.stop()
# h1.stop()
# h2.stop()
# b1.stop()

# Pad chords only
c2 >> organ((0, 2, 4, 6),dur=4,oct=(3, 4, 5),amp=0.5,sus=4,lpf=linvar([800, 2400], 64),lpr=0.2,mverb=0.7)

# Sustained melody
m2 >> bell([0, 2, 4],dur=4,oct=6,amp=0.6,sus=4,mverb=0.8)

# (Breakdown - 32 beats)

# ===== SECTION 8: BUILD-UP =====
# Bring back kick
# k1.start()
# (wait 8 beats)

# Add filtered hi-hat
h3 >> play("-", dur=1/4, sample=2,hpf=linvar([6000, 12000], 16),hpr=0.4,amp=linvar([0.4, 0.8], 16))

# Rising snare roll (in last 4 beats before drop)
# s2 >> play("s", dur=1/8, sample=1, amp=linvar([0.4, 1.2], 4))

# (Build - 16 beats)

# ===== SECTION 9: DROP =====
# Everything hits
# Stop build elements
# h3.stop()
# s2.stop()
# c2.stop()
# m2.stop()

# Restart main groove
# s1.start()
# h1.start()
# h2.start()
# b1.start()

# Add energy to bass
b1.lpf = linvar([800, 1800], 32)
b1.amp = 0.9

# Bring back melody
# m1.start()

# (Peak drop - 64 beats)

# ===== SECTION 10: OUTRO =====
# Gradually remove elements
# m1.stop()  # Remove melody
# (wait 16 beats)
# c1.amp = linvar([0.4, 0], 16)  # Fade chords
# (wait 16 beats)
# b1.stop()  # Remove bass
# (wait 16 beats)
# h2.stop()
# p1.stop()
# p2.stop()
# (wait 16 beats)
# s1.stop()  # Remove snare
# (wait 16 beats)
# h1.amp = linvar([0.6, 0], 16)  # Fade hi-hat
# k1.amp = linvar([1.4, 0], 16)  # Fade kick

# ===== ALTERNATIVE VARIATIONS =====

# Variation 1: Add vocal sample
# v1 >> loop("vocals8", dur=8, sample=2, hpf=400, mverb=0.5, amp=0.7)

# Variation 2: Add string pad
# str1 >> swell((0, 2, 4, 6), dur=8, oct=4, amp=0.4, mverb=0.7, slide=-0.1)

# Variation 3: Add filtered noise riser
# n1 >> play("*", dur=16, sample=5, hpf=linvar([2000, 12000], 16), amp=linvar([0, 0.6], 16))

# Variation 4: Add chord stabs
# stab >> organ((0, 2, 4), dur=2, oct=5, amp=0.7, sus=0.1, lpf=2400).every(8, "shuffle")

# ===== CONTROL TIPS =====
# Add swing to hi-hats
# h1.human(60, 6, 5)

# Open bass filter gradually
# b1.lpf = linvar([1000, 2000], 64)

# Add distortion to kick
# k1.drive = 0.2
# k1.shape = 0.3

# Vary chord voicings
# c1.oct = var([4, (4, 5)], 16)
