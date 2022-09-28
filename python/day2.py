def day2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (part1(lines), part2(lines))


def part1(lines):
    h = 0
    v = 0

    for line in lines:
        temp = line.split(' ')
        if temp[0] == 'forward':
            h += int(temp[1])
        elif temp[0] == 'down':
            v += int(temp[1])
        elif temp[0] == 'up':
            v -= int(temp[1])
    return h * v


def part2(lines):
    h = 0
    v = 0
    a = 0

    for line in lines:
        temp = line.split(' ')
        if temp[0] == 'forward':
            h += int(temp[1])
            v += a * int(temp[1])
        elif temp[0] == 'down':
            a += int(temp[1])
        elif temp[0] == 'up':
            a -= int(temp[1])
    return h * v


if __name__ == '__main__':
    answer_day1, answer_day2 = day2('input/input_day2.txt')
    print(answer_day1)
    print(answer_day2)
