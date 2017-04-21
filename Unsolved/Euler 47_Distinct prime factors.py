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
                                     and (isprime(i) or (i % 2 == 0 and (i in [2, 4, 8, 16, 32, 64, 128, 256]))))))


print factors(644)