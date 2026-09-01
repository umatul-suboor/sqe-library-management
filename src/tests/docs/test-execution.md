# Manual Test Execution – LibraryHub

| ID     | Test Case                                     | Status  | Execution Note                                                                                             |
| ------ | --------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| TC-001 | Add Book with Valid ISBN                      | BLOCKED | A book can be added successfully, but the current `Book` class does not implement ISBN validation/storage. |
| TC-002 | Reject Duplicate ISBN                         | BLOCKED | Duplicate ISBN checking is not implemented in the current code.                                            |
| TC-003 | Reject Malformed ISBN                         | BLOCKED | ISBN format validation is not implemented in the current code.                                             |
| TC-004 | Borrow Book When Copies Are Available         | BLOCKED | The required `borrow_book()` method is not implemented.                                                    |
| TC-005 | Borrow Book When No Copies Are Available      | BLOCKED | The required borrowing/copy-availability behavior is not implemented.                                      |
| TC-006 | Return Book Currently on Loan                 | PASS    | Book was issued successfully, returned successfully, and `book.available` became `True`.                   |
| TC-007 | Return Book Not on Loan by Member             | BLOCKED | The current `return_book()` method accepts only `book_id` and does not validate the borrowing member.      |
| TC-008 | Member Borrows at Allowed Limit               | BLOCKED | Member borrowing limits are not implemented.                                                               |
| TC-009 | Member Borrows Beyond Allowed Limit           | BLOCKED | Member borrowing limits are not implemented.                                                               |
| TC-010 | Fine Calculation for Zero Days Overdue        | BLOCKED | Fine calculation is not implemented.                                                                       |
| TC-011 | Fine Calculation for Mid-Range Overdue Period | BLOCKED | Fine calculation and overdue ranges are not implemented.                                                   |
| TC-012 | Fine Calculation at Overdue-Tier Boundary     | BLOCKED | Overdue fine tiers and boundary rules are not implemented.                                                 |

## Execution Summary

| Result  | Count |
| ------- | ----: |
| PASS    |     1 |
| FAIL    |     0 |
| BLOCKED |    11 |
| Total   |    12 |

## Automated Regression Test

The existing automated test suite was executed using:

```bash
pytest -v
```

**Result: 6 passed**

All 6 existing automated tests passed successfully.

## Conclusion

One of the 12 Lab 4 test cases could be directly executed against the current implementation and passed. The remaining test cases are blocked because the required ISBN, borrowing-limit, and fine-calculation functionality is not present in the current LibraryHub codebase.

No test case was marked as FAIL because no implemented requirement produced an incorrect result during this execution. Therefore, no defect GitHub Issue is required from these execution results.
