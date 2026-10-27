Clock.bpm = 120
Scale.default = Scale.chromatic
Root.default = "C"

# Nacht1Satz
d1 >> pluck(PRand([(11,2),(0,2),(7,7,11,2),(6,6),2,7,9,11]), dur=PRand([1/2,1/4,1/6,1/8,3/8]), sus=PRand([1/2,1/4,1/6]), oct=PRand([2,3,4,5,6,7]), amp=PWhite(0.5,1.0))

