with open('input/input_day10.txt') as f:
    lines = f.read().splitlines()

openers = '<{[('

# Part 1 & 2
total_error = 0
incomplete_line_scores = []

for line in lines:
    stack = []
    illegal = False
    for token in line:
        if token in openers:
            stack.append(token)
        else:
            if len(stack) > 0:
                match = stack.pop(-1)
                if token == '>':
                    if match != '<':
                        total_error += 25137
                        illegal = True
                        break
                elif token == '}':
                    if match != '{':
                        total_error += 1197
                        illegal = True
                        break
                elif token == ']':
                    if match != '[':
                        total_error += 57
                        illegal = True
                        break
                elif token == ')':
                    if match != '(':
                        total_error += 3
                        illegal = True
                        break

    if not illegal:
        line_score = 0
        while len(stack) > 0:
            line_score *= 5
            val = stack.pop(-1)
            if val == '(':
                line_score += 1
            elif val == '[':
                line_score += 2
            elif val == '{':
                line_score += 3
            elif val == '<':
                line_score += 4
        incomplete_line_scores.append(line_score)
incomplete_line_scores.sort()

print(total_error)
print(incomplete_line_scores[len(incomplete_line_scores)//2])
