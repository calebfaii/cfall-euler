# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual
# in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are
# permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
# property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?


import progressbar


def primes_sieve(limit):

    print "Generating primes..."
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        if i > 999:
            primes.append(i)
    print "Primes generated."
    print " "
    return primes


def break_int(n):

    return {int(i) for i in str(n)}


def get_permutations():

    options = []
    primes = primes_sieve(10000)
    print "Generating candidates..."
    for p in primes:
        candidates = [p]
        pp = break_int(p)
        for h in primes:
            if h > p:
                hh = break_int(h)
                if pp == hh:
                    candidates.append(h)
            if len(candidates) > 3:
                options.append(candidates)
    print "Candidates generated."
    print " "
    return options


def solve():

    narrow = []
    strings = []
    candidates = get_permutations()
    print "Solving..."
    bar = progressbar.ProgressBar(max_value=len(candidates) + 1)
    counter = 1
    for c in candidates:
        for i in c:
            for j in c:
                for k in c:
                    if i - j == j - k and i != j and j != k and i != k:
                        answer = {i, j, k}
                        if answer not in narrow:
                            narrow.append(answer)
                            string = str(i) + str(j) + str(k)
                            strings.append(string)
        bar.update(counter)
        counter += 1
    print " "
    print "Solutions: "
    for i in strings:
        print i


solve()
# SOLVED
