import numpy as np

coords = np.fromregex('input/input_day5.txt', r'(\d+),(\d+) -> (\d+),(\d+)',
                      dtype=[('x1', int), ('y1', int), ('x2', int), ('y2', int)])

offset = (min(np.min(coords[:]['x1']), np.min(coords[:]['x2'])), min(np.min(coords[:]['y1']), np.min(coords[:]['y2'])))

span = (max(np.max(coords[:]['x1']), np.max(coords[:]['x2']))- offset[0] + 1,max(np.max(coords[:]['y1']), np.max(coords[:]['y2'])) - offset[1] + 1)

# Part 1

grid = np.zeros(span, dtype=int)

for line in coords:
    if line['x1'] == line['x2']:
        min_y = min(line['y1'], line['y2'])
        max_y = max(line['y1'], line['y2'])
        for j in range(min_y, max_y + 1):
            grid[line['x1'] - offset[0], j - offset[1]] += 1
    elif line['y1'] == line['y2']:
        min_x = min(line['x1'], line['x2'])
        max_x = max(line['x1'], line['x2'])
        for i in range(min_x, max_x + 1):
            grid[i - offset[0], line['y1'] - offset[1]] += 1

print(np.sum(grid > 1))

# Part 2

grid = np.zeros_like(grid)

for line in coords:

    step_x = 1 if line['x1']<line['x2'] else -1 if line['x1']>line['x2'] else 0
    step_y = 1 if line['y1']<line['y2'] else -1 if line['y1']>line['y2'] else 0

    if line['x1'] == line['x2']:
        for j in range(line['y1'],line['y2']+step_y,step_y):
            grid[line['x1']-offset[0],j-offset[1]] += 1
    elif line['y1'] == line['y2']:
        for i in range(line['x1'],line['x2']+step_x,step_x):
            grid[i-offset[0],line['y1']-offset[1]] += 1
    else:
        for index,i in enumerate(range(line['x1'],line['x2']+step_x,step_x)):
            grid[i-offset[0],index*step_y+line['y1']-offset[1]] += 1

print(np.sum(grid>1))
