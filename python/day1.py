import numpy as np

vals = np.loadtxt('input.txt',dtype=int)
diffs = vals[1:]-vals[:-1]
print(np.sum(diffs>0))

diffs = vals[3:]-vals[:-3]
print(np.sum(diffs>0))
