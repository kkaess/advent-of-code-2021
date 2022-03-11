import numpy as np


def add_two_right_edge(ndarray1, ndarray2):
    l1 = np.shape(ndarray1)[0]
    l2 = np.shape(ndarray2)[0]
    if l1 < l2:
        ndarray2[-l1:, :] += ndarray1
        return ndarray2
    else:
        ndarray1[-l2:, :] += ndarray2
        return ndarray1


def add_two_bottom_edge(ndarray1, ndarray2):
    l1 = np.shape(ndarray1)[1]
    l2 = np.shape(ndarray2)[1]
    if l1 < l2:
        new_array = np.copy(ndarray2)
        new_array[:, -l1:] += ndarray1
        return new_array
    else:
        new_array = np.copy(ndarray1)
        new_array[:, -l2:] += ndarray2
        return new_array


def display_grid(grid):
    n, m = grid.shape
    for j in range(m):
        line = ''
        for i in range(n):
            if grid[i, j]:
                line += '* '
            else:
                line += '. '
        print(line)


dots = np.loadtxt('input/input_day13.txt', delimiter=',', dtype='uint', max_rows=722)

max_x, max_y = np.max(dots, 0).astype(int)

grid = np.zeros((max_x + 1, max_y + 1), dtype=bool)

with open('input/input_day13.txt') as f:
    lines = f.read().splitlines()

instructions = [direction[11:].split('=') for direction in lines[723:]]


for dot in dots:
    grid[dot[0], dot[1]] = True

first = instructions[0]
line = int(first[1])

if first[0] == 'x':
    new_array = add_two_right_edge(grid[:line + 1, :], np.flipud(grid[line:, :]))[:-1, :]
else:
    new_array = add_two_bottom_edge(grid[:, :line + 1], np.fliplr(grid[:, line:]))[:, :-1]

print(np.sum(new_array))

for instruction in instructions[1:]:
    line = int(instruction[1])

    if instruction[0] == 'x':
        new_array = add_two_right_edge(new_array[:line + 1, :], np.flipud(new_array[line:, :]))[:-1, :]
    else:
        new_array = add_two_bottom_edge(new_array[:, :line + 1], np.fliplr(new_array[:, line:]))[:, :-1]

display_grid(new_array)
