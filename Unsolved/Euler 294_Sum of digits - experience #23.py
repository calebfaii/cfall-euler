# For a positive integer k, define d(k) as the sum of the digits of k in its usual decimal
# representation. Thus d(42) = 4+2 = 6.
#
# For a positive integer n, define S(n) as the number of positive integers k < 10^n with
# the following properties :
#
#     k is divisible by 23 and
#     d(k) = 23.
#
# You are given that S(9) = 263626 and S(42) = 6377168878570056.
#
# Find S(11^12) and give your answer mod 10^9.

import progressbar


def d(k):

    k_score = 0
    for num in str(k):
        k_score += int(num)
    return k_score


def s(n):

    upper_bound = 10**n
    bar = progressbar.ProgressBar(max_value=(upper_bound / 23) + 1)
    mod_23s = []
    counter = 1
    for value in range(23, upper_bound, 23):
        bar.update(counter)
        counter += 1
        if d(value) == 23:
            mod_23s.append(value)
    print " "
    print " "
    print len(mod_23s)


# s(9)

# ABANDON SHIP!




