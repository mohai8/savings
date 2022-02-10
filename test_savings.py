import savings

def test_zero():
    assert savings.calculate_savings(0) == [6000]

def test_one():
    assert savings.calculate_savings(1) == [6000, 6300]