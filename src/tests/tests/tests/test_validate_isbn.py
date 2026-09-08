import pytest
from library import validate_isbn


def test_valid_isbn():
    assert validate_isbn("9781234567890") is True


@pytest.mark.parametrize('isbn', [
    "",
    "123456789",
    "12345678901234",
    "978123456789A",
    "978-123456789",
])
def test_invalid_isbn_classes(isbn):
    with pytest.raises(ValueError):
        validate_isbn(isbn)
