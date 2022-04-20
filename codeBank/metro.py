# metro
f1 >> faim([(0,12),15, P*(5,8,14), _, P*(3,7,12),_, P*(2,5,11),_, (0,12),15, P*((5,17),15,14),_, P*((3,15),14,12),_, (2,14), 11], dur=1.5, hpf=PRand(250,400), hpr=PWhite(0.2,0.5), sus=2.5, mverb=0, room=1, mix=0.3).gtr(1)
f2 >> faim([5,8,P*(10,8,7),7,P*(8,7,5),5, 7, 4], dur=1.5, drive=0.2, amp=0.5, room=1, mix=.5).gtr(5)
f2 >> faim([5,5,8,8,1,1,0,[0,-4]],dur=1.5).gtr(5) 
f3 >> faim(var([0,3,5],12), dur=0.5).gtr(1)
f4 >> play("<k..kk.><--(...[.-----])><..u>", sample=(9,5,9), amp=1).human(40,0).every(14, "stutter", PRand(1,6), cycle=16, degree=PRand(["u","-","k"]), amp=PWhite(0.3,1))