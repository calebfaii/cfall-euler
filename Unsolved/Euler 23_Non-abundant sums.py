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
import progressbar


def generateIntegers(num):

    """Generates a list of integers from 1 to num."""

    return list(i for i in range(1, num + 1))


def sumFactors(n):

    """Receives an integer; returns the sum of the factors of that integer."""

    return sum(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))) - n


def isAbundant(num):

    """Receives an upper bound.  Returns a list of all abundant numbers in that range."""

    abundant = []
    for i in range(2, num + 1):
        factor_sum = sumFactors(i)
        if factor_sum > i:
            abundant.append(i)
    return abundant


def abundantSums(abundant_list):

    """Receives a list of abundant numbers.
    Returns the sums of all possible r=2 permutations."""

    absums = []
    a_list = itertools.combinations_with_replacement(abundant_list, r=2)
    bar = progressbar.ProgressBar(max_value=14604310)
    counter = 1
    for i in a_list:
        value = sum(i)
        if value <= 21823:
            if value not in absums:
                absums.append(value)
        bar.update(counter)
        counter += 1
    absums.sort()
    return absums


def editList(absums, integers):

    """Receives a list of sums of abundant numbers.
    If the sum is itself abundant, the number is removed from a list of integers.
    Returns the sum of all non-abundant integers in a given range."""

    for i in absums:
        if i in integers:
            integers.remove(i)
    print integers
    print "Answer: ", sum(integers)

def solve(n):

    start = time.time()
    editList(abundantSums((isAbundant(n))), generateIntegers(n))
    elapsed = (time.time() - start)
    print "Found in", elapsed, "seconds."

solve(21823)
# IT WORKS!