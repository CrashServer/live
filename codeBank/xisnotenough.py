# xisnotenough 130
# todo


#@intro(16)
Clock.bpm = 130
Scale.default = "minor"
Root.default = "E"
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@build(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.5, fbfeed=0.5, fbcutoff=4000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@peak(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@break(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.4, tapedrive=1.7)

#@drop(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@outro(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.1, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@part7(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=0.9, click=0.65, sub=1, body=4, tone=0.5, tape=0.5, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1)

#@part8(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=0.9, click=0.65, sub=1, body=36, tone=[0.6, 0.8, 0.6, 0.6])

#@part9(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=var([1, 0], [28, 4]), click=0.65, sub=1, body=36, tone=0.5, echo=0.5)

#@part10(4)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=var([1, 0], [28, 4]), click=0.66, sub=1, body=36, tone=0.5, echo=0.5)

#@part11(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=var([1, 0], [28, 4]), click=0.67, sub=1, body=36, tone=0.5, echo=0.5)

#@part12(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=var([1, 0], [28, 4]), click=0.68, sub=1, body=36, tone=0.5, echo=0.5)

#@part13(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=var([1, 0], [28, 4]), click=0.70, sub=1, body=36, tone=0.5, echo=0.5)



#@part14(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=var([1, 0], [28, 4]), click=0.75, sub=1, body=36, tone=0.5, echo=0.5)

#@part15(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=2, comp=1, click=0, sub=1, body=34, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part16(16)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=0, comp=1, click=12, fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=1000, fbspread=0.20, beat_dur=1, sub=0, body=16, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part17(4)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=0, comp=1, click=8, fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=1000, fbspread=0.20, beat_dur=1, sub=0, body=16, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part18(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

m1 >> darkpad([0, -5], dur=16, sus=17, oct=5, amp=0.8, cutoff=linvar([600, 3200], 48), res=0.4, detune=0.35, dark=0.7, sub=0.6, cheapverb=0.65, cvdecay=2.5, hpf=180, csweep=0.2, cswfreq=200, cswdepth=0.1, cswrate=0.5, cswdecay=0.5, vowel=1, vowelf=1, vowelq=1)


#@part19(8)
d2 >> click(0, dur=1/2, sus=0.1, amp=[0, 0.35], rate=24, hpf=2400, pan=0.1, leg=1, mverb=0.5)

#@part20(16)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part21(8)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.5, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part22(8)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part23(16)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([2, 1.1], 32), echo=0.5)

#@part24(16)
~d1 >> compkick(0, dur=1, oct=2, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=36, tone=linvar([1, 1.1], 32), echo=0.5)

#@part25(8)
~d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=24, tone=linvar([1, 1.1], 32), echo=0.5)

#@part26(16)
~d1 >> compkick(PRand([0, 5, 7, 12]), dur=1, oct=4, amp=0.40, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=1, body=12, mverb=0.5, tone=linvar([0.5, 1.1], 32), echo=0.5)


#@part27(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(5,8), sus=PDur(5,8)*0.8, oct=6, amp=2, cutoff=sinvar([500, 1100], 32), res=0.1, sub=0, body=8, growl=0.2, pumper=.1, pumprate=0, tape=1.7, tapedrive=1.4)

#@part28(4)
e1 >> compperc(PRand([0, 5, 7, 12]), dur=PDur(5, 16), sus=0.38, amp=4, tone=4, noise=4, body=1.5, metal=1.9, ring=0.35, comp=0.4, hpf=100, cheapverb=0.4, pan=PRand([-0.5, -0.2, 0.2, 0.5]))

#@part29(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part30(16)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

e9 >> tb304([0, 0, 3, 0, _, 0, 5, 0, 0, _, 0, 3], dur=1/4, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1,amp=4, shape=0, shapemix=0.5, oct=6, hpf=1200, mverb=0.2)

#@part31(8)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part32(8)
h2 >> click(0, dur=1/4, sus=0.015, amp=Pacc("ghost")*4, rate=18, hpf=5500, pan=PRand([-0.3, 0.3]))
r7 >> play("X ", lpf=[800, 1600, 400, 0])
e9.amp=0.6
#@part33(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)

#@part34(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.8, tapedrive=1)

#@part35(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.9, tapedrive=1)
e9 >> plaitsX([0, 0, 3, 0, _, 0, 5, 0, 0, _, 0, 3], dur=1/4, amp=4, shape=1, shapemix=0.5, oct=6, hpf=1200, mverb=0.5)

#@part325(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=2.1, tapedrive=1)

#@part36(4)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=2.2, tapedrive=1)
#@part40(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=2.4, tapedrive=1)

#@part35(8)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=5, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=2.3, tapedrive=1)
e9 >> tb303([0, 0, 3, 0, _, 0, 5, 0, 0, _, 0, 3], dur=1/4, amp=1, shape=0, shapemix=0.0, oct=6, hpf=2701, mverb=0.5)
g8 >> play("[--]", hpf=12200, sample=15, echo=0.5, gdel=0.2, gdeltime=0.125, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.9)
#@part36(28)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)

#@part37(16)
b1 >> pumpbass([0, 0, -5, -5, 0, 0, -7, -5], dur=PDur(5,8), sus=PDur(5,8)*0.75, oct=4, amp=1.8, cutoff=sinvar([380, 900], 32), res=0.6, sub=0.0, body=1.2, growl=0, tape=0.9, tapedrive=0.8, hpf=55)

#@part38(4)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)
m1.stop()
#@part40(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)

#@part42(16)
b1 >> pumpbass([0, 0, -3, 0, 0, -5, 0, 0], dur=PDur(15,16), sus=PDur(5,8)*0.8, oct=6, amp=1, cutoff=sinvar([500, 1100], 32), res=0.05, sub=0, body=16, growl=0.0, pumper=0.1, pumprate=3, tape=1.7, tapedrive=1)

#@part43(16)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)

f7 >> play("k ", dur=1/4)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@part18(8)
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=2, comp=0.1, click=10, fbdelay=0.5, fbtime=0.5, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0, tone=linvar([0.5, 1.1], 32), echo=0.5)


#@part18(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=5, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.5, fbfeed=0.5, fbcutoff=4000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)

#@part18(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part18(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=7, amp=2, cutoff=linvar([700, 1600], 32), res=0.4, sub=0.0, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, rgaterate=4, rgatewave=1, drift=1, driftspeed=1, driftdepth=1, driftsmooth=0.5, beat_dur=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.0, tapedrive=0)

#@part18(8)
d1 >> compkick(0, dur=1, oct=3, amp=0.95, punch=6, comp=.2, click=14, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, tone=linvar([0.5, 1.1], 32), echo=0.5)

#@part19(8)
b1 >> pumpbass([0, 0, 3, 0, -3, 0, 5, 0, 0, -3, 0, 3], dur=PDur(7,12), sus=PDur(7,12)*0.85, oct=6, amp=2, cutoff=linvar([700, 1600], 32), res=0.2, sub=0.1, body=4, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=4000, fbspread=0.1, beat_dur=1, rgaterate=4, rgatewave=1, growl=0.0, pumper=0.0, pumprate=0, tape=0.2, tapedrive=1.7)
r7 >> play("X ", lpf=[800, 1600, 400, 0]).stop()
~d1 >> compkick(0, dur=1, oct=3, amp=1, punch=9, comp=1, click=48, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, sub=0, body=36, mverb=0.0, tone=linvar([0.5, 1.1], 32), echo=0.5)
