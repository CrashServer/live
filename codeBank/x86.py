# x86 82
# interlude
Clock.bpm = 82
Root.default = "G#"

i1 >> dbass([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], lpr=0.1, oct=PStep(16, 5, (5, 4)), dur=8, amp=PCoin(1, 0, 0.25), crush=PWhite(0.1, 0.2), mix2=0, bits=0, fmod=4,lpf=4000, mid=4, spf=4, spfslide=4, chop=4, chopwave=1, chopmix=0.4, spfend=12200, hpf=0).every(8, "shuffle").unison(4)
i3 >> faim(var([[P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], (0, -2)]), dur=1/4, oct=5, amp=var([0, 1], [5, 7]), hpf=[400, 1600], chop=4, fmod=4, lpf=0).slider().solo(0)
i4 >> lbass([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 3, (4, 3)), dur=var([ [10, 1, 1, 1, 1, 1/2, 1/2, 1], [1/2, 1/4, 1/4, 1/2, 1, 1/2, 1, 12]]), echo=[0.5, 0.25], echomix=[0.25, 0.5, 0.25], amp=1,octer=0.1, bpf=1200, octersub=0.1, octersubsub=var([0.1, PRand(1,4)], [15, 1]), dist2=1).slider().every(4, "shuffle")

j0 >> loop("break16", dur=8, dist2=(1), sample=4, amp=[0, 1, 0.5, 1, 1], shift=[0, 1], hpf=100, hpr=0.9)
j1 >> glitchbass([0], oct=PStep(4, 5, [6, 3]), dur=[1, 1/2, 1/2, 1, 1/2, 1/2], vib=0.015, leg=12, cut=1/2, bpf=[400, 1200])
j2 >> play("[xBo[B+]]", dur=j1.dur*PRand([1/2, 1, 2]), sample=5, lpf=4480, hpf=60, lpr=0.2, amp=0.8)
j4 >> loop("hiphop8", dur=8, sample=1, dist2=2)
