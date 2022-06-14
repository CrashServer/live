#intro
scene0
Clock.bpm=48

i5 >> ews(melody(), dur=8, oct=(3,4,5), detune=(PRand(4),PRand(8),PRand(16)), rate=(PRand(4),PRand(8),PRand(160)), cutoff=(PRand(200,2800),PRand(200,3800),PRand(200,4800)))

i4 >> play("{yYnNFlL}", sample=PRand(99), dur=PDur(3,8)*PRand([2,4,8,16]), pan=PWhite(-1,1), amp=linvar([0,0.5],[PRand(16,32),PRand(16,64)]), amplify=P*[0,1], rate=P*[1,PWhite(-1,4)], mverb=P*[0,PWhite(0.2,0.9)])

i1 >> eeri((melody()), oct=(3), dur=8, atk=0.05, blur=PWhite(1,2), rate=PRand(0,12), vib=PRand(12))
i2 >> eeri((melody()), oct=(4), dur=12, atk=0.05, blur=PWhite(1,2), rate=PRand(0,4), vib=PRand(32))
i3 >> eeri((melody()), oct=(5), dur=PRand(8,14), atk=0.05, blur=PWhite(1,2), rate=PRand(0,120), vib=PRand(62))

# bien apres
Clock.bpm=linbpm(128,512)

d1 >> play(".", dist2=0, amp=1, mverb=0.9, lpf=0).drummer()
b1 >> faim(Pvar([0,melody()],[6,2]), dur=1/4, amp=d1.degree[0]=="k", oct=4, dist2=0)

d2 >> play("x.", sample=3, lpf=400, amp=2)
