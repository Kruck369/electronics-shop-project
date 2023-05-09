from src.keyboard import Keyboard
import pytest


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_language("EN")
    assert str(kb.language) == "RU"
    kb.change_language("CH")
    assert str(kb.language) == "RU"
