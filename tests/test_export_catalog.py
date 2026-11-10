import pytest
from library import Library, Book, LibraryIOError
def test_export_catalog_os_error(mocker, populated_library):
    mocker.patch(
        "builtins.open",
        side_effect=OSError("Permission denied")
    )

    with pytest.raises(
        LibraryIOError,
        match="Unable to export catalog: Permission denied"
    ):
        populated_library.export_catalog("catalog.txt")
