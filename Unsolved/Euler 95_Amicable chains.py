# The proper divisors of a number are all the divisors excluding the number itself. For example,
# the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we
# call it a perfect number.
#
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors
# of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
#
# Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
#
# 12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 ->...)
#
# Since this chain returns to its starting point, it is called an amicable chain.
#
# Find the smallest member of the longest amicable chain with no element exceeding one million.

import math
import progressbar


def sum_factors(n):

        return sum(set(reduce(list.__add__, ([i, n // i]
                                             for i in range(1, int(math.sqrt(n)) + 1)
                                             if n % i == 0)))) - n


def run_chain(n):

    match_seen = False
    results = [sum_factors(n)]

    while not match_seen:

        if results[-1] > 0:
            current_sum = sum_factors(results[-1])
        else:
            return(0, 0)

        if current_sum in results:
            return((len(results), min(results)))

        if current_sum <= 1000000:
            results.append(current_sum)

        if current_sum > 1000000:
            return (0, 0)



def solve():

    longest_chain = 0
    smallest_element = 0

    bar = progressbar.ProgressBar(initial_value=11, max_value=327601)

    for num in range(17, 327600):

        outcome = run_chain(num)
        chain_length, smallest_val = outcome[0], outcome[1]
        if chain_length > longest_chain:
            longest_chain = chain_length
            smallest_element = smallest_val
        bar.update(num)

    return smallest_element

print solve()









