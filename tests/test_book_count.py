import pytest
from library import Member, Roster


@pytest.mark.parametrize("book_count, should_raise", [
    (0, True),
    (3, False),
    (8, True),
])
def test_books_per_member(book_count, should_raise):
    member = Member("M001")
    member.borrowed_books = [f"book{i}" for i in range(book_count)]

    roster = Roster()

    if should_raise:
        with pytest.raises(ValueError):
            roster.add_student(member)
    else:
        roster.add_student(member)
        assert member in roster.members
