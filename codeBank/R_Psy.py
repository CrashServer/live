# R_Psy
p1 >> loop("uk16", dur=16,pos=0, room=0.1, sample=3)
p3 >> loop("hiphop16", dur=16,pos=0, room=0.1, sample=0)
g2 >> loop("xtech8", dur=8, comp=1)
s3 >> play("X.")
s4 >> loop("xvermin16", dur=16, sample=4)
u9 >> loop("wa8", dur=8, comp=1, lofi=0, mverb=.1)
c9 >> loop("synth4", dur=4, amp=PBin(16), sample=6, mverb=0.5, echo=0.5, a=0.2)
# l5 >> varicelle([], dur=1/2,amp=PZero(16), a=0.4, oct=6, fx2=1, valad=500, valadr=0.3, valadd=5, valadt=0, valadc=0.3)

# bass intro
e9 >> loop("seq16", dur=16, sample=[2, 3, 4], comp=1, mverb=0.5)
# bass intro
e9 >> loop("seq16", dur=16, sample=5, comp=1, mverb=0.1).lclip(var([PRand([1,2,4,8])],32))
z4 >> loop("psych32", dur=32, sample=var(PRand(808), 32), fx1=0, fx=0, hpf=200).lclip(var([PRand([1,2,4,8])],32))
i5 >> loop("psydrum32", dur=32, sample=var(PRand(16), 32)).lclip(var([PRand([1,2,4,8])],32))
i4 >> loop("psybass32", dur=32,pos=0, amp=1, room=0.1, sample=var(PRand(16), 32), beat_stretch=1, looping=1.0, drcomp=0.1).lclip(var([PRand([1,2,4,8])],32))
y8 >> four(linvar([0,2],64), fx2=0, tremolo=P*[2,4,8], amp=.8, mverb=0.5, oct=4, shape=.3, pan=PWhite(-1, 1))
x8 >> play("<k.><.>", hpf=0, amp=2, drcomp=0.6)