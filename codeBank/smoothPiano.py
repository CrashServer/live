# smoothPiano 98
# interlude

Clock.bpm=98
Scale.default="mixolydian"
Root.default=var(P*[0,4,8],[32,55,15])

p1 >> pianovel(Pvar(PRand([list(VIIsus2),list(VIsus2),list(Vsus2),list(IVsus2)]),8), oct=[3,[4,5]], dur=1/2, velocity=PRand(50,79), mverb=.5, chop=0, mpf=var([900,400,2800,1235,180], [5,8,2,13])).every(16, "rotate")

p2 >> pianovel(p1.degree[0], dur=[6,2], oct=[3,4], mpf=800)

p3 >> pianovel(PChords(), dur=[12,4], oct=[5,(5,6),5], room=1, mix=0.3, velocity=PRand(59,99), pan=(-1,1))

rb >> play("<(v...)(v..(.v))(...(.v))(..v.)><(.r)...><-.><.+><...(.(.:))>", dur=1/2, sample=(2,PStep(9,5,9),0,1,3), lpf=linvar([780,17800],[128]), room=PStep(13,1,0), mix=0.7).sometimes("stutter", PRand(2,4))