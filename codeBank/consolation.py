# consolation
# Reisub
Scale.default="minor"
Clock.bpm = 120
Root.default=12
var.cho = var(PMarkov(I),8)
t9 >> tb303(PArp(var.cho,5), oct=(3), dur=1/4, top=linvar([200,10000],128), wave=linvar([0, 1], 128), cutoff=linvar([500,4000],[PRand(24,36),PRand(2,12)]), rq=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.7, pan=PWhite(-1, 1), lpr=0.1, lpf=linvar([5000, 12000], 32), fx2=0).unison(6)
t9.lpf=linvar([20, 6000],[256, inf], start=now)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=1, fx1=0, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)
d1 >> play("x.", feedfreq=[[0,PRand(500)],0], hpf=30, sample=4, amp=0.4, tanh=2, chop=1)
d1.feed=var(P*[0,0.125,0.25,0.5],16)
d7 >> play(P["x-(-m)"][:8].rotate(var([1,3])), rate=1.5, dur=1/4,amplify=0.8, delay=var([0,(0,0.75)],PRand(8)),sample=1)
