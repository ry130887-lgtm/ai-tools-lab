def is_palindrome(s):
    """Return True if the given string is a palindrome."""
    return s == s[::-1]


def count_words(text):
    """Return the number of words in the given text."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32