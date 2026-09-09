# B2 135
# drone

Clock.bpm = 135;
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=3, feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.01)

#@intro(32)
Clock.bpm = 135;
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=3, feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.01)

#@build(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=3, feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.02)

#@peak(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=3, feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.03)

#@break(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.03)

#@drop(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.04)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.05)

#@outro(8)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.05)

#@part7(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.6, dublen=0.05)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, dublen=0.05)

#@part8(8)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1 dublen=0.05)

#@part9(32)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@part10(32)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.1, rbfreq=50, rbdecay=0.5, rbspread=1.0, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@part11(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.1, rbfreq=[50, 50, 48, 48], rbdecay=0.5, rbspread=1.0, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@part12(8)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.1, rbfreq=[50, 50, 48, 48], rbdecay=0.5, rbspread=1.0, rgate=1, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@part13(32)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.2, rbfreq=[50, 50, 48, 48], rbdecay=0.5, rbspread=1.0, rgate=1, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.2, rbfreq=[50, 50, 48, 48], rbdecay=0.5, rbspread=1.0, rgate=1, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@part14(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.2, rbfreq=[50, 50, 48, 48], rbdecay=0.5, rbspread=1.0, leg=4, rgate=1, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@part15(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.2, rbfreq=[50, 50, 48, 48], rbdecay=0.5, rbspread=1.0, leg=4, chop=4, rgate=1, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@part16(16)
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/2], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=(3, 4), feed=[0.5, 0.33, 0.33, 0.33], dubd=0.7, resonbank=0.2, rbfreq=[50, 50, 48, 48], rbdecay=0.5, rbspread=1.0, leg=4, chop=4, chopmix=0.5, rgate=1, rgaterate=4, rgatewave=0, beat_dur=1, dublen=0.05)

#@end(16)
