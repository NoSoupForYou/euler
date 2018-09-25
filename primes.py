"""Prime number library"""


def primes():
    """Slowly generate primes"""
    primes = []
    current = 1
    while True:
        current += 1
        if any((current % n == 0 for n in primes)):
            continue
        else:
            primes.append(current)
            yield current


def n_primes_fast(n):
    """Quickly generate primes up to n"""
    candidates = list(range(n + 1)) # candidates[i] == i
    for i in range(2, n + 1):
        if candidates[i] is not None:
            yield i

            # Remove all multiples of i
            j = 2
            while j * i <= n:
                candidates[j * i] = None
                j += 1
