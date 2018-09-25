"""Project Euler Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from math import sqrt


def triplets(n):
    """Generate all triplets that sum to n"""
    for i in range(1, n - 2):
        for j in range(i, n - i):
            yield i, j, n - i - j


def pythagorean(i, j, k):
    """Evaluate whether i, j, k is a pythagorean triplet"""
    largest = max(i, j, k)
    smaller = {i, j, k}
    smaller.remove(largest)
    return sqrt(sum((x ** 2 for x in smaller))) == largest


def special_triplet(n):
    """Find the special pythagorean triplet that sums to n"""
    for i, j, k in triplets(n):
        if pythagorean(i, j, k):
            return i, j, k


i, j, k = special_triplet(1000)
print(i * j * k)
