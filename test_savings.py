import savings

def test_initial_value():
    assert savings.calculate_savings(0) == [6000]

def test_amount_after_one_year_at_default_interest():
    assert savings.calculate_savings(1) == [6000, 6300]


def test_amount_after_one_year_at_ten_percent():
    assert savings.calculate_savings(1, interest=10) == [
        6000, 6600
    ]

def test_amount_5000_after_one_year_at_ten_percent():
    assert savings.calculate_savings(
        1, annual_savings=5000, interest=10
    ) == [5000, 5500]


def test_amount_and_two_years_at_ten_percent():
    assert savings.calculate_savings(2, interest=10) == [
        6000, 6600, 13860
    ]