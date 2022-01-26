import numpy as np

angelfish = np.loadtxt('input/input_day6.txt', delimiter=',', dtype=int)


def angelfish_recursion(respawn, days):
    if respawn > days - 1:
        return 1
    else:
        return angelfish_recursion(6, days - 1 - respawn) + angelfish_recursion(8, days - 1 - respawn)


vals, temp_counts = np.unique(angelfish, return_counts=True)
counts = np.zeros(9)
for val, count in zip(vals, temp_counts):
    counts[val] = count


def angelfish_iteration(generations, counts):
    for i in range(generations):
        new_counts = np.zeros(9, dtype=int)
        new_counts[:8] = counts[1:]
        new_counts[6] += counts[0]
        new_counts[8] += counts[0]
        counts = new_counts

    return np.sum(counts)


# Part 1

nums = [angelfish_recursion(val, 80) for val in vals]
nums2 = angelfish_iteration(80, counts)
print(np.sum(nums * temp_counts))
print(nums2)


# Part 2

print(angelfish_iteration(256,counts))