# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there
# are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?

import progressbar


def get_sides(perimeter):

    solutions = []

    for a in range(1, perimeter / 2):
        for b in range(a, perimeter / 2):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                sides = {a, b, c}
                if sides not in solutions:
                    solutions.append(sides)
    return solutions


def solve():

    maximum = 0
    solution = 0
    bar = progressbar.ProgressBar(max_value=1000)

    for p in range(1, 1001):
        solutions = get_sides(p)
        num_solutions = len(solutions)
        if num_solutions > maximum:
            maximum = num_solutions
            solution = p
        bar.update(p)
    print " "
    return "The perimeter value %d yields %d solutions." % (solution, maximum)


print solve()
# SOLVED
