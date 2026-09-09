# alvaa 128
# todo

Root.default = "A#"
Clock.bpm = 128
j1 >> alva([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=12, mod=0.1, hpf=0).unison(4)
j2 >> bass(dur=1/2, amp=j1.degree==4, oct=(6, 7), leg=40)
j1.dur=PDur([3, 5], 8)
j1.oct=2 # 4
j4 >> alva(dur=2, shape=2, a=0.5, hpf=linvar([20, 1500], 32), lpr=0.1)

# --- part 2: percussion bleeds in ---
d1 >> play("x..x.x..", dur=1/4, amp=var([0,0.8],[16,16]))
d2 >> play("..o...o.", dur=1/4, sample=3, amp=var([0,0.6],[24,8]))
d3 >> play("-", dur=1/4, amp=PWhite(0.1,0.4), hpf=6000, pan=PWhite(-1,1))
j1.hpf = linvar([0, 2000], 32)
j1.oct = var([(4, 5, 6), 2], [12, 4])

# --- part 3: counter + texture ---
j3 >> varsaw(j1.degree+2, oct=(4, 5), dur=1/2, lpf=linvar([800, 3000], 16), lpr=0.2, leg=8, amp=var([0, 0.5], [16, 16])).unison(2)
l1 >> loop("cinambi8", dur=8, sample=var([3, 4, 5], [8, 8, 16]), amp=0.5)
l2 >> loop("dnbfx16", dur=16, sample=var([4, 5, 6], [16, 16, 16]), amp=var([0, 0.6], [24, 8]))
j4.shimmer = var([0, PWhite(0, 0.2)], [16, 16])
j4.fbdelay = var([0, 0.1], [12, 4])

# --- part 4: full, bass heavy ---
j1.dur = PDur([3, 5, 7], 12)
j1.shape = var([0, j1.degree==2], [8, 8])
j2.oct = var([(6, 7), (4, 5)], [8, 8])
j2.amp = var([j1.degree==4, 0.8], [8, 8])
b1 >> bass(P*[12, 11, 4], dur=var([1/2, 1], [3, 1]), oct=var([(4, 5), 3], PRand([4, 8, 16])), leg=PRand(64), dist2=0.5, shape=0.3).unison(4)
d1.amp = 1
d2.amp = 0.8
d4 >> play("#...............#.......", dur=1/4, amp=var([0, 0.3], [32, 32]))
j4.dur = var([2, 1], [12, 4])

# --- part 5: strip back, j1 alone evolves ---
d1.amp = var([0.8, 0], [4, 12])
d2.amp = var([0.6, 0], [4, 12])
b1.amp = var([0.8, 0], [8, 8])
j1.dur = PDur(var([3, 7, 5], PRand([4, 8])), 12)
j1.oct = var([2, (4, 5, 6), (3, 6)], [8, 4, 4])
j1.leg = var([12, PRand(64)], [8, 8])
j1.hpf = linvar([0, 4000], 64)
j3.lpf = linvar([3000, 400], 32)
j4.hpf = linvar([1500, 20], 32)
