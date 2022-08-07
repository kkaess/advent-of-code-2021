from lark import Lark, Token

translation_dict = \
    {'0': '0000',
     '1': '0001',
     '2': '0010',
     '3': '0011',
     '4': '0100',
     '5': '0101',
     '6': '0110',
     '7': '0111',
     '8': '1000',
     '9': '1001',
     'A': '1010',
     'B': '1011',
     'C': '1100',
     'D': '1101',
     'E': '1110',
     'F': '1111'}

with open('input/input_day16.txt') as f:
    hex_data = f.read().strip()

bin_data = ''.join([translation_dict[ch] for ch in hex_data])

def count_total_version(tree):
    all_tokens = tree.scan_values(lambda v: isinstance(v, Token))
    total = 0
    for token in all_tokens:
        if token.type == 'VERSION':
            total += int(token.value,2)
    return total


with open('day16_syntax.lark') as f:
    parse_string = f.read()

test1 = "110100101111111000101000"
test2 = "00111000000000000110111101000101001010010001001000000000"
test3 = "11101110000000001101010000001100100000100011000001100000"

version_total = []


def add_version(token):
    globals()['version_total'].append(int(token.value, 2))
    return token

print("Test 1")
parser = Lark(parse_string)
output = parser.parse(test1)
print(count_total_version(output))

print("Test 2")
output2 = parser.parse(test2)
print(count_total_version(output2))

print("Test 3")
output3 = parser.parse(test3)
print(count_total_version(output3))

test4_raw = "8A004A801A8002F478"
test4 = ''.join([translation_dict[ch] for ch in test4_raw])
print("Test 4")
output4 = parser.parse(test4)
print(count_total_version(output4))

test5_raw = "620080001611562C8802118E34"
test5 = ''.join([translation_dict[ch] for ch in test5_raw])
print("Test 5")
output5 = parser.parse(test5)
print(count_total_version(output5))
test5_raw = "C0015000016115A2E0802F182340"
test5 = ''.join([translation_dict[ch] for ch in test5_raw])
print("Test 6")
output5 = parser.parse(test5)
print(count_total_version(output5))

test5_raw = "A0016C880162017C3686B18A3D4780"
test5 = ''.join([translation_dict[ch] for ch in test5_raw])
print("Test 7")
output5 = parser.parse(test5)
print(count_total_version(output5))

output6 = parser.parse(bin_data)
print(count_total_version(output6))
