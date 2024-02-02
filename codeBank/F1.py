# F1
f1 >> loop("half16", dur=16, sample=2 , lpf=0)
f2 >> loop("xtbass16", dur=16, sample=0, amp=1)
f3 >> loop("noizebeat16", dur=16, sample=3, amp=[0.5, 0])
f4 >> loop("noizebeat16", dur=16, sample=4, amp=[0, 1], chop=4)
f5 >> play("<[--]><..U(..[UU])><..o.><.:>", amp=1, sample=4, room2=1, mix2=0.3, revsus=0.5, revatk=-0.3).sometimes("stutter", 4)
f6 >> play("..C.", amp=1)
f7 >> play("V ", sample=2, amp=1).sometimes("stutter")
f8 >> loop("ragegtr16", dur=16, sample=1, amp=0.5, room=0)
