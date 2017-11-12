# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five
# coins can be separated into piles in exactly seven different ways, so p(5)=7.
#
#      OOOOO
#    OOOO   O
#     OO   OO
#   OOO   O   O
#   OO   OO   O
#  OO   O   O   O
# O   O   O   O   O
#
# Find the least value of n for which p(n) is divisible by one million.

import progressbar


def pentagonal(term):

    return ((3 * (term**2)) - term) / 2

def get_pentagonal_numbers(maxval):

    pentagonals = []
    p = 0
    n = 1
    while p <= maxval:
        p = pentagonal(n)
        pentagonals.append(p)
        n += 1

    return reversed(pentagonals)

def modulo_mil(partitions):

    return partitions % 1000000

def accel_asc(n):

    """
    Returns the number of integer partitions of n.
    :param n: integer to analyze
    :return: number of partitions of n
    """

    partitions = 0
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            partitions += 1
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        partitions += 1
    return partitions


def solve(maxvalue):

    """
    Returns the smallest n for which p(n) % 1000000 == 0.

    The first n for which p(n) >= 1000000 is 61.
    """

    bar = progressbar.ProgressBar(initial_value=70, max_value=progressbar.UnknownLength)
    nums = get_pentagonal_numbers(maxvalue)

    for n in nums:
        if modulo_mil(accel_asc(n)) == 0:
            return n
        bar.update(n)

# print solve(56000)
# print accel_asc(55374)

# This algorithm might simply be too slow.