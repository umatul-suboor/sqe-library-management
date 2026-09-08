import pytest
from library import validate_name


@pytest.mark.parametrize("name", [
    "Ali Khan",
    "Muhammad Ali",
    "Noor-Ain",
])
def test_valid_names(name):
    assert validate_name(name) is True


def test_empty_name():
    with pytest.raises(ValueError):
        validate_name("")


def test_over_length_name():
    with pytest.raises(ValueError):
        validate_name("A" * 51)


@pytest.mark.parametrize("name", [
    "Ali123",
    "Ali@Khan",
])
def test_invalid_characters(name):
    with pytest.raises(ValueError):
        validate_name(name)
