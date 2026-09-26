from app import calculate_total, apply_discount


def test_calculate_total():
    assert calculate_total(100, 3) == 300


def test_apply_discount():
    assert apply_discount(300, 10) == 270
