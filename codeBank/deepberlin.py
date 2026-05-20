# deep berlin — hypnotic techno 7-part journey
# techno

Clock.bpm = 130
Scale.default = "minor"
Root.default = "E"

#@intro(32)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=0.85, comp=0.9, click=0.65, sub=0.75, body=0.65, tone=0.5)
d2 >> click(0, dur=1/2, sus=0.04, amp=[0, 0.35], rate=14, hpf=2400, pan=0.1)

#@sub(32)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(5,8), sus=PDur(5,8)*0.8, oct=4, amp=0.8, cutoff=sinvar([500, 1100], 32), res=0.5, sub=0.75, body=0.55, growl=0.4, pumper=0.55, pumprate=4, tape=0.4, tapedrive=1.4)

#@stab(32)
s1 >> hardstab([(0,3,7), (0,3,7), (-2,1,5), (0,3,7)], dur=var([4,2,4,2],4), sus=[0.12, 0.18, 0.1, 0.15], oct=5, amp=0.5, cutoff=2200, res=0.45, comp=5, detune=0.015, fold=0.3, feedback=0.25, hpf=180, dubdelay=0.55, dublen=0.375, dubfeed=0.72, jpverb=0.6, jpsize=0.92, jpdamp=0.35, stereowidth=0.85)

#@detail(32)
h1 >> space(PRand([0,3,5,7,10]), dur=PDur(3,8), sus=0.35, oct=6, amp=0.3, rq=0.04, cheapverb=0.6, cvdecay=2.2, hpf=600, pan=PRand([-0.6,-0.3,0.3,0.6]))
g1 >> sawbass([-7, -7, -10, -7], dur=var([8,4,12,8],4), sus=[1.4, 0.9, 1.8, 1.1], oct=4, amp=0.45, cutoff=sinvar([450,900],16), rq=0.35, fuzz=0.55, fuzzgain=1.8, fuzztone=0.5, fuzzoctave=0.2, tape=0.4, tapedrive=1.6, dubdelay=0.35, dublen=0.25, dubfeed=0.55, pumper=0.4, pumprate=4)

#@break(64)
d1.amp = 0
d2.amp = linvar([0.35, 0.12, 0.22], [16, 32, 16])
b1.amp = linvar([0.8, 0, 0.3], [8, 40, 16])
p1 >> industrialdrone([0, -5, 0, 3], dur=16, sus=17, oct=4, amp=0.5, cutoff=linvar([280, 2400], 48), res=0.55, detune=0.4, noise=0.3, sub=0.5, feedback=0.35, cheapverb=0.75, cvdecay=3.5, miVerb=0.5, mverbfreeze=linvar([0, 0.7, 0], [24, 16, 24]), stereowidth=0.85)
s1.djf = linvar([0.18, 0.68], 56)
s1.amp = linvar([0.35, 0.8], 48)
s1.jpsize = linvar([0.92, 0.98], 48)
g1.amp = linvar([0.45, 0.15, 0.55], [16, 24, 24])

#@peak(64)
Root.default = "G"
d1 >> compkick(0, dur=1, oct=3, amp=1.0, punch=0.95, comp=0.95, click=0.75, sub=0.85, body=0.7, tone=0.55)
d2 >> click(0, dur=1/2, sus=0.04, amp=[0, 0.42, 0, 0.38], rate=15, hpf=2600, pan=[0.1, -0.1])
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=4, amp=0.85, cutoff=linvar([700, 1600], 32), res=0.6, sub=0.8, body=0.65, growl=0.5, pumper=0.6, pumprate=4, tape=0.55, tapedrive=1.7)
s1 >> hardstab([(0,3,7), (0,3,7), (-2,1,5), (3,7,10), (0,3,7), (-4,-1,3), (0,3,7), (-2,1,5)], dur=var([4,2,2,2,4],3.5), sus=[0.11, 0.16, 0.09, 0.13], oct=5, amp=0.75, cutoff=2800, res=0.5, comp=6, detune=0.02, fold=0.4, feedback=0.3, hpf=200, dubdelay=0.62, dublen=0.375, dubfeed=0.78, jpverb=0.55, jpsize=0.9, jpdamp=0.35, stereowidth=0.92)
g1 >> sawbass([-7, -7, -5, -10, -7, -3, -7, -5], dur=var([4,2,2,4],[6,4,4,2]), sus=[0.9, 0.6, 1.2, 0.8], oct=4, amp=0.55, cutoff=sinvar([400, 1100], 16), rq=0.35, fuzz=0.7, fuzzgain=2.2, fuzztone=0.6, fuzzoctave=0.3, tape=0.55, tapedrive=1.9, dubdelay=0.45, dublen=0.25, pumper=0.5, pumprate=4)
h1.amp = 0.35
h1.cutoff = linvar([2400, 4200], 32)
p1.amp = linvar([0.5, 0.25], 16)

#@outro(32)
Root.default = "E"
g1.stop()
s1.amp = linvar([0.75, 0], 28)
b1.amp = linvar([0.85, 0], 32)
h1.amp = linvar([0.35, 0], 20)
p1.amp = linvar([0.25, 0], 32)
d2.amp = linvar([0.4, 0], 28)
d1.amp = linvar([1.0, 0.6, 0], [16, 12, 4])

#@endfade(16)
