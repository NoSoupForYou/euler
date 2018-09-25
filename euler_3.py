"""Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


from primes import primes


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
