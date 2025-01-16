#depths
y1 >> plaitsX([0,[P+[7,5], P+[1,2,PRand(8),7]]], preset=(11,12), dur=16, oct=(2,3,PStep(5,5,4)), dfm=PRand(900,5200)*1, dfmd=1, tremolo=PStep(8,4,0), tremolo_=0.5, dfmr=0.69, fdecay=1, mverb=0.8, amp=1)
p1 >> plaits(P[0,4,8,7], dur=1/4, oct=(3,4), harm=0.0, timbre=0.6, morph=0.94, engine=1, fdecay=1.8, cutoff=9000, bright=PFr(0.9,0.99), aux=0, porta=0.09, dist2=0.6) + var([0,7],8)
