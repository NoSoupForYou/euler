"""Project Euler Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


divisors = list(range(2, 21))
n = max(divisors)
while True:
    if all((n % d == 0 for d in divisors)):
        print(n)
        break
    n += max(divisors)
