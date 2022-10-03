import string
import HomeWork as hm
import pytest

tests = [("ABc dbE FRl Ama", "50%"), ("NDp Lka nuR vtE", "25%")]

@pytest.mark.parametrize('input_string, result', tests)
def test_digit_count(input_string, result):
    assert hm.digit_count(input_string) == result

test_date = [(29, 12, 2022, True)]

@pytest.mark.parametrize('day, month, year, result', test_date)
def test_date_check(day, month, year, result):
    assert hm.date_check(day, month, year) == result
