import pytest
from library import Library


@pytest.mark.parametrize(
    "current_books, should_raise",
    [
        (0, False),
        (1, False),
        (2, False),
        (4, False),
        (5, False),
        (6, True),
    ],
    ids=[
        "zero_books",
        "one_book",
        "two_books",
        "four_books",
        "five_books",
        "six_books_over_limit",
    ],
)
def test_borrow_book_limit(current_books, should_raise):
    library = Library()
    library.borrowed_books["M001"] = current_books

    if should_raise:
        with pytest.raises(ValueError):
            library.borrow_book("M001", "9781234567890")
    else:
        assert library.borrow_book("M001", "9781234567890") is True