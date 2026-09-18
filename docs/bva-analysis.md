# Boundary Value Analysis (BVA)

## 1. Fine Tier Boundaries

| Boundary | Value - 1 | Boundary Value | Value + 1 | Expected Results |
|---|---:|---:|---:|---|
| 0 | -1 | 0 | 1 | Invalid, No Fine, No Fine |
| 1 | 0 | 1 | 2 | No Fine, Low, Low |
| 8 | 7 | 8 | 9 | Low, Medium, Medium |
| 15 | 14 | 15 | 16 | Medium, High, High |
| 31 | 30 | 31 | 32 | High, Overdue, Overdue |

## 2. Borrow Limit Boundaries

The valid borrow limit is 0–5 books per member.

| Boundary | Value - 1 | Boundary Value | Value + 1 | Expected Result |
|---|---:|---:|---:|---|
| Maximum limit | 4 | 5 | 6 | Borrow allowed, Borrow allowed, Borrow rejected |

## 3. ISBN Length Boundaries

The valid ISBN length is 13 digits.

| Boundary | Value - 1 | Boundary Value | Value + 1 | Expected Result |
|---|---:|---:|---:|---|
| 13 digits | 12 | 13 | 14 | Invalid, Valid, Invalid |

Additional BVA values:

| Length | Expected Result |
|---:|---|
| 11 | Invalid |
| 12 | Invalid |
| 13 | Valid |
| 14 | Invalid |
| 15 | Invalid |

## 4. BVA Summary

Boundary Value Analysis focuses on values just below, at, and just above important boundaries. It helps identify off-by-one errors and incorrect boundary conditions.