Clock.bpm = 50
Scale.default = Scale.chromatic
Root.default = "C"

# 1st Mvmt Sonata No.14, Opus 27, No.2
d1 >> pluck(PRand([0,1,3,4,6,8,9,11]), dur=PRand([1/3,3/4]), amp=PWhite(0.25,0.75))

# Sonata Quasi Una Fantasia
d2 >> pluck(PRand([(6,6),(8,8),(1,1),1,3,4,6,8]), dur=PRand([1,1/3,2,3/4,4]), sus=PRand([1,1/3,2]), oct=PRand([2,3,4]), amp=PWhite(0.25,0.75))

