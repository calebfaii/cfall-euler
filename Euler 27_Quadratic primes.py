# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39
# . However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
#
# is clearly divisible by 41.
#
# The incredible formula n2-79n+1601
# was discovered, which produces 80 primes for the consecutive values 0<=n<=79
#
# . The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
#     n2+an+b
#
# , where |a|<1000 and |b|<=1000
#
# where |n|
# is the modulus/absolute value of n
# e.g. |11|=11 and |-4|=4
#
# Find the product of the coefficients, a
# and b, for the quadratic expression that produces the maximum number of primes for consecutive
# values of n, starting with n=0.

import progressbar

coef = 0
consecutive = 0
pair = [0, 0]


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


def quadratic(n, a, b):

    return (n**2) + (a * n) + b


def evaluate_pair(alist, blist, primelist):

    bar = progressbar.ProgressBar(max_value=4000000)
    bar_ticker = 1
    for anum in alist:
        for bnum in blist:
            # print "ANUM:", anum
            # print "BNUM:", bnum
            n = 0
            consec = 0
            cond = True
            while cond:
                # print "N:", n
                trial = quadratic(n, anum, bnum)
                # print "Trial:", trial
                if trial in primelist:
                    n += 1
                    consec += 1
                else:
                    global consecutive
                    if consec > consecutive:
                        consecutive = consec
                        global coef
                        coef = anum * bnum
                        global pair
                        pair = [anum, bnum]
                    cond = False
            bar.update(bar_ticker)
            bar_ticker += 1

    print " "
    print "Consecutive prime outcomes: ", consecutive
    print "Coefficient: ", coef
    print "Pair: ", pair


A = list(range(-999, 1000))
B = list(range(-1000, 1001))
plist = primes_sieve(10000)

evaluate_pair(A, B, plist)
# SOLVED
