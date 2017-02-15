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


def a1_func(bag):

    a1 = bag[0]
    a2 = bag[1]
    a3 = bag[2]
    a4 = bag[3]
    a5 = bag[4]
    prob = bag[5]
    a1 -= 1
    a2 += 1
    a3 += 1
    a4 += 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5, prob]
    return outcome


def a2_func(bag):
    a1 = bag[0]
    a2 = bag[1]
    a3 = bag[2]
    a4 = bag[3]
    a5 = bag[4]
    prob = bag[5]
    a2 -= 1
    a3 += 1
    a4 += 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5, prob]
    return outcome


def a3_func(bag):
    a1 = bag[0]
    a2 = bag[1]
    a3 = bag[2]
    a4 = bag[3]
    a5 = bag[4]
    prob = bag[5]
    a3 -= 1
    a4 += 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5, prob]
    return outcome


def a4_func(bag):
    a1 = bag[0]
    a2 = bag[1]
    a3 = bag[2]
    a4 = bag[3]
    a5 = bag[4]
    prob = bag[5]
    a4 -= 1
    a5 += 1
    outcome = [a1, a2, a3, a4, a5, prob]
    return outcome


def a5_func(bag):
    a1 = bag[0]
    a2 = bag[1]
    a3 = bag[2]
    a4 = bag[3]
    a5 = bag[4]
    prob = bag[5]
    a5 -= 1
    outcome = [a1, a2, a3, a4, a5, prob]
    return outcome


def run_batch(bag):

    """Receives a configuration with probability.  Returns at most 4 configurations with probabilities."""

    states = []

    a1 = bag[0]
    a2 = bag[1]
    a3 = bag[2]
    a4 = bag[3]
    a5 = bag[4]
    prob = bag[5]

    sheets = (a1 + a2 + a3 + a4 + a5)

    a1_prob = (float(a1) / sheets)
    a2_prob = (float(a2) / sheets)
    a3_prob = (float(a3) / sheets)
    a4_prob = (float(a4) / sheets)
    a5_prob = (float(a5) / sheets)

    if sheets == 1:
        print prob

    if sheets == 0:
        return [0, 1, 1, 1, 1, prob]

    if sheets > 0:

        if a1 > 0:
            out = a1_func(bag)
            out[5] = (out[5] * a1_prob)
            states.append(out)

        if a2 > 0:
            out = a2_func(bag)
            out[5] = (out[5] * a2_prob)
            states.append(out)

        if a3 > 0:
            out = a3_func(bag)
            out[5] = (out[5] * a3_prob)
            states.append(out)

        if a4 > 0:
            out = a4_func(bag)
            out[5] = (out[5] * a4_prob)
            states.append(out)

        if a5 > 0:
            out = a5_func(bag)
            out[5] = (out[5] * a5_prob)
            states.append(out)
    return states

def all_batches(max):

    batch = 0
    results_table = []
    temp_table = []
    initial_state = [1, 0, 0, 0, 0, 1.0]
    output = run_batch(initial_state)
    batch += 1
    while batch < max:
        for o in output:
            res = run_batch(o)
            for j in res:
                temp_table.append(j)

        batch += 1


all_batches(3)


