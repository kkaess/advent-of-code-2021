from ..day1 import day1

def test_day1():
    answer_day1,answer_day2 = day1('input/testinput_1_day1.txt')
    assert answer_day1 == 7
    assert answer_day2 == 5