# The following iterative sequence is defined for the set of positive integers:
# n - n/2 (n is even)
# n - 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?


def collatz(n):
    table = []
    while n > 1:
        table.append(n)
        if n % 2 == 0:
            n = (n/2)
        else:
            n = (3 * n) + 1
        if n == 1:
            table.append(n)
    return len(table)


def return_best(n):
    upper = n - 1
    best_val = 0
    best_num = 0
    for i in range(2, upper):
        print "Evaluating: ", i
        i_length = collatz(i)
        if i_length > best_val:
            best_val = i_length
            best_num = i
    print "Best Length: ", best_val
    print "Start: ", best_num

return_best(1000000)
