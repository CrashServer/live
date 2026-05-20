# recorded_072851
# recorded

#@intro(16)
Clock.bpm = 130
Scale.default = "minor"
Root.default = "E"
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@build(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=0.9, click=0.65, sub=1, body=4, tone=0.5, tape=0.5, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1)

#@peak(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=0.9, click=0.65, sub=1, body=36, tone=[0.6, 0.8, 0.6, 0.6])

#@break(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=var([1, 0], [28, 4]), click=0.65, sub=1, body=36, tone=0.5, echo=0.5)

#@drop(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=1, click=0, sub=1, body=34, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@outro(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=0, comp=1, click=12, fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=1000, fbspread=0.20, beat_dur=1, sub=0, body=16, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part7(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part8(8)
d2 >> click(0, dur=1/2, sus=0.1, amp=[0, 0.35], rate=24, hpf=2400, pan=0.1, leg=1, mverb=0.5)

#@part9(16)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part10(8)
~d1 >> compkick(PRand([0, 5, 7, 12]), dur=1, oct=3, amp=0.40, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=12, mverb=0.5, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part11(16)
c1 >> industrialsnare(0, dur=2, delay=1, oct=5, amp=1, tone=0.2, noise=0.85, rattle=0.45, ring=0.35, bend=0.3, snap=0.55, comp=0.7, hpf=250, jpverb=0.75, jpsize=0.88, jpdamp=0.4, pan=PRand([-0.1, 0.1]))

#@part12(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part13(16)
e6 >> hardstab([(0,3,7), (0,3,7), (-2,1,5), (0,3,7)], dur=var([2,1,2,1],4), sus=[0.4, 0.75, 0.85, 1], oct=5, amp=0.9, cutoff=2200, res=0.45, comp=5, detune=0.015, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, hpf=180)
e1 >> compperc(PRand([0, 5, 7, 12]), dur=PDur(5, 16), sus=0.38, amp=4, tone=4, noise=4, body=1.5, metal=1.9, ring=0.35, comp=0.4, hpf=100, cheapverb=0.4, pan=PRand([-0.5, -0.2, 0.2, 0.5]))

#@part14(16)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part15(16)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part16(8)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part17(8)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part18(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(5,8), sus=PDur(5,8)*0.8, oct=6, amp=2, cutoff=sinvar([500, 1100], 32), res=0.1, sub=0, body=8, growl=0.2, pumper=.1, pumprate=0, tape=1.7, tapedrive=1.4)

#@part19(16)
h2 >> click(0, dur=1/4, sus=0.015, amp=Pacc("ghost")*4, rate=18, hpf=5500, pan=PRand([-0.3, 0.3]))

#@part20(8)
r7 >> play("X ", lpf=[800, 1600, 400, 0])

#@part21(4)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)

#@part22(8)
b1 >> pumpbass([0, 0, -5, -5, 0, 0, -7, -5], dur=PDur(5,8), sus=PDur(5,8)*0.75, oct=4, amp=1.8, cutoff=sinvar([380, 900], 32), res=0.6, sub=0.0, body=1.2, growl=0, tape=0.9, tapedrive=0.8, hpf=55)
b1 >> pumpbass([0, 0, -5, -5, 0, 3, -7, -5, 0, 0, -3, -5], dur=PDur(7, 12), sus=PDur(7, 12)*0.8, oct=4, amp=2.0, cutoff=linvar([550, 1500], 32), res=0.65, sub=0.0, body=0.75, growl=0.6, tape=0.7, tapedrive=2.0, multicrush=0.35, hpf=60)

#@part23(16)
d1 >> compkick(0, dur=1, oct=3, amp=1.0, punch=0.95, comp=0.95, click=0.75, sub=0.85, body=0.7, tone=0.55)
d2 >> click(0, dur=1/2, sus=0.04, amp=[0, 0.42, 0, 0.38], rate=15, hpf=2600, pan=[0.1, -0.1])
d1 >> compkick(0, dur=1, oct=3, amp=1.05, punch=0.95, comp=0.95, click=0.5, sub=0.9, body=0.8, tone=0.45)
g4 >> subbass([0, 0, -5, 0], dur=8, sus=5, oct=5, amp=1.8, lpf=220, lpr=0.25, hpf=40, tape=0.5, tapedrive=1.5)
c1 >> industrialsnare(0, dur=2, delay=1, oct=5, amp=0.65, tone=0.2, noise=0.9, rattle=0.5, ring=0.4, bend=0.35, snap=0.55, comp=0.7, hpf=260, jpverb=0.72, jpsize=0.88, jpdamp=0.4, pan=PRand([-0.12, 0.12]))

#@part24(32)
p1 >> industrialdrone([0, -5, -7, 0, -3], dur=16, sus=17, oct=4, amp=0.7, cutoff=linvar([240, 2100], 40), res=0.6, detune=0.45, noise=0.35, sub=0.55, feedback=0.4, cheapverb=0.8, cvdecay=4, miVerb=0.55, mverbfreeze=sinvar([0, 0.8], 32), spectralfreeze=sinvar([0, 0.5], 24), stereowidth=0.88, hpf=80)
Clock.clear()
soff()
Server.clearFx()

#@part25(16)
rec_stop()

#@endfade(16)
