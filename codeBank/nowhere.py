# nowhere # 122
# epic

#still not epic
# pretty much really really brouillon as fuck. 
d3 >> pianovel(dur=8, degree=[0,2,4], oct=6, amp=linvar([0.5,1.0],32), sus=8, atk=4, lpf=linvar([200,800],64), mverb=0.0, vol=1.4).every(2, "stutter", degree=PRand([0, -2, -4, -8]))
d2 >> prof(dur=4, degree=[0,7], oct=6, amp=linvar([0,0.15],16), sus=4, atk=2, rq=0.02, mverb=0.8, shimmer=0.6, shimmix=0.3)            
d3 >> pianovel(dur=1/2, degree=[0,2,4, 7, 12, 3, 5], oct=6, amp=linvar([0.5,1.0],32), sus=8, atk=4, lpf=linvar([200,800],64), mverb=0.0, vol=1.4)
d4.unison(1)
d3 >> bell(dur=8, degree=[0,1,4], oct=4, amp=0.3, sus=8, atk=2, lpf=linvar([800,2000],32), mverb=0.7) 
d3 >> pianovel(dur=1/2, degree=[0,2,4, 7, 12, 3, 5], oct=6, amp=linvar([0.5,2.0],32), sus=8, atk=4, lpf=linvar([200,800],64), mverb=0.0, velhard=PRand(0, 60), vol=1.4).unison(4)
d2 >> darkpad(dur=PDur(3,8), degree=[0,7,4,7,0,11], oct=6, amp=0.15, sus=1, atk=0.5, rq=linvar([0.02,0.005],32), mverb=0.8, shimmer=0.6)  

d3.stop()
d8 >> tb303([0,0,3,0, 0,5,0,3], dur=0.25, oct=4, lpf=400, sus=0.15, cutoff=linvar([400,2000],8), rq=0.15, shape=0.6, amp=var([0,2],[8,8]), leg=12, mverb=0.5)
d4 >> dbass(0, feed=0.3, dur=8, sus=8, dublen=0.8, dubd=0.2, mverb=0.0, dafilter=200, lpf=80, oct=(4,3), shape=0, dist2=0, valad=1500,    valadr=0.5, valadd=5, valadt=0, valadc=0.3).unison(3)   

d4 >> bell()
d5 >> plaitsX([4,5,6,4, 5,8,6,3], dur=[0.5,0.25,0.25,0.5, 0.25,0.25,0.5,0.5], oct=7, sus=0.46, shape=1.0).unison(8) + var([0, 3], 8)

d7 >> plaitsX([4,5,6,4, rest(0),8,6,rest(0), 5,3,6,8, 4,rest(0),5,6], dur=0.25, oct=7, sus=[0.06,0.12,0.06,0.2, 0.06,0.06,0.12,0.06],  shape=var([0.4, 0.8], [6, 2])).unison(8) + var([0, 3, -2, 3], [8, 4, 4, 8])   

d4.stop()
d7 >> faim([0,0,rest(0),0, rest(0),3,0,rest(0)], lpf=1200, dur=0.25, sus=0.11, oct=4, pick=0.95, cutoff=var([600,1800],[4,4]), fold=0.0,           shape=0.0, amp=1.5)                               

d1 >> dbass(0, dur=4, sus=2, oct=3, amp=linvar([0,0.4],16), lpf=60, shape=0)                       
d2.stop()
t8.stop()
d5.stop()
d4 >> dbass([0,0,3,0, 5,rest(0),0,3, 0,7,0,rest(0), 3,0,5,0], dur=0.25, oct=6, sus=0.3, shape=0, dist2=0, lpf=linvar([800,3000],16),    feed=0.2, mverb=0.4).unison(3) + var([0,3,-2,3],[8,4,4,8]) 

d4 >> dbass(0, feed=0.5, dur=8, sus=8, dublen=0.2, dubd=0.4, mverb=0.5, dafilter=400, lpf=400,oct=(5, 4), shape=linvar([0, 0.8], 32),  dist2=var([0, 0.9], [24, 8]), valad=1500,valadr=0.5, valadd=5, valadt=0, valadc=0.3).unison(4)                                  

d4.stop()

d4 >> dbass(0.0,feed=0.5, echo=[0.2, 0.4, 0.3, 0.6], dur=8, dubd=0.4, sus=8, dublen=0.2, mverb=0.5, dubl=0.1, lpr=0.2, dafilter=400, lpf=linvar([200, 1200], 32), oct=(6, 5, 4), shape=0.0, dist2=0.0, valad=1500, valadr=0.5, valadd=5, valadt=0, valadc=0.3).unison(4)


d4 >> dbass(0,feed=0.5, echo=[0.2, 0.4, 0.3, 0.6], dur=8, dubd=0.4, sus=8, dublen=0.2, mverb=0.5, dubl=0.1, lpr=0.2, dafilter=400, amp=0.5, lpf=linvar([200, 1200], 32), oct=(6, 5, 4), shape=0.0, dist2=0.0, valad=1500, valadr=0.5, valadd=5, valadt=0, valadc=0.3).unison(4)
d9 >> play("X ", lpf=2400, amp=4, sample=8, leg=1, lofi=0)
d5 >> dbass(PTri(0, 8), dur=var([0.25, 0.125], [8, 4]), oct=var([5, 8], [12, 4]), sus=0.22, shape=0.7, lpf=linvar([1200, 6000],  16)).unison(8) + var([0, 3, 5, -2], 4)                       
d4.lpf=200
d5 >> dbass([4, 5, 6] ,dur=1/2, oct=7).unison(8) + var([0, 3], 8)                                 
d8 >> tb305([0,0,3,0, 0,5,0,3], dur=0.25, oct=5, sus=0.15, cutoff=linvar([400,3500],16), rq=0.1, shape=0.8, amp=var([0,2],[8,8]))                                                                        
d8 >> tb305([0,0,3,0, 5,rest(0),0,3, 0,7,0,rest(0), 3,0,5,0], dur=0.25, oct=5, sus=[0.15,0.1,0.3,0.1], cutoff=linvar([400,4000],8), rq=0.08, shape=0.8, amp=var([0,2],[8,8]))                                    
d8 >> tb304([0,0,3,0, 5,rest(0),0,3, 0,7,0,rest(0), 3,0,5,0], dur=0.25, oct=var([5,6],[12,4]), sus=[0.15,0.1,0.3,0.1],  cutoff=linvar([800,6000],8), rq=0.05, shape=0.9, amp=2)                   

d4 >> dbass(0, feed=0.7, echo=[0.2,0.4,0.3,0.6], dur=8, dubd=0.6, sus=8, dublen=0.4, mverb=0.5, dubl=0.2, lpr=0.2, dafilter=300, amp=0.5, lpf=linvar([100,800],32), oct=(6,5,4), shape=var([0,0.5],[16,16]), dist2=0, valad=1500, valadr=0.5, valadd=5, valadt=0,          valadc=0.3).unison(4)                                                                                                                   
 d4 >> dbass(0, feed=0.5, echo=[0.2, 0.4, 0.3, 0.6], dur=8, dubd=0.4, sus=8, dublen=0.2, mverb=0.5, dubl=0.1, lpr=0.2, dafilter=400,     lpf=linvar([200, 1200], 32), oct=(6, 5, 4), shape=linvar([0, 0.8], 32), dist2=var([0, 0.9], [24, 8]), valad=1500, valadr=0.5, valadd=5,   valadt=0, valadc=0.3).unison(4)                                                                                                                                           
                           
