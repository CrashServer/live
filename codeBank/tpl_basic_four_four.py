# tpl drums fourfour
# template

# Setup
Clock.bpm = 128

# ===== MINIMAL HOUSE =====
# Simple kick on every beat
d1 >> play("x ", sample=0, amp=1.2, lpf=200)

# Snare on 2 and 4
d2 >> play("..s.", sample=1, amp=0.8)

# Continuous hi-hat
d3 >> play("-", dur=1/4, sample=2, amp=0.6, hpf=8000)

# ===== CLASSIC HOUSE =====
# Kick with slight variation
k1 >> play("x.x.x.x.", sample=0, amp=1.2)

# Backbeat snare
s1 >> play("....s....", dur=1/4, sample=1, amp=0.8)

# 16th note hi-hats
h1 >> play("-", dur=1/4, sample=2, amp=0.5, hpf=6000, pan=PWhite(-0.3, 0.3))

# Clap layer
c1 >> play("....c....", dur=1/4, sample=3, amp=0.6)

# ===== TECHNO GROOVE =====
# Four-on-the-floor kick
k2 >> play("x ", sample=0, amp=1.5, lpf=150, lpr=0.2)

# Snare with variation
s2 >> play("..s.", sample=var([1, 2], [16, 8]), amp=0.9)

# Closed + open hi-hat pattern
h2 >> play("-.--.-[-]", dur=1/4, sample=2, amp=0.7, hpf=7000)
h3 >> play("......o.", dur=1/4, sample=3, amp=0.5, hpf=5000)

# ===== DEEP HOUSE =====
# Soft kick
k3 >> play("x ", sample=5, amp=1.0, lpf=300)

# Subtle snare
s3 >> play("..s.", sample=4, amp=0.6, mverb=0.3)

# Sparse hi-hat
h4 >> play("-.--.--.", dur=1/4, sample=1, amp=0.4, hpf=9000, pan=linvar([-0.5, 0.5], 16))

# Percussion layer
p1 >> play("..p...p.", dur=1/4, sample=7, amp=0.5, pan=PWhite(-1, 1))

# ===== MINIMAL TECHNO =====
# Clean kick
k4 >> play("x.", sample=0, amp=1.3, lpf=0)

# Minimal snare/clap
s4 >> play("....s...", dur=1/2, sample=0, amp=0.7)

# Sparse rhythmic hi-hat
h5 >> play("-.--..--", dur=1/4, sample=0, amp=0.5, hpf=10000)

# ===== WITH HUMAN FEEL =====
# Humanized kick
k5 >> play("x ", sample=0, amp=1.2).human(40, 5, 5)

# Humanized hi-hats with velocity variation
h6 >> play("-", dur=1/4, sample=2, amp=PWhite(0.4, 0.8), hpf=7000).human(60, 6, 3)

# Snare with timing variation
s5 >> play("..s.", sample=1, amp=0.8).human(30, 4, 4)

# ===== CONTROL TIPS =====
# Stop all drums
# d_all.stop()

# Solo just kick and hi-hat
# k1.solo()
# h1.solo()

# Add occasional stutter
# k1.sometimes("stutter", PRand(4))

# Shuffle hi-hats every 4 bars
# h1.every(4, "shuffle")
