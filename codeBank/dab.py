# dab smooth
a4 >> abass([8, 4, 12], dur=8, lpf=3200, delay=0.5, sus=1/2, echo=0.25, echomix=2, mverb=0.3 + a4.degree==12, chop=0)
a3 >> abass((4, [0, [8, (8, 0, 4)]]), dur=4, lpf=800, oct=(5, 6), delay=1.25, sus=1, echo=0, mverb=0.5) 
b5 >> plaitsX(10, dur=[(16,8), 1/2, 1/2], lpf=(3200, 0), delay=(0.5, 1), oct=(2, 3), sus=1/2, echo=0, mverb=0.5).unison(2)
a5 >> plaitsX(12, dur=16, lpf=3200, delay=2, sus=2, echo=0, mverb=1)
a6 >> plaitsX((0, 4), dur=32, lpf=0, delay=4, sus=2, echo=0, mverb=1).slider()
a7 >> dab((0, 1, 4, 12, 8), mverb=0.5, dur=16, lpf=1200, lpr=0.2, a=0.5, amp=0.5).unison(4)
a9 >> abass(10, dur=[(16,8), 1/2, 1/2], lpf=(3200, 0), delay=(0.25, 0.5), sus=1, hpf=400, hpf_=3200, echo=0, mverb=0.5, a=0.8).unison(2)
