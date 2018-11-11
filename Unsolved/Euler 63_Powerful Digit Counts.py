# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8**9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?


def evaluate(power):

    value = 0
    start = 2
    n_digit_ints = set()
    while value <= 10**power:
        value = start**power
        if len(str(value)) == power:
            n_digit_ints.add(value)
            print value
        start += 1
    return n_digit_ints

solution = set()
for number in range(2, 25):
    print "\nEvaluating powers of %d..." % number
    result = evaluate(number)
    print "Found %d matching powers.\n" % len(result)
    solution = solution | result

print "\n\n____________________"
print "Solution: %d" % len(solution)
