from src.phone import Phone
import pytest


def test_class():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = -1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 1.5
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3

