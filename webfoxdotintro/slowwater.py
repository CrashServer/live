# ════════════════════════════════════════════════════════════════════
#   slow water
#   72 bpm · lydian, then dorian, then lydian again
# ════════════════════════════════════════════════════════════════════
#
#   Not a lesson — a piece. Put the cursor anywhere in the block below
#   and press Ctrl+Alt+Enter, or click "still" in the parts list.
#   It runs about five minutes and comes back to where it started.
#
#   One figure carries the whole thing:
#
#       [0, 2, 4, 6, 4, 2]     up to the lydian fourth, and back down
#
#   Everything else is that figure slowed, reversed, moved into a
#   darker mode and brought home again. Nothing new arrives after the
#   first minute; it only keeps turning over.
#
#   Every line stands alone — Ctrl+Enter any one of them on its own.
#
# ────────────────────────────────────────────────────────────────────

#@#@ slow_water

Clock.bpm = 72
Scale.default = "lydian"


# ── still ────────────────────────────────────────────────────────────
# A bed and a sub, and 32 beats for the filter to open. Nothing to
# follow yet — this is the room before anyone plays.

#@still(32)
pad >> spicepad([(0,2,4), (5,7,9)], oct=4, dur=8, amp=0.4, cutoff=linvar([400, 1900], [32]), room=0.9, reverb=0.5)
sub >> sine([0, 0, 5, 5], oct=3, dur=8, amp=0.22, lpf=500)


# ── light ────────────────────────────────────────────────────────────
# The figure, stated plainly, one note a beat. It will not be this
# simple again.

#@light(32)
pad >> spicepad([(0,2,4), (5,7,9)], oct=4, dur=8, amp=0.4, cutoff=1900, room=0.9, reverb=0.5)
sub >> sine([0, 0, 5, 5], oct=3, dur=8, amp=0.22, lpf=500)
mel >> rhodes([0, 2, 4, 6, 4, 2], oct=5, dur=1, amp=0.42, lpf=linvar([1400, 4200], [32]), reverb=0.35, room=0.7)


# ── turn ─────────────────────────────────────────────────────────────
# A second voice at half speed underneath, so the figure hears itself
# from below. The bell is one note every four beats and nothing more.

#@turn(32)
pad >> spicepad([(0,2,4), (5,7,9), (3,5,7), (4,6,8)], oct=4, dur=8, amp=0.4, cutoff=sinvar([1500, 2600], [16]), room=0.9, reverb=0.5)
sub >> sine([0, 0, 5, 5], oct=3, dur=8, amp=0.22, lpf=500)
mel >> rhodes([0, 2, 4, 6, 4, 2], oct=5, dur=1, amp=0.42, lpf=3200, reverb=0.35, room=0.7)
low >> karp([0, 2, 4, 6, 4, 2], oct=4, dur=2, amp=0.26, lpf=2200, pan=sinvar([-0.6, 0.6], [24]), reverb=0.4)
~ring >> bell([7], oct=6, dur=4, amp=0.16, reverb=0.8, room=0.95)


# ── deeper ───────────────────────────────────────────────────────────
# The mode changes under the same notes. Nobody plays anything new —
# lydian's bright fourth becomes dorian's flat third, and the whole
# piece tilts.

#@deeper(32)
Scale.default = "dorian"
pad >> spicepad([(0,2,4), (5,7,9), (3,5,7), (4,6,8)], oct=4, dur=8, amp=0.42, cutoff=sinvar([1200, 2200], [16]), room=0.9, reverb=0.55)
sub >> sine([0, 0, 3, 3], oct=3, dur=8, amp=0.24, lpf=480)
mel >> rhodes([0, 2, 4, 6, 4, 2], oct=5, dur=1, amp=0.4, lpf=2600, reverb=0.4, room=0.75).every(16, "reverse")
low >> karp([0, 2, 4, 6, 4, 2], oct=4, dur=2, amp=0.26, lpf=1800, pan=sinvar([-0.6, 0.6], [24]), reverb=0.4)


# ── wide ─────────────────────────────────────────────────────────────
# The top of the piece. Marimba doubles the figure an octave up and a
# quarter-beat behind, which is the only place two voices disagree.

#@wide(32)
pad >> spicepad([(0,2,4), (5,7,9), (3,5,7), (4,6,8)], oct=4, dur=8, amp=0.45, cutoff=linvar([1800, 3400], [32]), room=0.9, reverb=0.55)
sub >> sine([0, 0, 3, 3], oct=3, dur=8, amp=0.26, lpf=520)
mel >> rhodes([0, 2, 4, 6, 4, 2], oct=5, dur=1, amp=0.44, lpf=linvar([2600, 5200], [32]), reverb=0.4, room=0.75)
low >> karp([0, 2, 4, 6, 4, 2], oct=4, dur=2, amp=0.28, lpf=2400, reverb=0.4)
top >> marimba([0, 2, 4, 6, 4, 2], oct=6, dur=1, amp=0.2, delay=0.25, pan=sinvar([0.7, -0.7], [20]), reverb=0.5, room=0.8)
~ring >> bell([7, 11], oct=6, dur=4, amp=0.18, reverb=0.8, room=0.95)


# ── fade ─────────────────────────────────────────────────────────────
# Lydian comes back and the voices leave in the order they arrived.

#@fade(32)
Scale.default = "lydian"
pad >> spicepad([(0,2,4), (5,7,9)], oct=4, dur=8, amp=linvar([0.45, 0.3], [32]), cutoff=linvar([3000, 900], [32]), room=0.9, reverb=0.6)
sub >> sine([0, 0, 5, 5], oct=3, dur=8, amp=0.2, lpf=440)
mel >> rhodes([0, 2, 4, 6, 4, 2], oct=5, dur=2, amp=linvar([0.4, 0.12], [32]), lpf=linvar([3600, 1200], [32]), reverb=0.5, room=0.85)
low >> karp([0, 2, 4], oct=4, dur=4, amp=linvar([0.24, 0], [32]), lpf=1400, reverb=0.5)
top >> marimba([0, 2, 4, 6, 4, 2], oct=6, dur=2, amp=linvar([0.18, 0], [32]), reverb=0.6, room=0.85)


# ── last ─────────────────────────────────────────────────────────────
# The bed alone, and the first two notes of the figure, twice as slow
# as they began.

#@last(16)
pad >> spicepad([(0,2,4)], oct=4, dur=16, amp=linvar([0.3, 0.12], [16]), cutoff=700, room=0.95, reverb=0.7)
mel >> rhodes([0, 2], oct=5, dur=8, amp=linvar([0.18, 0.05], [16]), lpf=900, reverb=0.6, room=0.9)


# ── end ──────────────────────────────────────────────────────────────
# One note, left to ring out on its own.

#@end(8)
~ring >> bell([0], oct=5, dur=8, amp=0.16, reverb=0.9, room=0.98)


# ────────────────────────────────────────────────────────────────────
#   If you want it to breathe on a wall while it plays:
#
#       video1 >> aurora(speed=0.15) + grain(0.12)
#
#   Ctrl+; stops. Twice cuts the tails.
# ────────────────────────────────────────────────────────────────────
