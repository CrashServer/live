# R_toto
# R_

Clock.bpm=168
f8 >> loop("beats8", dur=8, sample=5)
c1 >> loop("berlin8", dur=8, sample=4)
m0 >> loop("cinambi8", dur=8, sample=var([3,2],[24,8]), hpf=200)
v3 >> loop("circlebreak16", dur=16, sample=7, comp=1, sbrk=.5, sbrkdur=.5)
b4 >> loop("nbvarp16", dur=32, sample=6, hpf=120)

x4 >> loop("ragedrum16", dur=32, sample=5, amp=1, comp=1, fx=1)
r9 >> loop("electrodrum16", dur=16, sample=3, comp=1)
p6 >> play("<x.><.><..o.><k.>", sample=1, amp=1, bank=0).sometimes("stutter")
p6.bank=1
~x4 >> play("x ", sample=3, amp=9)

e9 >> loop("housebass24", dur=32, chop=0, sample=7, amp=0.5, hpf=0, fx1=0, a=0, octer=0, shift=0, octersub=à, octersubsub=1).unison(4).lclip(var([PRand([1,2,4,8])],32))

h2 >> play(".(.U)..", rate=PWhite(-.5,-1), fx2=1)
