import pytest
from library import fine_tier


@pytest.mark.parametrize(
    "days, expected",
    [
        (-1, "Invalid"),
        (0, "No Fine"),
        (1, "Low"),
        (7, "Low"),
        (8, "Medium"),
        (9, "Medium"),
        (14, "Medium"),
        (15, "High"),
        (16, "High"),
        (30, "High"),
        (31, "Overdue"),
        (32, "Overdue"),
    ],
)
def test_fine_tier_boundaries(days, expected):
    assert fine_tier(days) == expected