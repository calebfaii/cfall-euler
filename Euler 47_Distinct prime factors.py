# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 x 7
# 15 = 3 x 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

import time
import itertools
from operator import mul


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


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0
                                     and (((isprime(i) or isprime(n//i))
                                           or (i % 2 == 0 and (i in [2**x for x in xrange(1, 200)]))
                                           or (i % 3 == 0 and (i in [3**x for x in xrange(1, 200)])))))))


def get_factorization(number):

    if isprime(number):
        return None
    factor_set = factors(number)
    iterator = list(itertools.permutations(factor_set, r=4))
    for factorization in iterator:
        product = reduce(mul, factorization)
        if product == number:
            return factorization


def get_starting_list(number):

    value = number
    while True:
        if not isprime(value) and not isprime(value + 1) and not isprime(value + 2) and not isprime(value + 3):
            return [i for i in range(value, value + 4)]
        else:
            value += 1


def solve(start_index=1, step=1000):

    solved = False
    index = start_index
    start = time.time()
    while not solved:
        r_factors = {}
        for k in xrange(index, index + step):
            k_fac = get_factorization(k)
            if k_fac:
                if len(k_fac) > 0:
                    r_factors.update({k: k_fac})
        factor_keys = [k for k in r_factors.keys()]
        factor_keys.sort()
        for i in xrange(len(factor_keys) - 3):
            if factor_keys[i] + 1 == factor_keys[i + 1]:
                if factor_keys[i] + 2 == factor_keys[i + 2]:
                    if factor_keys[i] + 3 == factor_keys[i + 3]:
                        num1 = set(i for i in r_factors[factor_keys[i]])
                        num2 = set(i for i in r_factors[factor_keys[i + 1]])
                        num3 = set(i for i in r_factors[factor_keys[i + 2]])
                        num4 = set(i for i in r_factors[factor_keys[i + 3]])
                        compare = num1 | num2 | num3 | num4
                        if len(num1) + len(num2) + len(num3) + len(num4) == len(compare):
                            print "Solution found in %d seconds." % (time.time() - start)
                            return "The solution is %d." % factor_keys[i]
            continue
        print "No matches below %d." % (index + step)
        index += step

print solve()
# SOLVED
