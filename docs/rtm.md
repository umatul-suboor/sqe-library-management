# Requirements Traceability Matrix (RTM) – LibraryHub

## 1. Purpose

The Requirements Traceability Matrix maps LibraryHub functional requirements to their corresponding test cases. It ensures that the planned requirements are covered by tests and helps identify any requirement that has no associated test case.

## 2. Requirements Traceability Matrix

| Requirement ID | Requirement                                                                                      | Test Case ID(s) | Coverage Status |
| -------------- | ------------------------------------------------------------------------------------------------ | --------------- | --------------- |
| REQ-01         | The system shall allow a book with a valid, new ISBN to be added.                                | TC-001          | Covered         |
| REQ-02         | The system shall reject a book with a duplicate ISBN.                                            | TC-002          | Covered         |
| REQ-03         | The system shall reject a book with a malformed ISBN.                                            | TC-003          | Covered         |
| REQ-04         | The system shall allow a member to borrow a book when copies are available.                      | TC-004          | Covered         |
| REQ-05         | The system shall reject borrowing when no copies are available.                                  | TC-005          | Covered         |
| REQ-06         | The system shall allow a member to return a book currently on loan and reject an invalid return. | TC-006, TC-007  | Covered         |
| REQ-07         | The system shall allow a member to borrow books up to the allowed borrowing limit.               | TC-008          | Covered         |
| REQ-08         | The system shall reject borrowing beyond the allowed member limit.                               | TC-009          | Covered         |
| REQ-09         | The system shall calculate zero fine for zero overdue days.                                      | TC-010          | Covered         |
| REQ-10         | The system shall calculate the correct fine for a mid-range overdue period.                      | TC-011          | Covered         |
| REQ-11         | The system shall apply the correct fine tier at an overdue-tier boundary.                        | TC-012          | Covered         |

## 3. Coverage Summary

| Metric                            | Result |
| --------------------------------- | -----: |
| Total Requirements                |     11 |
| Total Test Cases                  |     12 |
| Requirements with Test Coverage   |     11 |
| Requirements with Zero Test Cases |      0 |
| Requirement Coverage              |   100% |

## 4. Untraced Requirements

No requirement has zero linked test cases. All identified requirements are linked to at least one test case.

## 5. Test Case Coverage

All 12 planned test cases are linked to a requirement. TC-006 and TC-007 both verify REQ-06 because the requirement includes both successful and invalid return behavior.

## 6. Important Implementation Note

The RTM represents the requirements specified for Lab 4. Some of these requirements, including ISBN validation, borrowing limits, and fine calculation, are not currently implemented in the provided LibraryHub source code. Their actual execution status will therefore be determined during Task 4 rather than assumed to be passing.
