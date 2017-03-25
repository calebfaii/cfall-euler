# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time


def findtriplet(x=0, y=500):

    for a in range(x, y):
        for b in range(a, y):
            for c in range(b, y):
                if a < b < c and a + b + c == 1000:
                    a2 = a**2
                    b2 = b**2
                    c2 = c**2

                    if a2 + b2 == c2:

                        product = (a * b * c)
                        print "A =", a
                        print "B =", b
                        print "C =", c
                        print "Product =", product
                        break


def solve():
    start = time.time()
    findtriplet()
    elapsed = (time.time() - start)
    print " "
    print "Run time: ", elapsed, "seconds."


solve()
# SOLVED
