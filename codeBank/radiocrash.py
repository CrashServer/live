# radiocrash
# Cover

Scale.default="major"
Root.default="Db"
Clock.bpm = 76
Clock.meter=(3,2)

i1 >> pluck((const(0), PRand(12).rnd(2), PRand(8)), rate=PWhite(0,1), atk=PWhite(0,4), oct=(3,4), dur=PRand(4,16), rel=PWhite(0,8), sus=16, decay=PWhite(0,8), blur=PRand(4), lpf=8000, triode=1, amp=1, room=1, mix=0.3).unison(3,linvar([0.02,0.25],128),99)
y1 >> play("K", sample=PRand(9), rate=(PWhite(-1,-0.3),PWhite(0.1,1)), dur=PRand(3,17), hpf=60, crush=4, room=1, mix=PWhite(0.4,0.7), lpf=1800, pan=(PWhite(-1,1),PWhite(-1,1)))

p1 >> pianovel([var([(P*[-2,-9],0,5),PRand([(-2.5,-1,5),(-2.5,5),(-5,2.5,-1,5)])],[6,12]),-1,0,-1,0,-1,P*[0,-5],PwRand([5,6,3,-1,P+[5,6,3]],[3,3,3,3,1])], oct=(4.99,5.01), dur=[1,1,1,1,1/2,1/2,1/2,1/2], delay=PWhite(-0.025,0.025), lpf=var(PRand(800,2800),12), lpr=PWhite(0.4,0.8), velhard=PWhite(0.5,0.7), velocity=PRand(38,var([80,60],[1,5])), amplify=var([0,1],[PRand(6),PRand(24)]), room=1, mix=PWhite(0,0.4)).sometimes("stutter",amplify=1, velhard=(1, 0.1), oct=(5, 6), delay=0.125).sometimes("pivot", 5)

b3 >> pianovel(var([-2,0,5,[2,-4]],6), oct=3, dur=6, lpf=1200, hpf=100, velocity=PRand(70,80))
b1 >> faim(var([0,-4,-5,2],[12,12,6,6]), dur=PDur([[9,3],5],12), lpf=PRand(1200,3800), hpf=100, oct=PStep(6,4,3), amplify=PWhite(0.8,1.2)) + var([0,const([-2,2])],[5,1])
p9 >> donk((0, 0.5, [-0.5, 1]), delay=(0, 0.5, 0.75), dur=3, rate=P*[1, 2, 4, 8], room=PWhite(0.5,1), mix=PWhite(0.3,0.8), pan=(PWhite(-1,1),PWhite(-1,1)), hpf=PRand(60,580)).often("stutter").accompany(b1)

s1 >> dab(-2, dur=8, lpf=PRand(800,2000), fmod=PRand(8).rnd(2), oct=PStep(3,6,5), amp=0.5).every(4, "rotate").unison(3,0.25,99).after(8, "only")
d1 >> play("<K..><I...><..O.><[--]><.(.:)>", sample=P[0:9], amp=0.8, cut=PWhite(0,2), rate=(1,PWhite(-1,2))).sometimes("stutter", PRand(8)).every(16, "sample.rotate", PRand(8))
d2 >> play("<X.>", sample=1, amplify=2).every(4, "stutter", PRand(8))
n1 >> dafbass(linvar([0,0.3],[128,0]), dur=PDur([6,8,5],8), oct=[5,6], amplify=[0.5,0,d2.degree!="X",0.2,0.8], fmod=PRand([0,2,PRand(8)])).unison(3)
