from heapq import heappush, heappop

import numpy as np
from pairing import pair, depair

with open('input/input_day15.txt') as f:
    rows = f.read().splitlines()

rows = [[char for char in row] for row in rows]

grid = np.asarray(rows, int)

MAX_DIST = (grid.shape[0] + grid.shape[1] - 2) * 9
dist_grid = np.full_like(grid, MAX_DIST)
dist_grid[0, 0] = 0
visited = np.zeros(dist_grid.shape, bool)

neighbor_list = {}

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        neighbor_list[cantor := pair(i, j)] = []
        if i > 0:
            neighbor_list[cantor] += [pair(i - 1, j)]
        if i < grid.shape[0] - 1:
            neighbor_list[cantor] += [pair(i + 1, j)]
        if j > 0:
            neighbor_list[cantor] += [pair(i, j - 1)]
        if j < grid.shape[1] - 1:
            neighbor_list[cantor] += [pair(i, j + 1)]

current_location = pair(0, 0)
visited[0, 0] = True
end = pair(grid.shape[0] - 1, grid.shape[1] - 1)
location_queue = []

while current_location != end:
    x, y = depair(current_location)
    dist = dist_grid[x, y]
    for neighbor in neighbor_list[current_location]:
        nbr_x, nbr_y = depair(neighbor)
        new_dist = dist + grid[nbr_x, nbr_y]
        if new_dist < dist_grid[nbr_x, nbr_y]:
            dist_grid[nbr_x, nbr_y] = new_dist
        if not visited[nbr_x, nbr_y]:
            visited[nbr_x, nbr_y] = True
            heappush(location_queue, (dist_grid[nbr_x, nbr_y], neighbor))
    current_location = heappop(location_queue)[1]

x, y = depair(end)
print(dist_grid[x, y])

# Part 2

x_length = grid.shape[0]
y_length = grid.shape[1]

big_grid = np.zeros((x_length * 5, y_length * 5), int)
for i in range(5):
    ulc = i * x_length
    for j in range(5):
        utc = j * y_length
        big_grid[ulc:ulc + x_length, utc:utc + y_length] = grid + (i + j)

for i in range(big_grid.shape[0]):
    for j in range(big_grid.shape[1]):
        if big_grid[i, j] > 9:
            new = big_grid[i, j] % 9
            big_grid[i, j] = new if new != 0 else 9

# np.savetxt("big_grid.csv", big_grid, delimiter=",")
MAX_DIST = (big_grid.shape[0] + big_grid.shape[1] - 2) * 9
big_dist_grid = np.full_like(big_grid, MAX_DIST)
big_dist_grid[0, 0] = 0
visited = np.zeros(big_dist_grid.shape, bool)


neighbor_list = {}

for i in range(big_grid.shape[0]):
    for j in range(big_grid.shape[1]):
        neighbor_list[cantor := pair(i, j)] = []
        if i > 0:
            neighbor_list[cantor] += [pair(i - 1, j)]
        if i < big_grid.shape[0] - 1:
            neighbor_list[cantor] += [pair(i + 1, j)]
        if j > 0:
            neighbor_list[cantor] += [pair(i, j - 1)]
        if j < big_grid.shape[1] - 1:
            neighbor_list[cantor] += [pair(i, j + 1)]

current_location = pair(0, 0)
visited[0,0] = True
end = pair(big_grid.shape[0] - 1, big_grid.shape[1] - 1)
location_queue = []

while current_location != end:
    x, y = depair(current_location)
    dist = big_dist_grid[x, y]
    for neighbor in neighbor_list[current_location]:
        nbr_x, nbr_y = depair(neighbor)
        new_dist = dist + big_grid[nbr_x, nbr_y]
        if new_dist <= big_dist_grid[nbr_x, nbr_y]:
            big_dist_grid[nbr_x, nbr_y] = new_dist
        if not visited[nbr_x, nbr_y]:
            visited[nbr_x, nbr_y] = True
            heappush(location_queue, (new_dist, neighbor))
    current_location = heappop(location_queue)[1]

x, y = depair(end)
print(big_dist_grid[x, y])
