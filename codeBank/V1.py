# VoiceCrash
# utils

v1 >> play("E ", dur=16, sample=PRand(200), amp=2)
v2 >> play("E", sample=PRand(200), dur=3, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0,bits=PRand(8)+4, lofi=P*[0,PWhite(0,1)], room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1), amp=2)
v3 >> play("{EG}", sample=PRand(200), dur=16, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0,1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0, bits=PRand(8)+4, lofi=PWhite(0,1), feed=0.5, room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
