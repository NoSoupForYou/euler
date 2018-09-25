"""Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def primes():
    """Generate primes"""
    primes = []
    current = 1
    while True:
        current += 1
        if any((current % n == 0 for n in primes)):
            continue
        else:
            primes.append(current)
            yield current


def prime_factors(n):
    """Generate prime factors of n"""
    if n == 1: return
    for i in primes():
        yielded = False
        while n % i == 0:
            n /= i
            if not yielded:
                yield i
                yielded = True
            if n == 1:
                return


print(max(prime_factors(600851475143)))
