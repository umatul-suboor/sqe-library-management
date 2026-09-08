# Equivalence Partitioning Analysis

## 1. Number of Books a Member Can Have

Business Rule:

A member can have a maximum of 5 books on loan at one time.

| Class | Values | Valid/Invalid | Representative |
|---|---|---|---|
| Valid | 0–5 | Valid | 3 |
| Invalid | 6+ | Invalid | 8 |

### Explanation

The valid equivalence class contains values from 0 to 5.
Instead of testing every value, 3 is selected as a representative of the valid class.

The invalid equivalence class contains values 6 and above.
The value 8 is selected as a representative of the invalid class.

---

## 2. ISBN

Business Rule:

An ISBN must contain exactly 13 numeric digits.

| Class | Example | Valid/Invalid |
|---|---|---|
| Valid 13-digit ISBN | 9781234567890 | Valid |
| Empty string | "" | Invalid |
| Too short | 123456789 | Invalid |
| Too long | 12345678901234 | Invalid |
| Letters | 978123456789A | Invalid |
| Symbols | 978-123456789 | Invalid |

### Explanation

The valid class contains ISBN values with exactly 13 numeric digits.

The invalid classes represent different types of invalid input, including empty input, values that are too short or too long, letters, and symbols.
