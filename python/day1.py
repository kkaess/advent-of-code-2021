import numpy as np

def day1(filename):
    vals = np.loadtxt(filename, dtype=int)
    return (part1(vals), part2(vals))

def part1(vals):
    diffs = vals[1:] - vals[:-1]
    return np.sum(diffs>0)

def part2(vals):
    diffs = vals[3:] - vals[:-3]
    return np.sum(diffs>0)

if __name__ == '__main__':
    answer_day1,answer_day2 = day1('input/input_day1.txt')
    print(answer_day1)
    print(answer_day2)
