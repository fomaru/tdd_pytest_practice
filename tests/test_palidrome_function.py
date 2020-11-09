from scripts.palidrome_function import palidrome_function
import pytest


def test_palidrome_function_possitive():
    assert palidrome_function("racecar") is True


def test_palidrome_function_negative():
    assert palidrome_function("test") is False
    assert palidrome_function("asdasdwdadsa") is False


def test_palidrome_function_non_str_input():
    with pytest.raises(Exception) as exp:
        palidrome_function("")
    assert str(exp.value) == "Empty string"


def test_palidrome_function_not_str_input():
    with pytest.raises(Exception) as exp:
        palidrome_function(8888)
    assert str(exp.value) == "Not string value"
