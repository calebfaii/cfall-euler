# By replacing the 1st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
# 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily
# adjacent digits) with the same digit, is part of an eight prime value family.

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


def is_prime(n):


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

print primes_sieve(10)