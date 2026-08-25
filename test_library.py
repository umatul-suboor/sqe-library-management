from library import Book, Library


def test_add_book():
    library = Library()
    book = Book("B001", "Python Programming", 5)

    library.add_book(book)

    assert len(library.books) == 1


def test_search_book():
    library = Library()
    book = Book("B002", "Python Programming", 5)

    library.add_book(book)

    result = library.search_book("Python Programming")

    assert result is not None


def test_issue_book():
    library = Library()
    book = Book("B003", "Java Programming", 3)

    library.add_book(book)
    result = library.issue_book("B003", "Ali")

    assert result is True
    assert book.available is False


def test_return_book():
    library = Library()
    book = Book("B004", "C++ Programming", 2)

    library.add_book(book)
    library.issue_book("B004", "Ali")
    result = library.return_book("B004")

    assert result is True
    assert book.available is True

def test_same_book_cannot_be_issued_twice():
    library = Library()
    book = Book("B005", "Database Systems", 1)

    library.add_book(book)

    first_issue = library.issue_book("B005", "Ali")
    second_issue = library.issue_book("B005", "Ahmed")

    assert first_issue is True
    assert second_issue is False
