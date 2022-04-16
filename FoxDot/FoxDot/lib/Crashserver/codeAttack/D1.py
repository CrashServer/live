# D1
d1 >> loop("ravebass4", dur=8, sample=4)
d2 >> loop("ravebass8", dur=8, sample=5, drive=0.0, amp=0.5, hpf=4000)
d3 >> loop("ravebass8", dur=16, sample=0, shift=PRand(1, 2), room2=0, drive=0, revsus=0, amp=0.5).unison(2)
d4 >> loop("ravebass4", dur=4, sample=0, room2=0.5, drive=0, revsus=4).unison(2)
d5 >> loop("ravebass4", dur=4, sample=0, room2=0.5, drive=0, revsus=8).unison(0)
d6 >> play("X:", sample=(5, 4), lpf=(1200, 4000)).sometimes("stutter")
d7 >> loop("nsbass16", dur=16, sample=1, hpf=400)
d8 >> loop("psych32", dur=32, sample=3, lpf=4000)