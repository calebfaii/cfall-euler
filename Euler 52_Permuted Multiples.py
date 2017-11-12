# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
# and 6x, contain the same digits.

import progressbar


def break_integer(x):
    return set(int(digit) for digit in str(x))

def check_multiples(x):

    digits = break_integer(x)
    multiple = 2
    while multiple <= 6:
        value = x * multiple
        if digits == break_integer(value):
            multiple += 1
        else:
            return False
    return True

def solve():

    start_value = int(raw_input("Enter a starting value: "))
    solved = False
    bar = progressbar.ProgressBar(start_value=start_value, max_value=progressbar.UnknownLength)

    while not solved:
        check = check_multiples(start_value)
        if check:
            return "The solution is %d" % start_value
        if not check:
            start_value += 1
            bar.update(start_value)


print solve()
# SOLVED
