# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and
# product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as
# a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import itertools


def break_int(n):

    return list(int(i) for i in str(n))


digits = list(range(1, 10))

two_dig = itertools.permutations(digits, r=4)
two_three_dig = itertools.permutations(digits, r=5)
one_four_dig = itertools.permutations(digits, r=5)
solutions = []

print "2-digit times 2-digit:"
for perm in two_dig:
    product = int("".join(map(str, perm[:2]))) * int("".join(map(str, perm[2:])))
    chars = list(perm) + break_int(product)
    if len(chars) == 9:
        chars.sort()
        if digits == chars:
            print perm, product
            if product not in solutions:
                solutions.append(product)

print "2-digit times 3-digit:"
for perm in two_three_dig:
    product = int("".join(map(str, perm[:2]))) * int("".join(map(str, perm[2:])))
    chars = list(perm) + break_int(product)
    if len(chars) == 9:
        chars.sort()
        if digits == chars:
            print perm, product
            if product not in solutions:
                solutions.append(product)


print "3-digit times 2-digit:"
for perm in two_three_dig:
    product = int("".join(map(str, perm[:3]))) * int("".join(map(str, perm[3:])))
    chars = list(perm) + break_int(product)
    if len(chars) == 9:
        chars.sort()
        if digits == chars:
            print perm, product
            if product not in solutions:
                solutions.append(product)

print "1-digit times 4-digit:"
for perm in one_four_dig:
    product = int("".join(map(str, perm[:1]))) * int("".join(map(str, perm[1:])))
    chars = list(perm) + break_int(product)
    if len(chars) == 9:
        chars.sort()
        if digits == chars:
            print perm, product
            if product not in solutions:
                solutions.append(product)

print "4-digit times 1-digit:"
for perm in one_four_dig:
    product = int("".join(map(str, perm[:5]))) * int("".join(map(str, perm[-1])))
    chars = list(perm) + break_int(product)
    if len(chars) == 9:
        chars.sort()
        if digits == chars:
            print perm, product
            if product not in solutions:
                solutions.append(product)

print sum(solutions)
