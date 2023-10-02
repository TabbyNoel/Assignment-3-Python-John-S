import script
import pytest
from unittest.mock import patch

def test_a_returns_word_from_w():
    word = script.a()
    assert word in script.w, f"Expected word from w but got {word}"

def test_f_takes_single_character():
    with patch('builtins.input', return_value='ab'):
        with pytest.raises(ValueError):  # or check some other behavior
            script.f()

def test_f_takes_alphabetical_character():
    with patch('builtins.input', return_value='1'):
        with pytest.raises(ValueError):  # or check some other behavior
            script.f()

@patch('builtins.input', side_effect=['a', 'a'])
def test_repeated_guesses_no_penalty(mocked_input):
    x, y, z_before = script.b()
    script.f()
    script.f()
    _, _, z_after = script.b()
    assert z_before == z_after, "Expected no penalty for repeated guesses"
