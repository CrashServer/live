# Postri 112
# mud, chaosbits
Clock.bpm=112
Root.default="A"
Scale.default="minor"

v2 >> guit(P[0, 2,4], dur=1/3,formant=PStep(8,PRand(5),0), formantmix=0.3,  oct=(4,5), detune=0.01, tone=0.8, beef=0.5, fdecay=0.2, mod=0.3, amp=.8, mverb=.2).unison(3) # + [0,0,0,2]

m9 >> faim(var([0, -2, -4, -5],[12, 6, 3,3]), oct=(3,4), dur=8, shape=.2, shape_=.8, beef=2, hpf=50)
d0 >> play("-{-=}", dur=1/3, sample=[1,2,4], pan=PWhite(-1,1))
k9 >> play("k", dur=P*[1,2,6]/3)
w5 >> play("o...", dur=1/3, rate=1, sample=12, high=2, room2=0.9, mix2=0.3, damp2=0.2, revatk=0.2, revsus=0.4)
k5 >> play("X", dur=P[2]/3)

# attention au cpu
o6 >> choir(PChords(VI), oct=(3,4,P*[5,5]),rel=.1,  atk=2, dur=8, bendc=0.1, vow=PTuple(PWhite(5), 3), amp=.8, eb=0.75, ebfeed=0.7, ebmix=0.3, ebmode=1, ebwow=.2, ebflutter=.15, ebsat=0.3, fx2=1)

