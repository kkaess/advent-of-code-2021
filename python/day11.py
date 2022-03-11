import numpy as np
from scipy.signal import convolve2d

pattern = r'(\d)' * 10
dtype = [('', 'uint8')] * 10

grid = np.fromregex('input/input_day11.txt', pattern, dtype=dtype)
full_grid = np.zeros((10, 10), dtype='uint8')
for i in range(10):
    for j in range(10):
        full_grid[i, j] = grid[i][j]

kernel = np.ones((3, 3), dtype='uint8')
kernel[1, 1] = 0

# Part 1
flashes = 0
for step in range(100):
    full_grid += 1
    flashed = np.zeros((10, 10), dtype=bool)
    while np.any(new_sites := np.logical_and(full_grid > 9, ~flashed)):
        flashed = np.logical_or(flashed, new_sites)
        addition = convolve2d(new_sites, kernel, mode='same')
        full_grid += addition
    flashes += np.sum(flashed)
    full_grid = full_grid*~flashed

print(flashes)

# Part 2, assumes number of steps larger than 100

flashes = 0
steps = 100

while flashes < 100:
    steps += 1
    full_grid += 1
    flashed = np.zeros((10, 10), dtype=bool)
    while np.any(new_sites := np.logical_and(full_grid > 9, ~flashed)):
        flashed = np.logical_or(flashed, new_sites)
        addition = convolve2d(new_sites, kernel, mode='same')
        full_grid += addition
    flashes = np.sum(flashed)
    full_grid = full_grid * ~flashed

print(steps)
