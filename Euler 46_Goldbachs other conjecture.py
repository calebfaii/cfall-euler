# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#
# 9 = 7 + 2x1^2
# 15 = 7 + 2x2^2
# 21 = 3 + 2x3^2
# 25 = 7 + 2x3^2
# 27 = 19 + 2x2^2
# 33 = 31 + 2x1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written
# as the sum of a prime and twice a square?


import itertools


def isprime(n):

    """Returns True if n is prime."""

    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def primes_sieve(limit):

    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
    return primes


def squares(maximum):

    results = []
    for i in itertools.count(1):
        if i ** 2 <= maximum:
            results.append(i ** 2)
        else:
            return results


def get_odd_composites(maximum):

    odd_composites = set()
    for num in range(3, maximum + 1, 2):
        if not isprime(num):
            odd_composites.add(num)
    return odd_composites


def get_combos(maximum):

    primes = primes_sieve(maximum)
    square = squares(maximum)

    outputs = set()
    for p in primes:
        for s in square:
            result = p + (2 * s)
            if result % 2 != 0 and not isprime(result):
                outputs.add(result)
    odd_comps = get_odd_composites(max(outputs))
    print "The solution is %d." % min(outputs ^ odd_comps)

get_combos(10000)
# SOLVED
