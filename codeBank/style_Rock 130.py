# style_Rock 130
Clock.bpm =130
Scale.default="minor"
Root.default = "E"

b1 >> pbass(var([0, 0, 7], [2, 1, 1]),dur=1/2, oct=PStep(4,4,3), valad=500, valadr=linvar([0.1, 0.8], [32, 0]), valadd=25, valadt=0, valadc=0.3, drive=0.1, rate=0.9, hpf=30)
e3 >> guit((P*[0,-2], P*[2,10,12,3],P*[5,7]), dur=var(P*[1, 1/2, 8], 8), oct=(5,6), rate=0.4, drive=0.5, mod=.4, amp=0.3, echo=0, eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3)
k1 >> play("<k(...(...k))..><..u.><-><.s.>", drcomp=.5).sometimes("stutter")
k2 >> play("{tTmM}").fill()
b9 >> soprano((0,2,7), dur=4, amp=0.6, mverb=.7)
