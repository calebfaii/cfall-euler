# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
# divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each
# of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and
# 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
# so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import progressbar


def sumofdivisors(number):

    if number > 1:
        table = []
        if number % 2 == 0:
            numhalf = (int(number * 0.5) + 1)
            for i in range(1, numhalf):
                if number % i == 0:
                    table.append(i)
            return sum(table)

        else:
            numhalf = int((number * 0.5) + 0.5)
            for i in range(1, numhalf):
                if number % i == 0:
                    table.append(i)
            return sum(table)
    if number <= 1:
        return 0


def find_amicable():

    amicablenumbers = []
    bar = progressbar.ProgressBar(max_value=10001)
    for num in range(3, 10001):
        num_sum = int(sumofdivisors(num))
        sum_num = int(sumofdivisors(num_sum))
        if num == sum_num:
            if num_sum != sum_num:
                amicablenumbers.append(num)
        bar.update(num)
    print " "
    print "Solution: ", sum(amicablenumbers)
    print "Pair value: ", sumofdivisors(sum(amicablenumbers))
    return


find_amicable()
# SOLVED
