# filter2
masterAll("rate", var([1, 16, -16, 32, -32, 0.125], [8, 1, 1, 0.5, 0.5, 16]))
masterAll("lpf", expvar([20000, 50, 20000, 20, 20000], [16, 4, 16, 2, 32]))
masterAll("hpf", expvar([0, 8000, 0, 12000, 0], [16, 4, 16, 2, 32]))
masterAll("degree", var([0, 12, -12, 24, -24, 0], [16, 4, 4, 2, 2, 32]))
masterAll(0, "slide", var([0, 8, -8, 16, -16, 0], [8, 1, 1, 0.5, 0.5, 16]))
masterAll(0,"lpf", sinvar([200, 8000], var([1, 16], [8, 8])))
masterAll(0,"lpr", var([0.1, 0.99], [4, 4]))
