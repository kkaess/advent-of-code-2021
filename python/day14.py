import numpy as np

with open('input/input_day14.txt') as f:
    file_input = f.read().splitlines()

chain = file_input[0]
#
# rule_map = {}
#
# for rule in file_input[2:]:
#     pattern, insertion = rule.split(' -> ')
#     rule_map[pattern] = pattern[0] + insertion
#
# print(chain)
#
# for i in range(10):
#     new_chain = ''
#     for j in range(len(chain) - 1):
#         new_chain += rule_map[chain[j:j + 2]]
#     chain = new_chain + chain[-1:]
#
# split_chain = [char for char in chain]
# chars, counts = np.unique(split_chain, return_counts=True)
# print(max(counts) - min(counts))
#
# for i in range(30):
#     print(i)
#     new_chain = ''
#     for j in range(len(chain) - 1):
#         new_chain += rule_map[chain[j:j + 2]]
#     chain = new_chain + chain[-1:]
#
# split_chain = [char for char in chain]
# chars, counts = np.unique(split_chain, return_counts=True)
# print(max(counts) - min(counts))

pairs = {}
chars = {}
for i in range(len(chain) - 1):
    pair = chain[i:i+2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1
for i in range(len(chain)):
    char = chain[i]
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1

pair_char_prop_table = {}
for rule in file_input[2:]:
    pattern, insertion = rule.split(' -> ')
    pair_char_prop_table[pattern] = [pattern[0] + insertion, insertion + pattern[1], insertion]
    if pattern not in pairs:
        pairs[pattern] = 0
    if insertion not in chars:
        chars[insertion] = 0

for i in range(10):
    new_pairs = dict.fromkeys(pairs.keys(), 0)
    for pair in pairs:
        num = pairs[pair]
        prop_rule = pair_char_prop_table[pair]
        new_pairs[prop_rule[0]] += num
        new_pairs[prop_rule[1]] += num
        chars[prop_rule[2]] += num
    pairs = new_pairs

char_counts = chars.values()
print(max(char_counts) - min(char_counts))

for i in range(30):
    new_pairs = dict.fromkeys(pairs.keys(), 0)
    for pair in pairs:
        num = pairs[pair]
        prop_rule = pair_char_prop_table[pair]
        new_pairs[prop_rule[0]] += num
        new_pairs[prop_rule[1]] += num
        chars[prop_rule[2]] += num
    pairs = new_pairs

char_counts = chars.values()
print(max(char_counts) - min(char_counts))