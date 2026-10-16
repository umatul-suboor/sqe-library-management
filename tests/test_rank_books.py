import library


def test_rank_books_empty_catalog_returns_empty_list():
    catalog = library.Library()
    assert library.rank_books_by_popularity(catalog) == []


    def test_rank_books_single_book_returns_that_book():
    catalog = library.Library()
    book = library.Book("B1", "Python Basics", 3)
    catalog.add_book(book)

    assert library.rank_books_by_popularity(catalog) == [book]