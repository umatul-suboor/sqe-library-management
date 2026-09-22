import pytest


@pytest.mark.parametrize('days,expected', [
    (0, 'No Fine'),
    (4, 'Low'),
    (20, 'High'),
    (45, 'Overdue'),
])
def test_fine_tier_valid_classes(fine_calculator, days, expected):
    assert fine_calculator(days) == expected


def test_fine_tier_negative_days(fine_calculator):
    assert fine_calculator(-3) == 'Invalid'