# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely
# of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such
# numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed
# in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion?

import progressbar


def all_digits_are_odd(number_str):

    digits = [i for i in number_str]
    odds = {'1', '3', '5', '7', '9'}
    for digit in digits:
        if digit in odds:
            continue
        else:
            return False
    return True


def has_no_trailing_zeroes(number):
    if number % 10 == 0:
        return False
    return True


def starts_and_ends_with_odd_digit(number_str):
    odds = {'1', '3', '5', '7', '9'}
    first_digit = number_str[0]
    last_digit = number_str[-1]
    if first_digit in odds and last_digit in odds:
        return True
    return False


def starts_and_ends_with_even_digit(number_str):
    evens = {'2', '4', '6', '8'}
    first_digit = number_str[0]
    last_digit = number_str[-1]
    if first_digit in evens and last_digit in evens:
        return True
    return False


def reversed_number(number_str):
    reversed_num = number_str[::-1]
    return int(reversed_num)


def check_for_reversibility(number):
    if has_no_trailing_zeroes(number):
        number_str = str(number)
        if not starts_and_ends_with_odd_digit(number_str):
            if not starts_and_ends_with_even_digit(number_str):
                summed_str = str(number + reversed_number(number_str))
                if all_digits_are_odd(summed_str):
                    return True
    return False


def check_range(maximum):
    reversible_number_count = 0
    bar = progressbar.ProgressBar(max_value=maximum)
    for num in xrange(1, maximum):
        if check_for_reversibility(num):
            reversible_number_count += 1
        bar.update(num)
    return reversible_number_count


print check_range(1000000000)
# SOLVED! 608,720
