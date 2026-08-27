# tpl drums breakbeat
# template

# Setup
Clock.bpm = 140

# ===== BASIC BREAKBEAT =====
# Syncopated kick pattern
k1 >> play("x..x.x..", sample=0, amp=1.2, lpf=200)

# Snare on offbeats
s1 >> play("..s...s.", sample=1, amp=0.9)

# Breakbeat hi-hat
h1 >> play("-.--.--.", dur=1/4, sample=2, amp=0.6, hpf=7000)

# ===== AMEN BREAK STYLE =====
# Complex kick pattern
k2 >> play("x...x.x.", sample=0, amp=1.3)

# Layered snare with ghost notes
s2 >> play("..s.s.s.", sample=1, amp=[1, 0.4, 0.9], hpf=200)

# Fast hi-hat pattern
h2 >> play("-.-[--].-.-", dur=1/4, sample=2, amp=0.7, hpf=8000)

# Crash hits
c1 >> play("*.......", dur=1, sample=5, amp=0.8)

# ===== JUNGLE/DNB =====
# Fast tempo setting
Clock.bpm = 174

# Rapid fire kick
k3 >> play("x.x.x..x", dur=1/2, sample=0, amp=1.4, lpf=150)

# Snare rolls
s3 >> play("..s...s.", dur=1/2, sample=1, amp=1.0)
s4 >> play("......[ss]", dur=1/2, sample=2, amp=0.7)

# Continuous hi-hat
h3 >> play("-", dur=1/8, sample=3, amp=0.5, hpf=9000, pan=PWhite(-0.5, 0.5))

# ===== EUCLIDEAN BREAKBEAT =====
# Using PDur for interesting rhythms
k4 >> play("x ", dur=PDur(5, 8), sample=0, amp=1.2)

# Polyrhythmic snare
s5 >> play("s", dur=PDur(3, 8), sample=1, amp=0.8, delay=0.25)

# Complex hi-hat euclidean
h4 >> play("-", dur=PDur(7, 16), sample=2, amp=0.6, hpf=7000)

# ===== GLITCH BREAKBEAT =====
# Stuttering kick
k5 >> play("x.", sample=0, amp=1.2).sometimes("stutter", PRand([2, 4, 8]))

# Random snare placement
s6 >> play("s", dur=var([1/2, 1/4, 1], [8, 4, 2]), sample=PRand(8), amp=0.8)

# Glitchy hi-hat
h5 >> play("-", dur=1/4, sample=PRand(16), rate=PWhite(0.8, 2), amp=0.5, hpf=6000).sometimes("stutter", 4)

# ===== HALF-TIME BREAKBEAT =====
# Slow, heavy kick
k6 >> play("x...", sample=0, amp=1.5, lpf=180)

# Big snare
s7 >> play("..s.", sample=5, amp=1.2, mverb=0.4)

# Sparse hi-hat
h6 >> play("-.--.-.-", dur=1/2, sample=2, amp=0.6, hpf=8000)

# ===== COMPLEX PATTERN STRING =====
# Advanced pattern notation
b1 >> play("<(xxx(x.))(...(.x))..><.(---.)><..o.><..(...*).>",sample=((7,6),7,(7,2),7),dur=1/2,amp=0.8,lpf=linvar([200, 4000], 64)).sometimes("stutter", PRand(4).rnd(2))

# ===== WITH AMEN METHOD =====
# Apply amen break transformation
k7 >> play("x ", sample=0, amp=1.2)
h7 >> play("-", dur=1/4, sample=2, amp=0.6).sometimes("amen")

# ===== TRIM EFFECTS =====
# Cutting and rearranging
b2 >> play("x.s.-", sample=[0, 1, 2], amp=0.9).rarely("trim", 3, cycle=8)

# ===== CONTROL TIPS =====
# Convert to breakbeat feel
# d1.every(4, "amen")

# Add occasional fills
# s1.sometimes("stutter", 8)

# Shuffle pattern
# h1.every(8, "shuffle")
