# flow — 110 bpm, G dorian, warm current
Clock.bpm = 110
Scale.default = "dorian"
Root.default = "G"

#@#@ flow

#@ intro

dk >> play("X.", dur=0.5, amp=var([1,0.9,1,0.88],4))

ab >> abass([0,-7,0,-5,3,-7,0,-3], oct=4, dur=0.5, sus=var([0.35,0.3,0.45,0.35],[4,4,4,4]), amp=0.75, dubdelay=sinvar([0,0.2],16))

ky >> keys([0,2,3,5,7,5,3,0], oct=5, dur=0.5, sus=PRand([0.3,0.5,0.7,1],8), amp=0.45, chorus=0.35, room=0.45, mix=0.35, pan=sinvar([-0.3,0.3],8))

#@ groove

sn >> play("..o.", dur=0.5, amp=var([0.8,0.5,0.8,0.45],4), cheapverb=0.2, cvdecay=0.7)

ht >> play("i", dur=0.25, amp=Pacc(3,8), hpf=7000, pan=PRand([-0.25,0,0.25],4))

cl >> play("..u.", dur=0.5, amp=0.55, pan=-0.2, cheapverb=0.15, cvdecay=0.5)

sv >> svdk([(0,4,7),(-7,0,4),(2,5,9),(-5,-2,2)], oct=4, dur=var([2,1.5,2,2.5],[8,4,8,4]), sus=var([1.5,1,1.5,2],[8,4,8,4]), amp=0.3, chorus=0.4, dubdelay=sinvar([0,0.3],32), lpf=sinvar([1500,4000],32))

kp >> karp(melody(), oct=5, dur=PRand([0.5,0.25,1,0.75],4), sus=PRand([0.25,0.4,0.6],4), amp=0.35, cheapverb=0.45, cvdecay=1.5, pan=PRand([-0.4,0,0.4],4))

#@ open

rh >> rhodes([(0,4,7),(2,5,9),(-2,2,5),(0,3,7)], oct=4, dur=var([2,1.5,2,2.5],[8,4,8,4]), sus=var([1.2,0.8,1.5,1],[8,4,8,4]), amp=0.32, phaser=sinvar([0,0.45],16), room=0.5, mix=0.4)

mr >> marimba([7,9,12,7,5,3,7,9], oct=5, dur=PRand([0.5,0.25,1],8), sus=PRand([0.1,0.25,0.4],8), amp=0.28, room=0.5, mix=0.4, pan=PRand([-0.3,0.3],4))

og >> organx([0,2,3,5,7], oct=5, dur=PBal("clave"), sus=0.12, amp=sinvar([0.15,0.4],16), chop=sinvar([0,0.5],32), room=0.4, mix=0.3)

vi >> viola([-7,-5,0,2], oct=4, dur=var([4,6,8],[16,8,16]), sus=sinvar([3,6],16), amp=sinvar([0.08,0.22],24), room=0.8, mix=0.7, vibrato=sinvar([0,0.35],16))

#@ peak

ab.dubdelay = sinvar([0.2, 0.5], 16)
ky.oct = var([5,6],[16,8])
kp.amp = linvar([0.35, 0.55], 32)
og.amp = sinvar([0.3, 0.6], 16)
rh.phaser = sinvar([0.3, 0.8], 8)

#@ end(32)
