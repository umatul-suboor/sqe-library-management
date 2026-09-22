import pytest


def test_valid_isbn(isbn_validator):
    assert isbn_validator("9781234567890") is True


@pytest.mark.parametrize('isbn', [
    "",
    "123456789",
    "12345678901234",
    "978123456789A",
    "978-123456789",
])
def test_invalid_isbn_classes(isbn_validator, isbn):
    with pytest.raises(ValueError):
        isbn_validator(isbn)


@pytest.mark.parametrize('length,expected', [
    (11, False),
    (12, False),
    (13, True),
    (14, False),
    (15, False),
])
def test_isbn_length_boundaries(isbn_validator, length, expected):
    isbn = "1" * length

    if expected:
        assert isbn_validator(isbn) is True
    else:
        with pytest.raises(ValueError):
            isbn_validator(isbn)