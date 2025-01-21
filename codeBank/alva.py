#alvaa
Root.default = "A#"
Clock.bpm = 128
j1 >> alva([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=12).unison(4)
j2 >> bass(dur=1/2, amp=j1.degree==4, oct=(6, 7), leg=40)
j3 >> play("X ", lpf=400)
j1.dur=PDur([3, 5], 8)
j1.oct=4
j1.rate=-1
j1.hpf=1200
j4 >> alva(dur=2, shape=2, a=0.5)
j1.oct=2
j2.dur=1/4
j4.dur=1/2
j4.shape=0.1
j4.hpr=0.1
j4.hpf=linvar([200, 1500], 32)
j5 >> play("[--].-", sample=8)
j6 >> loop("circledrum32", dur=32)

j1.dur=1/4
