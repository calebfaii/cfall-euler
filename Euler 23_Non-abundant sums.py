# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
# sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def generateIntegers(num):

    ints = [1]
    for i in range (2, num + 1):
        ints.append(i)
    return ints


def sumFactors(num):

    factorsum = 0
    halfnum = (num / 2) + 1

    for i in range(1, halfnum):
        if num % i == 0:
            factorsum += i
    return factorsum



def isAbundant(num):

    abundant = []
    for i in range (2, num + 1):
        factor_sum = sumFactors(i)
        if factor_sum > i:
            abundant.append(i)
    return abundant

def abundantSums(abundant_list):

    absums = []
    for i in abundant_list:
        for j in abundant_list:
            print(i, j)
            val = i + j
            if val < 21824:
                if val not in absums:
                    absums.append(val)
    absums.sort()
    return absums

# TODO: OPTIMIZE SO THIS WILL RUN
integers = generateIntegers(21823)
print 1
abundant_nums = isAbundant(21823)
print 2
abundant_sums = abundantSums(abundant_nums)
print 3
print abundant_sums

