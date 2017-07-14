# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
# sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
import time
import itertools


def generate_integers(num):

    """Generates a list of integers from 1 to num."""

    return [i for i in range(1, num + 1)]


def sum_factors(n):

    """Receives an integer; returns the sum of the factors of that integer."""

    return sum(set(reduce(list.__add__, ([i, n // i]
                                         for i in range(1, int(math.sqrt(n)) + 1)
                                         if n % i == 0)))) - n


def is_abundant(num):

    """Receives an upper bound.  Returns a list of all abundant numbers in that range."""

    abundant = []
    for i in range(2, num + 1):
        factor_sum = sum_factors(i)
        if factor_sum > i:
            abundant.append(i)
    return abundant


def abundant_sums(abundant_list):

    """Receives a list of abundant numbers.
    Returns the sums of all possible r=2 permutations."""

    print "Running..."
    absums = set(sum(i) for i in itertools.combinations_with_replacement(abundant_list, r=2) if sum(i) <= 21823)
    return sorted(absums)


def edit_list(absums, integers):

    """Receives a list of sums of abundant numbers.
    If the sum is itself abundant, the number is removed from a list of integers.
    Returns the sum of all non-abundant integers in a given range."""

    for i in absums:
        if i in integers:
            integers.remove(i)
    print "Answer: ", sum(integers)


def solve(n):

    start = time.time()
    edit_list(abundant_sums((is_abundant(n))), generate_integers(n))
    elapsed = (time.time() - start)
    print "Found in", elapsed, "seconds."


solve(21823)
# SOLVED
