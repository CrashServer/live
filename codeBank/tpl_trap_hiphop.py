# tpl drums trap
# template

# Setup
Clock.bpm = 140

# ===== BASIC TRAP =====
# 808 kick pattern
k1 >> play("x...x..x", sample=0, amp=1.5, lpf=100)

# Trap snare
s1 >> play("....s...", sample=1, amp=0.9, mverb=0.2)

# Hi-hat pattern with rolls
h1 >> play("-.--.--[--]", dur=1/4, sample=2, amp=0.6, hpf=8000)

# ===== CLASSIC 808 PATTERN =====
# Deep 808 kick
k2 >> play("x...x.x.", sample=5, amp=1.6, lpf=80, lpr=0.3, sus=2)

# Clap on 2 and 4
c1 >> play("....c...", dur=1/2, sample=3, amp=0.8)

# Fast hi-hat with rolls
h2 >> play("-.--.--[---]", dur=1/4, sample=2, amp=0.7, hpf=9000)

# Open hi-hat hits
o1 >> play("......o.", dur=1/2, sample=4, amp=0.5, hpf=6000)

# ===== HI-HAT ROLLS =====
# Regular hi-hat
h3 >> play("-", dur=1/4, sample=2, amp=0.6, hpf=8000)

# Roll pattern (16th and 32nd notes)
h4 >> play("[----]", dur=var([1, 1/2], [7, 1]), sample=2, amp=0.7, hpf=9000, pan=PWhite(-1, 1))

# ===== TRIPLET HI-HATS =====
# Triplet feel hi-hats
h5 >> play("-", dur=1/3, sample=2, amp=PWhite(0.4, 0.8), hpf=8000)

# Triplet rolls
h6 >> play("---", dur=var([1, 1/3], [6, 2]), sample=2, amp=0.7, hpf=9000)

# ===== SNARE VARIATIONS =====
# Main snare
s2 >> play("....s...", dur=1/2, sample=1, amp=1.0)

# Ghost snares
s3 >> play(".s.s.s.s", dur=1/4, sample=1, amp=0.3, hpf=400)

# Layered clap
c2 >> play("....c...", dur=1/2, sample=3, amp=0.7, delay=0.01)

# ===== BOOMBAP HIP-HOP =====
Clock.bpm = 93

# Classic boom
k3 >> play("x.x.", sample=0, amp=1.3, lpf=150)

# Bap snare
s4 >> play("..s.", sample=4, amp=1.0, mverb=0.3)

# Jazzy hi-hat
h7 >> play("-.--.--.", dur=1/4, sample=2, amp=0.5, hpf=7000, pan=var([-0.5, 0.5], 4))

# ===== MODERN TRAP WITH SAMPLES =====
Clock.bpm = 140

# 808 kick with pitch envelope
k4 >> play("x...x..x", sample=0, amp=1.5, bend=-0.3, sus=1.5, lpf=100)

# Layered snare + rim
s5 >> play("....s...", sample=[1, 5], amp=[1.0, 0.6])

# Rapid hi-hat pattern
h8 >> play(".{...c}..c...", sample=5, amp=P*[0, 1], rate=(0.5, 2)).sometimes("stutter")

# 808 rim shots
r1 >> play("...r.r..", dur=1/2, sample=2, amp=0.7, hpf=2000)

# ===== DRILL PATTERN =====
# Fast drill hi-hats
h9 >> play("-", dur=1/8, sample=2, amp=PWhite(0.3, 0.7), hpf=9000, pan=PWhite(-0.5, 0.5))

# Sliding 808
k5 >> play("x...x.x.", sample=0, amp=1.5, slide=var([0, 0.3], [7, 1]), lpf=100)

# Snare with reverb
s6 >> play("....s...", sample=1, amp=0.9, mverb=0.4, mverbmix=0.6)

# ===== STUTTER EFFECTS =====
# Hi-hat with random stutters
h10 >> play("-", dur=1/4, sample=2, amp=0.6, hpf=8000).sometimes("stutter", PRand([2, 4, 8, 16]))

# Kick with occasional glitch
k6 >> play("x ", sample=0, amp=1.3).rarely("stutter", PRand(4))

# ===== PERCUSSION LAYERS =====
# Congas
p1 >> play("..p...p.", dur=1/4, sample=7, amp=0.6, pan=PWhite(-0.7, 0.7))

# Shakers
p2 >> play("v.....v.", dur=1/2, sample=8, amp=0.4, hpf=5000)

# Rim shots
p3 >> play("...u....", dur=1/2, sample=2, amp=0.5, hpf=3000)

# ===== HUMAN FEEL =====
# Humanized 808 kick
k7 >> play("x...x..x", sample=0, amp=1.4, lpf=100).human(30, 4, 4)

# Humanized hi-hats with swing
h11 >> play("-", dur=1/4, sample=2, amp=PWhite(0.4, 0.8), hpf=8000).human(60, 5, 5)

# ===== CONTROL TIPS =====
# Add rolls every 4 bars
# h1.every(4, lambda: h1.dur.set(1/8))

# Reset
# h1.dur = 1/4

# Stutter snare occasionally
# s1.sometimes("stutter", 4, rate=2)
