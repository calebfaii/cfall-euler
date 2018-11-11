# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously
# remove digits from left to right, and remain prime at
# each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are
# both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import progressbar


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


def break_int(n):

    return list(int(i) for i in str(n))


def join_list(p_list):

    return int(''.join(map(str, p_list)))


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


def solve(bound):

    primes = primes_sieve(bound)
    solutions = []
    bar = progressbar.ProgressBar(max_value=len(primes) + 1)
    counter = 1

    for prime in primes:
        bar.update(counter)
        counter += 1

        perms = []
        prime_split = break_int(prime)
        length = len(prime_split)

        if 0 in prime_split:
            continue

        if 4 in prime_split or 6 in prime_split or 8 in prime_split:
            continue

        if (prime_split[0] not in [2, 3, 5, 7]) or (prime_split[-1] not in [2, 3, 5, 7]):
            continue

        if length == 2 and all(val in primes for val in prime_split):
                solutions.append(prime)

        if length > 2:
            for num in range(1, length):
                if num not in perms:
                    perms.append(join_list(prime_split[:-num]))
                    perms.append(join_list(prime_split[num:]))

            if all(isprime(p) for p in perms):
                solutions.append(prime)


    print " "
    if len(solutions) == 11:
        print "The solution is", sum(solutions)
        return solutions

print solve(798000)
# SOLVED
