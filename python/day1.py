import numpy as np

vals = np.loadtxt('input/input_day1.txt', dtype=int)
# Part 1
diffs = vals[1:] - vals[:-1]
print(np.sum(diffs > 0))
# Part 2
diffs = vals[3:] - vals[:-3]
print(np.sum(diffs > 0))
