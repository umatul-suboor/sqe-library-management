class Book:
    def __init__(self, book_id, title, quantity):
        if quantity < 0:
            raise ValueError("Book quantity cannot be negative")

        self.book_id = book_id
        self.title = title
        self.quantity = quantity
        self.available = True
        self.issued_to = None


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

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
<<<<<<< HEAD
                return True
=======

                self.borrowed_books[student] = (
                    self.borrowed_books.get(student, 0) + 1
                )

                return True

>>>>>>> 94c4518c30fc306007a7aa855e1843ff79970cff
        return False

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.issued_to in self.borrowed_books:
                    self.borrowed_books[book.issued_to] -= 1

                book.available = True
                book.issued_to = None
                return True
<<<<<<< HEAD
        return False
=======

        return False

    def borrow_book(self, member_id, isbn):
        current_books = self.borrowed_books.get(member_id, 0)

        if current_books >= 5:
            raise ValueError("Member cannot borrow more than 5 books")

        self.borrowed_books[member_id] = current_books + 1

        return True


def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")

    if days_overdue == 0:
        return "None"
    elif days_overdue <= 7:
        return "Low"
    elif days_overdue <= 14:
        return "Medium"
    elif days_overdue <= 30:
        return "High"
    else:
        return "Severe"


def validate_isbn(isbn):
    if not isinstance(isbn, str):
        raise ValueError("ISBN must be a string")

    if len(isbn) != 13:
        raise ValueError("ISBN must contain exactly 13 digits")

    if not isbn.isdigit():
        raise ValueError("ISBN must contain only numeric digits")

    return True

def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")

    if days_overdue == 0:
        return "None"
    elif days_overdue <= 7:
        return "Low"
    elif days_overdue <= 14:
        return "Medium"
    elif days_overdue <= 30:
        return "High"
    else:
        return "Severe"


class Member:
    def __init__(self, member_id):
        self.member_id = member_id
        self.borrowed_books = []


class Roster:
    def __init__(self):
        self.members = []

    def add_student(self, student):
        if len(student.borrowed_books) < 1 or len(student.borrowed_books) > 6:
            raise ValueError("A member must have between 1 and 6 borrowed books")

        self.members.append(student)

def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")

    if len(name) == 0:
        raise ValueError("Name cannot be empty")

    if len(name) > 50:
        raise ValueError("Name cannot exceed 50 characters")

    for char in name:
        if not (char.isalpha() or char in " -"):
            raise ValueError("Name can contain only letters, spaces, and hyphens")

    return True

>>>>>>> 94c4518c30fc306007a7aa855e1843ff79970cff
