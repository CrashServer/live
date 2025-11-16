# alvaa 128
# todo

Root.default = "A#"
Clock.bpm = 128
j1 >> alva([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=12, mod=0.1, hpf=0).unison(4)
j2 >> bass(dur=1/2, amp=j1.degree==4, oct=(6, 7), leg=40)
j1.dur=PDur([3, 5], 8)
j1.oct=2 # 4
j4 >> alva(dur=2, shape=2, a=0.5, hpf=linvar([20, 1500], 32), lpr=0.1)
