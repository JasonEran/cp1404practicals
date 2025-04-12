"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_as_sentence(phrase):
    """
    Format the phrase as a sentence: start with a capital letter and end with a single full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('python code')
    'Python code.'
    """
    phrase = phrase.strip()
    if phrase:
        phrase = phrase[0].upper() + phrase[1:]
        if not phrase.endswith('.'):
            phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car("Test Car")
    assert car._odometer == 0, "Car does not set odometer correctly"
    assert car.fuel == 0, "Car does not set fuel to default correctly"

    car = Car("Test Car", fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when specified"


run_tests()

doctest.testmod()