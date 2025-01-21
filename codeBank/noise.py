#noise
a1 >> play("mow b", dur=P*[1/2, 2, 1/2], rate=(PWhite(-1, 1),PWhite(-1, 1)) * 2, sample=PRand(8)[:4], leg=2, shape=PWhite(0, 1))
a2 >> play("{vls }", dur=P*[1/2, 1/4, 1/2], rate=(PWhite(-1, 1),PWhite(-1, 1)) * 4, sample=PRand(8)[:4], leg=1)
