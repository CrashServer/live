# horrDrum
# drums
o7 >> play("k.", amp=4).sometimes("stutter")
b5 >> loop("rock16", hpf=400, dur=16, wshape=1, wtype=5, wmix=0.5, sample=var(PRand(909), 32), amp=PwRand([0,1],[40,60])).lclip(var([16,4],16))
s5 >> loop("cindrum16", dur=16, hpf=100, wshape=1, wtype=8, sample=2, wmix=0.5, sbrk=var([0,P*[0.5, 0.25, 1, 2]],24), amp=PwRand([0,1],[40,60])).lclip(var([8,4,2,1,0.5], [16,8,4,2,2]))
f2 >> loop("cinambi16", dur=16, sample=var(PRand(808), 64), mverb=0.2, amp=3 ).lclip(var([8,4,2,1,0.5], [16,8,4,2,2]))
