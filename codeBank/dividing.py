# dividing 91
# album_untitled 


Clock.bpm = 91
Scale.default = "minor"
Root.default = "E"

g1 >> guit((P*[0, -2, 5], P*[2, 10, 12, 3, 7], P*[5, 7, 10]), dur=var(P*[1/2, 1/4, 4], 8), oct=(5, 6), rate=0.4, mod=0.55, shape=0.6, amp=0.42, eb=0.6, ebfeed=0.65, ebmix=0.4, ebmode=2, ebwow=0.15, ebflutter=0.2, ebsat=0.45, hpf=180, lpf=fb(24, 1200, 5800), tubedrive=fperlin(32, 0.4, 1.2), tubewarm=0.5)
w1 >> lapin(([0, 7, 12, 10, 7, 5, 7, 0], 4), amp=var([0, 0.6], [PRand(6, 12), PRand(3, 8)]), dur=PDur(var([3, 5, 7], [8, 4, 4]), 8), sus=fperlin(16, 0.1, 0.5), oct=(5, 6, 7), rate=0.85, shape=0.0, fx1=0, fx2=1, tanh=0.3, fold=fperlin(32, 0.2, 0.6), lpf=fb([8, 4], 2000, 7000), octclean=0.3, ocup=0.6).unison(3, 0.2, 90)
b1 >> ebass([0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=linvar([1.4, 0], 32) * P[1, 0, 0, 0.9, 1, 0, 0.9, 0, 0.9, 0.85, 0.9, 0.85, 1, 0, 0.85, 0.9], oct=PStep(8, 4, 3), pick=0.45, cutoff=linvar([2400, 600], 32), decay=1.0, rel=0.18, fold=linvar([0.3, 0], 32), hpf=80, tanh=linvar([0.2, 0], 32)).penta()
b1 >> ebass(var([P[0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], P[0, 0, 7, 0, 5, 3, 0, 0, 0, 5, 7, 5, 3, 0, -2, -2]], [16, 16]), dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.6, 0, 0, 1.5, 1.7, 0, 1.5, 0, 1.5, 1.4, 1.5, 1.4, 1.7, 0, 1.4, 1.5], oct=PStep(8, 4, 3), pick=0.6, cutoff=fb(8, 1000, 3800), decay=1.0, rel=0.18, fold=fb(24, 0.2, 0.6), hpf=80, tanh=0.3, octclean=0.4, ocsub=0.3, ocup=0.5).penta()
w1.lpf=400

k1 >> play("<k(...(...k))..><..u.><-><.s(s.)>", drcomp=0.55, amp=1.2, shape=0.2).sometimes("stutter")
n1 >> play("..(.s)(s.)..(s.)", sample=4, dur=1/2, amp=P[0.55, 0.3, 0.5, 0.3, 0.4], hpf=400, delay=PSwing(0.05)).often("stutter", 3)

w1.lpf=100
g1.lpf=100
h1 >> play("-(--)-(--)-(--)-([--])", dur=1/2, sample=PStep(16, 1, 3), rate=PWhite(0.95, 1.08), amp=PWhite(0.25, 0.5), pan=PWhite(-0.4, 0.4)).degrade(0.15)
s1 >> play("<..o.><..o(.o)>", sample=3, bank=0, amp=0.95, hpf=200, room=0.15).human(40, 4)

b1 >> ebass(var([P[0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], P[0, -2, -1, 0, 3, 5, 7, 8, 7, 5, 3, 0, -1, -2, 0, 0]], [16, 16]), dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.5, 0, 0, 1.4, 1.6, 0, 1.5, 0, 1.5, 1.4, 1.5, 1.4, 1.6, 0, 1.4, 1.5], oct=PStep(8, 4, 3), pick=0.55, cutoff=fb(8, 800, 3200), decay=1.0, rel=0.18, fold=fperlin(16, 0.15, 0.5), hpf=80, tanh=0.25, lofi=fi(16, 0, 0.4)).penta()

i9 >> faim(b1.degree, dur=1/4, oct=6, sus=1/8)
o7 >> play("..[:::].")
w1.stop()
j3 >> loop("hiphop16", dur=16, sample=2)

g1.oct=4
b1.shape=0.5

k1 >> play("<X.><..><.X><..>", dur=1/2, sample=(0, 1), amp=0.9, hpf=40, lpf=2000, drcomp=0.5)                                            
h1 >> play("-...-...", dur=1/2, sample=PStep(8, 1, 3), rate=PWhite(0.95, 1.05), amp=PWhite(0.18, 0.32), pan=PWhite(-0.3, 0.3))                                                        
b1 >> ebass([0, 0, 12, 7, 5, 0, -2, -5], dur=2, sus=P[1.5, 0.6, 1.2, 0.4, 1.5, 0.5, 1.0, 0.8], amp=P[1.4, 0, 1.3, 1.2, 1.5, 0, 1.2, 1.4], oct=PStep(4, 4, 3), pick=0.4,f=linvar([800, 2200], 16), decay=1.5, rel=0.4, fold=0.2, hpf=80, tanh=0.15).penta()

g1 >> guit((P*[0, 5], P*[7, 10]), dur=4, oct=(5, 6), rate=0.3, mod=0.4, shape=0.4, amp=0.32, eb=0.55, ebfeed=0.6, ebmix=0.45, ebmode=2, ebwow=0.2, ebflutter=0.25, ebsat=0.5, hpf=180,lpf=fb(24, 1200, 4400), tubedrive=0.5, tubewarm=0.6)

s1 >> sinepad((0, 7), dur=8, oct=4, atk=4, sus=6, rel=2, amp=linvar([0, 0.45], 12), lpf=linvar([400, 2000], 16), room=0.7, mix=0.5)                                                   
                                                                                                                                                                                       
g1.stop()
i9.stop()
b1 >> ebass([0, -2, -3, 0, 7, 5, 3, 0, -2, -3, -4, -5, 0, 0, 7, 0], dur=1/4, sus=P[0.4, 0.05, 0.05, 0.4, 0.1, 0.1, 0.1, 0.5, 0.4, 0.05, 0.05, 0.05, 0.5, 0.05, 0.4, 0.5], amp=P[1.4, 1.2, 1.2, 1.5, 1.4, 1.3, 1.3, 1.5, 1.3, 1.2, 1.2, 1.2, 1.5, 0, 1.4, 1.5], oct=PStep(8, 4, 3), pick=0.5, cutoff=linvar([1200, 3600], 16), decay=1.0, rel=0.2, fold=fperlin(16, 0.15,  0.45), hpf=80, tanh=0.25, octclean=0.3, shape=0.6, ocup=0.4).penta()                                                                                                                             
c1 >> sinepad((0, 7, 12), dur=8, oct=4, atk=2, sus=6, rel=2, amp=0.5, lpf=linvar([2000, 4400], 16), room=0.8, mix=0.6)                                                                
                     
  
k1 >> play("<k(...(...k))..><..u.><-(.k)><.s(s.)>", drcomp=0.6, amp=1.25, shape=0.25).often("stutter")
n1 >> play("..(.s)(s.)..(s.)..(.s)..(s.)", sample=4, dur=1/2, amp=P[0.6, 0.3, 0.55, 0.3, 0.4, 0.35, 0.5], hpf=400, delay=PSwing(0.05)).often("stutter", 3)                            
h1 >> play("-(--)-(--)-(--)-([-=])", dur=1/4, sample=PStep(16, 1, 3), rate=PWhite(0.95, 1.15), amp=PWhite(0.32, 0.6), pan=PWhite(-0.5, 0.5)).degrade(0.12)                            
b1 >> ebass(var([P[0, 0, 0, 12, 0, 0, 7, 0, 0, 3, 5, 3, 0, 0, -2, 0], P[0, 0, 7, 0, 5, 3, 0, 0, 0, 5, 7, 5, 3, 0, -2, -2], P[0, 12, 7, 0, 5, 12, 3, 0, 7, 5, 3, 0, -2, 0, 7, 0]], [16, 16, 16]), dur=1/4, sus=P[0.6, 0.05, 0.05, 0.12, 0.45, 0.05, 0.15, 0.05, 0.35, 0.06, 0.06, 0.06, 0.5, 0.05, 0.25, 0.5], amp=P[1.7, 0, 0, 1.6, 1.8, 0, 1.6, 0, 1.6, 1.5, 1.6, 1.5, 1.8,   0, 1.5, 1.6], oct=PStep(8, 4, 3), pick=0.65, cutoff=fb(8, 1200, 4400), decay=1.0, rel=0.18, fold=fb(24, 0.25, 0.7), hpf=80, tanh=0.35, octclean=0.5, ocsub=0.4, ocup=0.6).penta()    

b1.oct=(4, 6)

                                                                             
f1 >> faim(var([0, 5, 7, -2], 4), dur=var([2, 1, 1, 4], [8, 4, 4, 4]), oct=(5, 6), beef=2, shape=0.5, amp=0.4, eb=0.55, ebfeed=0.5, ebmix=0.35, ebmode=2, ebwow=0.15, ebflutter=0.2, ebsat=0.4, lpf=fb(32, 1200, 4400), tubedrive=0.5)                                                                                                          

y1 >> klank(b1.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(5, 6), dur=P*[2, 4, 8], lpf=linvar([800, 4400], 128), lpr=0.1, amp=0.32, hpf=600, fdist=1, fdistfreq=PWhite(1200,  2400)).unison(2)                 
g1 >> guit((P*[0, -2, 5, 7], P*[2, 10, 12, 3, 7, 14], P*[5, 7, 10, 12]), dur=var(P*[1/2, 1/4, 2], 8), oct=(5, 6, 7), rate=0.45, mod=0.65, shape=0.2, amp=0.5, eb=0.65, ebfeed=0.7, ebmix=0.5, ebmode=2, ebwow=0.2, ebflutter=0.25, ebsat=0.5, hpf=180, lpf=fb(24, 1400, 6800), tubedrive=fperlin(32, 0.5, 1.4), tubewarm=0.55)                                           
m8 >> play("X[KK]", csweep=0.2, cswfreq=1200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)
j9 >> play("X ")

c8 >> play("[--]")
o7 >> play("[----]")
b2 >> dbass(b1.degree, dur=1/4, wshape=1, wgain=1, wmix=0.5, dist2=1, lpf=2200, lpr=0.2, dist2mix=1, dist2shape=0.1).unison(2)
b3 >> a_gesa(b1.degree, dur=2/3, oct=6, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, wshape=1, wgain=1, wmix=0.5, dist2=1, lpf=2200, lpr=0.2, dist2mix=1, dist2shape=0.1).unison(2)
b3.oct=4
c8.stop()
o7.stop()
