# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


def solve():

    value = str(2**1000)
    digit_sum = 0
    for num in value:
        digit_sum += int(num)
    print "Solution: ", digit_sum


solve()
# SOLVED
