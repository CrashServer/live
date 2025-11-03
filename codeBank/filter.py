# filter
# Utils

masterAll("lpf", var([0, 4000, 6000, 15000], [24, 4, 2, 2]))
masterAll("hpf", var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2]))
masterAll("cut", var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2]))
masterAll("degree", linvar([1, linvar([0, 2],[4, 0])], 8))
masterAll("rate", 2) 
masterAll("dur", P*[1/2, 1, 1, 1/2, 2])
masterAll("reset")