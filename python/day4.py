import numpy as np

boards = np.reshape(np.loadtxt('input/input_day4.txt', dtype=int, skiprows=2), (-1, 5, 5))
values = np.loadtxt('input/input_day4.txt', max_rows=1, delimiter=',', dtype=int)

# Part 1
index = 0
index_overflow = len(values)
max_fill = 0
winning_board = -1

fills = np.zeros((np.shape(boards)[0], 2, 5))

while index < index_overflow:
    n, y, x = np.where(boards == values[index])
    for n, y, x in zip(n, y, x):
        fills[n, 0, y] += 1
        max_fill = max(fills[n, 0, y], max_fill)
        fills[n, 1, x] += 1
        max_fill = max(fills[n, 1, x], max_fill)
        if max_fill == 5:
            winning_board = n
            break
    if max_fill == 5:
        break
    else:
        index += 1

vals = values[:index + 1]
board = boards[winning_board, :, :]
final_score = values[index] * np.sum(np.setdiff1d(board, vals, assume_unique=True))

print(final_score)

# Part 2

moves_to_win = np.zeros((np.shape(boards)[0]), dtype=int)

for i, board in enumerate(boards):
    max_fill = 0
    fill = np.zeros((2, 5))
    index = 0
    while index < index_overflow:
        y, x = np.where(board == values[index])
        for y, x in zip(y, x):
            fill[0, y] += 1
            max_fill = max(max_fill, fill[0, y])
            fill[1, x] += 1
            max_fill = max(max_fill, fill[1, x])
            if max_fill == 5:
                break
        if max_fill == 5:
            moves_to_win[i] = index
            break
        else:
            index += 1

losing_number_of_moves = np.max(moves_to_win)
losing_board_index = np.where(moves_to_win == losing_number_of_moves)

vals = values[0:losing_number_of_moves + 1]
board = boards[losing_board_index, :, :]
final_score = values[losing_number_of_moves] * np.sum(np.setdiff1d(board, vals, assume_unique=True))

print(final_score)
