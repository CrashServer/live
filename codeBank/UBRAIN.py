# UBRAIN
Clock.bpm=88
Clock.bpm=88*2

l4 >> loop("rageambi16", dur=16, hpf=300)

x9 >> loop("ragegtr16", dur=32, lpf=1400, sample=var([[8, 12], 9, 14], [8, 7, 1])).lclip(var([0.5, 1, 2], [8, 4, 2]))
x0 >> loop("ragegtr16", dur=16, lpf=1400, sample=var([[8, 12], 9, 14], [8, 7, 1])).lclip(var([0.5, 1, 2], [8, 4, 2]))
d6 >> play("X " , sample=5, amp=x0.sample==12)
d2 >> play("<---{-[--]=:#}><.:>", sample=7, high=2).sometimes("stutter", PRand(8), rate=PWhite(1,8))
d3 >> play("..u(...{u[uu][.u]})", sample=(10,4))

d5 >> loop("rock8", dur=8, sample=(3,7), drcomp=0.5)
e4 >> waves(melody(), dur=4, oct=6, rate=PRand(1,9), fx2=1, chop=4, chopwave=5).slider()

k4 >> ethpad(dur=8,oct=(6, 5, var([4, 7], [28, 4])), fx2=1).unison(4)
h5 >> noloop("vocalcrash8", dur=8,pos=PWhite(0, 1), room=0.1, ratelfo=0, ratelfoadd=0.5, ratelfomul=0.5,  start=PWhite(0, 1), sample=PRand(8), trig=0, valad=500, valadr=0.3, valadd=5, valadt=0, valadc=0.3)
