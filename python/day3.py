# with open('input/input_day3.txt') as f:
#     lines = f.read().splitlines()

import numpy as np

lines = np.loadtxt('input/input_day3.txt', dtype=str)

# Part 1

ones = [0] * 12
zeros = [0] * 12
for line in lines:
    for ind, ch in enumerate(line):
        if ch == '0':
            zeros[ind] += 1
        else:
            ones[ind] += 1

gamma_str = ''
epsilon_str = ''
for a, b in zip(ones, zeros):
    if a > b:
        gamma_str += '1'
        epsilon_str += '0'
    else:
        gamma_str += '0'
        epsilon_str += '1'

gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)
print(gamma * epsilon)


# Part 2

def find_first_one_sorted(a_list, index):
    upper_bound = len(a_list)
    lower_bound = 0
    while abs(upper_bound - lower_bound) > 1.5:
        curr_index = (upper_bound + lower_bound) // 2
        if a_list[curr_index][index] == '1':
            upper_bound = curr_index
        else:
            lower_bound = curr_index

    return upper_bound


lines.sort()

min = 0
max = len(lines)

view = lines[min:max]
pos = 0
while len(view) > 1 and pos < 12:
    first_one = find_first_one_sorted(view, pos)
    if first_one <= len(view) / 2:
        view = view[first_one:]
    else:
        view = view[:first_one]
    pos += 1
ogr = int(view[0], 2)

view = lines[min:max]
pos = 0
while len(view) > 1 and pos < 12:
    first_one = find_first_one_sorted(view, pos)
    if first_one > len(view) / 2:
        view = view[first_one:]
    else:
        view = view[:first_one]
    pos += 1
csr = int(view[0], 2)

print(ogr * csr)
