# yellow — 86 bpm, B major, looking at stars
# Coldplay / Yellow: clean arpeggios, emotional arc, strings swell at chorus
Clock.bpm = 86
Scale.default = "major"
Root.default = "B"

#@#@ yellow

#@ verse

# main arpeggio — follows B F# G#m E chord cycle (16-beat loop)
# degrees per chord: B=(0,2,4) F#=(4,6,8) G#m=(5,7,9) E=(3,5,7)
gt >> nylon([0,2,4,2,0,2,4,2, 4,6,8,6,4,6,8,6,
             5,7,9,7,5,7,9,7, 3,5,7,5,3,5,7,5],
            oct=5, dur=0.5, sus=0.45, amp=0.5,
            room=0.65, mix=0.55, chorus=0.2,
            pan=sinvar([-0.15,0.15],16))

# piano chord stabs — underlining each chord root
pd >> piano([(0,2,4),(4,6,8),(5,7,9),(3,5,7)], oct=4,
            dur=4, sus=3.6, amp=0.32,
            room=0.7, mix=0.6)

# warm bass — roots only, no embellishment
ba >> fbass([0,4,5,3], oct=3, dur=4, sus=3.5, amp=0.6,
            cutoff=350, rq=0.4)

#@ prechorus

# melody enters — the "look at the stars" line
ml >> keys([4,4,3,2,0,2,3,4,4,4,3,2,0], oct=5,
           dur=var([0.5,1],[8,5]),
           sus=PRand([0.5,0.7,1,1.5],5), amp=0.45,
           room=0.7, mix=0.55, chorus=0.15,
           pan=0.1)

# strings hint — very quiet
sw >> swell([-7,-5,0,4], oct=4, dur=4,
            sus=4.5, amp=sinvar([0.05,0.18],32),
            rate=0.4, wide=0.4,
            room=0.9, mix=0.8)

#@ chorus

# strings fully in — soar
sw.amp = sinvar([0.25, 0.45], 16)
sw.wide = 0.8
sw >> swell([(0,2,4),(4,6,8),(5,7,9),(3,5,7)], oct=4,
            dur=4, sus=4.8, amp=sinvar([0.3,0.5],16),
            rate=0.3, wide=0.8, room=0.95, mix=0.85)

# cello line — countermelody
vi >> viola([0,-2,3,2,0,-2], oct=4,
            dur=var([2,1,1,1,2,1],[4,2,2,2,4,2]),
            sus=var([1.8,0.8,0.8,0.8,1.8,0.8],[4,2,2,2,4,2]),
            amp=sinvar([0.15,0.35],16),
            room=0.9, mix=0.8, vibrato=sinvar([0,0.3],16))

# cs80 — warm orchestral pad underneath
cx >> cs80([0,4,5,3], oct=4, dur=4,
           sus=4.5, amp=sinvar([0.1,0.28],32),
           cutoff=sinvar([1500,3500],32),
           vibspeed=4, vibdepth=0.015,
           room=0.9, mix=0.8)

# bass opens up, starts walking slightly
ba.amp = linvar([0.6, 0.8], 32)

#@ bridge

# stripped back — just arpeggio and piano, hushed
sw.amp = linvar([0.35, 0.05], 16)
vi.amp = linvar([0.3, 0], 8)
cx.amp = linvar([0.25, 0], 8)
ml.amp = linvar([0.45, 0.15], 16)

# second guitar voice — angel texture (shimmer)
al >> angel([0,4,5,3], oct=6, dur=4,
            sus=5, amp=sinvar([0,0.12],16), rq=0.4,
            room=0.99, mix=0.95,
            shimmer=0.4)

#@ outro(48)

# everything swells back — climax then fade
sw >> swell([(0,2,4),(4,6,8),(5,7,9),(3,5,7)], oct=4,
            dur=4, sus=4.8, amp=linvar([0.45, 0], 48),
            rate=0.3, wide=0.9, room=0.95, mix=0.9)
cx.amp = linvar([0.3, 0], 48)
ml.amp = linvar([0.5, 0], 48)
al.amp = linvar([0.15, 0], 48)
ba.amp = linvar([0.75, 0], 48)
pd.amp = linvar([0.35, 0], 48)
gt.amp = linvar([0.5, 0], 48)
