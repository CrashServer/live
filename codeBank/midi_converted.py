### ===== DAFT PUNK — Harder Better Faster Stronger =====
Clock.bpm = 105
Scale.default = Scale.major
Root.default = "C#"
d1 >> a_daft([1,1,5,4,1,1,4,3,3,3,2,1,3,3,5,4,1,3,4,3,1,3,4,3,5,4,3,3,1,0,1,3,1,1,3,1,3,5,3,1,3,0,0,3,0,4,3,2,3,6,6,1,6,4,3,1,6,5,5,1,3,1,1,1,1], dur=1/4, sus=1/2, rate=12, cutoff=var([800, 1200, 1300, 4000, 1600, 3200], 8), resonance=0.1, punch=2, oct=PStutter([5,6,5,6,5,6,5,6,5,6,5,7,5,6,4],[2,6,2,4,6,13,2,6,2,6,2,6,2,2,4]), shapemix=1).unison(3)
v0 >> compkick(tone=4.0, noise=3.0, comp=1, drive=0.2, ring=1, metal=3.5, body=0.4, bend=1.3, dur=1/4)
# >> Try: add lpf=linvar([400,4000],64) for filter sweep, .every(16,"stutter",4) for glitch drops
# >> Try: Root.default=var(["C#","E","A"],32) for key changes between sections


### ===== DAFT PUNK — Around the World =====
Clock.bpm = 123
Scale.default = Scale.mixolydian
Root.default = "D"
d2 >> a_daft([4,4,4,4,5,6,6,6,6,0,1,1,1,1,2,1,0,5,5,4,3], cutoff=linvar([2000, 6000], 32), fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, dur=PStutter([1,1/2,1/4,3/2,1,1/2,1/4,3/2,1,1/2,1],[3,1,1,1,2,1,1,1,3,6,1]), sus=PStutter([1/2,1/4,1/2,1/4,1/2,1/4,1],[4,1,4,1,4,6,1]), oct=PStutter([5,6,6],[5,12,4]), mverb=0.1).unison(4)
# >> Try: add shape=sinvar([0,0.4],16) for breathing distortion, .every(32,"stutter",8,rate=2) for build-ups
# >> Try: d3>>soprano([3,2,3,3,4,3,2,3,5,3], dur=PDur(10,16)*2) for the vocal hook


### ===== DAFT PUNK — Da Funk =====
Clock.bpm = 111
Scale.default = Scale.dorian
Root.default = "C"
d4 >> a_daft([4,3,4,6,1,0,1,3,6,5,6,1,4,5,6], dur=PStutter([2,1/2,3,1/2,3,1/2,3,1],[1,3,1,3,1,3,1,2]), sus=PStutter([3/2,1/4,2,1/4,2,1/4,2,3/4],[1,3,1,3,1,3,1,2]), oct=PStutter([5,4,5,4],[8,3,1,3]), mverb=0.2, sgate=0.5, sgthresh=1, sgmode=0, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=0).unison(3)
d5 >> a_daft([4,3,4,6,1,0,1,3,6,5,6,1,4,5,6], dur=PStutter([2,1/2,3,1/2,3,1/2,3,1],[1,3,1,3,1,3,1,2]), sus=PStutter([3/2,1/4,2,1/4,2,1/4,2,3/4],[1,3,1,3,1,3,1,2]), oct=PStutter([6,5,6,5],[8,3,1,3]), cutoff=4000)
b1 >> play("x", sample=4, dur=[1/2,3/4,3/4,1,1], sus=1/2, dist=0.0).unison(3)
# >> Try: add lpf=var([800,4000,800,2000],[16,8,8,16]) on d4 for wah-wah feel
# >> Try: d4.every(32,"stutter",16,rate=PRand([0.5,2,4])) for glitch breakdowns
# >> Try: p2>>pluck(4, dur=1, sus=1/2, oct=3) for the sub bass pedal note


### ===== DR. DRE — Still D.R.E. =====
Clock.bpm = 96
Scale.default = Scale.major
Root.default = "C"
d1 >> dbass(Pvar([(0,5),P[(0,5),(6,4)],(6,4)],[5,1,2]), dur=1/2, oct=PStutter([5,4],[11,5]))
d2 >> dbass([4,5,6,2], dur=[1,3], sus=[1,3/4], oct=[5,5,5,6])
d3 >> pluck(Pvar([(0,5),P[(0,5),(6,4)],(6,4)],[5,1,2]), dur=1/2, oct=PStutter([6,4],[11,5]))
# >> Try: add d1.unison(2,0.01) for subtle detuning, tape=var([0,0.3],32) for lo-fi warmth
# >> Try: v0>>compkick(dur=PDur(3,8), comp=1, body=0.6) + play("..o.",dur=1/4,sample=3) for boom-bap drums
# >> Try: Root.default=var(["C","A","F"],16) for chord progression movement


### ===== METALLICA — Enter Sandman =====
Clock.bpm = 110
Scale.default = Scale.chromatic
Root.default = "C"
d3 >> faim(PRand([0,(7,2),(6,1),4,6,7,9,11]), dur=PRand([1/2,1/4]), oct=4, beef=1).unison(3)
d2 >> faim([2,2,4,5,5,2], dur=[1,1/2,1/2,1/2,1,1/2], oct=[4,5,5,4,4,5])
# >> Try: add shape=var([0,0.8],[28,4]) for verse/chorus distortion contrast
# >> Try: d2.every(8,"stutter",2,rate=0.5) for palm-mute chug effect
# >> Try: play("x..x..x.",dur=1/4,sample=5,amp=Pacc(0)) for thrash drums


### ===== JUSTICE — Shrine (Ultima VII) =====
Clock.bpm = 80
Scale.default = Scale.mixolydian
Root.default = "D"
d1 >> pluck([0,5,2,5,0,5,6,4,1,4,6,4], dur=1/2, oct=[6,5], amp=0.25)
d2 >> pluck([(5,0,2),(4,6,1)], dur=3, sus=2, amp=0.5)
d3 >> pluck([0,5,2,5,0,5,6,4,1,4,6,4], dur=1/2, oct=[5,4], amp=0.5)
d4 >> pluck([5,6,0,1,2,3,3], dur=PStutter([1/2,4,2],[5,1,1]), sus=[1/2,1/2,1/8,1/8,1/2,1/8,2], oct=[7,8,8,8,8,8,8], amp=0.5)
b1 >> pluck([2,2,4,1,1,3,5,6,0,1,2,4,5,6,0,1,2,2,3,1,1,4,5,6,0,1,2,3,4,5,4,3,2,0], dur=PStutter([2,1/2,2,1/2,1,1/2,1,2,1/2,2,1/2,1,1/2,1/4,2],[1,2,1,6,1,4,1,1,2,1,8,2,1,2,1]), sus=PStutter([1/2,1/8,1,1/2,1/8,1,1/2,1/8,1/2,1,1/2,1/8,2],[8,2,1,2,2,1,8,2,2,2,1,2,1]), oct=PStutter([7,5,6,5,6,7,5,6],[6,1,4,2,3,6,1,11]), amp=0.5)
b2 >> pluck([5,6,0,1,2,4,5,6,0,1,2,2,3,1,1,4,5,6,0,1,2,3,4,5,4,3,2,0], dur=PStutter([1/2,1,1/2,1,2,1/2,2,1/2,1,1/2,1/4,1/3,2],[4,1,4,1,1,2,1,8,2,1,1,1,1]), sus=PStutter([1/2,1/8,1,1/2,1/8,1,3/4,1/2,1/8,1/2,1,1/2,1/8,2],[2,2,1,2,2,1,6,2,2,2,2,1,2,1]), oct=PStutter([4,5,4,5,7,4,5,6],[1,4,2,3,6,1,10,1]), amp=0.5)
p1 >> pluck([0,0,2,6,6,1,0,0,1,6,6,1], dur=[2,1/2,1/2], sus=1/2, oct=6, amp=0.25)
# >> Try: add cheapverb=0.6 + shimmer=0.3 on d1/d3 for cathedral reverb
# >> Try: lpf=linvar([600,8000],64) on b1 for slow filter bloom
# >> Try: d1.follow(d3) to lock upper and lower voices, .every(16,"reverse")


### ===== JUSTICE — Valentine (Gesaffelstein vibe) =====
Clock.bpm = 105
Scale.default = Scale.major
Root.default = "C#"
d1 >> dbass(Pvar([P[(1,1,3),(1,3),(1,3),(1,3),(0,0,2),(0,2),(0,1),(0,1),(4,6,1),(6,1)],(6,1),P[(5,5,0),(5,0)],(5,0),P[(3,5,0),(5,0)],(5,0)],[5,3,1,3,1,11]), dur=1/2, sus=PStutter([2,1/4,2,1/4,4,1/4,4,1/4,4,1/4],[1,3,1,3,1,7,1,7,1,7]), oct=PStutter([5,6,5,6,4,6,4,5,4,5],[1,3,1,3,1,7,1,7,1,7])).unison(3)
d2 >> dbass([3,2,3,4,5,4,5,3,4,3,2,3,4,5,1,2,3,1,5,0,5,0,5,5,5,5,3,2], dur=[2,1/4,2,1/4,2,2,3/2,2,1/4,4,8,2,1/4,3/2,1/4,1/4,3/2,3,1/4,1/4,3/2,3/2,1/2,1/4,1/4,1,2,1/4], sus=1/4, oct=PStutter([5,4,5,6,5,6,5,6,5],[6,1,7,4,1,1,1,1,6])).unison(3)
# >> Try: add dynfuzz=sinvar([0,0.6],16) for breathing fuzz, tape=0.3 for warmth
# >> Try: play("x",dur=1/2,sample=5,amp=Pacc(3,8),shape=2) for industrial kick
# >> Try: d1.every(16,"stutter",8,rate=var([1,0.5],8)) for half-speed drops


### ===== JUSTICE — Phantom =====
Clock.bpm = 120
Scale.default = Scale.mixolydian
Root.default = "C"
d1 >> pluck(PStutter([1,4,5,6,5,6],[8,1,3,1,5,1]), dur=[1,1,1,1,1,1,3/4,1/2,3/4,1,1,1/4,3/4,1,1,1,3/4,1/2,3/4], oct=4)
d2 >> pluck(PStutter([1,4,5,6,5,6],[8,1,3,1,5,1]), dur=[1,1,1,1,1,1,3/4,1/2,3/4,1,1,1/4,3/4,1,1,1,3/4,1/2,3/4], oct=4)
d3 >> pluck([5,3,1,5,1,3,5,1,3,1,5,3,1,3,1,5,2,0,5,0,2,5,0,2,0,5,2,0,5,0,2,5,2,0,5,2,0,5,2,0,5,2,0,5,2,0,5,2,4,2,0,4,2,0,4,2,0,4,2,0,4,2,0,4], dur=1/4, oct=PStutter([6,5,6,7,6,5,6,5,6,7,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6],[3,1,3,3,5,1,2,1,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,17]))
# >> Try: add dist2=var([0,1.5],[24,8]) for verse/drop contrast
# >> Try: d3.every(8,"stutter",PRand([2,4,8])) for rhythmic stutters on the arp
# >> Try: cheapverb=sinvar([0,0.8],32) + shimmer=0.2 for epic builds


### ===== DEVO — Gut Feeling =====
Clock.bpm = 148
Scale.default = Scale.major
Root.default = "C"
d1 >> dbass([2,4,0,5,1], dur=4, oct=[4,4,5,4,5]).unison(3)
d2 >> tb304(PRand([0,1,2,3,4,5,6]), dur=PRand([1,1/2,3/2]), sus=3/2, oct=PRand([3,4,5]))
d3 >> tb305([2,4,0,5,1], dur=4, oct=4)
b1 >> faim([(2,4),(4,6),(4,0),(2,5),(5,1)], dur=4, oct=5)
b2 >> cs80([(2,6),(4,6),(4,0),(2,0),(5,1),(6,2),(6,1),(0,2),(0,2),(1,3),(2,4),(1,4),(2,4),(5,5),(1,5)], dur=4, oct=PStutter([5,6,5,6],[7,6,1,1]), fatk=0.75, fdec=0.5, fsus=0.4, frel=1.0, cutoff=200, detune=0.002, vibspeed=0.1, vibdepth=0.004, glide=0.8, glidedur=0.015)
p1 >> faim(Pvar([(1,1),P[(1,1),(0,0)],(0,0),(1,1)],[1.5,1,1.5,4]), dur=PStutter([1/2,1/4,1/2,1/4,1/2,1/4,1/2,1/4,1/2,1/4],[1,1,1,1,2,1,1,1,5,8]), sus=PStutter([1/2,1/4,1/2,1/4],[1,4,1,16]), oct=6)
p2 >> pluck(PwRand([(1,1),(0,0),(2,6)],[247,75,1]), dur=PRand([1/2,1/4]), sus=1/4, oct=[3,5])
d4 >> faim(Pvar([P[2,4,0,5,1,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,1,1,1],P[1,1,1,1,1,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,1,1,1]],[37.5,580]), dur=PStutter([4,1/2,1/4],[5,1199,1]), sus=PStutter([1/2,1/4],[5,1200]), oct=7)
# >> Try: add shape=var([0,0.6,0,1.2],[8,4,12,4]) on d2 for breathing distortion
# >> Try: d1.every(16,"stutter",4,rate=2) for punk energy bursts
# >> Try: Root.default=var(["C","G","F","C"],[16,8,8,16]) for chord movement under the riff
