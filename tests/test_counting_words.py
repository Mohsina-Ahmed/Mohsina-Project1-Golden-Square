from lib.counting_words import *
import pytest
def test_given_text_with_200_words():
    text = ' '.join("word" for i in range(0,200))
    result = calculate_reading_time(text)
    assert result == 1

def test_given_text_with_400_words():
    text = ' '.join("word" for i in range(0,400))
    result = calculate_reading_time(text)
    assert result == 2

def test_given_text_with_500_words():
    text = ' '.join("word" for i in range(0,500))
    result = calculate_reading_time(text)
    assert result == 2.5

def test_given_text_with_no_words():
    with pytest.raises(Exception) as e:
        result = calculate_reading_time(" ")
    error_message = str(e.value)
    assert error_message == "No word is given"
