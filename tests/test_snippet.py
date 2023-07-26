import pytest
from lib.snippet import *
def test_snippet_less_than_five():
    result = make_snippet("This is a test")
    assert result == "This is a test"
def test_snippet_greater_than_five():
    result = make_snippet("This is not a small test but a bigger one")
    assert result == "This is not a small..."
def test_snippet_equal_to_five():
    result = make_snippet("This is a small drill")
    assert result == "This is a small drill"


def test_snippet_no_argument():
    with pytest.raises(Exception) as e:
        make_snippet()
    error_message = str(e.value)
    assert error_message == "make_snippet() missing 1 required positional argument: 'sentense'"

def test_count_words_zero():
    result = count_words(" ")
    assert result == 0
def test_count_words():
    result = count_words("This is my test")
    assert result == 4