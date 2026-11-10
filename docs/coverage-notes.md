# Lab 11 - Automated Test Coverage

## Task 1: Baseline Coverage Report

### Coverage Results

| File | Statements | Missing | Line Coverage | Branches | Partial | Branch Coverage | Total Coverage |
|------|------------|---------|---------------|----------|---------|-----------------|----------------|
| library.py | 73 | 15 | 79% | 32 | 3 | 59% | 73% |
| Total | 73 | 15 | 79% | 32 | 3 | 59% | 73% |

### Observation

The baseline report shows that the project has 79% line coverage, 59% branch coverage, and 73% total coverage.

Some statements and branches are 
not covered by the existing automated tests. These gaps will be identified and improved in the next tasks.




## Task 2: Identify the Three Weakest Areas

### Source File: library.py

Three important areas identified for further coverage testing:

1. validate_isbn()
   - ISBN is not a string.
   - ISBN has an invalid length or contains non-digit characters.

2. return_book()
   - Book ID does not exist.
   - Borrower is not present in borrowed_books.

3. export_catalog()
   - File export fails due to an OSError.
   - LibraryIOError exception handling needs testing.

### Observation

The library.py file contains several conditional and exception-handling paths.
These areas should be tested to improve line and branch coverage.


## Task 4: Coverage vs. Quality Discussion

### Selected Test
test_export_catalog_os_error()

### Original Weak Assertion
The original test used try-except and assert True.
It only checked whether LibraryIOError was raised.

### Improved Assertion
The test now uses pytest.raises() with a match argument
to verify the exact exception message.

### Why Was It a Coverage Trap?

The original test executed the exception-handling code,
but it did not verify the actual error message.

This could allow incorrect error messages to pass the test.

The improved test checks both the exception type and
its message, making the test more reliable.

### Conclusion
Code coverage measures executed code, but test quality
depends on checking actual expected results.