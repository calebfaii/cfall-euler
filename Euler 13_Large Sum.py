# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# Filename: PE13.txt


def import_text():

    numbers = []
    number_list = open("PE13.txt")
    lines = number_list.read().split()
    for number in lines:
        numbers.append(number)
    return numbers


def solve(numbers):

    sum_total = 0
    for number in numbers:
        sum_total += int(number)
    print "Solution: ", str(sum_total)[0:10]


solve(import_text())
# SOLVED
