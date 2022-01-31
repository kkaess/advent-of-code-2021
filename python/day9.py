import numpy as np
from skimage.morphology import local_minima
from skimage.segmentation import watershed

pattern = r'(\d)' * 100
dtype = [('', 'uint8')] * 100

grid = np.fromregex('input/input_day9.txt', pattern, dtype=dtype)
full_grid = np.zeros((100, 100), dtype='uint8')
for i in range(100):
    for j in range(100):
        full_grid[i, j] = grid[i][j]

# Part 1

minima = local_minima(full_grid)
print(np.sum(full_grid[minima] + 1))

# Part 2

watersheds = watershed(full_grid, mask=(full_grid != 9), watershed_line=False)
labels, counts = np.unique(watersheds, return_counts=True)
sorted_counts = np.sort(counts[1:])
print(np.prod(sorted_counts[-3:]))
