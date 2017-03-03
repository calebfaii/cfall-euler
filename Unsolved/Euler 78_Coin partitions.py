# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five
# coins can be separated into piles in exactly seven different ways, so p(5)=7.
#
#      OOOOO
#    OOOO   O
#     OO   OO
#   OOO   O   O
#   OO   OO   O
#  OO   O   O   O
# O   O   O   O   O
#
# Find the least value of n for which p(n) is divisible by one million.

def rule_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]


def gen_parts():

    x = 1
    parts = len(list(rule_asc(x)))

    while x > 0:
        if x % 1000000 == 0:
            print x * 1000000
        if parts < 1000000:
            x += 1
        if parts > 1000000:
            if parts % 1000000 == 0:
                return x
            else:
                x += 1

print len(list(rule_asc(55374)))
