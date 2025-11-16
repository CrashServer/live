# oxydation 175
# interlude

Scale.default="yu"
Clock.bpm = var([175,175/4],[56,8])
f1 >> pluck(var(PChords(),8), dur=PRand(1,8)/PRand(1,4), blur=PWhite(1,4), decay=PRand(1,4), oct=(3,4,PStep(7,6,5)), drive=PWhite(0,0.1), sus=PRand(1,16), atk=PStep(8,0.2,PRand(1,6)), room2=1, mix2=0.6, damp2=PWhite(0.1,0.5), revatk=PWhite(0.2,2), revsus=PWhite(1,4), hpf=160, lpf=PRand(1800,9065), amp=0.3).unison(4,0.25)

jb.shape=0
jb >> jbass([f1.degree[0],f1.degree[2]], dur=[6,2], amp=1, oct=[5,6,5], glide=P[0:8]*PRand([-1,0,1]), glidedelay=PWhite(0.7,0.99), shape=[0,PWhite(0,1),0.2,0,0.3], echo=(jb.shape>0)*jb.dur/PWhite(0.1,4), echotime=jb.degree, lpf=[4500,5500+jb.shape*1000], hpf=60).every(6, "unison", cycle=[0,4])

d3 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25).unison(3, 1,99)
d1 >> play("<x.(...(.x))><..(**.*).><..(.((CCC.).)..)><(-.)->", sample=4, amp=var([1,0,1],[13,1,1]), crush=PRand(8), dur=1/2).sometimes("stutter", PRand(16))
p1 >> blip(f1.degree[0] + (0,[2,4]), dur=[1/2,1/2,1/2,P*[0.5,rest(2.5)]], amp=(b1.sus<6 and (d1.degree[0]!="x")), amplify=d1.degree[1]!="*", oct=(5), rate=PRand(1,4), leg=PRand(0,8),glide=0.5, fmod=4, vib=PRand(2,16), sus=PWhite(0.5,1), echo=[0,0.25], lpf=PRand(400,8888), room=1, mix=PWhite(0,0.5)).unison(3).every(8, "mirror")
b1 >> sawbass(f1.degree[0], dur=8, sus=[8,PRand(1,8)], echo=1/2, mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01)).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))
