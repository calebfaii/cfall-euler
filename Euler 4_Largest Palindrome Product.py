# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

factors = []
products = []
start = time.time()


def generatefactors():
    for num in range(100, 1000):
        factors.append(num)
    for num in factors:
        for num2 in factors:
            product = num * num2
            products.append(product)
    products.sort(reverse=True)


def checkpalindrome(list_of_products):
    counter = 0
    while counter < len(products):
        number1 = str(list_of_products[counter])
        number = list(number1)
        if len(number) == 6:
            if number[0] == number[5] and number[1] == number[4] and number[2] == number[3]:
                return number, "is the solution."

            else:
                counter += 1
        else:
            return "End of six-digit numbers."

generatefactors()
print checkpalindrome(products)
elapsed = (time.time() - start)
print "Run time: ", elapsed, "seconds."
