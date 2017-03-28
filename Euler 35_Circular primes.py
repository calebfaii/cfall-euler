# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import progressbar


def primes_sieve(limit):

    not_prime = set()
    primes = []
    for i in range(2, limit):
        if i in not_prime:
            continue
        for f in range(i*2, limit, i):
            not_prime.add(f)
        primes.append(i)
    return primes


def split_int(n):

    vals = list(i for i in str(n))
    maxval = len(vals)
    circulars = []
    while maxval > 0:
        circulars.append(int(''.join(map(str, vals))))
        vals.append(vals[0])
        vals.remove(vals[0])
        maxval -= 1
    return circulars


def solve():

    solution = []
    primes = primes_sieve(1000000)
    maxbar = len(primes) + 1
    bar = progressbar.ProgressBar(max_value=maxbar)
    counter = 1
    for prime in primes:
        templist = split_int(prime)
        if all(i in primes for i in templist):
            solution.append(prime)
        bar.update(counter)
        counter += 1
    print " "
    print "Circular Primes: ", solution
    print "Number of Circular Primes: ", len(solution)


print solve()
# SOLVED
