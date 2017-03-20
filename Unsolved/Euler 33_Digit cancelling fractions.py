# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than
# one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from operator import mul


def get_decimal_fracs():

    values = list(x for x in range(11, 99))
    tens = list(y for y in range(20, 91, 10))
    for ten in tens:
        values.remove(ten)
    return values


def break_int(n):

    return list(int(i) for i in str(n))


def gen_candidates():

    splits = []
    candidates = []
    for num in get_decimal_fracs():
        splits.append(break_int(num))
    for a in splits:
        for b in splits:
            if a != b:
                frac = [a, b]
                if frac[0][1] == frac[1][0]:
                    candidates.append(frac)
    print " "
    print "There are", len(candidates), "fractions in the problem space."
    print " "
    return candidates


def compute_and_compare(candidate_list):

    solutions = []
    dec_vals = []
    for i in candidate_list:
        temp = []
        for f in i:
            temp.append(int(''.join(map(str, f))))
        if temp[0] < temp[1]:
            dec_vals.append(temp)
    maximum = len(dec_vals)
    print "Evaluating", maximum, "candidates whose value is less than 1."
    print " "
    for i in range(0, maximum):
        initval = float(dec_vals[i][0]) / float(dec_vals[i][1])
        reduced = float(str(dec_vals[i][0])[0]) / float(str(dec_vals[i][1])[-1])
        if initval == reduced:
            solutions.append(dec_vals[i])
    print "The non-trivial examples are:"
    for s in solutions:
        print s
    print " "
    return solutions


def reduce_and_solve(answers):

    decs = []
    for i in answers:
        decs.append(float(i[0]) / float(i[1]))
    print "The product is", reduce(mul, decs, 1), "."

reduce_and_solve(compute_and_compare(gen_candidates()))
# SOLVED
