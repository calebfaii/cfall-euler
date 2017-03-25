# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time


def generatefactors():

    factors = list(range(100, 1000))
    products = []
    for num in factors:
        for num2 in factors:
            products.append(num * num2)
    products.sort(reverse=True)
    return products


def checkpalindrome(list_of_products):
    counter = 0
    while counter < len(list_of_products):
        number1 = str(list_of_products[counter])
        number = list(number1)
        if len(number) == 6:
            if number[0] == number[5] and number[1] == number[4] and number[2] == number[3]:
                print "Solution: ", int(number1)
                break
            else:
                counter += 1
        else:
            print "End of six-digit numbers."
            break


def solve():
    start = time.time()
    checkpalindrome(generatefactors())
    elapsed = (time.time() - start)
    print "Run time: ", elapsed, "seconds."

solve()
# SOLVED
