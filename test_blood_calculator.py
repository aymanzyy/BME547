import pytest

@pytest.mark.parametrize("input_HDL, expected", [
    [70, "Normal"], 
    [45, "Borderline Low"],
    [20, "Low"]])

    
def test_check_HDL(input_HDL, expected):
    from interfacer import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected
