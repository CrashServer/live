# abyss — heavy dirty rumbling dark techno
# techno

Clock.bpm = 135
Scale.default = "minor"
Root.default = "G"

#@intro(32)
d1 >> compkick(0, dur=1, oct=3, amp=1.05, punch=0.95, comp=0.95, click=0.5, sub=0.9, body=0.8, tone=0.45)
b1 >> subbass([0, 0, -5, 0], dur=8, sus=8, oct=4, amp=1.8, lpf=220, lpr=0.25, hpf=40, tape=0.5, tapedrive=1.5)

#@pulse(32)
d2 >> click(0, dur=1/2, sus=0.04, amp=[0, 0.3], rate=13, hpf=2400, pan=0.1)
b1 >> pumpbass([0, 0, -5, -5, 0, 0, -7, -5], dur=PDur(5,8), sus=PDur(5,8)*0.75, oct=4, amp=1.8, cutoff=sinvar([380, 900], 32), res=0.6, sub=0.85, body=0.7, growl=0.55, tape=0.6, tapedrive=1.8, hpf=55)
b1.amp = 1.8 * var([0.22, 1, 1, 1], 1)

#@stab(32)
s1 >> hardstab([(0,3,7), (0,3,7), (-1,2,6), (0,3,7), (-2,1,5), (-2,1,5), (-4,-1,3), (0,3,7)], dur=var([2,1,1,2,2,2,2,2],3), sus=[0.18, 0.35, 0.12, 0.4], oct=5, amp=0.55, cutoff=2400, res=0.5, comp=6, detune=0.02, fold=0.4, feedback=0.35, hpf=220, tubedrive=0.55, tubegain=1.8, tubewarm=0.65, tubebias=0.15, tape=0.45, tapedrive=1.5, fbdelay=0.55, fbtime=0.375, fbfeed=0.75, fbcutoff=3000, fbspread=0.02, beat_dur=1, stereowidth=0.85)
s1.jpverb = var([0, 0.65, 0.65, 0.65], 1)
s1.jpsize = 0.92
s1.jpdamp = 0.4
s1.amp = 0.55 * var([0.35, 1, 1, 1], 1)

#@depth(32)
c1 >> industrialsnare(0, dur=2, delay=1, oct=5, amp=0.65, tone=0.2, noise=0.9, rattle=0.5, ring=0.4, bend=0.35, snap=0.55, comp=0.7, hpf=260, jpverb=0.72, jpsize=0.88, jpdamp=0.4, pan=PRand([-0.12, 0.12]))
h1 >> click(0, dur=1/4, sus=0.014, amp=Pacc("ghost"), amplify=0.2, rate=18, hpf=5200, pan=PRand([-0.35, 0.35]))
t1 >> compperc(PRand([0, 5, 7, 12, -3]), dur=PDur(7, 16), sus=0.08, amp=0.32, tone=0.35, noise=0.55, body=0.25, metal=0.45, ring=0.4, comp=0.5, hpf=900, cheapverb=0.45, cvdecay=1.8, pan=PRand([-0.55, -0.2, 0.2, 0.55]))
t1.amp = 0.32 * var([0.4, 1, 1, 1], 1)

#@void(48)
d1.amp = 0
d2.amp = linvar([0.3, 0.15], 32)
c1.amp = linvar([0.65, 0], 16)
t1.amp = linvar([0.32, 0], 20)
h1.amp = linvar([0.2, 0], 14)
b1.amp = linvar([1.8, 0], 10)
p1 >> industrialdrone([0, -5, -7, 0, -3], dur=16, sus=17, oct=4, amp=0.7, cutoff=linvar([240, 2100], 40), res=0.6, detune=0.45, noise=0.35, sub=0.55, feedback=0.4, cheapverb=0.8, cvdecay=4, miVerb=0.55, mverbfreeze=sinvar([0, 0.8], 32), spectralfreeze=sinvar([0, 0.5], 24), stereowidth=0.88, hpf=80)
m1 >> darkpad([0, -5], dur=16, sus=17, oct=5, amp=0.45, cutoff=linvar([600, 3200], 48), res=0.4, detune=0.35, dark=0.7, sub=0.4, cheapverb=0.65, cvdecay=2.5, hpf=180)
s1.djf = linvar([0.15, 0.72], 40)
s1.amp = linvar([0.4, 0.9], 40)
s1.jpsize = linvar([0.92, 0.98], 40)

#@peak(64)
Root.default = "Bb"
d1 >> compkick(0, dur=1, oct=3, amp=1.15, punch=1.0, comp=0.98, click=0.6, sub=0.95, body=0.85, tone=0.5)
d2 >> click(0, dur=1/2, sus=0.04, amp=[0, 0.42, 0, 0.36], rate=15, hpf=2700, pan=[0.1, -0.1])
b1 >> pumpbass([0, 0, -5, -5, 0, 3, -7, -5, 0, 0, -3, -5], dur=PDur(7, 12), sus=PDur(7, 12)*0.8, oct=4, amp=2.0, cutoff=linvar([550, 1500], 32), res=0.65, sub=0.9, body=0.75, growl=0.6, tape=0.7, tapedrive=2.0, multicrush=0.35, hpf=60)
b1.amp = 2.0 * var([0.2, 1, 1, 1], 1)
s1 >> hardstab([(0,3,7), (0,3,7), (-1,2,6), (3,7,10), (0,3,7), (-4,-1,3), (-2,1,5), (-2,1,5)], dur=var([2,1,1,2],2.5), sus=[0.14, 0.22, 0.1, 0.18], oct=5, amp=0.8, cutoff=2900, res=0.55, comp=6, detune=0.025, fold=0.5, feedback=0.4, hpf=220, tubedrive=0.7, tubegain=2.2, tubewarm=0.6, tubebias=0.2, tape=0.55, tapedrive=1.7, fbdelay=0.62, fbtime=0.375, fbfeed=0.78, fbcutoff=3200, fbspread=0.02, beat_dur=1, stereowidth=0.92)
s1.jpverb = var([0, 0.6, 0.6, 0.6], 1)
s1.amp = 0.8 * var([0.3, 1, 1, 1], 1)
g1 >> sawbass([-7, -7, -10, -7, -5, -3, -7, -5], dur=var([4,2,2,4],[6,4,4,2]), sus=[0.85, 0.55, 1.1, 0.7], oct=4, amp=0.6, cutoff=sinvar([380, 1000], 16), rq=0.35, tubedrive=0.7, tubegain=2.2, tubewarm=0.55, tubebias=0.2, tape=0.55, tapedrive=1.9, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=2500, fbspread=0.03, beat_dur=1, hpf=110)
g1.amp = 0.6 * var([0.3, 1, 1, 1], 1)
l1 >> darklead(PRand([0, 3, 5, 7, 10, -2]), dur=PDur(5, 8), sus=[0.35, 0.2, 0.5, 0.3], oct=5, amp=0.45, cutoff=linvar([1500, 3500], 16), res=0.55, detune=0.3, width=0.4, sub=0.3, hpf=400, tubedrive=0.5, tubegain=1.6, tubewarm=0.55, tubebias=0.1, tape=0.4, tapedrive=1.4, fbdelay=0.45, fbtime=0.25, fbfeed=0.65, fbcutoff=3500, fbspread=0.02, beat_dur=1, jpverb=0.5, jpsize=0.85, jpdamp=0.4, stereowidth=0.85)
l1.amp = 0.45 * var([0.35, 1, 1, 1], 1)
c1 >> industrialsnare(0, dur=2, delay=1, oct=5, amp=0.75, tone=0.18, noise=0.95, rattle=0.55, ring=0.45, bend=0.4, snap=0.6, comp=0.75, hpf=260, jpverb=0.7, jpsize=0.88, jpdamp=0.4, pan=PRand([-0.12, 0.12]))
h1 >> click(0, dur=1/4, sus=0.014, amp=Pacc("ghost"), amplify=0.25, rate=18, hpf=5200, pan=PRand([-0.35, 0.35]))
t1 >> compperc(PRand([0, 5, 7, 12, -3, 9]), dur=PDur(9, 16), sus=0.08, amp=0.38, tone=0.35, noise=0.55, body=0.25, metal=0.5, ring=0.4, comp=0.55, hpf=950, cheapverb=0.4, pan=PRand([-0.55, -0.2, 0.2, 0.55]))
t1.amp = 0.38 * var([0.4, 1, 1, 1], 1)
p1.amp = linvar([0.7, 0.4], 16)
m1.amp = linvar([0.45, 0.25], 16)

#@outro(32)
Root.default = "G"
l1.stop()
g1.stop()
s1.amp = linvar([0.8, 0], 28)
b1.amp = linvar([2.0, 0], 32)
c1.amp = linvar([0.75, 0], 24)
t1.amp = linvar([0.38, 0], 24)
h1.amp = linvar([0.25, 0], 18)
m1.amp = linvar([0.25, 0], 28)
p1.amp = linvar([0.4, 0], 32)
d2.amp = linvar([0.4, 0], 26)
d1.amp = linvar([1.15, 0.7, 0], [16, 12, 4])

#@endfade(16)
