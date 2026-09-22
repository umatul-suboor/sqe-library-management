from library import Library, Book


def test_total_available_copies_empty():
    library = Library()

    assert library.total_available_copies() == 0


def test_total_available_copies_single_book():
    library = Library()
    book = Book("B001", "Clean Code", 2)
    library.add_book(book)

    assert library.total_available_copies() == 2


def test_total_available_copies_multiple_books(populated_library):
    assert populated_library.total_available_copies() == 3