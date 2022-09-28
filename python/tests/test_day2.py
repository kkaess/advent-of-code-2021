from ..day2 import day2


def test_day2():
    answer_part1, answer_part2 = day2('input/testinput_1_day2.txt')
    assert answer_part1 == 150
    assert answer_part2 == 900
