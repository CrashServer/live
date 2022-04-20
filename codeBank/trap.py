# trap
d0 >> play(".{...u}..u...", sample=5, hpf=var(PRand(4000)+10), rate=(.5,2)).sometimes("stutter")
d1 >> play(".{...c}..c...", sample=5, mverb=0, flanger=0, chorus=var(PWhite(0, 1)), amp=P*[0, 1], rate=(P*[.5,.5,.5,-1],2))
d2 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, drive=(0,var(PWhite(0,0.2)))).sometimes("stutter")
d3 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d4 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=4, crush=8,bits=8)
d5 >> play("-{-[--]}-.-{[---][--]}(-.)(-[----])", sample=2, amp=PCoin(PWhite(0, 1),0,0.5), hpf=6000, pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble").sometimes("stutter", PRand(16), rate=PWhite(-1,5))
d6 >> play("---.-{[---][--]}(-.)(-[----])", hpf=5000, sample=10, amp=PCoin(PWhite(0, 1), 0, 0.5), pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble")
d7 >> play("---.-{[---][--]}(-.)(-[----])", pan=PWhite(-1, 1), hpf=4000, amp=PCoin(PWhite(0, 1), 0, 0.5), sample=8).sometimes("amen").sometimes("bubble").every(4, "shuffle")