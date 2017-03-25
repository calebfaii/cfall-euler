import progressbar


def primes_sieve(limit):

    limitn = limit+1
    not_prime = set()
    primes = []
    bar = progressbar.ProgressBar(max_value=2000000)
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
        bar.update(i)
    return primes


def solve():

    primes = primes_sieve(2000000)
    solution = sum(primes)
    print " "
    print "Solution: ", solution

solve()
# SOLVED
