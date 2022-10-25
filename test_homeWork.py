import HomeWork as Hw
import pytest

tests = [("ABc dbE FRl Ama", "50%"), ("NDp Lka nuR vtE", "25%")]


@pytest.mark.parametrize('input_string, result', tests)
def test_digit_count(input_string, result):
    assert Hw.digit_count(input_string) == result


test_date = [(29, 12, 2022, True)]


@pytest.mark.parametrize('day, month, year, result', test_date)
def test_date_check(day, month, year, result):
    assert Hw.date_check(day, month, year) == result
