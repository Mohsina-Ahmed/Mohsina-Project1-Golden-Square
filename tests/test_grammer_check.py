from lib.grammer_check import *
import pytest
def test_grammer_check_capital_punct():
    result = grammer_check("This is my test.")
    assert result == True

def test_grammer_check_no_capital_punct():
    result = grammer_check("this is my test.")
    assert result == False

def test_grammer_check_no_capital_no_punct():
    result = grammer_check("this is my test")
    assert result == False

def test_grammer_check_no_capital_punct():
    with pytest.raises(Exception) as e:
        result = grammer_check(" ")
    error_message = str(e.value)
    assert error_message == "No sentense is given"

