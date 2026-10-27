# FoxDot Drum Patterns

A pattern dictionary system for creating complex drum grooves with short codes.

## Quick Start

```python
# Use pat() to look up patterns
d1 >> play(pat("t1"), dur=1/4)          # Techno combined
d1 >> play(pat("h1"), dur=1/4)          # House combined
d1 >> play(pat("b1"), dur=1/4)          # Breaks (amen)

# Layer separate elements
d1 >> play(pat("tk1"), dur=1/4)         # Techno kick only
d2 >> play(pat("th1"), dur=1/4)         # Techno hat only
d3 >> play(pat("tc1"), dur=1/4)         # Techno clap only

# List all patterns
patterns()
```

---

## Naming Convention

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

## Pattern Reference

### TECHNO (128-135 BPM, dur=1/4)

| Code | Description | Pattern |
|------|-------------|---------|
| `tk1` | 4/4 kick | `x---x---x---x---` |
| `tk2` | Extra 16th | `x---x---x---x-x-` |
| `tk3` | Syncopated | `x---x---x-x-x---` |
| `tk4` | Driving 8ths | `x-x-x-x-x-x-x-x-` |
| `th1` | Short hats offbeat | `--:-:-:---:-:-:-` |
| `th2` | 8th short hats | `:-:-:-:-:-:-:-:-` |
| `th3` | Open pattern | `=--=--=-=--=--=-` |
| `th4` | 16th short | `:::::::::::::::::` |
| `tc1` | Clap 2&4 | `----c-------c---` |
| `t1` | Classic | `x-:-c-:-x-:-c-:-...` |
| `t2` | Open end | `x-:-c-:-...x-:=c-:-` |
| `t3` | Driving 16th | `x:::c:::x:::c:::...` |
| `t4` | Minimal | `x---c---x-x-c---...` |
| `t5` | No snare | `x-:-:-:-...x-:-:-:=` |
| `t6` | Acid open hats | `x=-=c=-=x=-=c=-=...` |

### HOUSE (120-128 BPM, dur=1/4)

| Code | Description | Pattern |
|------|-------------|---------|
| `hk1` | 4/4 kick | `x---x---x---x---` |
| `hh1` | Classic house | `--=---=---=---=-` |
| `hh2` | Disco | `=--==--==--==--=` |
| `hc1` | Clap 2&4 | `----c-------c---` |
| `h1` | Classic | `x-:=c-:=x-:=c-:=...` |
| `h2` | Deep | `x---c---x---c---...` |
| `h3` | Disco crash | `x=:=c=:=...x=:=c=:#` |
| `h4` | Jackin | `x:::c:::x:::c:::...` |
| `h5` | Garage | `x-:=c-:-x-:=c=:-...` |
| `h6` | Tribal | `x-e-c-:-x-:-c-e-...` |

### BREAKS (130-145 BPM, dur=1/4)

| Code | Description | Pattern |
|------|-------------|---------|
| `bk1` | Amen kick | `x-x-------xx----` |
| `bs1` | Amen snare | `----u--u-u--u--u` |
| `br1` | Amen ride | `-~-~-~-~-~-~-~-~` |
| `b1` | Amen full | `x~x~u~~u~uxxu-~u...` |
| `b2` | Amen variation | `x~x~u~~u~~xu-~u...` |
| `b3` | Think break | `x-:-u-:-x-x-u---...` |
| `b4` | Funky drummer | `x-:-u-:-x-:-u---...` |
| `b5` | Soul | `x---u---x-x-u---...` |
| `b6` | Apache | `x-u:--u-x-:-u-u-...` |

### DRUM & BASS (170-180 BPM, dur=1/4)

| Code | Description | Pattern |
|------|-------------|---------|
| `dk1` | Twostep kick | `x-------x-------` |
| `dk2` | Roller kick | `x-----x-x-------` |
| `ds1` | Twostep snare | `----o-------o---` |
| `dh1` | 8th hats | `:-:-:-:-:-:-:-:-` |
| `d1` | Twostep | `x---:-:-o---:-:-...` |
| `d2` | Roller | `x-:-:-o-x-:-:-:-...` |
| `d3` | Jungle | `x~x~U~~u~Uxxu-~U...` |
| `d4` | Liquid | `x---:-:-o---:-:-...` |
| `d5` | Neuro | `x-:-:-:-O---:-:-...` |

### HIP-HOP (85-100 BPM, dur=1/4)

| Code | Description | Pattern |
|------|-------------|---------|
| `hpk1` | Boom bap kick | `x-------x-x-----` |
| `hps1` | Acoustic snare | `----u-------u---` |
| `hph1` | 8th hats | `-:-:-:-:-:-:-:-:` |
| `hph2` | Trap rolls | `-(--)--(----)-(-` |
| `hp1` | Boom bap | `x--:u-:-x---u--:...` |
| `hp2` | Golden era | `x---u---x-x-u---...` |
| `hp3` | Dusty | `k-:-U-:-k---U-:-...` |
| `hp4` | West coast | `x---o---x---o---...` |
| `hp5` | Trap | `x-------O-------...` |

### EBM / INDUSTRIAL (120-140 BPM, dur=1/4)

| Code | Description | Pattern |
|------|-------------|---------|
| `ek1` | EBM kick | `x---x---x-x-x---` |
| `ec1` | Electro clap | `----C-------C---` |
| `e1` | EBM classic | `x-:-:-C=x-:-x-C=...` |
| `e2` | Hard EBM | `X::::-C:X:X::-C:...` |
| `e3` | Industrial | `X---C---X-X-C---...` |

### GABBER / HARDCORE (160-200 BPM, dur=1/8)

| Code | Description | Pattern |
|------|-------------|---------|
| `gk1` | Gabber 8th | `g-g-g-g-g-g-g-g-` |
| `gk2` | Gabber 16th | `gggggggggggggggg` |
| `g1` | Gabber 8th | `g-g-C-g-g-g-C-g-...` |
| `g2` | Gabber 16th | `g:g:C:g:g:g:C:g:...` |
| `g3` | Hardcore roll | `ggggggggCggggggg...` |

### LATIN / WORLD

| Code | Description | Pattern |
|------|-------------|---------|
| `lc1` | Son clave 3-2 | `x--x---x--x-x---` |
| `lc2` | Son clave 2-3 | `--x-x---x--x--x-` |
| `l1` | Bossa nova | `x-x---x-x-x---x-...` |
| `l2` | Samba | `x-x-o-x-x-x-o-x-...` |
| `l3` | Afrobeat | `x--x-ox--x-xo-x-...` |

### EXPERIMENTAL

| Code | Description | Pattern |
|------|-------------|---------|
| `x1` | 3 over 4 | `x--x--x--x--x--x...` |
| `x2` | Ultra sparse | `x---------------o---...` |
| `x3` | Glitch random | `[xov]-[:-]u-[x-]...` |

### FILLS (16 steps)

| Code | Description | Pattern |
|------|-------------|---------|
| `fo` | Snare build | `o-o-ooooOOOOOOOO` |
| `fx` | Kick build | `x-x-xxxxXXXXXXXX` |
| `ft` | Tom roll | `t-m-M-T-tmMTtmMT` |
| `fc` | Crash | `#---------------` |
| `fb` | Break/silence | `                ` |
| `fr` | Snare roll | `oooooooooooooooo` |

### PERCUSSION LAYERS

| Code | Description | Pattern |
|------|-------------|---------|
| `ps1` | Shaker 8th | `s-s-s-s-s-s-s-s-` |
| `ps2` | Shaker 16th | `ssssssssssssssss` |
| `pt1` | Tambourine | `S---S---S---S---` |
| `pe1` | Cowbell sparse | `----e-----e-----` |
| `pe2` | Cowbell offbeat | `--e---e---e---e-` |

---

## Sample Character Reference

Your samples (Bank 0):

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

---

## Usage Examples

### Basic Usage

```python
# Single combined pattern
d1 >> play(pat("t1"), dur=1/4)

# Change pattern
d1 >> play(pat("t3"), dur=1/4)

# Short alias
d1 >> play(p("h1"), dur=1/4)
```

### Layered Approach

```python
# Separate control over each element
d1 >> play(pat("tk1"), dur=1/4)                    # Kick
d2 >> play(pat("th1"), dur=1/4, sample=2)          # Hats
d3 >> play(pat("tc1"), dur=1/4)                    # Clap

# Mix and match genres
d1 >> play(pat("tk1"), dur=1/4)                    # Techno kick
d2 >> play(pat("hh2"), dur=1/4)                    # House hat (disco)
```

### With Sample Banks

```python
# Switch banks
d1 >> play(pat("b1"), dur=1/4, sample=var([0,1,2], 8))

# Specific sample
d1 >> play(pat("t1"), dur=1/4, sample=3)
```

### Pattern Combination

```python
# Concatenate patterns (plays one after other)
d1 >> play(pat("t1") + pat("t2"), dur=1/4)

# Use var() to switch
d1 >> play(var([pat("t1"), pat("t3")], 16), dur=1/4)
```

### With Effects

```python
d1 >> play(pat("b1"), dur=1/4,
    hpf=500,
    room=0.3,
    amp=linvar([0.8, 1], 4))
```

### Fill Insertion

```python
# Manual fill trigger
d1 >> play(pat("t1"), dur=1/4)
# Then run:
d1 >> play(pat("fo"), dur=1/4)  # Snare fill
# Then back:
d1 >> play(pat("t1"), dur=1/4)
```

---

## Implementation Details

### Files

- **Module:** `FoxDot/lib/DrumPatterns.py`
- **Patterns stored in:** `PATTERNS` dictionary
- **Functions:** `pat()`, `p()`, `patterns()`

### How It Works

1. `pat("t1")` looks up key `"t1"` in `PATTERNS` dict
2. Returns the pattern string
3. If not found, returns input unchanged (fallback)

```python
def pat(name):
    return PATTERNS.get(name, name)
```

### Adding Custom Patterns

Edit `DrumPatterns.py` and add to `PATTERNS`:

```python
PATTERNS = {
    # ... existing patterns ...

    # Your custom patterns
    "my1": "x---o-x-x---o-x-",
    "my2": "x-:-c-:-x-x-c---",
}
```

Or at runtime:

```python
PATTERNS["custom1"] = "x---o---x-x-o---"
d1 >> play(pat("custom1"), dur=1/4)
```

---

## Pattern Design Tips

### Grid Reference

```
Step:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
Beat:  1  e  +  a  2  e  +  a  3  e  +  a  4  e  +  a
```

- **Beats 1,2,3,4** = steps 1, 5, 9, 13
- **Offbeats ("and")** = steps 3, 7, 11, 15
- **e and a** = steps 2,4,6,8,10,12,14,16

### Common Positions

| Element | Steps | Beats |
|---------|-------|-------|
| 4/4 kick | 1,5,9,13 | 1,2,3,4 |
| Backbeat snare | 5,13 | 2,4 |
| Offbeat hats | 3,7,11,15 | +,+,+,+ |
| 8th hats | odd steps | all 8ths |
| 16th hats | all steps | all 16ths |

### Pattern Lengths

- 16 steps = 1 bar at dur=1/4
- 32 steps = 2 bars at dur=1/4
- 64 steps = 4 bars at dur=1/4

---

## Sources

Patterns based on research from:
- Native Instruments - Drum Patterns Guide
- Attack Magazine - TR-909 Guide, Beat Dissected series
- drumpatterns.onether.com - Amen Break
- Studio Brootle - Techno/EBM Patterns
- Academic research on Amen break, clave patterns
