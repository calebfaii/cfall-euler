# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#     192 x 1 = 192
#     192 x 2 = 384
#     192 x 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving
# the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
# product of an integer with (1,2, ... , n) where n > 1?


def get_product(n):

    multiplier = 1
    product = str(n)

    while len(product) < 9:
        multiplier += 1
        product += str(multiplier * n)

    if len(product) == 9:
        prod_list = [int(char) for char in product]

        if all(num in prod_list for num in range(1, 10)):
            return int(product)
        else:
            return None


def solve():

    candidates = 0
    integer = 0

    for num in range(1, 9999):
        prod = get_product(num)
        if prod:
            if prod > candidates:
                candidates = prod
                integer = num
    print "The solution is", candidates, ", which is a product of", integer


solve()
