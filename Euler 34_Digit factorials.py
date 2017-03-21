# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from operator import mul
import progressbar


def factorial(n):

    return reduce(mul, list(range(2, n + 1)), 1)


def break_int(n):

    return list(int(i) for i in str(n))


def factorial_sum(number):

    num_sum = 0
    digits = break_int(number)
    for digit in digits:
        num_sum += factorial(digit)
    return num_sum


def solve(maximum):
    answers = []
    bar = progressbar.ProgressBar(initial_value=10, max_value=maximum + 1)
    for number in range(11, maximum + 1):
        fsum = factorial_sum(number)
        if fsum == number:
            answers.append(number)
        bar.update(number)
    print " "
    return answers

print solve(100000)
# SOLVED
