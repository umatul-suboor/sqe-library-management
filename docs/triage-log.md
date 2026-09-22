# Triage Log — v0.2

## Defect Prioritization

| Rank | Issue                                                      | Severity | Priority | Rationale                                                                                                                               |
| ---- | ---------------------------------------------------------- | -------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | #3 — Library allows the same book to be issued twice       | High     | P0       | This can corrupt library records and allow the same physical book to be assigned to multiple users, so it requires immediate attention. |
| 2    | #5 — Returned book remains marked as unavailable           | High     | P1       | This prevents returned books from being issued again and directly affects normal library operations.                                    |
| 3    | #4 — Library accepts negative book quantity                | Medium   | P1       | Invalid quantities can corrupt inventory data and should be fixed soon, although the impact is less severe than duplicate issuing.      |
| 4    | #6 — Book search fails when capitalization is different    | Medium   | P2       | Users may fail to find existing books because of capitalization differences, but the books and records themselves are not corrupted.    |
| 5    | #7 — Library allows return of a book that was never issued | Low      | P3       | This is an edge-case validation problem with limited impact and can be deferred while higher-impact defects are fixed.                  |

## Severity and Priority Trade-offs

Issue #3 is High severity and P0 priority because allowing the same book to be issued twice can create incorrect lending records and affect multiple users. It is therefore more urgent than defects that only affect convenience.

Issue #6 has Medium severity but P2 priority because the search problem affects usability, while the underlying book records remain intact. Issue #7 has Low severity and P3 priority because it is an edge-case validation problem with relatively low business impact.

## Sprint Decision

The three highest-priority issues (#3, #5, and #4) will be fixed during this sprint.

Issues #6 and #7 will not be fixed this sprint. They are deferred because their impact is lower than the selected defects and the team should focus on issues that affect core library operations and data integrity.
