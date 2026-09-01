# LibraryHub Software Test Plan

## 1. Introduction

This Test Plan defines the testing activities for the LibraryHub module. The purpose is to verify that the implemented library functions behave correctly and that invalid inputs and error conditions are handled appropriately. Testing will focus on the functional requirements of the current LibraryHub codebase.

## 2. Test Items

The following LibraryHub components are included in testing:

* `Book` class
* `Library` class
* `add_book()`
* `search_book()`
* `issue_book()`
* `return_book()`
* Book quantity validation
* Book availability and issue status

## 3. Features to be Tested

The following features will be tested:

* Creating a valid book
* Rejecting negative book quantity
* Adding a book to the library
* Searching for an existing book
* Searching for a non-existing book
* Issuing an available book
* Preventing an already issued book from being issued again
* Handling invalid book IDs
* Returning an issued book
* Allowing a returned book to become available again

## 4. Features Not to be Tested

The following features are outside the scope of the current LibraryHub implementation and therefore will not be tested:

* Graphical User Interface (GUI)
* Database connectivity
* User login and authentication
* Online reservation
* Fine calculation
* Member borrowing limits
* ISBN validation

These features are excluded because they are not implemented in the current codebase.

## 5. Test Approach

Both positive and negative functional testing will be performed. Positive tests will verify that valid library operations produce the expected results. Negative tests will verify that invalid inputs and unsupported operations are handled correctly.

Existing automated tests will be executed using pytest, while additional scenarios will be manually checked using the Python environment.

## 6. Test Levels

### Unit Testing

Individual classes and methods will be tested independently, including `Book` and `Library` methods.

### Regression Testing

Existing tests will be executed after testing changes to ensure that previously working functionality continues to work.

## 7. Pass/Fail Criteria

The following numeric criteria will be used:

* At least **95% of planned test cases** must pass.
* **100% of Critical defects** must be closed before testing is considered complete.
* No more than **5% of planned test cases** may fail.
* All test cases must have a recorded result of **Pass, Fail, or Blocked**.

A test case is considered **PASS** when the actual result matches the expected result. A test case is considered **FAIL** when the actual result differs from the expected result.

## 8. Test Deliverables

The following documents will be produced:

1. `docs/test-plan.md`
2. `docs/test-cases.md`
3. `docs/rtm.md`
4. Manual test execution results
5. GitHub Issues for identified failures

## 9. Test Environment

Testing will be performed using:

* **Operating System:** Windows
* **Programming Language:** Python
* **IDE:** Visual Studio Code
* **Testing Framework:** pytest
* **Repository:** GitHub
* **Test Documentation:** Markdown

## 10. Test Data

Test data will include valid and invalid book information.

Examples include:

* Valid book ID: `B001`
* Valid title: `Python Programming`
* Positive quantity: `5`
* Zero quantity: `0`
* Negative quantity: `-5`
* Existing and non-existing book IDs
* Existing and non-existing book titles
* Student names such as `Ali` and `Ahmed`

## 11. Entry Criteria

Testing can begin when:

* The LibraryHub source code is available.
* Python is installed correctly.
* pytest is installed.
* Test data is prepared.
* The test documentation is available.

## 12. Exit Criteria

Testing will be considered complete when:

* All 12 planned test cases have been executed.
* Every test case has a Pass, Fail, or Blocked status.
* Test results have been documented.
* Any identified failure has a corresponding GitHub Issue.
* The numeric pass/fail criteria have been evaluated.

## 13. Schedule

| Activity              | Planned Duration |
| --------------------- | ---------------: |
| Test Plan Preparation |       60 minutes |
| Test Case Preparation |       75 minutes |
| RTM Preparation       |       30 minutes |
| Manual Test Execution |       35 minutes |
| **Total**             |      **3 hours** |

## 14. Risks and Mitigation

| Risk                                      | Mitigation                                                    |
| ----------------------------------------- | ------------------------------------------------------------- |
| Missing functionality in the current code | Mark affected tests as Fail or Blocked and document the issue |
| Incorrect input handling                  | Include negative test cases                                   |
| Changes breaking existing functionality   | Run the existing pytest suite as regression testing           |
| Incomplete requirements coverage          | Review the RTM before completing testing                      |

## 15. Responsibilities

The student/tester is responsible for:

* Preparing test documentation
* Executing test cases
* Recording results
* Identifying defects
* Creating GitHub Issues for failures
* Updating the RTM

## 16. Approval

This Test Plan provides the testing framework for the LibraryHub module and will be used as the basis for test case design, traceability, and manual test execution.
