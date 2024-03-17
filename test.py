import pytest

# Тесты для list
def test_list_length():
    my_list = [1, 2, 3]
    assert len(my_list) == 3

def test_list_indexing():
    my_list = ['apple', 'banana', 'cherry']
    assert my_list[0] == 'apple'

def test_list_append():
    my_list = []
    my_list.append('apple')
    assert my_list == ['apple']

# Тесты для float
def test_float_addition():
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3)

def test_float_multiplication():
    result = 2.5 * 4
    assert result == 10.0

@pytest.mark.parametrize("num", [-100.0, -1.0, 0.0, 1.0, 100.0])
def test_float_valid(num):
    assert isinstance(num, float)

def test_float_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 1.0 / 0.0
