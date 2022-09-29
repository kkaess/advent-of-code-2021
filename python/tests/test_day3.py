from ..day3 import day3

def test_day3():
    answer_part1, answer_part2 = day3('input/testinput_1_day3.txt')
    assert answer_part1 == 198
    assert answer_part2 == 230

#TODO add more tests for day3, especially for find_first_one_sorted