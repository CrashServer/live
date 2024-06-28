#weird intro
Clock.bpm = 135;
a0 >> loop("cosmic16", dur=16, sample=2, hpf=(300, PRand([400, 300])), room2=1, revsus=18, shift=var([(0.5, 1), 1], [4, 4]), beat_dur=1).unison(2)
e1 >> play("c", dur=4, hpf=8000, leg=4, echotime=4, echo=0.5, echomix=0.25, pan=PWhite(-1, 1))
a1 >> loop("sub4", dur=4, sample=9, amp=PWhite(0.5, 0) + 0.5, shift=(0, 1.01), hpf=0, drive=var([0, 0.1], [3, 1]))
s1 >> play("o ", amp=2, dur=4, sample=2, room2=1, lpf=400, hpf=400, echotime=4, echo=0.25, echomix=0.2)
z1 >> loop("cosmic16", dur=[16, 32], pos=0.5, chop=4, chopmix=0.5, sample=2, hpf=0, room2=1, revsus=8, shift=var([(1, [0.99, 2.01]), 1], [4, 4]), beat_dur=1).unison(0)

a2 >> loop("perc8", dur=8, sample=4, amp=1 - a1.amp, hpf=4000, pan=PWhite(-1, 1))
a3 >> loop("berlin8", dur=8, sample=11, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=1, revsus=4)
a2.leg=4

a4 >> loop("berlin8", dur=8, sample=4, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=[1, 0], revsus=4)
a5 >> loop("berlin8", dur=8, sample=2, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=1, revsus=4)

e_all.dafilter=1
a_all.mverb=0.5

a6 >> loop("futur8", dur=16, sample=9, amp=[1, 1, 1, 0])
a7 >> loop("berlin8", dur=8, sample=2, lofi=1, amp=[0, 0, 0, 1])

a_all.sample=3
