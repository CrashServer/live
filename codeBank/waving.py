# waving 130
# todo
s1 >> sine(linvar([0,12],48), dur=0.1, oct=3, amp=sinvar([0,0.25,0],48), sus=3, lpf=2000, fbdelay=0.5)
s2 >> sine(linvar([0,12],48), dur=0.1, oct=4, amp=sinvar([0,0.25,0],48), sus=3, lpf=3000, delay=12, gate=0.5)
s3 >> sine(linvar([0,12],48), dur=0.1, oct=5, amp=sinvar([0,0.25,0],48), sus=3, lpf=5000, delay=24)
s4 >> sine(linvar([0,12],48), dur=0.1, oct=6, amp=sinvar([0,0.25,0],48), sus=3, lpf=8000, delay=36)
