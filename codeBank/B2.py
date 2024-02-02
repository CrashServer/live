# B3_135
Clock.bpm = 135;
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=3, feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.01)
