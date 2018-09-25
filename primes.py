"""Prime number library"""


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
