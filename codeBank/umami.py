# umami 170
# drums
Clock.bpm = 170
Root.default = var([3, 8, 4, 11], 4)
g3 >> play("xGx", sample=1, dur=4, mverb=0.5)
g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.4, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
g3.mverb=0
g7 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), rate=2, amp=0.7, cut=PWhite(0.5, 1), sample=PRand(20), dur=1/2, lpf=0, leg=10, krush=0).sometimes("stutter").slider()

g4 >> play("-", sample=7,  rate=linvar([PRand([1, 2, 4, 8, 16]), 1], PRand([1, 2, 4, 8])), dur=var([PRand([4, 16, 32]), 1/4]))
g5 >> play(PRand("fff".replace("f", "{o--}")), rate=1, sample=PRand(20), dur=1/4, amp=0.6, lpf=0, leg=200, krush=P*[0,8]).sometimes("stutter").slider()
g6 >> play("o ", sample=4, dur=PDur([0, 0, 3], 8), rate=[2, 4], hpf=4000, shift=0.5)

a4 >> play(".//.", dur=4, sample=5, rate=[-0.5, 0.25, -0.125], chop=4, hpf=1400, mverb=0.5, echo=0.5, delay=PRand([0.25, 0.5, 0.75]))
g_all.rate=var([12, linvar([12, -12])], [2, 4])

g_all.shift=var([0,  linvar([PCoin(12, 1, 0.25), PCoin(1, 12, 0.25), 24])], [48, 4])
g_all.dur=var([1/4, linvar([PCoin(1, 1/8, 0.25), PCoin(1/8, 1, 0.25)], 16)], [24, 4])
g_all.rate=var([1, PWalk(8, 4, 1)], PRand(16))

a4 >> play("x ")

g_all.dur=var([1/4, 4], PRand(16))
# silence attente

g5.degree="b"
g5.rate=[1, 1, 1.2, 1]
g5.sample=PRand(8)
g_all.dur=1/2
g_all.rate=1

g5.drive=0.2
#Groove

g1 >> play("Xx{x.x{--}.}")
g3 >> tb304(dur=1/4, oct=5, delay=0.25, shape=0.5).unison(4)


# alternate with g3 under this 
l5 >> play("X ")
k5 >> play("C...", dur=2, amp=3, leg=4, echo=0.5)
~g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.4, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
k6 >> play("c.{cC}.", sample=7, tanh=0.2, formant=1, dur=2, amp=2, leg=8, echo=0.456)
k7 >> play("X ", amp=1)

drop()

g3.shape=1
f8 >> play("g", dur=4).solo(8)

m4 >> play("j ", sample=6, formant=1, rate=3, dur=[2, 4, 8])
d1 >> play("W ", drive=0, dur=4, bpf=80, bpr=0.9, amp=PMorse("thisiskickistooloud"),vol=0.5, slide=[0, -4], rate=var([1, linvar([1, 0.2], 4)])).unison(4)
d8 >> play("@ ", dur=PDur(1, 15, 4), echo=0.25)
d2 >> brown(dur=8, cut=1/2, room2=0.2, chop=4, damp2=0.2, fold=0.5, lofi=0.5, hpf=4000)

k4 >> play("X ", amp=2, sample=6).often("stutter", 8, rate=PWhite(0.5, 4))
l6 >> play("..U.", sample=4, amp=4)
m8 >> play("[--]{[--][-]}", sample=9)

k7 >> play("X ", amp=4, lpf=400)
