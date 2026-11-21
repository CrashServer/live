# ════════════════════════════════════════════════════════════════════
#   hello, crashDot
#   a little tune that builds itself, one idea per line
# ════════════════════════════════════════════════════════════════════
#
#   Put the cursor on a line. Press Ctrl+Enter. Listen.
#   Then move down one line and do it again.
#
#   Every line is the line above it plus exactly one new thing, so you
#   always know what you just heard. Nothing here needs the line below
#   it — you can stop anywhere and it still sounds like something.
#
#   Ctrl+;  stops everything.  Press it twice to cut the tails too.
#
# ────────────────────────────────────────────────────────────────────

Clock.bpm = 112

# Chromatic: one step is one semitone, so a number IS an interval.
# -7 is a fifth down, 12 is an octave up, and nothing gets bent to fit
# a key you did not ask for.
Scale.default = "chromatic"


# ── 1 · a voice ──────────────────────────────────────────────────────
# g1 is a name you invented. >> points a synth at it. That is the
# whole sentence.

g1 >> dirt()

# higher up
g1 >> dirt(oct=6)

# shorter notes — sus is how long each one is held
g1 >> dirt(oct=6, sus=1/2)

# twice as often — dur is the gap between them
g1 >> dirt(oct=6, sus=1/2, dur=1/2)

# a list is a sequence: it plays them in turn, forever
g1 >> dirt([0, 0, -5], oct=6, sus=1/2, dur=1/2)

# a longer phrase, with a fifth in it
g1 >> dirt([0, 0, -7, -7, 0, 0], oct=6, sus=1/2, dur=1/2)

# three copies, slightly detuned — the same notes, thicker
g1 >> dirt([0, 0, -7, -7, 0, 0], oct=6, sus=1/2, dur=1/2).unison(3)

# sus can be a list too. Long, short, long, short.
g1 >> dirt([0, 0, -7, -7, 0, 0], oct=6, sus=[1/2, 1], dur=1/2).unison(3)

# soften the top — lpf is a low-pass filter, in Hz
g1 >> dirt([0, 0, -7, -7, 0, 0], oct=6, sus=[1/2, 1], dur=1/2, lpf=2200).unison(3)


# ── 2 · something to sit on ──────────────────────────────────────────
# play() speaks in characters instead of numbers. x is a kick,
# o is a snare, - is a hat, and . is a rest.

b1 >> play("x")

b1 >> play("x-o-")

b1 >> play("x-o-", amp=0.9)

# [ ] means "fit these into one step", so the hats double up
b1 >> play("x-o[--]", amp=0.9)


# ── 3 · the cute part ────────────────────────────────────────────────
# Five notes that cannot sound wrong together: 0 2 4 7 9.
# In chromatic that is a major pentatonic, spelled out in semitones.

m1 >> marimba([0, 4, 7, 9], oct=6, dur=1/2, amp=0.6)

# () inside a list is a CHORD — played together, not in turn
m1 >> marimba([0, 4, (7, 12), 9], oct=6, dur=1/2, amp=0.6)

# a little room around it
m1 >> marimba([0, 4, (7, 12), 9], oct=6, dur=1/2, amp=0.6, reverb=0.4, room=0.7)

# every 8 beats, play the phrase backwards, then carry on
m1 >> marimba([0, 4, (7, 12), 9], oct=6, dur=1/2, amp=0.6, reverb=0.4, room=0.7).every(8, "reverse")


# ── 4 · something that moves on its own ──────────────────────────────
# linvar walks from the first number to the second over that many
# beats, then back. Put it where a number goes and the number breathes.

p1 >> pluck([0, 7, 12, 7], oct=6, dur=1/4, amp=0.35, lpf=linvar([600, 5000], [16]))

# pan it side to side, slower
p1 >> pluck([0, 7, 12, 7], oct=6, dur=1/4, amp=0.35, lpf=linvar([600, 5000], [16]), pan=sinvar([-0.8, 0.8], [12]))


# ── 5 · a ceiling ────────────────────────────────────────────────────
# ~ in front means "play it once, let it ring" — no loop.

~bell1 >> bell([0, 12, 19], oct=6, dur=4, amp=0.3, reverb=0.7, room=0.9)


# ── 6 · look at it ───────────────────────────────────────────────────
# The visuals speak the same language. A scene goes on a video channel.

video1 >> plasma()

video1 >> plasma(speed=0.4) + grain(0.25)


# ── 7 · all of it, as a piece ────────────────────────────────────────
# Ctrl+Alt+Enter runs a whole block at once. Run the one below and the
# tune plays itself: #@name(beats) marks a section, and they advance in
# order. This is the same eight lines you just built, arranged.

#@#@ hello_crashdot

#@wave(16)
g1 >> dirt([0, 0, -7, -7, 0, 0], oct=6, sus=[1/2, 1], dur=1/2, lpf=linvar([700, 2600], [16])).unison(3)
~bell1 >> bell([0, 12, 19], oct=6, dur=4, amp=0.25, reverb=0.7, room=0.9)

#@walk(16)
g1 >> dirt([0, 0, -7, -7, 0, 0], oct=6, sus=[1/2, 1], dur=1/2, lpf=2200).unison(3)
b1 >> play("x-o-", amp=0.85)
m1 >> marimba([0, 4, (7, 12), 9], oct=6, dur=1/2, amp=0.55, reverb=0.4, room=0.7)

#@skip(16)
b1 >> play("x-o[--]", amp=0.9)
m1 >> marimba([0, 4, (7, 12), 9], oct=6, dur=1/2, amp=0.55, reverb=0.4, room=0.7).every(8, "reverse")
p1 >> pluck([0, 7, 12, 7], oct=6, dur=1/4, amp=0.3, lpf=linvar([600, 5000], [16]), pan=sinvar([-0.8, 0.8], [12]))

#@hush(16)
g1 >> dirt([0, 0, -7, -7, 0, 0], oct=6, sus=[1/2, 1], dur=1/2, lpf=linvar([2200, 500], [16]), amp=linvar([0.9, 0.2], [16])).unison(3)
b1 >> play("x...", amp=0.6)
m1 >> marimba([0, 4, (7, 12), 9], oct=6, dur=1/2, amp=linvar([0.55, 0], [16]), reverb=0.5, room=0.8)

#@bye(8)
~bell1 >> bell([0, 12, 19, 24], oct=6, dur=4, amp=0.3, reverb=0.8, room=0.95)

#@end(4)

# ────────────────────────────────────────────────────────────────────
#   Ctrl+; to stop. Ctrl+; twice to cut the tails.
#   The help panel has the rest of the words.
# ────────────────────────────────────────────────────────────────────
