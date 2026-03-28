# third 133
# launch

Clock.bpm = 133;
Root.default = "D#"
k0 >> dbass([3, 4, 4, 8, 4, 7, 4, [4, 5]], scale=Scale.chromatic, dur=1/3, rate=([4, 2, 1, 0.5], 0.1), lpf=1200, hpf=[1200, 400, 300, 600], lpr=0.4, lofi=PSine(256) + 0.5).every(5, "stutter", rate=0.25, oct=6)
d2 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], oct=P[5, 6], scale=Scale.chromatic, flanger=[0.7, 0.9, 0.8, 0.7], dur=var([1/3, 2/3], [15, 6]), echo=1/3).unison(4).sometimes("shuffle").sometimes("amen").sometimes("stutter", 4, oct=6, shape=1)
k0 >> play("-", dur=2, sample=8, echo=0.33, lpf=500)
e1 >> play("x ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1))
k0 >> dbass([3, 4, 4, 8, 4, 7, 4, [4, 5]], scale=Scale.chromatic, dur=1/3, rate=([4, 2, 1, 0.5], 0.1), lpf=1200, hpf=[1200, 400, 300, 600], lpr=0.4, lofi=PSine(256) + 0.5).every(5, "stutter", rate=0.25, oct=6, resonbank=0.1, csweep=0.4, cswfreq=230, cswdepth=0.5, cswrate=0.5, cswdecay=0.5, rbfreq=70, rbdecay=0.5, rbspread=1.0)
e1 >> play("x ", sample=4, hpf=40, amp=1, lpf=4000, mverb=(0, 0.1))
d2 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], oct=P[5, 6], scale=Scale.chromatic, vowel=fi(16, 1, 4), vowelf=2, vowelq=1, flanger=[0.7, 0.9, 0.8, 0.7], dur=var([1/3, 2/3], [15, 6]), echo=1/3).unison(4).sometimes("shuffle").sometimes("amen").sometimes("stutter", 4, oct=6, shape=1)



