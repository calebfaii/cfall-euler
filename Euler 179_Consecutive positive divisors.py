# Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors.
# For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

import time
import math


def factors(n):
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0))))


def compare_divisors(top):

    """Starting at n = 2, compares the number of divisors of n and n + 1. Returns an integer."""

    count = 0
    val = 3
    n1 = factors(2)
    # perc = 1
    while val <= top:
        # if (val - 1) % 100000 == 0:
        #     print perc, "% complete."
        #     perc += 1
        n2 = factors(val)
        if n2 == n1:
            count += 1
            val += 1
            n1 = n2
        else:
            val += 1
            n1 = n2
    return count


def evaluate(stop):
    start = time.time()
    sol = compare_divisors(stop)
    print "Solution: ", sol
    elapsed = (time.time() - start)
    print "Run time: ", elapsed, "seconds."

evaluate(10**7)

