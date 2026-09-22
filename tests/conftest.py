import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from library import Library, Book, fine_tier, validate_isbn


@pytest.fixture
def populated_library():
    library = Library()

    book1 = Book("B001", "Clean Code", 2)
    book2 = Book("B002", "The Pragmatic Programmer", 1)

    library.add_book(book1)
    library.add_book(book2)

    return library


@pytest.fixture
def empty_library():
    return Library()


# Function scope gives fresh data for each test; module scope reuses setup for all tests in the module.
@pytest.fixture(scope="module")
def module_library():
    library = Library()

    book = Book("B001", "Clean Code", 2)
    library.add_book(book)

    return library


@pytest.fixture
def library():
    return Library()


@pytest.fixture
def fine_calculator():
    return fine_tier


@pytest.fixture
def isbn_validator():
    return validate_isbn