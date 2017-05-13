# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
# nCr = n! / (r!(n-r)!)
# 	,where r <= n.
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

import math


def combinatoric_gen(n, r):

    nCr = (math.factorial(n) / (math.factorial(r) * math.factorial((n - r))))
    if nCr > 1000000:
        return True
    else:
        return False


def solve():

    matches = 0
    for n in xrange(23, 101):
        for r in xrange((n - 1), -1, -1):
            if combinatoric_gen(n, r):
                matches += 1
                continue
            continue
    return matches


print "Solution:", solve()
# SOLVED
