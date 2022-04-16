# slaap
Samples.addPath("/mnt/70225B03225ACDAA/CRASH SERVER/Production/Slaap - remix/zbdm version/")
Root.default="C"
Scale.default="minor"
Clock.bpm=176

w1 >> stretch("sl_wind", dur=P[16,32,64], sus=[32,64], lpf=1800, amp=0.2, rate=PWhite(-1,1)).unison(4)
w2 >> loop("sl_voice1", formant=1, dur=12, hpr=0.1, hpf=4000, amp=0.2, room=1, mix=0.6, pan=(-1,1))
w3 >> loop("sl_wind", 4, dur=6, sus=[12, 24], spin=[4, 8, 16, 2], hpr=0.1, hpf=0, amp=0.3, room=1, mix=0.4, pan=(-1,1))

w_all.stop()
g1 >> loop("sl_guit2", dur=32, shape=0)

g9 >> loop("sl_guit2", dur=[8,[16,4]], delay=[12,8,16,24], cut=[1/4,1/2,1/8], sus=16, chop=[16,32], room=0.3, mix=0.2, pan=(-1,1), crush=2)
l3 >> loop("sl_drum1", dur=32)
g3 >> loop("sl_guit3", dur=PRand([16,32]), chopwave=PRand(8), chop=PRand(8), room=1, mix=0.4, lpf=7800).unison(4)
g4 >> loop("sl_guit3", dur=PRand([8,16]), chopwave=PRand(8), chop=PRand(8), room=1, mix=0.4, lpf=7800).unison(4)

y1 >> loop("sl_voice2", dur=[16], shape=0.1, amplify=1).unison(0).after(16,"stop")
y2 >> loop("sl_voice3", dur=12, shape=0.2, amplify=1).after(12, "stop")
y3 >> loop("sl_voice1", dur=16, spin=0.4, amplify=PBern(8), room=1, mix=0.6).after(1, "stop")
y4 >> loop("sl_voice2", dur=15, spin=0.2, amplify=1, octafuz=1, room=1, mix=0.6).after(1, "stop")
y5 >> loop("sl_voice1", dur=14, spin=0.4, amp=PwRand([0, 1], [15, 1]), room=1, mix=0.6).after(1, "stop")

a1 >> play("x-", dur=1, sample=var(P[0:10],64), crush=0, amp=0.2).sometimes("stutter", PRand(8), rate=4).unison(5).sometimes("amen")
v_all.stop()
g_all.stop()
b1 >> loop("sl_bass1", dur=8, sus=8, shape=0.1, lpf=linvar([800,4800],[64,0]), lpr=PWhite(0,1)).unison(3)
b2 >> loop("sl_bass2", dur=16, shape=0.2, sus=16, amp=1.5, cut=[2/3,[0,1/3]], chop=[0,2,4]).unison(2)
b3 >> loop("sl_bass2", dur=16, lpf=800, sus=16)
k1 >> loop("sl_drum2", dur=32, lpf=4800)
k2 >> loop("fill4", sample=2, dur=8, hpf=4000)
k3 >> loop("fill4", sample=4, dur=8, hpf=2000)

b_all.stop()
y_all.stop()
k_all.stop()

p0 >> stretch("sl_guit1", pshift=-7, delay=8, dur=16, pan=-1)
p4 >> stretch("sl_guit1", pshift=-7, dur=8, pan=1)
p1 >> loop("sl_guit1", delay=4, dur=16, sus=32)
f1 >> loop("sl_guit1", dur=32)
p3 >> loop("sl_guit1", dur=16)

l4 >> loop("break16", sample=0, dur=16)
l5 >> loop("core16", sample=3, dur=16, chop=2, lpf=7800, amp=0.5)
l6 >> loop("core16", sample=2, dur=16)