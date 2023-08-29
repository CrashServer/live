Clock.bpm = 135;
c1 >> loop("xtech8", dur=8, sample=8, hpf=var([0, 200], [6, 2]), hpr=linvar([0.1, 0.9],8))
c0 >> loop("xtech8", dur=8, sample=8, lpf=var([10000, 200], [2, 6]), lpr=linvar([0.1, 0.9],32))
c3 >> loop("uk8", dur=16, sample=2, mverb=0.6, dist2=0) #0-3 -2
c4 >> play("x-", fx1=1, sample=P[0, 1], fx2=1, valad=0, amp=4, leg=PFrac(0.3,0.8,8).lmap(4, 1), valadr=0).solo(0)
c6 >> loop("xtech8", dur=16, sample=2)
c7 >> play("XCk-")
c8 >> loop("hiphop16", dur=32, sample=3)
c9 >> play("<b.><....W.......W...><W..W...W.WW.....>", dur=0.25, sample=56, rate=1)
c1 >> donk(P[0, 4, 5, 7], dur=PDur(8,8), oct=[6, 5, 3, 3, 4], rate = linvar([[4.15, 9.01, 10.48, 5.15, 3.02],[10.2, 3.56]],[15.69, 1.96, 26.38, 28.15]), leg=32)
c2 >> donk(P[2, 4, 2, 0, 0, 7, 0, 4, 2, 0, 2, 5, 7, 0, 0, 4], dur=SDur(16), oct=[3, 3, 6, 5, 6, 3], rq = linvar([[0.38, 0.2],[0.17, 0.5, 0.43]],[29.81, 11.72]), )
c3 >> pad2((0,2,var([4,5,7,-2],8)), dur=8, atk=2, blur=1.2, oct=([2, 4, 3],6), fx2=1, rate=8, amp=0.7, chop=4).unison(2)
