# horn — improvisation scratchpad over ostinato
# freejazz

# Ctrl+Enter individual lines to swap the horn character.
# All use player name `hn` — each line replaces the previous.
# Designed to play over ostinato.py's bed/shift/open/close/sparse/dense sections.

# === REED / HORN VOICE — melodic, expressive ===

# plaitsX preset morphing — Ayler-style reed shifts
hn >> plaitsX(PMarkov(), dur=PWhite(0.15, 2.5), sus=PWhite(0.1, 1.8), oct=6, amp=0.5, preset=var([3, 7, 5, 11], PRand([4, 8, 16])), porta=PRand([0, 0.2, 0.5]), harm=linvar([0.3, 0.7], 32), timbre=sinvar([0.3, 0.8], PWhite(4, 12)), hpf=400, jpverb=0.55, jpsize=0.9, jpdamp=0.3, stereowidth=0.85)

# plaitsX fast & dry — Ornette aperiodic lines with fbdelay
hn >> plaitsX(melody(), dur=PWhite(0.08, 1.5), sus=PWhite(0.05, 1.2), oct=6, amp=0.55, preset=PRand([0, 2, 6, 9]), cutoff=sinvar([800, 4500], PWhite(3, 10)), hpf=350, fbdelay=0.35, fbtime=PRand([0.125, 0.1875, 0.25]), fbfeed=0.55, fbcutoff=4000, fbspread=0.08, beat_dur=1, jpverb=0.45, stereowidth=0.85)

# alva — ECM smooth lead, long phrases
hn >> alva(PMarkov(), dur=PWhite(0.5, 4), sus=PWhite(0.3, 3), oct=5, amp=0.45, mod=sinvar([0.2, 0.8], PWhite(8, 20)), vib=linvar([0, 0.4], 32), hpf=300, jpverb=0.6, jpsize=0.92, jpdamp=0.4, tape=0.3, tapedrive=1.2, stereowidth=0.88)

# prof — prophet voice, modal lines over the bed
hn >> prof(PRand([0, 2, 4, 5, 7, 9, 11, 12]), dur=PWhite(0.2, 2), sus=PWhite(0.15, 1.5), oct=5, amp=0.5, hpf=300, tape=0.35, tapedrive=1.3, jpverb=0.55, jpsize=0.9, jpdamp=0.35, stereowidth=0.85)

# === CLUSTER / ATTACK — dense, percussive ===

# glitcher — Cecil Taylor Henon chaos clusters
hn >> glitcher(PWhite(0, 14), dur=PWhite(0.05, 0.6), sus=PWhite(0.03, 0.4), oct=6, amp=0.5, len=PWhite(0.1, 2), henA=PRand([1.2, 1.4, 1.6, 1.8]), henB=PRand([0.2, 0.3, 0.4]), hpf=500, jpverb=0.45, jpsize=0.85, jpdamp=0.35, stereowidth=0.85, pan=PRand([-0.8, -0.4, 0, 0.4, 0.8]))

# braids 48 models — Ayler tonal multiphonics, rapid model swaps
hn >> braids(melody(), dur=PWhite(0.2, 2.5), sus=PWhite(0.15, 2), oct=6, amp=0.45, model=PRand([0, 8, 17, 23, 29, 41]), timbre=sinvar([0.3, 0.8], PWhite(4, 12)), color=linvar([0.2, 0.8], 24), decim=PRand([0, 4, 8]), hpf=350, jpverb=0.55, jpsize=0.92, jpdamp=0.3, stereowidth=0.88)

# scatter + resonbank — Bartók percussive resonant cluster
hn >> scatter(PRand([0, 3, 7, 10, 2, 5]), dur=PWhite(0.2, 1.8), sus=PWhite(0.1, 0.8), oct=6, amp=0.5, rate=PWhite(0.5, 8), resonbank=0.85, rbfreq=PRand([150, 200, 300, 500, 800]), rbdecay=PWhite(0.3, 1.2), rbspread=PRand([0.3, 1, 1.5, 2.5]), hpf=400, jpverb=0.6, jpsize=0.9, stereowidth=0.88)

# === NOISE / BREATH — stochastic, untuned ===

# rave (Gendy1) — pure stochastic, Evan Parker circular breathing
hn >> rave(PWhite(0, 14), dur=PWhite(0.1, 1.2), sus=PWhite(0.08, 0.8), oct=6, amp=0.35, hpf=400, jpverb=0.55, jpsize=0.9, jpdamp=0.35, stereowidth=0.9, pan=PRand([-0.7, -0.3, 0.3, 0.7]))

# virus — chaos arrays, late Coltrane sheets of sound
hn >> virus(PWhite(0, 12), dur=PWhite(0.08, 0.8), sus=PWhite(0.05, 0.4), oct=6, amp=0.4, len=PWhite(0.2, 1.5), mod1=PRand([0.3, 0.5, 0.7, 0.9]), mod2=PRand([0.2, 0.4, 0.6]), hpf=500, jpverb=0.5, jpsize=0.88, stereowidth=0.85, pan=PRand([-0.7, 0.7]))

# fmsynth — growling FM, slow breath-like index modulation
hn >> fmsynth(PMarkov(), dur=PWhite(0.3, 2.5), sus=PWhite(0.2, 2), oct=5, amp=0.4, index=sinvar([2, 12], PWhite(4, 16)), hpf=300, tape=0.3, tapedrive=1.3, jpverb=0.6, jpsize=0.92, jpdamp=0.35, stereowidth=0.85)

# === STOP ===
hn.stop()
