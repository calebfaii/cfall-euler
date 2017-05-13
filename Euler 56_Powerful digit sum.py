# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost
# unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the
# digits in each number is only 1.
#
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?


def evaluate_a_b(a, b):

    return sum([int(i) for i in str(a**b)])


def solve():

    maximum_sum = 0

    for a in range(1, 100):
        for b in range(1, 100):

            digit_sum = evaluate_a_b(a, b)
            if digit_sum > maximum_sum:
                maximum_sum = digit_sum

    return "Solution: %d" % maximum_sum

print solve()
# SOLVED
