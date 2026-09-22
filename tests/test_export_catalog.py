from library import Library, Book, LibraryIOError


def test_export_catalog(mocker, populated_library):
    mock_file = mocker.mock_open()

    mocker.patch("builtins.open", mock_file)

    populated_library.export_catalog("catalog.txt")

    expected_content = (
        "B001,Clean Code,2\n"
        "B002,The Pragmatic Programmer,1\n"
    )

    handle = mock_file()
    handle.write.assert_any_call("B001,Clean Code,2\n")
    handle.write.assert_any_call(
        "B002,The Pragmatic Programmer,1\n"
    )


def test_export_catalog_os_error(mocker, populated_library):
    mocker.patch(
        "builtins.open",
        side_effect=OSError("Permission denied")
    )

    try:
        populated_library.export_catalog("catalog.txt")
    except LibraryIOError:
        assert True
    else:
        assert False