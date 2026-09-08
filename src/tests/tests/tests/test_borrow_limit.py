import pytest
from library import Library


@pytest.mark.parametrize('current_books,should_pass', [
    (3, True),
    (5, False),
])
def test_borrow_limit_equivalence_classes(current_books, should_pass):
    library = Library()

    member_id = "M001"

    library.borrowed_books[member_id] = current_books

    if should_pass:
        assert library.borrow_book(member_id, "ISBN001") is True
    else:
        with pytest.raises(ValueError):
            library.borrow_book(member_id, "ISBN001")
