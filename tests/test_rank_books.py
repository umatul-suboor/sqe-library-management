from library import Book, Library, rank_books_by_popularity


def test_rank_books_empty_catalog_returns_empty_list():
    catalog = Library()

    assert rank_books_by_popularity(catalog) == []


def test_rank_books_single_book_returns_that_book():
    catalog = Library()
    book = Book("B001", "Python Basics", 3)
    catalog.add_book(book)

    assert rank_books_by_popularity(catalog) == [book]


def test_rank_books_sorts_by_borrow_count_descending():
    catalog = Library()

    book_a = Book("B001", "Python Basics", 3)
    book_b = Book("B002", "Data Science", 2)
    book_c = Book("B003", "Algorithms", 1)

    book_a.borrow_count = 2
    book_b.borrow_count = 5
    book_c.borrow_count = 1

    catalog.add_book(book_a)
    catalog.add_book(book_b)
    catalog.add_book(book_c)

    assert rank_books_by_popularity(catalog) == [
        book_b, book_a, book_c
    ]


def test_rank_books_breaks_ties_alphabetically():
    catalog = Library()

    book_z = Book("B004", "Zebra", 2)
    book_a = Book("B005", "Apple", 2)

    book_z.borrow_count = 4
    book_a.borrow_count = 4

    catalog.add_book(book_z)
    catalog.add_book(book_a)

    assert rank_books_by_popularity(catalog) == [
        book_a, book_z
    ]


def test_rank_books_includes_never_borrowed_books():
    catalog = Library()

    book_b = Book("B006", "Banana", 2)
    book_a = Book("B007", "apple", 2)
    book_popular = Book("B008", "Python", 3)

    book_b.borrow_count = 0
    book_a.borrow_count = 0
    book_popular.borrow_count = 5

    catalog.add_book(book_b)
    catalog.add_book(book_a)
    catalog.add_book(book_popular)

    assert rank_books_by_popularity(catalog) == [
        book_popular, book_a, book_b
    ]