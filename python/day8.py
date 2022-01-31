import numpy as np
from collections import Counter

with open('input/input_day8.txt') as f:
    lines = f.read().splitlines()

# Part 1
ones = 0
fours = 0
sevens = 0
eights = 0

for line in lines:
    output = (line.split('|')[1]).strip()
    individual_outs = output.split(' ')
    for item in individual_outs:
        if len(item) == 2:
            ones += 1
        elif len(item) == 4:
            fours += 1
        elif len(item) == 3:
            sevens += 1
        elif len(item) == 7:
            eights += 1

print(ones + fours + sevens + eights)

# Part 2
sum = 0

for line in lines:
    keys, output = line.split(' | ')
    output_numbers = output.split(' ')
    place = 1000
    num = 0
    for number in output_numbers:
        if len(number) == 2:
            num += place
        elif len(number) == 4:
            num += 4*place
        elif len(number) == 3:
            num += 7*place
        elif len(number) == 7:
            num += 8*place
        else:
            key_counts = Counter(keys)
            key_counts.pop(' ')
            sorted_key_counts = key_counts.most_common()

            if len(number) == 5:
                a = sorted_key_counts[1][0]
                c = sorted_key_counts[2][0]
                f = sorted_key_counts[0][0]
                if a in number and c in number:
                    if f in number:
                        num += 3*place
                    else:
                        num += 2*place
                else:
                    num += 5*place
            elif len(number) == 6:
                d = sorted_key_counts[3][0]
                g = sorted_key_counts[4][0]
                e = sorted_key_counts[6][0]
                if d in number and g in number:
                    if e in number:
                        num += 6*place
                    else:
                        num += 9*place
        place /= 10
    sum += num

print(sum)

# 996684 too high