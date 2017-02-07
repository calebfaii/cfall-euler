# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there
# are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?

import math


def catalan(n):

    """Returns the Catalan number of the input."""

    c = math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))
    return c


def exceedance_paths(n):

    """Returns the number of exceedance values for an n by n matrix."""

    return n+1


def unique_paths(n):

    """Returns the number of unique paths through an n by n matrix (down and right only)."""

    return catalan(n) * exceedance_paths(n)

print unique_paths(20)
