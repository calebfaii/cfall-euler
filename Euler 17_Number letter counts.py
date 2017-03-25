# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
# there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
# 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
# out numbers is in compliance with British usage.


def single_digits(n):

    if n == 1:
        return 3
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 4
    if n == 5:
        return 4
    if n == 6:
        return 3
    if n == 7:
        return 5
    if n == 8:
        return 5
    if n == 9:
        return 4
    if n == 0:
        return 0


def teens(n):

    if n == 10:
        return 3
    if n == 11:
        return 6
    if n == 12:
        return 6
    if n == 13:
        return 8
    if n == 14:
        return 8
    if n == 15:
        return 7
    if n == 16:
        return 7
    if n == 17:
        return 9
    if n == 18:
        return 8
    if n == 19:
        return 8


def double_digits(n):

    if n == 1:
        pass
    if n == 2:
        return 6
    if n == 3:
        return 6
    if n == 4:
        return 5
    if n == 5:
        return 5
    if n == 6:
        return 5
    if n == 7:
        return 7
    if n == 8:
        return 6
    if n == 9:
        return 6
    if n == 0:
        return 0


def triple_digits(n):

    if n == 1:
        return 13
    if n == 2:
        return 13
    if n == 3:
        return 15
    if n == 4:
        return 14
    if n == 5:
        return 14
    if n == 6:
        return 13
    if n == 7:
        return 15
    if n == 8:
        return 15
    if n == 9:
        return 14
    if n == 0:
        return 0


def solve():

    numbers = list(range(1, 1001))
    score = 0

    for i in numbers:

        n_score = 0
        digits = list(int(x) for x in str(i))

        if len(digits) == 1:
            n_score += single_digits(digits[0])

        if len(digits) == 2:
            if digits[0] == 1:
                n_score += teens(i)
            else:
                n_score += double_digits(digits[0])
                n_score += single_digits(digits[1])

        if len(digits) == 3:
            if digits[1] == 1:
                two = i - 100 * digits[0]
                n_score += teens(two)
                n_score += triple_digits(digits[0])
                if digits[2] == 0:
                    n_score -= 3
            else:
                n_score += single_digits(digits[2])
                n_score += double_digits(digits[1])
                n_score += triple_digits(digits[0])

        if len(digits) == 4:
            n_score += 11

        score += n_score
    print "Solution: ", score


solve()
# SOLVED
