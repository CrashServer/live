# rebelisme 142
# mud

Clock.bpm=142

p4 >> loop("dnbfx16", dur=16, dist2=0.5, sample=[1, 3, 0], amp=2)
m0 >> vati(I,off=(7, 3), dur=(4, 6), tremolo=0.1, leg=0.5, oct=3, tanh=1, hpf=600).unison(4)

# Toms 
b4 >> play("mMt[T{mMTt}]", amp=1, drcomp=.5).sometimes("stutter")
b4.amp=var([PBin()*PWhite(0.1,0.5), PWhite(0.8,1.1)], [6,2])

w2 >> play("---(---{-:=})", amp=PWhite(0.8,1.2), pan=PWhite(-1,1), sample=5).sometimes("stutter")
n6 >> play("kkuk", drcomp=0.3, sample=5)

b0 >> play("k.", sample=0, amp=3)
n7 >> play("..c.", amp=2, drcomp=0.5, sample=1)

# ouinoooouuiooo   /\
q5 >> noloop("gdrop8", sample=11, dur=8, shape=.4, tanh=.4, vol=.6)
q6 >> noloop("gdrop8", sample=11, dur=8, delay=0, rate=-1.2, tanh=.3, vol=.6)
q_all.chop=4

c9 >> loop("gscreecha16", dur=16, sample=5).lclip(4) # 6 3 5 
g8 >> loop("gcindrum16", dur=32, sample=10)

t9 >> lbass((0, expvar([0,7,7.2], [16,14,2])), dur=P[1/4,1/4], oct=5, cutoff=PFr(1200,6000), tone=0.4, hpf=160, vol=.7)

# fill gabber
m7 >> loop("gfill4", dur=4, amp=var([0,1], [12,4]), sample=PRand(909), drcomp=.5)
m8 >> loop("gfill8", dur=8, amp=var([0,1], [24,8]), sample=PRand(909), drcomp=.5)

# Rise drop
y3 >> loop("gbuild16", dur=16, sample=6)
y4 >> loop("gbuild16", dur=16, sample=6, delay=4)
y5 >> loop("gbuild16", dur=16, sample=6, delay=8)
y6 >> loop("gbuild16", dur=16, sample=6, delay=12)

y_all.stop()

masterAll(0, "amp", PBin())

y_all.stop()

d0 >> play("<kk.Kkkkkk.kk><u.(...C).><~.><X...>", dur=1/4, valad=0, sample=P[0], valadr=0.3, valadd=139, valadt=0, valadc=0.1).sometimes("stutter")
