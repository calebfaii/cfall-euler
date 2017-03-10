# A number chain is created by continuously adding the square of the digits in a number to form a new number until it
# has been seen before.
#
# For example,
#
# 44 - 32 - 13 - 10 - 1 - 1
# 85 - 89 - 145 - 42 - 20 - 4 - 16 - 37 - 58 - 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that
# EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

import progressbar

one = 0
eightynine = 0


def square_digits(n):

    value = 0
    digits = list(int(i) for i in str(n))
    for x in digits:
        value += x**2
    return value


def run_chain(n):

    sq = square_digits(n)

    if sq == 89:
        global eightynine
        eightynine += 1
        return True
    if sq == 1:
        global one
        one += 1
        return True
    else:
        run_chain(sq)


def solve():

    bar = progressbar.ProgressBar(max_value=10000000)
    for num in range(1, 10000000):
        run_chain(num)
        bar.update(num)
    print " "
    print "Ones: ", one
    print "89's: ", eightynine

solve()
# WORKS!
