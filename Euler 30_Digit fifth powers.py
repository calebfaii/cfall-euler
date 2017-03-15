# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import progressbar


def break_int(n):

    return list(int(i) for i in str(n))


def raise_fifth(digits):

    value = 0
    for num in digits:
        value += num**5
    return value


def solve():

    solutions = []
    bar = progressbar.ProgressBar(max_value=1000000)
    for i in range(2, 1000000):
        num = break_int(i)
        bar.update(i)
        if i == raise_fifth(num):
            solutions.append(i)
    print " "
    return solutions


print solve()
