
import pytest
from library import Library, borrow_percentile


def test_borrow_percentile_for_multiple_members():
    library = Library()
    library.borrowed_books = {
        "M1": 1,
        "M2": 2,
        "M3": 3,
    }

    result = borrow_percentile("M3", library)

    assert result == pytest.approx(200 / 3)
