# David Lynch Code

Scale.default="major"
# LOW Tempo
Clock.bpm=108


##### PART I "drone"
r0 >> loop("dune_16", dur=16, sample=0, lofi=0)
r1 >> loop("dune_16", dur=PRand(12,22), sample=1, delay=4, a=.1, hpf=0)
r2 >> loop("dune_16", dur=16, sample=2, delay=8, a=.1, hpf=0)
r6 >> loop("dune8", dur=8, sample=1, hpf=0).lclip(4) # robot fight
w1 >> loop("losthighway4", dur=4, sample=0, mverb=0, comp=0, tanh=.2).lclip(4) # ry
v4 >> noloop("lynchvoice8", dur=16, sample=7, comp=1, fx2=1, trig=0, sus=16)

f8 >> play("<x.><.><....>", sample=0, amp=3).sometimes("stutter")
u7 >> loop("losthighway16", dur=16, sample=2, lofi=0).lclip(0) # heirate

#### PART III "INSANE VOICES"
# twin tech break reverse
s7 >> loop("lynchvoice8", dur=8, sample=8, comp=0, rate=1, chop=2, chopi=.5)
i1 >> loop("gbreak16", dur=16, fx=1, hpf=0, lpf=2200)
u3 >> noloop("lynchvoice8", dur=8, sample=8,rate=1)
u4 >> loop("lynchcrazy32", dur=32, sample=0) # noahs ark

x4 >> loop("twinpeaks16", dur=16, sample=5, amp=1.2, sus=16) # dark ambi laura
c7 >> play("<k.><..><..u.>", sample=0, amp=2, comp=1, lpf=0).sometimes("stutter")

### transition
v8 >> loop("twinpeaks16", dur=16, chop=2, sample=0, shape=0, valad=500, valadr=0.3, valadd=15, valadt=0, valadc=0.3).lclip(0) # intro
v9 >> loop("twinpeaks16", dur=16, chop=2, chopi=0.5, sample=1, valad=500, valadr=0.3, valadd=25, valadt=0, valadc=0.3) # 2 INtro

z4 >> loop("lynchcrazy8", dur=8, sample=2) # rise up down tempo

# INTERLUDE
Clock.bpm = 128;
y5 >> loop("elephant16", sample=0, pos=0, dur=16, comp=0, sbrk=0, t_reset=0, sbrkdur=0.125, shape=0, output=0).lclip(0)
i8 >> loop("hiphop16", dur=16, room=.1, sample=0)

k3 >> bass(var([0,1], 16), hpf=0, hpr=0.3, oct=4, vakorg=500, vakorgr=0.5, vakorgd=10, vakorgt=0, vakorgc=0.4, dur=1/2, rate=.3).unison(2)
e4 >> play("-")
d4 >> play("<[vv]...|U1|...>", comp=1)
e4 >> play("...(...z)", sample=2)

j7 >> play("<x.><.><....>", amp=2, lpf=400, sample=4).sometimes("stutter")

### Dancy
z4 >> loop("lynchcrazy8", dur=8, sample=0) # goodDay instru
z4 >> loop("lynchcrazy16", dur=16, sample=0, hpf=2000).lclip(0) # goodDay vocal
u6 >> loop("lynchcrazy16", dur=16, sample=4) # stone electro

u5 >> loop("lynchcrazy16", dur=16, sample=2) # low beat
x3 >> loop("mulholland8", dur=8, sample=0, chop=0, amp=PBin(445), blur=1).lclip(4) # damdada

### Ambi jazzy
u4 >> loop("losthighway16", dur=16, sample=3) # ambijazz
o6 >> loop("jazzb8", dur=8, sample=2)

c5 >> loop("jazzguitar8", dur=8)
# x5 >> loop("mulholland8", dur=8, sample=2, chop=2, chopi=0) # swing jazz

### PART "INSIDE DUNE"
# Epic dance 148
Clock.bpm=linbpm(148, 32)
u4 >> loop("losthighway16", dur=16, sample=4, chop=2, chopi=P*[0,.25,.5,.75], mverb=.6, shift=1.1, tanh=.2) # sax
b0 >> loop("losthighway32", dur=32) # piano sax
# a3 >> loop("elephant16", sample=1, dur=P[16:2:-2], chop=0, mverb=0.5, sus=16, cut=16/P[16:2:-2])
c7 >> play("<k.><..><..u.>", sample=0, amp=2, comp=1, lpf=0).sometimes("stutter")
# h5 >> loop("dune_8", dur=8, sample=PRand(8), tanh=.2, amp=0.5).lclip(2)
r4 >> loop("dune8", dur=8, sample=0, chop=0, chopwave=2, shift=(.25,.5,0,1.5,1.75), vol=.6) # ambi montee
l4 >> play("X ", dur=8)
e3 >> loop("losthighway8", dur=8, sample=3, chop=4, chopi=.5, mverb=0) # rammstein

# A placer TODO
z4 >> loop("dune16", dur=16, sample=1) # main
# x4 >> loop("twinpeaks16", dur=16, sample=3) # love
x5 >> loop("twinpeaks16", dur=16, sample=4, blur=1).lclip(2) # love 2
j9 >> loop("losthighway8", dur=8, sample=1) # putaSpell bass

# A placer TODO
u5 >> loop("lynchcrazy16", dur=16, sample=3) # so glad
u6 >> loop("lynchcrazy16", dur=16, sample=1) # i know
z4 >> loop("lynchcrazy8", dur=8, sample=1, shape=0, comp=1, chop=0, chopi=0).lclip(0) # hoop
j4 >> loop("losthighway8", dur=16, sample=6, comp=0, shape=0).lclip(2) # perfectDrugsTakem 
s4 >> loop("losthighway16", dur=16, sample=1) # eye
r5 >> loop("losthighway16", dur=16, sample=0, chop=0) # eye

u4 >> loop("lynchcrazy16", dur=16, sample=5) # in heaven
j5 >> loop("losthighway8", dur=8, sample=5, comp=1, shape=0) # perfectDrugs 
p4 >> noloop("lynchvoice8", dur=8, sample=5, fx1=0, sus=2, trig=.2) # sus  ## FIRE

### Ambiance
j0 >> loop("losthighway8", dur=8, sample=2) # insensatez
j8 >> loop("losthighway8", dur=8, sample=4) # groove 
j4 >> loop("losthighway8", dur=8, sample=0) # duub
x4 >> loop("twinpeaks16", dur=16, sample=6) # polar noire
x5 >> loop("mulholland8", dur=8, sample=1, chop=0) # electro swing

## A Test 148
u4 >> loop("lynchcrazy16", dur=16, sample=5) # in heaven
j5 >> loop("losthighway8", dur=8, sample=5, comp=1, shape=0) # perfectDrugs 
p4 >> noloop("lynchvoice8", dur=8, sample=5, fx1=0, sus=2, trig=.2) # sus  ## FIRE

## A Test 148
x4 >> loop("twinpeaks16", dur=8, sample=6, mverb=0.2, comp=1) # polar noire
x2 >> play("l ", bank=1, sample=6, amp=.4, rate=var([1,0.9],16))
p4 >> noloop("lynchvoice8", dur=8, sample=5, fx1=0, sus=6.5, trig=0, comp=1, delay=3.75, amp=[0,1], hpf=800) # sus  ## FIRE

## 
u5 >> loop("lynchcrazy16", dur=16, sample=3, sbrk=0.5) # so glad
z4 >> loop("lynchcrazy8", dur=8, sample=1, shape=0, comp=1, chop=0, chopi=0, valad=0, valadr=0.3, valadd=15, valadt=0, valadc=0.3).lclip(2) # hoop

