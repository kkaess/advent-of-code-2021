import numpy as np

positions = np.loadtxt('input/input_day7.txt', delimiter=',', dtype=int)

# Part 1
best_position = np.median(positions)
fuel = np.sum(np.abs(positions - best_position))

print(fuel)


# Part 2

# Letting x_0 be the chosen center and n_i = x_i - x_0 for the points,
# the weighting is 1/2*n_i*(n_i+1) or 1/2(n_i +n_i^2).
# The n_i term acts like part 1, for which the median is the minimum.
# The n_i^2 term acts like a normal central moment, for which the mean is the minimum.
# So we should fine the minimum between the median and the mean.
# The slope of the n_i term doesn't have a general form (depends on the points), so, while I could guess a center,
# I'm just going to iterate through the range between the median and the mean and pick a minimum.

def fuel_used(center, values):
    diffs = np.abs(values - center)
    fuel_usages = diffs * (diffs + 1) / 2
    return np.sum(fuel_usages)


val_1 = int(best_position)  # The median
val_2 = int(round(np.mean(positions)))

min_val, max_val = (val_1, val_2) if val_1 < val_2 else (val_2, val_1)
fuel_values = np.empty(max_val - min_val + 1)
for x in range(min_val, max_val + 1):
    fuel_values[x - min_val] = fuel_used(x, positions)

min_fuel_usage = np.min(fuel_values)

print(min_fuel_usage)
# integer_best_position = int(round(best_position))
# diffs = np.abs(positions - integer_best_position)
# fuel = 1/2*np.sum(diffs*(diffs+1))
# print(fuel)
