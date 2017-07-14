# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def fibo(max_output=4000000):

    fibo_series = [1, 1]
    value = 0
    while value <= max_output:
        value = fibo_series[-2] + fibo_series[-1]
        if value >= max_output:
            return "Solution: %d" % (sum({x for x in fibo_series if x % 2 == 0}))
        fibo_series.append(value)


print fibo()
# SOLVED