class Book:
    def __init__(self, book_id, title, quantity):
        self.book_id = book_id
        self.title = title
        self.quantity = quantity
        self.available = True
        self.issued_to = None


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

 def issue_book(self, book_id, student):
    for book in self.books:
        if book.book_id == book_id:
            if not book.available:
                return False

            book.available = False
            book.issued_to = student
            return True
    return False

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                book.issued_to = None
                return True
        return False


def test_returned_book_becomes_available():
    library = Library()
    book = Book("B006", "Operating Systems", 1)

    library.add_book(book)

    library.issue_book("B006", "Ali")
    library.return_book("B006")

    assert book.available is True
