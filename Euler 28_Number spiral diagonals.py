# Starting with the number 1 and moving to the right in a
# clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?


def diagonal_sums(dimension):

    right_up = list(i**2 for i in range(3, dimension + 1, 2))
    left_up = []
    left_down = []
    right_down = []
    counter = 2
    for ru in right_up:
        lu = ru - counter
        ld = lu - counter
        rd = ld - counter
        left_up.append(lu)
        left_down.append(ld)
        right_down.append(rd)
        counter += 2
    return sum(right_up) + sum(right_down) + sum(left_up) + sum(left_down) + 1

print diagonal_sums(1001)
# SOLVED
