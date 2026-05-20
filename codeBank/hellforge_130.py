# hellforge 130
# dark, industrial, banger, gesaffelstein
# F# minor, hammering 4/4 industrial. pumpbass growl + sidechain pump,
# hardstab with full tube cascade + jpverb plate, industrialdrone with
# spectralfreeze pulses, Reese sawbass, industrialsnare claps.
# Tape-stop trigger before re-explode.

Clock.bpm = 130
Scale.default = "minor"
Root.default = "F#"

#@forge(32) — subbass alone, 4/4 hammer kick

d1 >> compkick(0, dur=1, oct=3, amp=1.1, punch=0.95, comp=0.95, click=0.55, sub=0.95, body=0.85, tone=0.45, tape=0.6, tapedrive=1.5)
b1 >> subbass([0, 0, -5, 0], dur=8, sus=8, oct=4, amp=1.6, lpf=220, lpr=0.25, hpf=40, tape=0.55, tapedrive=1.6)

#@pulse(32) — pumpbass walks with growl + sidechain pump, click hat enters

b1 >> pumpbass([0, 0, -5, -5, 0, 0, -7, -5], dur=PDur(5, 8), sus=PDur(5, 8)*0.75, oct=4, amp=1.85, cutoff=sinvar([380, 920], 32), res=0.6, sub=0.85, body=0.7, growl=0.55, pumper=linvar([0.3, 0.85], 48), pumprate=2, tape=0.6, tapedrive=1.8, multicrush=0.25, hpf=55)
d2 >> click(0, dur=1/2, sus=0.04, amp=[0, 0.32], rate=13, hpf=2400, pan=0.1)

#@cold(48) — hardstab metallic 7th chords, full tube cascade + jpverb plate

s1 >> hardstab([(0, 3, 7), (0, 3, 7), (-1, 2, 6), (0, 3, 7), (-2, 1, 5), (-2, 1, 5), (-4, -1, 3), (0, 3, 7)], dur=var([2, 1, 1, 2, 2, 2, 2, 2], 3), sus=[0.18, 0.35, 0.12, 0.4], oct=5, amp=0.6, cutoff=2400, res=0.5, comp=6, detune=0.025, fold=0.45, feedback=0.4, hpf=220, tubedrive=0.6, tubegain=1.9, tubewarm=0.65, tubebias=0.18, tape=0.5, tapedrive=1.6, fbdelay=0.55, fbtime=0.375, fbfeed=0.78, fbcutoff=3000, fbspread=0.02, beat_dur=1, stereowidth=0.88, wshape=5, wgain=1, wmix=0.35)
h1 >> click(0, dur=1/4, sus=0.014, amp=Pacc("ghost"), amplify=0.22, rate=18, hpf=5200, pan=PRand([-0.35, 0.35]))

#@drone(32) — industrialdrone enters with spectralfreeze + miVerb pulses

p1 >> industrialdrone([0, -5, -7, 0, -3], dur=16, sus=17, oct=4, amp=0.7, cutoff=linvar([240, 2100], 40), res=0.6, detune=0.45, noise=0.35, sub=0.55, feedback=0.4, cheapverb=0.8, cvdecay=4, miVerb=0.55, spectralfreeze=sinvar([0, 0.5], 24), stereowidth=0.88, hpf=80)
m1 >> darkpad([0, -5], dur=16, sus=17, oct=5, amp=0.4, cutoff=linvar([600, 3200], 48), res=0.4, detune=0.35, dark=0.7, sub=0.4, cheapverb=0.6, cvdecay=2.5, hpf=180)

#@peak(64) — Reese sawbass + darklead + industrialsnare claps + compperc ride

Root.default = "A"

d1 >> compkick(0, dur=1, oct=3, amp=1.18, punch=1.0, comp=0.98, click=0.6, sub=0.95, body=0.85, tone=0.5, tape=0.65, tapedrive=1.7)
b1 >> pumpbass([0, 0, -5, -5, 0, 3, -7, -5, 0, 0, -3, -5], dur=PDur(7, 12), sus=PDur(7, 12)*0.8, oct=4, amp=2.0, cutoff=linvar([550, 1500], 32), res=0.65, sub=0.9, body=0.75, growl=0.6, pumper=linvar([0.4, 0.9], 32), pumprate=2, tape=0.7, tapedrive=2.0, multicrush=0.35, transient=var([0.5, 3, 6], [8, 4, 4]), transattack=linvar([0.5, 3], 32), hpf=60)
g1 >> sawbass([-7, -7, -10, -7, -5, -3, -7, -5], dur=var([4, 2, 2, 4], [6, 4, 4, 2]), sus=[0.85, 0.55, 1.1, 0.7], oct=4, amp=0.6, cutoff=sinvar([380, 1000], 16), rq=0.35, tubedrive=0.7, tubegain=2.2, tubewarm=0.55, tubebias=0.2, tape=0.55, tapedrive=1.9, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=2500, fbspread=0.03, beat_dur=1, hpf=110)
l1 >> darklead(PRand([0, 3, 5, 7, 10, -2]), dur=PDur(5, 8), sus=[0.35, 0.2, 0.5, 0.3], oct=5, amp=0.48, cutoff=linvar([1500, 3500], 16), res=0.55, detune=0.3, width=0.4, sub=0.3, hpf=400, tubedrive=0.55, tubegain=1.7, tubewarm=0.55, tubebias=0.12, tape=0.45, tapedrive=1.5, fbdelay=0.45, fbtime=0.25, fbfeed=0.65, fbcutoff=3500, fbspread=0.02, beat_dur=1, stereowidth=0.85)
c1 >> industrialsnare(0, dur=2, delay=1, oct=5, amp=0.78, tone=0.18, noise=0.95, rattle=0.55, ring=0.45, bend=0.4, snap=0.6, comp=0.75, hpf=260, pan=PRand([-0.12, 0.12]))
t1 >> compperc(PRand([0, 5, 7, 12, -3, 9]), dur=PDur(9, 16), sus=0.08, amp=0.4, tone=0.35, noise=0.55, body=0.25, metal=0.5, ring=0.4, comp=0.55, hpf=950, cheapverb=0.4, pan=PRand([-0.55, -0.2, 0.2, 0.55]))
d2 >> click(0, dur=1/2, sus=0.04, amp=[0, 0.42, 0, 0.36], rate=15, hpf=2700, pan=[0.1, -0.1])
s1 >> hardstab([(0, 3, 7), (0, 3, 7), (-1, 2, 6), (3, 7, 10), (0, 3, 7), (-4, -1, 3), (-2, 1, 5), (-2, 1, 5)], dur=var([2, 1, 1, 2], 2.5), sus=[0.14, 0.22, 0.1, 0.18], oct=5, amp=0.85, cutoff=2900, res=0.55, comp=6, detune=0.028, fold=0.55, feedback=0.45, hpf=220, tubedrive=0.75, tubegain=2.3, tubewarm=0.6, tubebias=0.22, tape=0.55, tapedrive=1.8, fbdelay=0.62, fbtime=0.375, fbfeed=0.8, fbcutoff=3200, fbspread=0.02, beat_dur=1, stereowidth=0.92, wshape=6, wgain=1.2, wmix=0.45)
p1 >> industrialdrone([0, -5, -7, 0, -3], dur=16, sus=17, oct=4, amp=0.55, cutoff=linvar([240, 2100], 40), res=0.6, detune=0.45, noise=0.35, sub=0.55, feedback=0.45, cheapverb=0.8, cvdecay=4, miVerb=0.55, spectralfreeze=sinvar([0, 0.5], 24), stereowidth=0.88, hpf=80)

#@stop(8) — TAPE STOP signature: trigger Server.addFx for global slowdown
# Server.addFx(tstop=1, tstoptime=4)   ## live trigger — comment lives, eval the line below
# Server.addFx(tstop=1, tstoptime=8)   ## softer stop variant

#@reexplode(64) — Root drops to E for the second drop, vati descending stab + cs80 chaos

Root.default = "E"

v1 >> vati([11, 10, 9, 8, 7, 4, 3, 0], dur=0.25, oct=6, cutoff=linvar([800, 4000], 8), amp=var([0, 0.7], [24, 8]), leg=0)
n1 >> cs80([0, 0, 0.5, 3], dur=0.5, oct=(3, PStep(4, 3, 4)), amp=var([0.35, 0.55], [16, 16]), cutoff=linvar([400, 5000], 8), shape=0.15, shimmer=linvar([0, 0.5], 32), shimsize=0.8, shimmix=0.4)
b1 >> pumpbass([0, 0, -5, -5, 0, 3, -7, -5, 0, 0, -3, -5], dur=PDur(7, 12), sus=PDur(7, 12)*0.8, oct=4, amp=2.1, cutoff=linvar([650, 1700], 32), res=0.7, sub=0.95, body=0.8, growl=0.65, pumper=linvar([0.5, 0.95], 32), pumprate=2, tape=0.75, tapedrive=2.2, multicrush=0.4, transient=4, transattack=2, hpf=60)
g1 >> sawbass([-7, -7, -10, -7, -5, -3, -7, -5], dur=var([4, 2, 2, 4], [6, 4, 4, 2]), sus=[0.85, 0.55, 1.1, 0.7], oct=4, amp=0.7, cutoff=sinvar([400, 1200], 16), rq=0.35, tubedrive=0.8, tubegain=2.4, tubewarm=0.55, tubebias=0.22, tape=0.6, tapedrive=2.0, fbdelay=0.5, fbtime=0.25, fbfeed=0.72, fbcutoff=2700, fbspread=0.03, beat_dur=1, hpf=110)
l1 >> darklead(PRand([0, 3, 5, 7, 10, -2, 12]), dur=PDur(5, 8), sus=[0.35, 0.2, 0.5, 0.3], oct=5, amp=0.55, cutoff=linvar([1500, 4000], 16), res=0.6, detune=0.35, width=0.45, sub=0.3, hpf=400, tubedrive=0.6, tubegain=1.8, tubewarm=0.55, tubebias=0.14, tape=0.5, tapedrive=1.6, fbdelay=0.45, fbtime=0.25, fbfeed=0.7, fbcutoff=3800, fbspread=0.02, beat_dur=1, stereowidth=0.88)
d1 >> compkick(0, dur=1, oct=3, amp=1.22, punch=1.05, comp=1.0, click=0.65, sub=1.0, body=0.9, tone=0.55, tape=0.7, tapedrive=1.9)

#@outro(48) — strip everything, drone fades through spectralfreeze, kick last to die

v1.stop()
n1.stop()
l1.stop()
g1.stop()
s1.stop()
c1.stop()
t1.stop()
h1.stop()
d2.stop()

m1 >> darkpad([0, -5], dur=16, sus=17, oct=5, amp=linvar([0.4, 0], 32), cutoff=linvar([600, 200], 48), res=0.4, detune=0.35, dark=0.9, sub=0.4, cheapverb=linvar([0.6, 0.95], 32), cvdecay=5, hpf=180)
p1 >> industrialdrone([0, -5, -7, 0, -3], dur=16, sus=17, oct=4, amp=linvar([0.55, 0], 40), cutoff=linvar([2100, 200], 40), res=0.6, detune=0.45, noise=0.35, sub=0.55, feedback=linvar([0.4, 0.7], 40), cheapverb=0.9, cvdecay=6, miVerb=0.7, spectralfreeze=linvar([0.3, 1], 32), stereowidth=0.88, hpf=80)
b1 >> pumpbass([0, 0, -5, -5, 0, 0, -7, -5], dur=PDur(5, 8), sus=PDur(5, 8)*0.75, oct=4, amp=linvar([1.85, 0], 32), cutoff=linvar([900, 200], 32), res=0.6, sub=0.85, body=0.7, growl=0.4, pumper=0.3, tape=0.6, tapedrive=1.6, multicrush=linvar([0.3, 0], 24), hpf=55)
d1 >> compkick(0, dur=1, oct=3, amp=linvar([1.18, 0], 24), punch=0.9, comp=0.95, click=0.5, sub=0.9, body=0.8, tone=0.45)

#@endfade(16)

m1.stop()
p1.stop()
b1.stop()
d1.stop()
