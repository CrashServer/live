Clock.bpm = 150
Scale.default = Scale.chromatic
Root.default = "C"

# Bass    (BB)
d1 >> dbass(PRand([0,1,2,5,6,7,8,9]), dur=PRand([1,3]), oct=[2,3])

# Piano   (BB)
d2 >> pianovel(PRand([0,(7,11,2),1,4,7,8,9,11]), dur=PRand([1,1/2,2,3]), sus=PRand([1/2,3,3/2]), oct=PRand([2,3,4,5,6]), amp=PWhite(0.25,0.75))

# Melody  (BB)
d3 >> pluck(PRand([0,(8,0),(5,8),4,6,7,9,11]), dur=PRand([1,1/2,2,3,3/2]), sus=PRand([3/2,3/4,3/8]))

# Soloist (BB)
d4 >> lazer(PRand([0,1,4,6,7,8,9,11]), dur=PRand([1,1/2,2,3,3/2]), sus=PRand([3/2,3/4,3/8]))

