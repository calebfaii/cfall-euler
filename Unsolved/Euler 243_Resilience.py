# A positive fraction whose numerator is less than its denominator is called a proper fraction.
# For any denominator, d, there will be d-1 proper fractions; for example, with d= 12:
# 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .
#
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be the
# ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
# In fact, d=12 is the smallest denominator having a resilience R(d) < 4/10 .
#
# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .


import fractions

def find_resilience(d):

    resilience = 1
    for n in range(2, d):
        if d % n != 0:
            if fractions.gcd(n, d) == 1:
                resilience += 1
    return fractions.Fraction(resilience, d - 1)

# x = (float(15499) / float(94744))
# print x


def solve():
    candidate = 94744
    benchmark = fractions.Fraction(15499, 94744)
    multiplier = 1
    while True:
        test = candidate * multiplier
        print "Evaluating: ", multiplier, test
        print "Fraction: ", fractions.Fraction(find_resilience(test))
        if fractions.Fraction(find_resilience(test)) < benchmark:
            print candidate
            break
        else:
            multiplier += 1

solve()

