import library


def test_rank_books_empty_catalog_returns_empty_list():
    catalog = library.Library()
    assert library.rank_books_by_popularity(catalog) == []