import pytest
from library import fine_tier


@pytest.mark.parametrize('days,expected', [
    (0, 'No Fine'),
    (4, 'Low'),
    (10, 'Medium'),
    (20, 'High'),
    (45, 'Overdue'),
])
def test_fine_tier_valid_classes(days, expected):
    assert fine_tier(days) == expected


def test_fine_tier_negative_days():
    assert fine_tier(-3) == 'Invalid'   