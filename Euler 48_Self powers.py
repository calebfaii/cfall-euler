# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

import progressbar

def raise_self(n):

    return n**n

def solve():

    value = 0
    bar = progressbar.ProgressBar(max_value=1000)
    for i in range(1,1001):
        value += raise_self(i)
        bar.update(i)

    print " "
    return value

print solve()
# 9110846700
