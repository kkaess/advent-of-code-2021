# IPython log file


f = open('input/input_day2.txt')
lines = f.readlines()
f.close()
h = 0
v = 0

for line in lines:
    temp = line.split(' ')
    if temp[0] == 'forward':
        h += int(temp[1])
    if temp[0] == 'down':
        v += int(temp[1])
    if temp[0] == 'up':
        v -= int(temp[1])

print(h * v)

h = 0
v = 0
a = 0

for line in lines:
    temp = line.split(' ')
    if temp[0] == 'forward':
        h += int(temp[1])
        v += a * int(temp[1])
    if temp[0] == 'down':
        a += int(temp[1])
    if temp[0] == 'up':
        a -= int(temp[1])

print(h * v)
