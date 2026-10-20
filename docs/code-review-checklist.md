# Code Review Checklist — Library Management System

## 1. Correctness
- [ ] Does the function return the correct result?
- [ ] Are boundary conditions handled correctly?
- [ ] Are invalid or missing members handled safely?

## 2. Tests
- [ ] Are normal cases covered by tests?
- [ ] Are edge cases, including a library with one member, tested?
- [ ] Do tests check expected results rather than only checking that code runs?

## 3. Readability
- [ ] Are variable and function names meaningful?
- [ ] Does each function have a clear docstring?
- [ ] Is the code formatted consistently and easy to understand?

## 4. Design
- [ ] Does the code follow the existing project structure?
- [ ] Is unnecessary repeated logic avoided?
- [ ] Does the function have one clear responsibility?

## 5. Risk
- [ ] Could the change break existing library features?
- [ ] Are missing or unexpected inputs handled safely?
- [ ] Is the solution efficient for larger libraries?

## Lessons Learned
The most valuable checklist item was checking boundary conditions because it helped identify an off-by-one error.

Next time, I would add a checklist item to verify how the function behaves when the requested member does not exist in the library.
