
Clock.bpm = 142



p4 >> dbass(oct=5,ws=0.0,  leg=4, transient=0.9, transattack=1, transsustain=1, transtime=0.38).unison(3)
g0 >> loop("break160_16", dur=16, sample=3, sbrk=0.5)

z5 >> loop("surfVoice8", dur=8, sample=2, amp=0)
q5 >> cs80(0.0, dur=PDur([5, 3, 7], 8), rgate=var([0, 0.5], 8), rgaterate=12, oct=3, rgatewave=2, spring=0.0, sprdecay=1.5, sprdamp=0.3, sprtens=0.5, resonbank=0.1, csweep=0.3, cswfreq=220, cswdepth=0.3, cswrate=0.5, cswdecay=0.5, rbfreq=[72, 72, 72, 75, 72, 78, 82],gdel=0, gdeltime=0.5, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3, rbdecay=0.5, rbspread=1.0, beat_dur=1).unison(5)
drop(1, 1, 1)

l9 >> loop("xtech8", dur=8, sample=4)
x1 >> play("X ", lpf=400)

