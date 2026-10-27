Clock.bpm = 96
Scale.default = Scale.major
Root.default = "C"

# TabIt MIDI - Track 1
d1 >> pluck(Pvar([(0,5),P[(0,5),(6,4)],(6,4)],[5,1,2]), dur=1/2, oct=PStutter([6,5],[11,5]))

# TabIt MIDI - Track 2
d2 >> pluck([4,5,6,2], dur=[1,3], sus=[1,3/4], oct=[2,2,2,3])

# TabIt MIDI - Track 3
d3 >> pluck(Pvar([(0,5),P[(0,5),(6,4)],(6,4)],[5,1,2]), dur=1/2, oct=PStutter([6,5],[11,5]))

