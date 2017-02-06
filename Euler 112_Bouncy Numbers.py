# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
# for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below
# one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers
# first reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy
# numbers is equal to 90%.
#
# Find the least number for which the proportion of bouncy numbers is exactly 99%.

import time


def is_bouncy(num):

    """Receives a number; returns True if the number is bouncy."""

    sort = sorted([int(d) for d in str(num)])
    rev = sorted([int(d) for d in str(num)])
    rev.reverse()
    sort1 = int(''.join(map(str, sort)))
    rev1 = int(''.join(map(str, rev)))
    if num == sort1:
        return False
    if num == rev1:
        return False
    else:
        return True


def count_pct():

    tally = 0
    value = 1

    start = time.time()
    print "Running..."

    while True:
        frac = (float(tally) / float(value))
        instance = is_bouncy(value)
        if value % 100000 == 0:
            print "Evaluating", value
        if instance is True:
            tally += 1
            if frac == 0.990:
                elapsed = (time.time() - start)
                print "Run time: ", elapsed, "seconds."
                print frac, "% bouncy."
                return value
            value += 1
        if instance is False:
            value += 1


print count_pct()
