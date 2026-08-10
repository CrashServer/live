# pump 133
# live2026_aube

#@intro(16)
Clock.bpm = 133
Scale.default = "minor"
Root.default = "E"

#@build(16)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.5, fbfeed=0.5, fbcutoff=4000, fbspread=0.02, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, apan=1, awidth=1, apwave=1, beat_dur=1, pumprate=0, tape=0.2, tapedrive=1.7)

#@peak(16)
~b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.4, tapedrive=1.7)

#@break(8)
~b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.4, tapedrive=1.7).only()

#@drop(16)
b1 >> pumpbass(P*[0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur([7],12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.1, sub=0.1, body=4, rgate=0.1, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, hpf=240, tapedrive=1.7).every(4, "stutter", degree=4, mverb=0.3)

#@outro(16)
~b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=7, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5,  fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.4, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@part7(16)
b1.degree=[0, 0, 3, 0, -3, 0, 5, 5, 7, -3, 5, 3]

#@part8(16)
b1 >> pumpbass(P*[0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur([7],12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.1, sub=0.1, body=4, rgate=0.1, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7).every(4, "stutter", degree=5, mverb=0.0)

#@part9(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=0, comp=1, click=12, fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=1000, fbspread=0.20, beat_dur=1, sub=0, body=16, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part10(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part11(8)
d2 >> click(0, dur=1/2, sus=0.1, amp=[0, 0.35], rate=24, hpf=2400, pan=0.1, leg=1, mverb=0.5)

#@part12(16)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part13(8)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.5, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part14(16)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=-0.08, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part15(16)
~b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.4, tapedrive=1.7)

#@part16(16)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([2, 1.1], 32), echo=0.5)

#@part17(8)
~d1 >> compkick(0, dur=1, oct=2, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.75, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([1, 1.1], 32), echo=0.5)

#@part18(8)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=24, tone=linvar([1, 1.1], 32), echo=0.5)

#@part19(16)
~d1 >> compkick(PRand([0, 5, 7, 12]), dur=1, oct=5, amp=0.40, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=12, mverb=0.5, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part20(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(5,8), sus=PDur(5,8)*0.8, oct=6, amp=1.2, cutoff=sinvar([500, 1100], 32), res=0.1, sub=0, body=8, growl=0.2, pumper=.1, pumprate=0, tape=1.7, tapedrive=1.4, high=2, leg=4, csweep=0.1, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part21(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(5,8), sus=PDur(5,8)*0.8, oct=6, amp=1.2, cutoff=sinvar([500, 1100], 32), res=0.1, sub=0, body=8, growl=0.2, pumper=.1, pumprate=0, tape=1.7, tapedrive=1.4, high=2, leg=4, csweep=0.0, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part22(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part23(16)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part24(8)
~b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(5,8), sus=PDur(5,8)*0.8, oct=6, amp=1.2, cutoff=sinvar([500, 1100], 32), res=0.1, sub=0, body=8, growl=0.1, pumper=.1, pumprate=1, tape=1.7, tapedrive=1.4, high=2, leg=4, resonbank=0.2, rbfreq=96, rbdecay=0.5, rbspread=1.0)

#@part25(32)
e9 >> tb304([0, 0, 3, 0, rest(), 0, 5, 0, 0,rest(), 0, 3], dur=1/4, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1,amp=4, shape=0, shapemix=0.5, oct=(4, 5), hpf=1200, mverb=0.2)

#@part26(4)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part27(8)
h2 >> click(0, dur=1/4, sus=0.015, amp=Pacc("ghost")*4, rate=18, hpf=5500, pan=PRand([-0.3, 0.3]))

#@part28(8)
e9.amp=0.9

#@part29(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1, resonbank=0.2, rbfreq=150, rbdecay=0.5, rbspread=1.0)

#@part30(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=2.0, pumper=0.1, pumprate=3, tape=1.8, tapedrive=1, reasonbank=0)

#@part31(16)
e9 >> plaitsX([0, 0, 3, 0, rest(), 0, 5, 0, 0, rest(), 0, 3], dur=1/4, amp=4, shape=1, shapemix=0.5, oct=6, hpf=1200, mverb=0.5, pan=PWhite(-1, 1))

#@part32(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.2, sub=0, body=128, growl=0.0, pumper=0.1, pumprate=3, tape=2.1, tapedrive=1)

#@part33(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=1, growl=0.0, pumper=0.1, pumprate=3, tape=2.4, tapedrive=1)

#@part34(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=160, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=8, pumprate=3, tape=1.7, tapedrive=1)

#@part35(4)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)

#@part36(8)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)
d2.stop()

#@part37(16)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=7, amp=2, cutoff=linvar([700, 1700], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.4, beat_dur=1, rgaterate=8, rgatewave=1, growl=0.0, pumper=0.9, pumprate=1, tape=0.2, tapedrive=1.7)

#@part38(8)
b1 >> pumpbass(P*[0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, resonbank=0.0, rbfreq=120, rbdecay=0.5, rbspread=1.0, fbdelay=.5, fbtime=2, fbfeed=0.5, fbcutoff=4000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.5, tapedrive=1.7, shape=0.1).every(8, "stutter", shape=0.76, dur=1)

#@part39(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part40(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.4, sub=0.0, body=16, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, rgaterate=4, rgatewave=1, drift=1, driftspeed=1, driftdepth=1, driftsmooth=0.5, beat_dur=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.0, tapedrive=0)

#@part41(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.1)

#@part42(8)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part43(8)
z0 >> play("V ", shape=lininf(0.2, 2.0, 32))

#@part44(32)
a4 >> play("q.q", amp=1,  sample=7, dur=1/3, shape=2.2, lpf=linvar([800, 2000], 32), lpr=0.2)

#@part45(8)
h2.stop()
r7.stop()
m1.stop()

#@part46(16)
l1 >> loop("electrodrum16", dur=16, sample=(2, 9), comp=1, multicrush=3, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=200, mchifreq=4000, sbrk=PWhite(0.4, 1.0), bpf=fb(16, 200, 4000), bpr=0.5, spin=PRand([2, 4, 8, 16]), amp=1)

#@part47(16)
w3 >> play("..c.", sample=8, amp=2, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)

#@part48(16)
b1.stop()
g1 >> gong(PRand([0, 7, -5, 11]), dur=PWhite(12, 32), sus=PWhite(16, 36), oct=4, amp=0.25, cheapverb=0.9, cvdecay=7, jpverb=0.8, jpsize=0.99, jpdamp=0.2, hpf=300, pan=PRand([-0.6, 0.6]))

#@part49(64)
m1.oct=5
b0 >> play("X ")
m1.oct=4
b1 >> a_daft([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=7, amp=1, cutoff=linvar([700, 1600], 32), res=0.1, sub=0, body=32, high=32, mid=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=1.0, pumper=0.0, pumprate=1, tape=0.1, tapedrive=1.1) + var([0, 4, 0, 7])

#@part50(16)
e9.stop()
z0.stop()
a4.stop()
b1.oct=5
b1.fbdelay=0.5
b1.shape=0.2

#@part51(16)
l1.sample=8

#@part52(8)
l4 >> lbass(detune=0.3, oscmix=0.5, submix=0.5, cutoff=4500, rq=0.5, sus=1.5, a=lininf(0.4, 0.01, 32), tone=linvar([0.14, 0.7], 32))

#@part53(16)
l4 >> lbass(detune=0.3, oscmix=0.5, submix=0.5, cutoff=4500, rq=0.5, sus=1.5, a=lininf(0.4, 0.01, 32), tone=linvar([0.14, 0.7], 32)).unison(2)

#@part54(8)
g1.stop()
b1.stop()
b0.stop()
w3.stop()

#@part55(32)
l5 >> lbass([0, 0.5, 3], dur=[1, 1/2, 1, 2], detune=0, oct=6, oscmix=0.3, delay=0.0, submix=0.8, cutoff=5600, rq=1.2, lpf=2200, lpr=0.1, leg=128, sus=1.0, a=0.01, tone=0.5).chroma()
l4.oct=4
l4.shape=0.55

#@part56(32)
e2 >> a_hhat(tone=8000, metallic=1, distortion=2, open=0, dur=1/4)
k9 >> play("X ", sample=8, amp=2)

#@part57(32)
s4 >> a_stress(([0, 1],32), dur=1/4, oct=6, drcomp=2, filterFreq=linvar([100, 800], 128), resonance=linvar([0.1, 0.5], 32), distortion=4, attack=0.01, release=0.2)

#@part58(16)
# c4 >> a_cy(amp=[1, 0, 0, 1], mverb=0.0, dur=[PDur(3, 8), 1/3], bright=0.5, echo=0.5)

#@part59(16)
c4.stop()

#@part60(8)
b1.stop()
e1.oct=7
l4.oct=4
l4 >> lbass(detune=0.3, oscmix=0.5, oct=5, submix=0.5, cutoff=4500, rq=0.5, sus=1.5, a=lininf(0.4, 0.01, 32), tone=linvar([0.14, 0.7], 32), shape=0)
l4.stop()
l5.stop()
s4.stop()
c4.stop()
k9.stop()
f7.stop()
z0.stop()
m1.stop()
a4.stop()
w3.stop()
b0.stop()
x4.stop()
b1.hpf=1000
x4.stop()

#@part61(16)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.2, sub=0, body=128, growl=0.0, pumper=0.1, pumprate=3, tape=2.1, tapedrive=1)
n3 >> play("X ")
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=7, amp=1, cutoff=sinvar([500, 1100], 32), res=0.2, sub=0, body=128, growl=0.0, pumper=0.1, pumprate=3, tape=2.1, tapedrive=1)

#@part62(32)
d1 >> compkick(-4, dur=1, oct=3, amp=0.95, punch=0, comp=1, click=12, fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=1000, fbspread=0.20, beat_dur=1, sub=0, body=16, tone=linvar([0.5, 1.1], 32), echo=0.5)
~d2 >> compkick(-4, dur=1, oct=3, amp=0.95, punch=4, comp=1, click=40, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)
d1 >> compkick(-4, dur=1, oct=5, amp=0.95, punch=0, comp=1, click=12,fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=1000, fbspread=0.20, beat_dur=1, sub=0, body=16, tone=linvar([0.5, 1.1], 32), echo=0.5)
~d1 >> compkick(-4, dur=1, oct=3, amp=0.95, punch=0, comp=1, click=12, fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=1000, fbspread=0.20, beat_dur=1, sub=0, body=16, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part63(16)
b1.stop()

#@part64(16)
~d1 >> compkick(0, dur=1, multicrush=0.5, mclowdrive=1.5, mcmiddrive=20, mchighdrive=18, mclofreq=2000, mchifreq=300, oct=3, amp=1, punch=var([12, 1, 2, 3]), comp=1, click=4800, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=10000, fbspread=0.1, beat_dur=1, sub=120, body=360, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5, leg=32)

#@part65(16)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([1, 4.1], 32), echo=0.5)

#@part66(32)
b1 >> a_daft([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=7, amp=1, cutoff=linvar([700, 1600], 32), res=0.1, sub=0, body=32, high=32, mid=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=1.0, pumper=0.0, pumprate=1, tape=0.1, tapedrive=1.1) + var([0, 4, 0, 7])
b1.amp=0.1

#@part67(16)
d2 >> click(0, dur=1/2, sus=0.1, amp=[0, 0.35], rate=24, hpf=2400, pan=0.1, leg=1, mverb=0.5)

#@part68(16)
~d1 >> compkick(0, dur=1, multicrush=0.5, mclowdrive=1.5, mcmiddrive=20, mchighdrive=18, mclofreq=2000, mchifreq=300, oct=3, amp=1, punch=var([12, 1, 2, 3]), comp=1, click=4800, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=10000, fbspread=0.1, beat_dur=1, sub=120, body=360, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5, leg=32)

#@part69(8)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=-0.08, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part70(4)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=var([0, 1, 2, 3]), comp=1, click=480, fbdelay=1, fbtime=0.5, fbfeed=0.7, fbcutoff=1000, fbspread=0.1, beat_dur=1, sub=120, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5).only()

#@part71(16)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=var([0, 1, 2, 3]), comp=1, click=480, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=1000, fbspread=0.1, beat_dur=1, sub=120, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=var([0, 1, 2, 3]), comp=1, click=48, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=1000, fbspread=0.1, beat_dur=1, sub=120, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=var([12, 1, 2, 3]), comp=1, click=1480, fbdelay=1, fbtime=(0.5, 0.25), fbfeed=0.7, fbcutoff=1000, fbspread=0.1, beat_dur=1, sub=120, body=36,  mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part72(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part73(16)
~d1 >> compkick(0, dur=1, multicrush=0.5, mclowdrive=1.5, mcmiddrive=20, mchighdrive=18, mclofreq=2000, mchifreq=300, oct=3, amp=1, punch=var([12, 1, 2, 3]), comp=1, click=4800, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=10000, fbspread=0.1, beat_dur=1, sub=120, body=360, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5, leg=32)

#@part74(4)
l1 >> loop("electrodrum16", dur=16, sample=(2, 9), comp=1, multicrush=3, mclowdrive=2, mcmiddrive=2.5, mchighdrive=3, mclofreq=200, mchifreq=4000, sbrk=PWhite(0.4, 1.0), bpf=fb(16, 200, 4000), bpr=0.5, spin=PRand([2, 4, 8, 16]), amp=1)

#@part75(16)
a4 >> play("q.q", amp=1,  sample=7, dur=1/3, shape=2.2, lpf=linvar([800, 2000], 32), lpr=0.2)

#@part76(16)
e2 >> a_hhat(tone=8000, metallic=1, distortion=2, open=0, dur=1/4)

#@part77(32)
w1 >> play("X ", sample=4)

#@part78(16)
m1 >> dbass([(0,4,7), rest(0), (-2,3,7), rest(0)], dur=1/2, oct=PRand([4, 5, 6, 7]), amp=1, fbdelay=0.68, fbtime=0.75, fbfeed=0.38, fbcutoff=600, cutoff=500, shape=0.3, cheapverb=0.0, cvdecay=1.5)

#@part79(16)
m1 >> dbass([(0,4,7), rest(0), (-2,3,7), rest(0)], dur=1/2, oct=PRand([4, 5, 6, 7]), amp=1, fbdelay=0.68, fbtime=0.75, fbfeed=0.38, fbcutoff=600, cutoff=500, shape=0.3, cheapverb=0.0, cvdecay=1.5).unison(3)

#@part80(16)
m1 >> dbass([(0,4,7), rest(0), (-2,3,7), rest(0)], dur=1/2, oct=PRand([4, 5, 6, 7]), amp=1, fbdelay=0.68, fbtime=0.75, fbfeed=0.38, fbcutoff=600, cutoff=500, shape=0.6, cheapverb=0.0, cvdecay=1.5).unison(3)

#@part81(16)
drop()

#@part82(16)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.4, sub=0.0, body=16, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, rgaterate=4, rgatewave=1, drift=1, driftspeed=1, driftdepth=1, driftsmooth=0.5, beat_dur=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.0, tapedrive=0)

#@part83(32)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part84(8)
# ~d1 >> compkick(0, dur=1, multicrush=0.5, mclowdrive=1.5, mcmiddrive=20, mchighdrive=18, mclofreq=200, mchifreq=300, oct=3, amp=1, punch=var([12, 1, 2, 3]), comp=1, click=480, fbdelay=1, fbtime=0.25, fbfeed=0.9, fbcutoff=1000, fbspread=0.1, beat_dur=1, sub=120, body=360, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5, leg=32)

#@part85(16)
c4 >> a_cy(amp=[1, 0, 0, 1], mverb=0.0, dur=[PDur(3, 8), 1/3], bright=0.5, echo=0.5)

#@part86(8)
c4.stop()
