# Composition Engine

Functions for playing, sequencing, and recording compositions from codeBank.

## File Format

Compositions use `#@` section tags in codeBank `.py` files:

```python
# edge93
# electronic

#@intro(32)
Clock.bpm = 93
d1 >> play("x-o-", amp=0.8)
b1 >> dbass([0,2,3], dur=1, amp=0.6)

#@build(64)
d1 >> play("x-o-{-[--]}", amp=1)
b1 >> dbass([0,2,3,5], dur=PDur(5,8), amp=0.8)
p1 >> pluck([0,2,4,7], dur=0.5, amp=linvar([0,0.6],32))

#@peak(32)
p1 >> pluck([0,2,4,7], dur=0.25, amp=0.8, lpf=4000)

#@endfade(16)
```

- First line: `# name` (used as attack name in menus)
- Second line: `# category` (optional, for autocomplete grouping)
- `#@name(beats)` — section with beat duration
- `#@name` — section without specified duration
- `#@end(N)` — special: calls `Clock.clear()` after N beats
- `#@endfade(N)` — special: fades all players to 0 then clears

Files without `#@` tags work normally — `fire("name")` executes the whole file.

---

## Functions

### fire(name, section=None, dur=None, seq=False)

Execute code from a codeBank attack.

```python
fire("edge93")                              # exec entire file
fire("edge93", "intro")                     # exec intro section, plays forever
fire("edge93", "intro", dur=32)             # exec intro, stop its players after 32 beats
fire("edge93", "intro", seq=True)           # auto-advance: intro -> build -> peak -> endfade
fire("edge93", "intro", seq=True, dur=64)   # auto-advance, override each section to 64 beats
```

**Behavior:**
- No section: executes entire file code
- With section: executes only that section's code
- `dur=N`: extracts player names from code (regex `p1 >>`, `b1.attr`), schedules stop after N beats
- `seq=True`: after current section finishes, auto-advances to next section using file's beat values
- `dur` + `seq`: dur overrides per-section beat timing for all sections
- Each `fire()` call cancels any previous fire/setlist via `_play_id` counter

### compose(name, section=None)

Paste a full attack into the editor, optionally auto-play from a section.

```python
compose("edge93")                # paste entire file in editor
compose("edge93", "intro")      # paste file + auto-evaluate intro section
```

Uses the existing `attack()` paste mechanism, then triggers section evaluation in the web IDE.

### sections(name)

Print the section structure of a composition.

```python
sections("edge93")
# Output: intro(32) -> build(64) -> peak(32) -> endfade(16)

sections("alva")
# Output: No sections in 'alva'
```

### reload()

Rescan all codeBank files. Use after saving new files or editing outside the IDE.

```python
reload()
# Output: Reloaded 147 attacks
```

### attack(name, section=None)

Paste attack code into the editor (existing function, now with section support).

```python
attack("edge93")                # paste full file
attack("edge93", "intro")      # paste only intro section code
```

---

## Setlist

Queue multiple sections for sequential playback.

### setlist(entries)

```python
setlist([
    ("edge93", "intro", 32),
    ("hearme", "part3", 64),
    ("antenna", "peak", 16),
    ("edge93", "endfade", 16),
])
```

Each entry is `(name, section, dur)`. Sections play sequentially — when one finishes (after `dur` beats), the next starts. The last entry's players are stopped after its duration.

Output during playback:
```
>> [1/4] edge93 -> intro (32b)
>> [2/4] hearme -> part3 (64b)
...
Setlist finished
```

### skip()

Jump to the next setlist entry immediately.

### back()

Go back to the previous setlist entry.

### current()

Print the full setlist with current position marked:

```
>> [1/4] edge93 -> intro (32b)
   [2/4] hearme -> part3 (64b)
   [3/4] antenna -> peak (16b)
   [4/4] edge93 -> endfade (16b)
```

---

## Recording

Capture a live coding session and generate a composed `#@` script.

### rec()

Start recording. Captures every code evaluation with its timestamp.

```python
rec()
# Output: Recording started at 128 BPM...
```

### rec_stop(name=None)

Stop recording and save the generated script.

```python
rec_stop()                  # saves as recorded_HHMMSS.py
rec_stop("my_session")     # saves as my_session.py
```

**What happens:**
1. Server converts timestamps to beats using BPM
2. Gaps > 4 beats create section boundaries
3. Durations snap to nearest [4, 8, 16, 32, 64] beats
4. Sections auto-named: intro, build, peak, break, drop, outro, part7...
5. File saved to `codeBank/`, attacks reloaded
6. Script pasted into editor

Generated file example:
```python
# my_session
# recorded

#@intro(16)
d1 >> play("x-o-", amp=0.8)
b1 >> dbass([0,2,3], dur=1)

#@build(32)
p1 >> pluck([0,2,4], dur=0.5, amp=0.6)

#@endfade(16)
```

---

## Cancellation

All composition functions share a single `_play_id` counter:
- Calling `fire()` cancels any running fire/setlist
- Calling `setlist()` cancels any running fire/setlist
- `Ctrl+;` (Clock.clear) cancels all scheduled callbacks
- `skip()`/`back()` cancel current setlist entry and jump

---

## Autocomplete

The IDE autocomplete supports all composition functions:

- `fire("` → shows attack names grouped by category (Right arrow to browse)
- `fire("edge93", "` → shows available sections with beat counts: `intro (32b)`, `build (64b)`...
- Same for `compose("`, `sections("`, `attack("`
