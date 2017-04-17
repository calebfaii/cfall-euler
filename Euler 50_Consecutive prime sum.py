# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?


def isprime(n):

    """Returns True if n is prime."""

    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def primes_sieve(limit):

    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
    return primes


def solve():

    p_list = primes_sieve(1000000)
    best_len = 21
    solutions = []
    lengths = []

    for num in range(10):
        stop = best_len + num

        while sum(p_list[num:stop]) < 1000000:
            candidate = sum(p_list[num:stop])

            if isprime(candidate):
                length = stop - num

                if length >= best_len:
                    best_len = length
                    lengths.append(length)
                    solutions.append(candidate)

            stop += 1

    index = lengths.index(best_len)
    print "%d can be written as the sum of %d consecutive primes." % (solutions[index], best_len)


solve()
# SOLVED
