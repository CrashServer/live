# glitch
# noise
c1 >> glitcher(oct=PRand(8), rate=PWhite(1, 128), amp=1, dur=8, len=PWhite(1, 16), henA=PWhite(0.01, 4), fmod=0, henB=PWhite(0.1, 0.2), t=[2, 4, 6, 8, 32], crush=PRand(16),bits=16, shape=4.0).unison(2)
