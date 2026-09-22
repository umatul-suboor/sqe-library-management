# Unit Testing Notes

## pytest -v tests/

The `-v` option gives verbose output.

It shows the name and result of each test.

Command:

pytest -v tests/

This is useful when we want to see individual test results clearly.

## pytest --tb=short

The `--tb=short` option gives a short traceback when a test fails.

Command:

pytest --tb=short

This is useful when we want concise error information.

## Test Results

### Verbose Test Run

45 tests passed successfully.

Command:

pytest -v tests/

### Short Traceback Test Run

All tests passed successfully.

Command:

pytest --tb=short