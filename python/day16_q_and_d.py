translation_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                    'E': '1110', 'F': '1111'}

with open('input/input_day16.txt') as f:
    hex_data = f.read().strip()

bin_data = '{0:b}'.format(int(hex_data, 16))
# bin_data = '110100101111111000101000'
# bin_data = '00111000000000000110111101000101001010010001001000000000'
total = 0
ptr = 0
length = len(bin_data)

while ptr + 6 < length:
    ver = bin_data[ptr:ptr + 3]
    type = bin_data[ptr + 3:ptr + 6]
    new_ptr = ptr + 6
    if type == '100':
        total += int(ver, 2)
        while bin_data[new_ptr] == '1':
            new_ptr += 5
        ptr = new_ptr + 5
    else:
        if new_ptr + 1 < length:
            type = bin_data[new_ptr]
            new_ptr += 1
            if type == '0' and new_ptr + 15 < length and int(bin_data[new_ptr:new_ptr + 15], 2) > 0:
                total += int(ver, 2)
                ptr = new_ptr + 15
            elif new_ptr + 11 < length and int(bin_data[new_ptr:new_ptr + 11], 2) > 0:
                total += int(ver, 2)
                ptr = new_ptr + 11
            else:
                ptr = new_ptr + 1
        else:
            ptr = new_ptr + 1

print(total)


def q_and_d_terminal_zero_trimmer(bin_data):
    total = 0
    ptr = 0
    length = len(bin_data)

    while ptr + 6 < length:
        ver = bin_data[ptr:ptr + 3]
        type = bin_data[ptr + 3:ptr + 6]
        new_ptr = ptr + 6
        if type == '100':
            total += int(ver, 2)
            while bin_data[new_ptr] == '1':
                new_ptr += 5
            ptr = new_ptr + 5
        else:
            if new_ptr + 1 < length:
                type = bin_data[new_ptr]
                new_ptr += 1
                if type == '0' and new_ptr + 15 < length and int(bin_data[new_ptr:new_ptr + 15], 2) > 0:
                    total += int(ver, 2)
                    ptr = new_ptr + 15
                elif new_ptr + 11 < length and int(bin_data[new_ptr:new_ptr + 11], 2) > 0:
                    total += int(ver, 2)
                    ptr = new_ptr + 11
                else:
                    ptr = new_ptr + 1
            else:
                ptr = new_ptr + 1
