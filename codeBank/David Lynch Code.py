# David Lynch Code

ploop("dune16")


Clock.bpm=128

Scale.default="minor"

# low tempo
Clock.bpm=108
# A placer TODO
# z4 >> loop("dune16", dur=16, sample=1) # main



w1 >> loop("losthighway4", dur=4, sample=0, mverb=0, comp=0, tanh=.2) # apples
r6 >> loop("dune8", dur=8, sample=1, hpf=0) # robot fight

# Epic dance
c7 >> play("<k.><..><..u.>", sample=0, amp=2, comp=1, lpf=0).sometimes("stutter")
h5 >> loop("dune_8", dur=8, sample=PRand(8), tanh=.2) 
r4 >> loop("dune8", dur=8, sample=0, chop=0, chopwave=2, shift=(.25,.5,0,1.5,1.75)) # ambi montee

# Drone
r0 >> loop("dune_16", dur=16, sample=0)
r1 >> loop("dune_16", dur=16, sample=1, delay=4, a=.1)
r2 >> loop("dune_16", dur=16, sample=2, delay=8, a=.1)

# hipElephop
y5 >> loop("elephant16", sample=0, dur=16, comp=0, sbrk=0, t_reset=0, sbrkdur=0.25, shape=0)
i8 >> loop("hiphop16", dur=16, room=.1, sample=2)
k3 >> dbass(var([0,-2], 16), oct=5, dur=1/2)


v8 >> loop("twinpeaks16", dur=16, chop=2, sample=0) # intro
v9 >> loop("twinpeaks16", dur=16, chop=2, chopi=0.5, sample=1) # 2 INtro
z4 >> loop("lynchcrazy8", dur=8, sample=2) # rise up down tempo

x4 >> loop("twinpeaks16", dur=16, sample=3) # love
x4 >> loop("twinpeaks16", dur=16, sample=4) # love 2

j4 >> loop("losthighway8", dur=8, sample=4) # groove 
j3 >> loop("losthighway8", dur=8, sample=2) # insensatez

# low metal dark ambiant
j3 >> loop("losthighway8", dur=8, sample=3, chop=2, chopi=.5) # rammstein
u4 >> loop("lynchcrazy32", dur=32, sample=0) # noahs ark
c7 >> play("<k-><..><..u.>", sample=0, amp=1).sometimes("stutter", PRand(2))

# ambi jazz
u4 >> loop("losthighway16", dur=16, sample=3) # ambijazz
o6 >> loop("jazzb8", dur=8, sample=2)
c5 >> loop("jazzguitar8", dur=8)

# swing metal
x5 >> loop("mulholland8", dur=8, sample=2, chop=2, chopi=0) # swing jazz
u4 >> loop("losthighway16", dur=16, sample=2) # heirate

# mid tempo
Clock.bpm=123
# a placer TODO
g4 >> loop("elephant16", dur=16, sample=1)


j3 >> loop("losthighway8", dur=8, sample=1) # putaSpell bass
j3 >> loop("losthighway8", dur=8, sample=0) # duub

z4 >> loop("lynchcrazy8", dur=8, sample=0) # goodDay instru
z4 >> loop("lynchcrazy16", dur=16, sample=0) # goodDay vocal

u4 >> loop("lynchcrazy16", dur=16, sample=3) # so glad
u4 >> loop("lynchcrazy16", dur=16, sample=4) # stone electro
u4 >> loop("lynchcrazy16", dur=16, sample=5) # heaven

j4 >> loop("losthighway8", dur=8, sample=5, comp=1, shape=0) # perfectDrugs 

u4 >> loop("lynchcrazy16", dur=16, sample=1) # i know

x4 >> loop("twinpeaks16", dur=16, sample=6) # lanoire
x5 >> loop("mulholland8", dur=8, sample=1, chop=0) # swing


u4 >> loop("lynchcrazy16", dur=16, sample=2) # low beat
x3 >> loop("mulholland8", dur=8, sample=0, chop=0) # damdada


# twin tech break reverse
s7 >> loop("lynchvoice8", dur=8, sample=8, comp=0, rate=1, chop=2, chopi=.5)
i1 >> loop("gbreak16", dur=16, fx=1)
x4 >> loop("twinpeaks16", dur=16, sample=5) # dark ambi laura
c7 >> play("<k.><..><..u.>", sample=0, amp=2, comp=1, lpf=0).sometimes("stutter")

# high tempo
Clock.bpm=148
z4 >> loop("lynchcrazy8", dur=8, sample=1, shape=0, comp=1, chop=0, chopi=0) # hoop
j4 >> loop("losthighway8", dur=16, sample=6, comp=0, shape=0) # perfectDrugsTakem 

m4 >> loop("gbreak16", dur=16, sample=2, fx=1)
r3 >> play("<x.><.><....>", sample=0, amp=2).sometimes("stutter")

u4 >> loop("losthighway16", dur=16, sample=1) # eye
u4 >> loop("losthighway16", dur=16, sample=0) # eye

u4 >> loop("losthighway16", dur=16, sample=4, chop=2, chopi=P*[0,.25,.5,.75], mverb=.6, shift=1.1, tanh=.2) # sax
b0 >> loop("losthighway32", dur=32) # piano sax

a3 >> loop("elephant16", sample=1,dur=4, chop=0)





