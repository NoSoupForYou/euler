"""Project Euler Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def products():
    """Yields products of two three-digit numbers"""
    for i in range(100, 1000):
        for j in range(100, 1000):
            yield i * j


def is_palindrome(n):
    """Evaluates whether n is a palindrome"""
    str_n = str(n)
    return "".join(reversed(str_n)) == str_n


print(max(filter(is_palindrome, products())))
