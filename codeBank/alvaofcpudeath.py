# alvaofdeath 96
# todo
Clock.bpm = 92
m2 >> alva(dur=PDur([5, 3, 7, 5, 9, 5, 6], 12), sus=0.76, fbdelay=var([0, 0, 0.5, 0.25, 0, 0]), gate=0.1, gaterate=1, gatewave=1, leg=PRand(8)[:13], glitch=0.0, oct=(3, 4), tube=1,fshift=var([0, 1, 2, 4, 0], PRand([1,2,4,8])), shimmer=0, shimsize=0, shimpitch=var([1, 1.5, 2], PRand(32)), shimmix=0, tape=0, fbfeed=0.9, fbtime=0.5, tapedrive=4, drift=0, envdist=0, lpf=var([4000, 2000, 1000],[13, 2, 1]), lpr=0.1, mu=4)
o8 >> loop("circledrum16", dur=16, amp=4, tape=1)
j1 >> alva([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=12, mod=0.1, hpf=0).unison(4)
o1 >> loop("dubstepbass32", dur=32, amp=1).lclip(var([0.25, 0.5]))
j2 >> bass(dur=1/2, amp=j1.degree==4, oct=(6, 7), leg=40)
j1.dur=PDur([3, 5], 8)
j1.oct=2 # 4
j4 >> alva(dur=2, shape=2, a=0.5, hpf=linvar([20, 1500], 32), lpr=0.1)
m2.degree=8
m2.degree=0
drop()
y3 >> play("..C.", amp=4, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)
k9 >> play("{X.X.[XX].X.[XXX]}", amp=4, sample=3, lpf=620, lpr=0.2, formant=1)
k9.rate=0
m2.solo(0)
