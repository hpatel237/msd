import pytest
from program import divide_numbers, reverse_string, get_list_element

def test_divide_normal():
    assert divide_numbers(10, 4) == 2.5

def test_divide_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(5, 0)

def test_divide_negative():
    assert divide_numbers(-10, 2) == -5.0

def test_reverse_normal():
    assert reverse_string("Hello") == "OLLEh"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_non_string():
    with pytest.raises(TypeError):
        reverse_string(12345)

def test_get_element_normal():
    assert get_list_element([1, 2, 3], 1) == 2

def test_get_element_out_of_range():
    with pytest.raises(IndexError):
        get_list_element([1, 2], 5)

def test_get_element_negative_index():
    assert get_list_element([1, 2, 3], -1) == 3
