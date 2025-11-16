# G1 72
# interlude
Clock.bpm=72
Root.default=3

g1 >> play("V ", sample=4, lpf=1200)
g2 >> dbass(dur=1/4, drive=PStep(9, 1,0), rate=linvar([2, .1],[64,0]), lpf=PFr(500,2200)).unison(4)
g3 >> play("[--]", sample=4, pan=PWhite(-1,1)).human(60, 10)
g4 >> loop("noizebeat16", dur=8, sample=4, amp=[0.5, 0.5, 0, 0.5])
g5 >> loop("noizebeat16", dur=8, sample=6, amp=[0, 0, 0.5, 0])
g6 >> loop("noizebeat16", dur=8, sample=5, amp=[0, 0, 0, 1])
g7 >> play("..C.", sample=4, amp=2, room2=linvar([0, 1], 8), feed=0, revsus=linvar([1, 4], 4),hpf=400)
g8 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=0, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
g9 >> play("<Oo><[Pp.@]>", sample=PRand(8), cut=PRand([1/2, 1/4, 0]), krush=PRand([0, 12]), bits=PRand([2, 12, 0]), crush=(8, 1), amp=1, lpf=PRand([1200, 3200, 15000]), hpf=4000)
