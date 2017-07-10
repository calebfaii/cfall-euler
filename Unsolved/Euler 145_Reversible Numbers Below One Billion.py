# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely
# of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such
# numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed
# in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion?

import progressbar

def flip_and_add(n):

    """
    Receives an integer; returns the sum of the integer and its reverse.
    """

    rev = str(n)[::-1]
    if int(rev[0]) == 0:
        return 0
    return n + int(rev)

def is_odd_digit(n):
    """
    Returns True if a digit is odd.
    """
    if n in [1, 3, 5, 7, 9]:
        return True
    return False


def all_odd_digits(n):

    """
    Returns True if each digit is odd.
    """

    digits = (int(i) for i in str(n))
    if all(is_odd_digit(i) for i in digits):
        return True
    else:
        return False


def solve():





