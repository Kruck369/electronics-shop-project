"""Здесь надо написать тесты с использованием pytest для модуля item."""

import os
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_item_name():
    item1 = Item("Телефон", 10000, 20)
    item1.name = "Смартфон"
    assert item1.name == "Смартфон"


def test_item_name_setter_long_name():
    item = Item("Телефон", 10000, 20)
    with pytest.raises(ValueError):
        item.name = "СуперСмартфон"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1 + item2 == 25
    assert item2 + item2 == 10
    assert item1 + 2 is None


def test_instantiate_from_csv_success(tmp_path):
    csv_file = tmp_path / "items.csv"
    with csv_file.open("w") as file:
        file.write("name,price,quantity\n")
        file.write("Item 1,10,5\n")
        file.write("Item 2,15,8\n")
    Item.instantiate_from_csv(str(csv_file))
    assert len(Item.all) == 2
    assert Item.all[0].name == "Item 1"
    assert Item.all[0].price == 10.0
    assert Item.all[0].quantity == 5
    assert Item.all[1].name == "Item 2"
    assert Item.all[1].price == 15.0
    assert Item.all[1].quantity == 8


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../tests/items.csv')


def test_instantiate_from_csv_file_corrupted(tmp_path):
    csv_file = tmp_path / "items.csv"
    with csv_file.open("w") as file:
        file.write("name,price\n")
        file.write("Item 1,10\n")
        file.write("Item 2,15\n")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(str(csv_file))
