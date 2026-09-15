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

@pytest.mark.parametrize('length,expected', [
    (11, False),
    (12, False),
    (13, True),
    (14, False),
    (15, False),
])
def test_isbn_length_boundaries(length, expected):
    isbn = "1" * length

    if expected:
        assert validate_isbn(isbn) is True
    else:
        with pytest.raises(ValueError):
            validate_isbn(isbn)