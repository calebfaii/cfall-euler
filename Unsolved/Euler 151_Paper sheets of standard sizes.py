# A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special
# colour-proofing paper of  size A5.
#
# Every Monday morning, the foreman opens a new envelope, containing a large sheet of the special
# paper with size A1.
#
# He proceeds to cut it in half, thus getting two sheets of size A2.
# Then he cuts one of them in half to get two sheets of size A3 and so on until he obtains
# the A5-size sheet needed for the first batch of the week.
#
# All the unused sheets are placed back in the envelope.
# At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random.
# If it is of size A5, he uses it. If it is larger, he repeats the 'cut-in-half' procedure until he
# has what he needs and any remaining sheets are always placed back in the envelope.
#
# Excluding the first and last batch of the week, find the expected number of times (during each week) that
# the foreman finds a single sheet of paper in the envelope.
#
# Give your answer rounded to six decimal places using the format x.xxxxxx .

import time
import math

initial = [1, 0, 0, 0, 0]
first = [0, 1, 1, 1, 1]

def a1_func(list):

    a1 = list[0]
    a2 = list[1]
    a3 = list[2]
    a4 = list[3]
    a5 = list[4]
    a1 -= 1
    a2 += 1
    a3 += 1
    a4 += 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5]
    return outcome


def a2_func(list):
    a1 = list[0]
    a2 = list[1]
    a3 = list[2]
    a4 = list[3]
    a5 = list[4]
    a2 -= 1
    a3 += 1
    a4 += 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5]
    return outcome


def a3_func(list):
    a1 = list[0]
    a2 = list[1]
    a3 = list[2]
    a4 = list[3]
    a5 = list[4]
    a3 -= 1
    a4 += 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5]
    return outcome


def a4_func(list):
    a1 = list[0]
    a2 = list[1]
    a3 = list[2]
    a4 = list[3]
    a5 = list[4]
    a4 -= 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5]
    return outcome


def a5_func(list):
    a1 = list[0]
    a2 = list[1]
    a3 = list[2]
    a4 = list[3]
    a5 = list[4]
    a5 -= 1
    outcome = [a1, a2, a3, a4, a5]
    return outcome


def all_outcomes(list):

    """Receives a list; outputs a list of lists containing all equiprobable outcomes."""

    outcomes = []

    a1 = list[0]
    a2 = list[1]
    a3 = list[2]
    a4 = list[3]
    a5 = list[4]

    choices = sum(list)

    if choices > 0:
        if a1 > 0:
            for i in range(0, a1):
                outcomes.append(a1_func(list))
        if a2 > 0:
            for i in range(0, a2):
                outcomes.append(a2_func(list))
        if a3 > 0:
            for i in range(0, a3):
                outcomes.append(a3_func(list))
        if a4 > 0:
            for i in range(0, a4):
                outcomes.append(a4_func(list))
        if a5 > 0:
            for i in range(0, a5):
                outcomes.append(a5_func(list))
    if choices == 0:
        x = [0, 1, 1, 1, 1]
        outcomes.append(x)
    return outcomes

round_1 = all_outcomes(initial)
r2 = []
for i in round_1:
    r2.append(all_outcomes(i))

print r2




