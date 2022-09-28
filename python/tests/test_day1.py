from ..day1 import day1

def test_day1():
    answer_part1,answer_part2 = day1('input/testinput_1_day1.txt')
    assert answer_part1 == 7
    assert answer_part2 == 5