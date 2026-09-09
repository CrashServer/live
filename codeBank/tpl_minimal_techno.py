# tpl minimal techno 128
# template

# ===== SETUP =====
Clock.bpm = 128
Scale.default = Scale.minor
Root.default = "F#"

# ===== SECTION 1: INTRO - KICK ONLY =====
# Clean four-on-the-floor kick
k1 >> play("x ", sample=0, amp=1.3, lpf=150, lpr=0.2)

# (Let run for 16-32 beats)

# ===== SECTION 2: ADD HI-HAT =====
# Minimal hi-hat pattern
h1 >> play("-.--..--", dur=1/4, sample=0, amp=0.5, hpf=10000)

# (Build for 16 beats)

# ===== SECTION 3: ADD BASS =====
# Simple root note bass
b1 >> lbass([0], dur=1, oct=4, amp=0.7, lpf=1200, cutoff=1000)

# (Let groove for 32 beats)

# ===== SECTION 4: ADD SUBTLE SNARE =====
# Minimal snare/clap
s1 >> play("....s...", dur=1/2, sample=0, amp=0.7)

# (Build tension for 16 beats)

# ===== SECTION 5: ADD MELODIC ELEMENT =====
# Filtered bass pattern
b2 >> lbass([0, _, 0, 2],dur=1/2,oct=4,lpf=linvar([400, 1600], 64),lpr=0.3,amp=0.6)

# (Main groove - 64 beats)

# ===== SECTION 6: ADD TEXTURE =====
# Sparse rhythmic hi-hat
h2 >> play("-", dur=1/4, sample=2, amp=0.4, hpf=7000, pan=PWhite(-0.3, 0.3))

# Subtle percussion
p1 >> play("..p...p.", dur=1/4, sample=7, amp=0.4, pan=PWhite(-0.7, 0.7))

# (Let it ride - 64 beats)

# ===== SECTION 7: BREAKDOWN =====
# Stop bass, keep drums minimal
# b1.stop()
# b2.stop()
# s1.stop()

# Just kick and filtered hi-hat
# h1.hpf = linvar([8000, 12000], 32)

# (Breakdown - 16-32 beats)

# ===== SECTION 8: DROP =====
# Bring everything back
# b1.start()
# b2.start()
# s1.start()

# Add moving bass
b1.lpf = linvar([600, 1600], 32)

# (Main section - 64 beats)

# ===== SECTION 9: OUTRO =====
# Gradually remove elements
# b2.stop()  # Remove melodic bass
# (wait 16 beats)
# s1.stop()  # Remove snare
# (wait 16 beats)
# b1.stop()  # Remove main bass
# (wait 16 beats)
# h2.stop()  # Remove texture
# p1.stop()
# (wait 16 beats)
# h1.stop()  # Just kick
# (wait 16 beats)
# k1.stop()  # Fade out

# ===== ALTERNATIVE VARIATIONS =====

# Variation 1: Add filter sweep bass
# b3 >> lbass([0], dur=1, oct=4, lpf=linvar([300, 2400], 128), lpr=0.4, amp=0.7)

# Variation 2: Add subtle chord stab
# c1 >> organ((0, 2, 4), dur=4, oct=4, amp=0.3, sus=0.1, lpf=800)

# Variation 3: Add noise texture
# n1 >> play("*", dur=8, sample=5, amp=0.2, hpf=8000, mverb=0.7)

# ===== CONTROL TIPS =====
# Build tension: Gradually open hi-hat filter
# h1.hpf = linvar([8000, 14000], 64)

# Create breakdown: Close bass filter
# b1.lpf = linvar([1200, 300], 32)

# Add movement: Modulate bass cutoff
# b1.cutoff = linvar([600, 1800], 32)

# Humanize: Add subtle timing variation
# k1.human(30, 4, 4)
# h1.human(50, 5, 5)
