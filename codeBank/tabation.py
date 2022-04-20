# tabation
cl >> click(0, dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), hpf=40, drive=[PWhite(0.4,0.8),0.2], oct=(3, PStep(9,5,4)), octer=1, octersub=2, octersubsub=var([2, PRand(15,2222)], [15, 1]), triode=4, amp=0.1, amplify=1).unison(3).rarely("stutter",PRand(6), oct=6, pan=[-1,1], mpf=2860, hpf=400)
db >> bass(0, dur=c1.dur, leg=12, amp=var([0.5, 0], [12, 4]), rate=PWhite(0.01, 0.2), sus=db.dur*1.5).unison(2)
n1 >> play("<u><t>", sample=(2,P[0:5]), delay=(0,(0,[0,0.25])), dur=cl.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=n1.crush*1500)