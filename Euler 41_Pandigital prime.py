# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

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


def solve():

    for length in range(9, 0, -1):
        print "Evaluating length %d..." % length
        permutations = list(itertools.permutations(range(length, 0, -1)))
        for p in permutations:
            p_int = int(''.join(map(str, p)))
            if isprime(p_int):
                return "The solution is %d, which is %d-digit pandigital." % (p_int, len(p))
        print "There are no %d-digit pandigital primes." % length
        print " "


print solve()
# SOLVED
