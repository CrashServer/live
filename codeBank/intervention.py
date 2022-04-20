# intervention
y1 >> pbass(5, oct=(3,4), dur=8, echo=0.25, echotime=PRand(7,10), drive=0.5, room=1).unison(3)
d9 >> play("k.", dur=[4,1/4,1/4,1/2,1,1/2,1], sample=(0,5)).sometimes("stutter", 3)
d8 >> play("d+d", sample=[2,1], dur=PDur(5,8,2)*2, room=PWhite(0.5,1), mix=0.4)