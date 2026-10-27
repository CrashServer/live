Clock.bpm = 111
Scale.default = Scale.dorian
Root.default = "C"

# Track 1 (drums)
d1 >> play("x", dur=PStutter([2,6,2,18,2,18,2,1],[29,1,31,1,23,1,31,1]), delay=1)
d2 >> play("-.-.-.-.-.-.-.--", dur=1/4, delay=1/8)
d3 >> play("+", dur=2, delay=1)

# Track 2
d4 >> pluck([4,3,4,6,1,0,1,3,6,5,6,1,4,5,6], dur=PStutter([2,1/2,3,1/2,3,1/2,3,1],[1,3,1,3,1,3,1,2]), sus=PStutter([3/2,1/4,2,1/4,2,1/4,2,3/4],[1,3,1,3,1,3,1,2]), oct=PStutter([5,4,5,4],[8,3,1,3]))

# Track 3
b1 >> pluck(1, dur=[1/2,3/4,3/4,1,1], sus=1/4)

# Track 4 (drums)
b2 >> play("v", dur=[3/4,1/4,3/2,1/4,1/2,1], delay=1/8)

# Track 5 (drums)
p1 >> play("x", dur=1, delay=1/8)

# Track 6
p2 >> pluck(4, dur=1, sus=1/2, oct=3)

# Track 7
p3 >> pluck(1, dur=48, oct=8)

