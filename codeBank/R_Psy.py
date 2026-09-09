# R_Psy
# R_

Clock.bpm=168
# p1 >> loop("uk16", dur=16,pos=0, room=0.1, sample=3)
p3 >> loop("hiphop16", dur=16,pos=0, room=0.1, sample=0)
g2 >> loop("xtech8", dur=8, comp=1)
s3 >> play("X.")
s4 >> loop("xvermin16", dur=16, sample=4)
# c9 >> loop("synth4", dur=4, amp=PBin(16)*0.8, sample=6, mverb=0.5, echo=0.5, a=0.2)
l5 >> varicelle(PTime(), dur=1/2, amp=PTimebin(), a=PWhite(0.001, 0.4), oct=6, fx2=1, valad=300, valadr=0.3, valadd=5, valadt=0, valadc=0.1, pan=PWhite(-1,1), echo=.25).end(4,16)
# z4 >> loop("psych32", dur=32, sample=PRand(111), fx1=0, fx=0, hpf=200, mverb=0.2)
# o4 >> play("z", dur=8, sample=PRand(8), echo=0.5, mverb=0.5, fx2=1)
i5 >> loop("psydrum32", dur=32, sample=var(PRand(202),64))
i0 >> loop("psybass32", dur=32,pos=0, amp=1, room=0.1, sample=var(PRand(808),64), beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.1)
e9 >> loop("seq16", dur=16, sample=0, comp=1, mverb=0.1).lclip(var([PRand([1,2,4,8])],32))
y8 >> four(linvar([0,2],64), fx2=0, tremolo=P*[2,4,8], amp=.8, mverb=0.5, oct=5, shape=.3, pan=PWhite(-1, 1))
x8 >> play("<k.><.>", hpf=0, amp=2, drcomp=0.6, sample=0)
