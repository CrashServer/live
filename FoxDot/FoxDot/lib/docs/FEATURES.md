# FoxDot Extended Features

## Table of Contents
- [Drum Patterns](#drum-patterns)
- [Synth Patterns](#synth-patterns)
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

# Synth Patterns

A pattern dictionary system for envelopes, melodies, arpeggios, and chord progressions.

## Functions

### `env(name)` / `e(name)`
Look up an envelope pattern by name. Returns values for `sus`, `amp`, or filter parameters.

```python
# Basic envelope usage
s1 >> pluck([0, 2, 4], sus=env("stab"))

# Short alias
s1 >> keys([0, 2, 4, 7], sus=e("hold"))

# Amplitude envelope
p1 >> pads([0, 2, 4], amp=env("pump"))

# Filter envelope
b1 >> bass([0], dur=1, lpf=linvar([200, 2000], env("swell")))
```

### `mel(name)` / `m(name)`
Look up a melodic pattern by name. Returns values for `degree`.

```python
# Basic melody usage
s1 >> pluck(mel("techno1"), dur=1/4)

# Short alias
s1 >> saw(m("acid1"), dur=1/8, lpf=400)

# With scale
s1 >> bass(mel("house1"), dur=1/2, scale=Scale.minor)

# Combine with envelope
s1 >> pluck(mel("techno2"), dur=1/4, sus=env("stab"))
```

### `arp(name)`
Look up an arpeggio pattern. Searches melody patterns with "arp" or "trance" prefix.

```python
# Basic arpeggio
s1 >> pluck(arp("up"), dur=1/4)

# Trance arp
s1 >> saw(arp("trance1"), dur=1/8, amp=0.6)

# With octave shift
s1 >> keys(arp("down") + [0, 12], dur=1/4)
```

### `chord(name)`
Look up a chord voicing. Returns a PGroup for simultaneous notes.

```python
# Basic chord
p1 >> pads(chord("maj"), dur=4)

# Seventh chord
p1 >> keys(chord("min7"), dur=2)

# Extended chord
p1 >> piano(chord("maj9"), dur=4, amp=0.7)
```

### `envs()`
Print all available envelope patterns organized by category.

```python
envs()
# Output:
# === ENVELOPE PATTERNS ===
# stab:
#   stab         [0.1]
#   stabshort    [0.05]
#   ...
```

### `mels()`
Print all available melodic patterns organized by category.

```python
mels()
# Output:
# === MELODIC PATTERNS ===
# techno_bass:
#   techno1      [0, 0, 0, -2, 0, 0, 3, 0]
#   ...
```

---

## Pattern Categories

### Envelope Patterns

#### Stab (short, punchy)
| Name | Values | Use |
|------|--------|-----|
| `stab` | `[0.1]` | Basic stab |
| `stabshort` | `[0.05]` | Very short stab |
| `stablong` | `[0.2]` | Longer stab |
| `stabvar` | `[0.1, 0.15, 0.1, 0.2]` | Varied stab |

#### Hold (sustained)
| Name | Values | Use |
|------|--------|-----|
| `hold` | `[1]` | Full sustain |
| `holdlong` | `[2]` | Extra long |
| `holdshort` | `[0.5]` | Half note |
| `holdvar` | `[1, 0.5, 1, 2]` | Varied hold |

#### Gate (rhythmic on/off)
| Name | Values | Use |
|------|--------|-----|
| `gate` | `[0.2, 0.2, 0.2, 0.2]` | Even gates |
| `gate16` | `[0.1] * 16` | 16th gates |
| `gatevar` | `[0.2, 0.1, 0.3, 0.1]` | Varied gates |
| `gatesynco` | `[0.1, 0.3, 0.1, 0.2]` | Syncopated gate |

#### Swell (rising/falling)
| Name | Values | Use |
|------|--------|-----|
| `swell` | `[0.1, 0.2, 0.4, 0.8]` | Building swell |
| `swelldown` | `[0.8, 0.4, 0.2, 0.1]` | Falling swell |
| `swellwave` | `[0.1, 0.4, 0.8, 0.4]` | Wave shape |

#### Pump (sidechain style)
| Name | Values | Use |
|------|--------|-----|
| `pump` | `[0.8, 0.2, 0.5, 0.3]` | Classic pump |
| `pumphard` | `[1, 0.1, 0.6, 0.2]` | Hard pump |
| `pumpsoft` | `[0.7, 0.4, 0.6, 0.5]` | Soft pump |

#### Accent (emphasis patterns)
| Name | Values | Use |
|------|--------|-----|
| `accent1` | `[1, 0.5, 0.5, 0.5]` | Beat 1 accent |
| `accent24` | `[0.5, 1, 0.5, 1]` | Backbeat |
| `accentsynco` | `[0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5]` | Syncopated |

#### Filter Envelopes
| Name | Values | Use |
|------|--------|-----|
| `lpfopen` | `[200, 500, 1000, 2000]` | Opening filter |
| `lpfclose` | `[2000, 1000, 500, 200]` | Closing filter |
| `lpfpulse` | `[2000, 200, 2000, 200]` | Pulsing filter |
| `lpfsweep` | `[200, 400, 800, 1600, 3200, 1600, 800, 400]` | Sweep up/down |

---

### Melodic Patterns

#### Techno Bass
| Name | Pattern | Description |
|------|---------|-------------|
| `techno1` | `[0, 0, 0, -2, 0, 0, 3, 0]` | Classic techno |
| `techno2` | `[0, 0, -5, 0, 0, 0, -5, -7]` | Dark techno |
| `techno3` | `[0, 0, 0, 0, -2, -2, 3, 3]` | Driving |
| `technominimal` | `[0, 0, 0, 0]` | Minimal root |

#### Acid
| Name | Pattern | Description |
|------|---------|-------------|
| `acid1` | `[0, 0, 12, 0, 3, 0, 12, 5]` | Classic 303 |
| `acid2` | `[0, 3, 7, 12, 7, 3, 0, -5]` | Rising acid |
| `acid3` | `[0, 0, 0, 7, 0, 0, 10, 12]` | Sparse acid |
| `acidwobble` | `[0, 0, 1, 0, 0, -1, 0, 2]` | Wobble acid |

#### House
| Name | Pattern | Description |
|------|---------|-------------|
| `house1` | `[0, 0, 7, 0]` | Classic house |
| `house2` | `[0, 5, 7, 5]` | Disco house |
| `housedisco` | `[0, 4, 7, 4, 0, 4, 7, 9]` | Full disco |
| `housechord` | `[0, 0, 0, 0, 7, 7, 5, 5]` | Chord bass |

#### Drum & Bass
| Name | Pattern | Description |
|------|---------|-------------|
| `dnb1` | `[0, 0, 0, 12, 0, 10, 0, 7]` | Jump up |
| `dnb2` | `[0, 0, 12, 0, 0, 0, 10, 0]` | Neurofunk |
| `dnbreese` | `[0, 0, 0, 0, -5, -5, -5, -5]` | Reese pattern |
| `dnbroller` | `[0] * 8` | Rolling root |

#### Arpeggios
| Name | Pattern | Description |
|------|---------|-------------|
| `arpup` | `[0, 2, 4, 7]` | Up arpeggio |
| `arpdown` | `[7, 4, 2, 0]` | Down arpeggio |
| `arpupdown` | `[0, 2, 4, 7, 4, 2]` | Up then down |
| `arppendulum` | `[0, 4, 2, 7, 4, 9, 7, 12]` | Pendulum |

#### Trance Arps
| Name | Pattern | Description |
|------|---------|-------------|
| `trance1` | `[0, 0, 4, 4, 7, 7, 4, 4]` | Classic trance |
| `trance2` | `[0, 4, 7, 12, 7, 4, 0, -5]` | Epic trance |
| `trancegate` | `[0, 0, 0, 0, 7, 7, 7, 7]` | Gated arp |

#### Chord Progressions
| Name | Pattern | Description |
|------|---------|-------------|
| `prog1` | `[0, 0, 5, 5, 7, 7, 3, 3]` | I-IV-V-ii |
| `prog2` | `[0, 0, 3, 3, 5, 5, 7, 7]` | Rising |
| `progminor` | `[0, 0, -2, -2, -4, -4, -5, -5]` | Minor descent |

#### Lead Lines
| Name | Pattern | Description |
|------|---------|-------------|
| `lead1` | `[7, 5, 4, 2, 0]` | Descending |
| `lead2` | `[0, 2, 4, 5, 7, 9, 11, 12]` | Scale run |
| `leadcall` | `[7, 9, 7, 5]` | Call phrase |
| `leadanswer` | `[4, 2, 0, -2]` | Answer phrase |

---

### Chord Dictionary

#### Triads
| Name | Notes | Description |
|------|-------|-------------|
| `maj` | `(0, 2, 4)` | Major triad |
| `min` | `(0, 2, 3)` | Minor triad (scale) |
| `dim` | `(0, 2, 3)` | Diminished |
| `aug` | `(0, 2, 5)` | Augmented |
| `sus2` | `(0, 1, 4)` | Suspended 2nd |
| `sus4` | `(0, 3, 4)` | Suspended 4th |

#### Seventh Chords
| Name | Notes | Description |
|------|-------|-------------|
| `maj7` | `(0, 2, 4, 6)` | Major 7th |
| `min7` | `(0, 2, 3, 6)` | Minor 7th |
| `dom7` | `(0, 2, 4, 5)` | Dominant 7th |
| `dim7` | `(0, 2, 3, 5)` | Diminished 7th |

#### Extended
| Name | Notes | Description |
|------|-------|-------------|
| `maj9` | `(0, 2, 4, 6, 8)` | Major 9th |
| `min9` | `(0, 2, 3, 6, 8)` | Minor 9th |
| `add9` | `(0, 2, 4, 8)` | Add 9 |
| `min11` | `(0, 2, 3, 6, 8, 10)` | Minor 11th |

#### Special
| Name | Notes | Description |
|------|-------|-------------|
| `power` | `(0, 4)` | Power chord (5th) |
| `octave` | `(0, 0)` | Octave doubling |
| `sixth` | `(0, 2, 4, 5)` | Major 6th |

---

## Complete Examples

### Basic Synth with Envelope
```python
Clock.bpm = 128

# Stab synth
s1 >> pluck(mel("techno1"), dur=1/4, sus=env("stab"), amp=0.8)

# Pad with long envelope
p1 >> pads([0, 2, 4], dur=4, sus=env("hold"), room=0.5)
```

### Acid Line
```python
Clock.bpm = 130

# Classic acid
b1 >> bass(mel("acid1"), dur=1/8,
    lpf=linvar([200, 2000], 8),
    res=0.8,
    sus=env("gate"))
```

### Trance Arp
```python
Clock.bpm = 140

# Trance arpeggio
s1 >> saw(arp("trance1"), dur=1/8,
    oct=5,
    lpf=1500,
    sus=env("gate"))

# Pad chords underneath
p1 >> pads(chord("maj7"), dur=4, oct=4, amp=0.5)
```

### Layered Production
```python
Clock.bpm = 126

# Drums
d1 >> play(pat("h1"), dur=1/4)

# Bass follows drum rhythm
b1 >> bass(mel("house1"), dur=ppat("hk1"), amp=0.9)

# Chord stabs
s1 >> keys(chord("min7"), dur=var([1, 0.5], [3, 1]),
    sus=env("stabvar"),
    amp=env("accent24"))

# Lead melody
l1 >> pluck(mel("lead1"), dur=1/2, oct=6, amp=0.6)
```

### Envelope Automation
```python
Clock.bpm = 128

# Filter envelope that opens over 8 bars
s1 >> saw([0, 0, 3, 0], dur=1/4,
    lpf=var(env("lpfopen"), 8),
    res=0.5)

# Amplitude pump effect
p1 >> pads([0, 2, 4], dur=1,
    amp=env("pump"))
```

### Chord Progression
```python
Clock.bpm = 120

# 4-bar chord progression
chords = var([
    chord("maj"),
    chord("min"),
    chord("sus4"),
    chord("maj7")
], 4)

p1 >> keys(chords, dur=4, sus=3, oct=4)

# Arp over the top
s1 >> pluck(arp("updown"), dur=1/4, oct=5, amp=0.5)
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
