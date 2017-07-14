# For a number written in Roman numerals to be considered valid there are basic rules
# which must be followed. Even though the rules allow some numbers to be expressed in
# more than one way there is always a "best" way of writing a particular number.
#
# For example, it would appear that there are at least six ways of writing the number
# sixteen:
#
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
#
# However, according to the rules only XIIIIII and XVI are valid, and the last example
# is considered to be the most efficient, as it uses the least number of numerals.
#
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one
# thousand numbers written in valid, but not necessarily minimal, Roman numerals; see
# About... Roman Numerals for the definitive rules for this problem.
#
# Find the number of characters saved by writing each of these in their minimal form.
#
# Note: You can assume that all the Roman numerals in the file contain no more than
# four consecutive identical units.

roman_numerals = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}

def import_data():

    array = []
    array_text = open("p089_numerals.txt")
    for row in array_text.read().splitlines():
        for value in row.split(','):
            array.append(value)
    return array


def numeral_to_int(roman):

    value = 0
    temp = 0

    ints = [roman_numerals.get(numeral) for numeral in roman]

    for i in xrange(len(ints) - 1):

        if ints[i] > ints[i + 1]:
            value += ints[i]
            value += temp
            temp -= temp
            print "1"
            continue

        if ints[i] == ints[i + 1]:
            temp += ints[i]
            print "2"
            continue

        if ints[i] < ints[i + 1]:

            temp += ints[i]
            value -= temp
            temp == 0
            print "3"
            continue

    value += ints[-1]

    return value

def value_to_roman(integer):

    val = integer
    sequence = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman = ''

    for numeral in sequence:
        remainder = float(val) / float(roman_numerals.get(numeral))

        if remainder < 0:
            continue

        if remainder > 0:
            continue





