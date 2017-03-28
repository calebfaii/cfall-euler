# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import progressbar


def reverse_num(number):

    split_int = list(digit for digit in str(number))
    split_int.reverse()
    return int(''.join(map(str, split_int)))


def solve(maxval):

    double_pals = []
    double_bin = []
    bar = progressbar.ProgressBar(max_value=1000000)

    for num in range(1, maxval):
        bar.update(num)
        if num == reverse_num(num):
            binary = int(bin(num)[2:])
            if binary == reverse_num(binary):
                double_pals.append(num)
                double_bin.append(binary)
    print " "
    print "Double palindromes: ", double_pals
    print "Binary equivalent: ", double_bin
    print "Solution: ", sum(double_pals)


solve(1000000)
# SOLVED
