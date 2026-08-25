# Triage Log

## Sprint Triage — Library Management System

### Issue Ranking

1. Same book can be issued twice — High severity, P1 priority — Fix this sprint.
2. Returned book remains unavailable — High severity, P1 priority — Fix this sprint.
3. Negative book quantity accepted — Medium severity, P2 priority — Fix this sprint.
4. Book search fails with different capitalization — Medium severity, P2 priority — Won't fix this sprint.
5. Non-issued book can be returned — Low severity, P3 priority — Won't fix this sprint.

### Triage Reasoning

The duplicate book issue is ranked first because it can create incorrect borrowing records and allow the same physical book to be issued to multiple students.

The returned-book availability issue is ranked second because it directly affects the library borrowing process and prevents returned books from being issued again.

The negative quantity issue is ranked third because it creates invalid inventory data, but it does not stop the main library operations.

The case-sensitive search issue has Medium severity but P2 priority because it affects usability while the main borrowing and returning functions still work.

The non-issued book return issue has Low severity and P3 priority because it has limited impact and can be addressed in a later sprint.

### Severity vs Priority Trade-offs

The duplicate-book defect has High severity and P1 priority because it corrupts important borrowing records and requires quick attention.

The case-sensitive search defect has Medium severity and P2 priority because it affects users' ability to find books but does not block the core library operations.

### Sprint Decision

The two defects that will not be fixed this sprint are:

- Case-sensitive book search — deferred because of lower business urgency.
- Non-issued book return — deferred because of low impact and limited effect on normal library operations.
