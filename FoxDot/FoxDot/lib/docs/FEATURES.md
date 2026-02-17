# FoxDot Extended Features

## Table of Contents
- [Drum Patterns](#drum-patterns)
- [Video Control](#video-control)

---

# Drum Patterns

A pattern dictionary system for creating complex drum grooves with short codes.

## Functions

### `pat(name)` / `p(name)`
Look up a pattern by its short code.

```python
# Basic usage
d1 >> play(pat("t1"), dur=1/4)

# Short alias
d1 >> play(p("h1"), dur=1/4)

# With effects
d1 >> play(pat("b1"), dur=1/4, hpf=500, room=0.3)

# With sample bank
d1 >> play(pat("t1"), dur=1/4, sample=2)
```

### `pbuild(items, mode="concat")`
Build longer patterns from multiple patterns or a pre-defined group.

```python
# Using a group name
d1 >> play(pbuild("tverse1"), dur=1/4)        # 4-bar techno verse

# Custom pattern list (concatenated)
d1 >> play(pbuild(["t1", "t2", "t1", "t3"]), dur=1/4)

# Layer mode - merge patterns (kick + hat + clap)
d1 >> play(pbuild(["tk1", "th1", "tc1"], mode="layer"), dur=1/4)

# Using kit groups with layer mode
d1 >> play(pbuild("tkit1", mode="layer"), dur=1/4)

# Build with fills
d1 >> play(pbuild(["t1", "t1", "t1", "fo1"]), dur=1/4)

# Tension and release
d1 >> play(pbuild(["fb", "fb", "fo1", "t3"]), dur=1/4)  # silence, silence, fill, drop
```

### `ppat(name, hits_only=True, chars=None, base=0.25)`
Convert a drum pattern to duration values for melodic players.

```python
# Bass follows kick pattern rhythm
b1 >> bass([0, 0, 3], dur=ppat("tk1"))

# Synth follows snare hits
s1 >> pluck([0, 2, 4], dur=ppat("tc1"))

# Custom characters to follow
m1 >> keys([0, 2, 4, 7], dur=ppat("t1", chars="xoc"))

# Include all sounds (not just hits)
p1 >> pulse([0, 3, 5], dur=ppat("th1", hits_only=False))
```

### `pamp(name, hits_only=True, chars=None, amp_on=1, amp_off=0)`
Convert a drum pattern to amplitude values.

```python
# Sidechain-style pumping
b1 >> bass([0], dur=1/4, amp=pamp("tk1", amp_on=0.2, amp_off=1))

# Accent pattern
d1 >> play("x", dur=1/4, amp=pamp("t1"))

# Reverse: quiet on hits, loud on rests
p1 >> pluck([0, 2, 4], dur=1/4, amp=pamp("tk1", amp_on=0, amp_off=0.8))
```

### `phits(name, chars=None)`
Get step positions where hits occur (0-indexed).

```python
# Get kick positions
positions = phits("tk1")  # Returns [0, 4, 8, 12] for 4/4

# Use with stutter or other effects
d1 >> play("x", dur=1/4, stut=4, stutrate=phits("th1"))
```

### `patterns()`
Print all available patterns organized by genre.

```python
patterns()
# Output:
# === PATTERNS ===
# Techno:
#   t1     x-:-c-:-x-:-c-:-...
#   tk1    x---x---x---x---
#   ...
```

### `groups()`
Print all available groups.

```python
groups()
# Output:
# === GROUPS ===
#   tverse1      ['t1', 't1', 't2', 't1']
#   tchorus1     ['t3', 't3', 't6', 't3']
#   ...
```

---

## Pattern Naming Convention

```
[genre][layer][number]

genre:  t=techno, h=house, b=breaks, d=dnb, hp=hiphop,
        e=ebm, g=gabber, l=latin, x=experimental

layer:  k=kick, h=hat, c=clap, s=snare, r=ride
        (no letter = combined full pattern)

number: variation (1, 2, 3...)
```

**Examples:**
- `t1` = techno combined pattern 1
- `tk1` = techno kick pattern 1
- `th2` = techno hat pattern 2
- `hp1` = hip-hop combined pattern 1
- `b1` = breaks combined pattern 1 (amen)

---

## Available Patterns

### Techno (128-135 BPM, dur=1/4)
| Code | Description |
|------|-------------|
| `t1`-`t12` | Combined patterns |
| `tk1`-`tk10` | Kick patterns |
| `th1`-`th12` | Hat patterns |
| `tc1`-`tc8` | Clap patterns |

### House (120-128 BPM, dur=1/4)
| Code | Description |
|------|-------------|
| `h1`-`h10` | Combined patterns |
| `hk1`-`hk4` | Kick patterns |
| `hh1`-`hh8` | Hat patterns |
| `hc1`-`hc4` | Clap patterns |

### Breaks (130-145 BPM, dur=1/4)
| Code | Description |
|------|-------------|
| `b1`-`b10` | Combined (amen, think, funky drummer) |
| `bk1`-`bk4` | Kick patterns |
| `bs1`-`bs4` | Snare patterns |
| `br1`-`br2` | Ride patterns |

### Drum & Bass (170-180 BPM, dur=1/4)
| Code | Description |
|------|-------------|
| `d1`-`d8` | Combined (twostep, roller, jungle) |
| `dk1`-`dk4` | Kick patterns |
| `ds1`-`ds4` | Snare patterns |
| `dh1`-`dh4` | Hat patterns |

### Hip-Hop (85-100 BPM, dur=1/4)
| Code | Description |
|------|-------------|
| `hp1`-`hp8` | Combined (boom bap, trap) |
| `hpk1`-`hpk4` | Kick patterns |
| `hps1`-`hps4` | Snare patterns |
| `hph1`-`hph4` | Hat patterns |

### EBM / Industrial (120-140 BPM, dur=1/4)
| Code | Description |
|------|-------------|
| `e1`-`e6` | Combined |
| `ek1`-`ek4` | Kick patterns |
| `ec1`-`ec4` | Clap patterns |

### Gabber / Hardcore (160-200 BPM, dur=1/8)
| Code | Description |
|------|-------------|
| `g1`-`g6` | Combined |
| `gk1`-`gk4` | Kick patterns |

### Latin / World
| Code | Description |
|------|-------------|
| `l1`-`l6` | Combined (bossa, samba, afrobeat) |
| `lc1`-`lc2` | Clave patterns |

### Experimental
| Code | Description |
|------|-------------|
| `x1`-`x6` | Polyrhythms, sparse, glitch |

### Fills (16 steps)
| Code | Description |
|------|-------------|
| `fo1`-`fo4` | Snare builds |
| `fx1`-`fx2` | Kick builds |
| `ft1`-`ft2` | Tom rolls |
| `fc1` | Crash |
| `fb` | Break/silence |
| `fr1`-`fr2` | Snare rolls |

### Percussion Layers
| Code | Description |
|------|-------------|
| `ps1`-`ps2` | Shaker |
| `pt1`-`pt2` | Tambourine |
| `pe1`-`pe2` | Cowbell |
| `pr1`-`pr2` | Rimshot |

---

## Available Groups

### Kits (use with `mode="layer"`)
| Group | Contents |
|-------|----------|
| `tkit1`-`tkit5` | Techno kits |
| `hkit1`-`hkit4` | House kits |
| `bkit1`-`bkit3` | Breaks kits |
| `dkit1`-`dkit3` | DnB kits |
| `hpkit1`-`hpkit3` | Hip-hop kits |

### Phrases (4-bar sequences)
| Group | Contents |
|-------|----------|
| `tverse1`-`tverse2` | Techno verses |
| `tchorus1`-`tchorus2` | Techno choruses |
| `hverse1`-`hverse2` | House verses |
| `hchorus1`-`hchorus2` | House choruses |
| `bverse1`-`bverse2` | Breaks verses |
| `dverse1`-`dverse2` | DnB verses |

### Builds (intensity progressions)
| Group | Contents |
|-------|----------|
| `tbuild1`-`tbuild2` | Techno builds |
| `hbuild1`-`hbuild2` | House builds |
| `build4`, `build8` | Generic builds |

### Drops
| Group | Contents |
|-------|----------|
| `tdrop1`-`tdrop2` | Techno drops |
| `hdrop1` | House drop |
| `bdrop1` | Breaks drop |
| `drop` | Generic drop |

### Fills
| Group | Contents |
|-------|----------|
| `tfill1`-`tfill2` | Techno with fills |
| `hfill1` | House with fill |
| `bfill1` | Breaks with fill |

### Intensity
| Group | Contents |
|-------|----------|
| `tintensity` | Techno: sparse → full |
| `hintensity` | House: minimal → disco |
| `dintensity` | DnB: minimal → jungle |

---

## Complete Examples

### Basic Loop
```python
# Simple techno loop
Clock.bpm = 130
d1 >> play(pat("t1"), dur=1/4)
```

### Layered Kit
```python
# Separate control over each element
Clock.bpm = 128
d1 >> play(pat("tk1"), dur=1/4, amp=1.2)      # Kick
d2 >> play(pat("th2"), dur=1/4, amp=0.6)      # Hats
d3 >> play(pat("tc1"), dur=1/4, amp=0.8)      # Clap
```

### Song Structure
```python
# Full song structure with var()
Clock.bpm = 126

# Switch between verse and chorus every 32 beats
d1 >> play(var([
    pbuild("tverse1"),
    pbuild("tchorus1")
], 32), dur=1/4)

# Bass follows kick
b1 >> bass([0, 0, 3, 0], dur=ppat("tk1"), amp=0.8)
```

### Build and Drop
```python
# 16-bar build into drop
Clock.bpm = 130

# Build section (bars 1-16)
d1 >> play(pbuild("tbuild1"), dur=1/4)

# After build finishes, trigger drop
@futureBar(16)
def drop():
    d1 >> play(pbuild("tdrop1"), dur=1/4)
```

### Genre Mixing
```python
# Combine elements from different genres
Clock.bpm = 125
d1 >> play(pat("tk4"), dur=1/4)       # Driving techno kick
d2 >> play(pat("hh2"), dur=1/4)       # Disco house hats
d3 >> play(pat("tc1"), dur=1/4)       # Standard clap
```

### Breaks with Variation
```python
# Amen break with variations
Clock.bpm = 140
d1 >> play(var([
    pat("b1"),   # Standard amen
    pat("b2"),   # Variation
    pat("b1"),
    pat("b7"),   # With crash
], 16), dur=1/4)
```

### Hip-Hop with Swing
```python
# Boom bap groove
Clock.bpm = 92
d1 >> play(pat("hp1"), dur=1/4,
    amp=var([0.9, 0.7], [0.5, 0.5]),  # Swing feel
    sample=1)
```

---

# Video Control

Control YouTube videos via WebSocket for live visual performances.

## Setup

```python
# VidCtrl is automatically available after import
# It auto-connects to WebTroop server on first use
```

---

## Transport Functions

### `VidCtrl.load(url_or_id)`
Load a YouTube video by URL or video ID. Opens video window if not open.

```python
# Load by URL
VidCtrl.load("https://youtube.com/watch?v=dQw4w9WgXcQ")

# Load by video ID
VidCtrl.load("dQw4w9WgXcQ")

# Load a different video
VidCtrl.load("https://youtu.be/xyz123abc")
```

### `VidCtrl.play()` / `VidCtrl.pause()`
Control playback.

```python
VidCtrl.play()
VidCtrl.pause()

# Schedule play/pause
@nextBar
def toggle():
    VidCtrl.play()
```

### `VidCtrl.stop()`
Pause video and stop all patterns.

```python
VidCtrl.stop()
```

---

## Seeking Functions

### `VidCtrl.seek(time_seconds)`
Seek to a specific position.

```python
VidCtrl.seek(30)       # Jump to 30 seconds
VidCtrl.seek(120.5)    # Jump to 2:00.5

# Callable syntax
VidCtrl(30)            # Same as seek(30)
```

### `VidCtrl.go(time_seconds)`
Alias for seek().

```python
VidCtrl.go(60)         # Jump to 1 minute
```

### `VidCtrl.jump(time_seconds)`
Jump to position and set as base for scrub/stutter.

```python
VidCtrl.jump(45)       # Jump to 45s, set as base
VidCtrl.scrub(0.5)     # Now scrubs relative to 45s
```

### `VidCtrl.scrub(offset)`
Scrub relative to the base position (set by jump).

```python
VidCtrl.jump(30)              # Set base at 30s
VidCtrl.scrub(2)              # Seek to 32s
VidCtrl.scrub(-1)             # Seek to 29s

# Use with linvar for oscillation
VidCtrl.scrub(linvar([0, 2], 8))
```

---

## Effect Functions

### `VidCtrl.stutter(amount=0.5)`
Jump back by specified amount (glitch effect).

```python
VidCtrl.stutter(0.2)   # Jump back 0.2 seconds
VidCtrl.stutter(1)     # Jump back 1 second

# Creates stuttering/glitch effect when called repeatedly
```

### `VidCtrl.rate(playback_rate=1.0)`
Set playback speed. YouTube supports: 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2

```python
VidCtrl.rate(0.5)      # Half speed
VidCtrl.rate(2)        # Double speed
VidCtrl.rate(0.25)     # Quarter speed (slowest)

# Aliases
VidCtrl.slow()         # 0.5x
VidCtrl.fast()         # 2x
VidCtrl.normal()       # 1x
VidCtrl.speed(1.5)     # Same as rate()
```

### `VidCtrl.loop(start, end)`
Set a loop region.

```python
VidCtrl.loop(10, 20)   # Loop between 10s and 20s
VidCtrl.loop(0, 5)     # Loop first 5 seconds
```

### `VidCtrl.clear_loop()`
Clear the loop region.

```python
VidCtrl.clear_loop()
```

### `VidCtrl.beat_loop(bars=1, start=None)` / `VidCtrl.bloop()`
Create a loop matching the duration of N bars at current BPM.

```python
Clock.bpm = 120

VidCtrl.beat_loop(2)           # 2-bar loop from current position
VidCtrl.beat_loop(4, start=10) # 4-bar loop starting at 10s
VidCtrl.bloop(1)               # Alias - 1-bar loop
```

---

## Pattern-Based Methods

### `VidCtrl.pos(positions, dur=1)`
Cycle through video positions on each beat.

```python
# Jump between positions every beat
VidCtrl.pos([10, 40, 120])

# Slower cycling (every 4 beats)
VidCtrl.pos([0, 30, 60], dur=4)

# Create rhythmic video cuts
VidCtrl.pos([5, 5.5, 6, 6.5])  # Rapid cuts
```

### `VidCtrl.stut(amounts, dur=1)`
Cycle through stutter amounts on each beat.

```python
# Stutter pattern
VidCtrl.stut([0, 0.1, 0, 0.2])

# Faster stuttering
VidCtrl.stut([0.1, 0.2, 0.3], dur=0.5)

# Only stutter every 4th beat
VidCtrl.stut([0, 0, 0, 0.5])
```

### `VidCtrl.rates(rates, dur=4)`
Cycle through playback rates.

```python
# Speed changes every 4 beats
VidCtrl.rates([1, 0.5, 1, 2])

# Faster changes
VidCtrl.rates([1, 0.5, 2, 0.25], dur=2)
```

### `VidCtrl.stop_patterns()`
Stop all running patterns (pos, stut, rates, grain).

```python
VidCtrl.stop_patterns()
```

---

## Granular Functions

### `VidCtrl.grain(position, size=0.1, density=4, spread=1.0, dur=None)`
Granular video - rapid tiny loops around a position with random offsets.

```python
# Basic granular at 30s
VidCtrl.grain(30)

# Smaller, faster grains
VidCtrl.grain(30, size=0.05, density=8)

# Wider spread, limited duration
VidCtrl.grain(30, spread=3, dur=16)  # 3s spread, stop after 16 beats

# Very tight grains (almost freeze)
VidCtrl.grain(45, size=0.02, density=16, spread=0.1)
```

**Parameters:**
- `position`: Center position in seconds
- `size`: How far back to stutter (default 0.1s)
- `density`: Grains per beat (default 4)
- `spread`: Random spread in seconds around position (default 1.0)
- `dur`: Duration in beats before stopping (None = infinite)

### `VidCtrl.freeze(position, intensity=0.5)`
Freeze frame effect - rapid micro-stutters at a position.

```python
VidCtrl.freeze(30)                # Freeze at 30s
VidCtrl.freeze(30, intensity=0.8) # More aggressive freeze
VidCtrl.freeze(45, intensity=0.2) # Subtle freeze
```

### `VidCtrl.unfreeze()`
Stop freeze/grain effect and resume normal playback.

```python
VidCtrl.unfreeze()
```

---

## Complete Examples

### Basic Video Control
```python
# Load and play
VidCtrl.load("https://youtube.com/watch?v=...")
VidCtrl.play()

# Jump around
VidCtrl.seek(60)
VidCtrl.rate(0.5)
```

### Synced to Music
```python
Clock.bpm = 128

# Video cuts on beat
VidCtrl.pos([10, 20, 30, 40])

# Match drum pattern
d1 >> play(pat("t1"), dur=1/4)
```

### Stutter Glitch Performance
```python
Clock.bpm = 140

# Set up video
VidCtrl.load("https://youtube.com/watch?v=...")
VidCtrl.seek(30)
VidCtrl.play()

# Glitch pattern
VidCtrl.stut([0, 0, 0.1, 0, 0, 0.2, 0, 0.5], dur=0.5)

# Match with breaks
d1 >> play(pat("b1"), dur=1/4)
```

### Granular Texture
```python
# Atmospheric granular video
VidCtrl.grain(45, size=0.2, density=2, spread=5)

# With ambient pad
p1 >> pads([0, 2, 4], dur=4, amp=0.5, room=0.8)
```

### Speed Manipulation
```python
Clock.bpm = 120

# Speed follows bar structure
@futureBar(0)
def verse():
    VidCtrl.rate(1)

@futureBar(16)
def buildup():
    VidCtrl.rates([1, 1.25, 1.5, 1.75], dur=4)

@futureBar(32)
def drop():
    VidCtrl.rate(0.5)
    VidCtrl.stut([0, 0.2, 0, 0.1])
```

### Full Performance Example
```python
Clock.bpm = 126

# Load video
VidCtrl.load("https://youtube.com/watch?v=...")

# Drums
d1 >> play(var([
    pbuild("tverse1"),
    pbuild("tchorus1")
], 32), dur=1/4)

# Bass follows kick
b1 >> bass([0, 0, 3], dur=ppat("tk1"), amp=0.8)

# Video synced to sections
@nextBar
def intro():
    VidCtrl.seek(0)
    VidCtrl.rate(1)
    VidCtrl.pos([0, 10, 20, 30], dur=4)

@futureBar(32)
def verse():
    VidCtrl.pos([40, 50, 60, 70], dur=2)
    VidCtrl.stut([0, 0, 0.1, 0])

@futureBar(64)
def chorus():
    VidCtrl.pos([80, 82, 84, 86], dur=1)  # Faster cuts
    VidCtrl.stut([0, 0.1, 0.2, 0.1])

@futureBar(96)
def breakdown():
    VidCtrl.grain(100, spread=3, dur=32)
    VidCtrl.rate(0.5)
```

---

## Sample Character Reference

For drum patterns, these characters map to samples:

**Kicks:**
- `x` = Kick electro
- `X` = Kick heavy electro
- `k` = Kick organic
- `v` = Kick bass
- `g` = Gabber kick

**Snares:**
- `o` = Snare electro
- `O` = Snare electro heavy
- `u` = Snare acoustic
- `U` = Snare break

**Claps:**
- `c` = Clap
- `C` = Clap electro

**Hi-hats:**
- `-` = Hihat closed
- `=` = Hihat open wide
- `:` = Hihat open short

**Cymbals:**
- `~` = Ride
- `#` = Crash

**Toms:**
- `t` = Tom low
- `T` = Tom high
- `m` = Tom mid low
- `M` = Tom mid high

**Percussion:**
- `r` = Rimshot acoustic
- `R` = Rimshot electro
- `s` = Shaker
- `S` = Tambourine
- `e` = Cowbell
- `^` = Donk
