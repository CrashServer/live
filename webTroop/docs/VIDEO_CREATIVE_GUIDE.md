# VidCtrl Creative Guide

## Quick Reference

```python
# Basic controls
VidCtrl.load(url)           # Load video (auto-opens window)
VidCtrl.seek(30)            # Jump to 30s
VidCtrl.stutter(0.2)        # Jump back 0.2s
VidCtrl.rate(0.5)           # Playback speed (0.25-2)
VidCtrl.play() / .pause()   # Transport
VidCtrl.loop(10, 20)        # Loop region
VidCtrl.clear_loop()        # Remove loop

# Patterns (auto-cycle on beat)
VidCtrl.pos([10, 40, 120])           # Cycle positions
VidCtrl.stut([0, 0.1, 0, 0.2])       # Cycle stutters
VidCtrl.rates([1, 0.5, 2, 0.25])     # Cycle speeds

# Beat-synced
VidCtrl.beat_loop(2)          # 2-bar loop at current BPM
VidCtrl.bloop(4, start=10)    # 4-bar loop from 10s

# Granular
VidCtrl.grain(30)             # Granular at 30s
VidCtrl.freeze(30)            # Freeze frame
VidCtrl.unfreeze()            # Resume

# Stop
VidCtrl.stop()                # Pause + stop patterns
VidCtrl.stop_patterns()       # Stop patterns only
```

---

## 1. POSITION PATTERNS

### Simple Position Cycling
```python
# Jump between 3 positions every beat
VidCtrl.pos([10, 40, 120])

# Slower cycling (every 4 beats)
VidCtrl.pos([0, 30, 60, 90], dur=4)

# Fast cuts (every half beat)
VidCtrl.pos([5, 10, 15, 20], dur=0.5)

# 16th note cuts
VidCtrl.pos([0, 2, 4, 6, 8, 10, 12, 14], dur=0.25)

# Sparse cuts
VidCtrl.pos([0, 60], dur=8)
```

---

## 2. STUTTER PATTERNS

### Basic Stutters
```python
# Classic stutter on beats 2 and 4
VidCtrl.stut([0, 0.1, 0, 0.1])

# Heavy stutter every beat
VidCtrl.stut([0.2, 0.2, 0.2, 0.2])

# Escalating stutter
VidCtrl.stut([0, 0.05, 0.1, 0.2, 0.3, 0.5])

# Glitchy micro-stutters
VidCtrl.stut([0.02, 0, 0.02, 0, 0.02, 0.02, 0, 0.05], dur=0.25)

# Syncopated
VidCtrl.stut([0.1, 0, 0, 0.2, 0, 0.1, 0, 0])
```

---

## 3. RATE/SPEED PATTERNS

### Basic Rate Changes
```python
# Classic slow-fast alternation
VidCtrl.rates([1, 0.5, 1, 2])

# Dramatic slowdown every 4 bars
VidCtrl.rates([1, 1, 1, 0.25], dur=4)

# Speed ramp
VidCtrl.rates([0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2], dur=2)

# Chaotic
VidCtrl.rates([0.25, 2, 0.5, 1.5, 0.75, 2], dur=0.5)
```

---

## 4. BEAT-SYNCED LOOPS

### Basic Beat Loops
```python
# 1-bar loop (synced to BPM)
VidCtrl.beat_loop(1)

# 2-bar loop starting at 30s
VidCtrl.beat_loop(2, start=30)

# 4-bar loop
VidCtrl.bloop(4, start=60)

# Half-bar loop (intense)
VidCtrl.beat_loop(0.5, start=10)
```

---

## 5. GRANULAR VIDEO

### Basic Granular
```python
# Granular cloud around 30s mark
VidCtrl.grain(30)

# Tighter grain (less spread)
VidCtrl.grain(30, spread=0.5)

# Wider grain (more chaos)
VidCtrl.grain(30, spread=5)

# Faster grain density
VidCtrl.grain(30, density=16)  # 16 grains per beat

# Smaller grain size (more choppy)
VidCtrl.grain(30, size=0.02)

# Limited duration (16 beats then stop)
VidCtrl.grain(30, dur=16)
```

### Granular Recipes
```python
# Glitch cloud
VidCtrl.grain(30, size=0.02, density=16, spread=0.5)

# Dreamy wash
VidCtrl.grain(30, size=0.3, density=2, spread=3)

# Aggressive chop
VidCtrl.grain(30, size=0.05, density=32, spread=0.2)

# Wandering grain (large spread)
VidCtrl.grain(30, size=0.1, density=4, spread=10)
```

### Freeze Frame
```python
# Basic freeze
VidCtrl.freeze(30)

# Intense freeze (more aggressive)
VidCtrl.freeze(30, intensity=0.9)

# Subtle freeze (gentler)
VidCtrl.freeze(30, intensity=0.2)

# Resume playback
VidCtrl.unfreeze()
```

---

## 6. COMBINED TECHNIQUES

### Stutter + Position
```python
# Jump to position then stutter there
VidCtrl.pos([10, 30, 50], dur=4)
VidCtrl.stut([0, 0.1, 0, 0.2], dur=1)
```

### Rate + Stutter
```python
# Slow motion with stutters
VidCtrl.rate(0.5)
VidCtrl.stut([0.1, 0, 0, 0])

# Speed changes with stutter accents
VidCtrl.rates([1, 0.5, 1, 2], dur=4)
VidCtrl.stut([0.2, 0, 0, 0], dur=1)
```

### Loop + Stutter
```python
# Beat loop with stutter overlay
VidCtrl.beat_loop(2, start=10)
VidCtrl.stut([0, 0.1, 0, 0.2])
```

---

## 7. PERFORMANCE PATTERNS

### Build Up
```python
# Start slow and sparse
VidCtrl.rate(0.5)
VidCtrl.pos([10, 40], dur=8)

# Increase intensity
VidCtrl.rate(0.75)
VidCtrl.pos([10, 25, 40], dur=4)

# More
VidCtrl.rate(1)
VidCtrl.pos([10, 20, 30, 40], dur=2)
VidCtrl.stut([0, 0.1, 0, 0])

# Peak
VidCtrl.rate(2)
VidCtrl.pos([10, 15, 20, 25, 30, 35, 40], dur=0.5)
VidCtrl.stut([0.1, 0.1, 0.05, 0.2], dur=0.25)
```

### Breakdown
```python
# From chaos to calm
VidCtrl.stop_patterns()
VidCtrl.rate(0.25)
VidCtrl.seek(30)

# Freeze moment
VidCtrl.freeze(30, intensity=0.3)

# Resume
VidCtrl.unfreeze()
VidCtrl.rate(1)
```

### Drop Structure
```python
# Breakdown - freeze
VidCtrl.freeze(30)

# Drop - chaos (after 16 beats)
Clock.future(16, lambda: VidCtrl.unfreeze())
Clock.future(16, lambda: VidCtrl.grain(30, density=16, spread=2))
```

---

## 8. EXPERIMENTAL TECHNIQUES

### Maximum Chaos
```python
VidCtrl.grain(30, spread=10, density=32, size=0.02)
VidCtrl.rates([0.25, 0.5, 1, 2], dur=0.25)
```

### Minimal/Ambient
```python
VidCtrl.rate(0.25)
VidCtrl.grain(30, spread=1, density=0.5, size=0.5)
```

### Polyrhythmic Patterns
```python
# 5-beat stutter pattern against 4/4
VidCtrl.stut([0.1, 0, 0, 0, 0], dur=1)

# 3-position pattern against 4/4
VidCtrl.pos([10, 30, 50], dur=4)  # Creates 3:4 phase
```

---

## 9. QUICK SHORTCUTS

```python
# Emergency stop
VidCtrl.stop()

# Reset to normal
VidCtrl.stop_patterns()
VidCtrl.clear_loop()
VidCtrl.rate(1)
VidCtrl.play()

# Aliases
VidCtrl.slow()     # rate(0.5)
VidCtrl.fast()     # rate(2)
VidCtrl.normal()   # rate(1)
VidCtrl.go(30)     # seek(30)
VidCtrl.speed(x)   # rate(x)
```

---

## PARAMETER REFERENCE

| Method | Parameters | Description |
|--------|-----------|-------------|
| `pos()` | positions, dur=1 | Cycle through seek positions |
| `stut()` | amounts, dur=1 | Cycle through stutter amounts |
| `rates()` | rates, dur=4 | Cycle through playback speeds |
| `beat_loop()` | bars=1, start=None | BPM-synced loop |
| `grain()` | position, size=0.1, density=4, spread=1.0, dur=None | Granular synthesis |
| `freeze()` | position, intensity=0.5 | Freeze frame effect |

### Grain Parameters
- **position**: Center point in seconds
- **size**: How much to stutter back (smaller = choppier)
- **density**: Grains per beat (higher = more chaotic)
- **spread**: Random range in seconds (higher = more wandering)
- **dur**: Auto-stop after N beats (None = infinite)

### Rate Values (YouTube limits)
`0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2`
