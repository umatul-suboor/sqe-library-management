
from library import Library, Book


def test_return_book_success():
    library = Library()
    book = Book("B001", "Clean Code", 2)

    library.add_book(book)
    library.borrowed_books["M001"] = 1
    book.issued_to = "M001"
    book.available = False

    result = library.return_book("B001")

    assert result is True
    assert book.available is True
    assert book.issued_to is None
    assert library.borrowed_books["M001"] == 0


def test_return_book_not_found():
    library = Library()

    result = library.return_book("B999")

    assert result is False


def test_return_book_borrower_not_registered():
    library = Library()
    book = Book("B001", "Clean Code", 2)

    library.add_book(book)
    book.issued_to = "M999"
    book.available = False

    result = library.return_book("B001")

    assert result is True
    assert book.available is True
    assert book.issued_to is None
