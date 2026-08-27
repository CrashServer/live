# tabation_var — D minor rock, 122 BPM

#@#@ TABATION
_seq_cancel()
Clock.bpm = 122
Scale.default = "minor"
Root.default = "D"

#@intro(16)
b1 >> pumpbass([0, 0, -2, 0, 3, 0, 4, 3], dur=PDur(7, 8), sus=PDur(7, 8)*0.85, oct=4, amp=1.8,
    cutoff=linvar([400, 1200], 32), res=0.3, sub=0.2, body=8, growl=0.15,
    tape=var([0, 0.3, 0, 0.5], [8, 4, 8, 4]), tapedrive=1.2, hpf=60)
p1 >> darkpad([0, -2], dur=8, sus=10, oct=4, amp=0.6,
    cutoff=linvar([300, 1800], 48), res=0.3, detune=0.4, dark=0.8,
    cheapverb=var([0.4, 0.7], [8, 8]), cvdecay=3.5, hpf=120)

#@groove(32)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=3, comp=0.8, click=0.6, sub=1, body=20,
    tone=var([0.5, 0.7], [16, 16]), tape=0.3, tapedrive=1.5, tapewarm=0.4)
d2 >> industrialsnare(0, dur=1, amp=[0.1, 0.8, 0.1, 0.8],
    tone=0.6, noise=0.4, comp=0.6, drive=var([0, 0.3], [16, 16]),
    ring=0.2, snap=0.7, hpf=200)
d3 >> dthihat(0, dur=1/4, amp=Pacc("ghost")*2, beat_dur=0.25, blur=0.02,
    atk=0.001, decay=0.08, rel=0.05, hpf=6000)
b1 >> pumpbass([0, 0, -2, 0, 3, 0, 4, 3], dur=PDur(7, 8), sus=PDur(7, 8)*0.85, oct=4, amp=2,
    cutoff=sinvar([600, 1800], 32), res=0.25, sub=0.15, body=12, growl=0.2,
    tape=var([0.2, 0.5], [16, 16]), tapedrive=1.4, hpf=60)
c1 >> cs80(var([(0,2,4), (-1,1,3), (-2,0,2), (-1,1,3)], 8), dur=2, sus=var([1.8, 2.5], [16, 16]),
    oct=4, amp=0.55, atk=0.1, rel=0.4, cutoff=linvar([800, 2400], 64),
    detune=0.3, vibspeed=5, vibdepth=var([0, 0.3], [16, 16]),
    fuzz=var([0, 0.4, 0, 0.6], [8, 8, 8, 8]),
    cheapverb=0.45, cvdecay=1.8, hpf=150)

#@rise(16)
l1 >> faim([0, -2, 4, 3, 0, 4, 3, -2], dur=PDur(5, 8), sus=PDur(5, 8)*0.7,
    oct=5, amp=lininf(0, 0.7, 16), atk=0.02, decay=0.15, rel=0.3, peak=0.8,
    hpf=linvar([1200, 180], 16), lpf=linvar([1500, 8000], 16),
    cheapverb=0.35, cvdecay=1.2).unison(2)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=4, comp=0.9, click=0.65, sub=1, body=24,
    tone=linvar([0.5, 0.9], 16), tape=0.4, tapedrive=1.6, tapewarm=0.45)

#@hit(32)
l1 >> faim([0, -2, 4, 3, 0, 4, 3, 4], dur=PDur(5, 8), sus=PDur(5, 8)*0.75,
    oct=5, amp=0.75, atk=0.015, decay=0.12, rel=0.25, peak=0.9,
    hpf=200, lpf=sinvar([3000, 9000], 32),
    cheapverb=var([0.3, 0.5], [16, 16]), cvdecay=1.5).unison(2)
s1 >> svdk(var([(0,2,4), (-1,1,3), (-2,0,2), (-1,1,3)], 8), dur=4, sus=var([3.5, 5], [16, 16]),
    oct=4, amp=0.45, blur=0.4, beat_dur=4,
    grit=var([0, 0.3, 0, 0.6], [8, 4, 8, 4]),
    cheapverb=0.5, cvdecay=2.5, hpf=180)

#@break(16)
d1.stop()
d2.stop()
d3.stop()
l1.stop()
c1.stop()
s1.stop()
b1 >> pumpbass([0, -2, 3, 4], dur=PDur(5, 8), sus=PDur(5, 8)*0.9, oct=4, amp=1.5,
    cutoff=sinvar([300, 900], 16), res=0.5, sub=0.3, body=6, growl=0.35,
    tape=0.6, tapedrive=1.3, hpf=55)
p1 >> darkpad([0, -2, -5], dur=var([8, 4, 4], 16), sus=var([9, 5, 5], 16),
    oct=4, amp=0.7, cutoff=linvar([500, 2800], 16), res=0.4,
    detune=0.5, dark=0.9, shimmer=var([0, 0.5, 0, 0.7], [4, 4, 4, 4]),
    cheapverb=0.6, cvdecay=4, hpf=100)

#@fire(32)
Root.default = "F"
d1 >> compkick(0, dur=1, oct=3, amp=1, punch=5, comp=1, click=0.8, sub=1.2, body=28,
    tone=var([0.6, 0.9, 0.6, 1.1], [8, 4, 8, 4]), tape=0.5, tapedrive=1.8, tapewarm=0.5)
d2 >> industrialsnare(0, dur=1, amp=[0.15, 0.9, 0.15, 0.9],
    tone=0.7, noise=0.5, comp=0.7, drive=var([0.2, 0.5], [16, 16]),
    ring=0.3, rattle=0.2, snap=0.8, hpf=200)
d3 >> dthihat(0, dur=1/4, amp=Pacc("ghost")*2, beat_dur=0.25, blur=0.02,
    atk=0.001, decay=0.07, rel=0.04, hpf=7000)
b1 >> pumpbass([0, 0, -2, 0, -3, 0, 3, 4], dur=PDur(7, 8), sus=PDur(7, 8)*0.8, oct=4, amp=2.2,
    cutoff=sinvar([700, 2200], 24), res=0.3, sub=0.2, body=14, growl=0.3,
    tape=var([0.4, 0.7], [16, 16]), tapedrive=1.6, hpf=60)
l2 >> darklead([0, -2, 3, 0, 4, 3, -2, 4], dur=PDur(7, 12), sus=PDur(7, 12)*0.7,
    oct=5, amp=0.8, atk=0.02, rel=0.4, cutoff=sinvar([1000, 5000], 32), res=0.5,
    drive=var([0.3, 0.7, 0.3, 1.0], [8, 8, 8, 8]),
    fuzz=var([0, 0.5, 0.3, 0.8], [8, 4, 4, 4]),
    cheapverb=0.4, cvdecay=1.5, hpf=250).unison(2)
c1 >> cs80(var([(0,2,4), (-1,1,3), (-2,0,2), (-1,1,3)], 8), dur=2, sus=var([1.5, 2.2], [16, 16]),
    oct=4, amp=0.5, atk=0.08, rel=0.35, cutoff=sinvar([1000, 3500], 32),
    detune=0.4, vibspeed=6, vibdepth=var([0, 0.4], [16, 16]),
    fuzz=var([0.3, 0.6, 0.3, 0.8], [8, 4, 4, 4]),
    cheapverb=0.4, cvdecay=1.6, hpf=150)

#@close(16)
Root.default = "D"
d1.stop()
d2.stop()
d3.stop()
l2.stop()
c1.stop()
b1 >> pumpbass([0, -2, 3, 4], dur=PDur(5, 8), sus=PDur(5, 8)*0.85, oct=4,
    amp=linvar([1.8, 0], 16), cutoff=linvar([1400, 300], 16), res=0.3,
    sub=0.2, body=8, growl=0.1, tape=0.4, tapedrive=1.2, hpf=55)
p1 >> darkpad([0, -2], dur=8, sus=10, oct=4, amp=linvar([0.5, 0], 16),
    cutoff=linvar([1800, 300], 16), res=0.3, detune=0.4, dark=0.8,
    shimmer=var([0.3, 0.7, 0.5, 0.8], [4, 4, 4, 4]),
    cheapverb=0.7, cvdecay=5, hpf=100)
