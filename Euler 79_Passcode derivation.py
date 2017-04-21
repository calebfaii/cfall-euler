# A common security method used for online banking is to ask the user for three random
# characters from a passcode. For example, if the passcode was 531278, they may ask
# for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file so
# as to determine the shortest possible secret passcode of unknown length.

import progressbar
import time


def break_int(n):

    """Receives an integer; returns a list of the integer's digits."""

    return list(int(i) for i in str(n))


def import_codes():

    """Imports 50 3-digit codes from text file as a list of lists."""

    print "Importing codes..."
    codes_list = []
    codes_text = open("keylog.txt")
    code_values = []
    lines = codes_text.read().splitlines()
    for line in lines:
        line_list = break_int(line)
        codes_list.append(break_int(line))
        for num in line_list:
            if num not in code_values:
                code_values.append(num)
    print "Codes imported successfully."
    print " "
    return [codes_list, code_values]


def solve():

    """For each number in the code, finds the other values which are to the right of that number.
    The right-most value of the passcode will have 0 values to its right.
    The left-most value of the passcode will have the largest number of values to its right."""

    t_input = raw_input("Run tests? Yes / No  ")
    if t_input == 'Yes':
        tests = True
    else:
        tests = False

    d_input = raw_input("Print details? Yes / No  ")
    if d_input == 'Yes':
        details = True
    else:
        details = False
    print " "

    get_codes = import_codes()
    codes_list = get_codes[0]
    code_values = get_codes[1]
    solution = []
    positions = []

    for number in code_values:
        number_position = [number]
        number_seq = []

        for code in codes_list:
            if number in code:
                numindex = code.index(number)

                if numindex == 0:
                    if code[1] not in number_seq:
                        number_seq.append(code[1])
                    if code[2] not in number_seq:
                        number_seq.append(code[2])

                if numindex == 1:
                    if code[2] not in number_seq:
                        number_seq.append(code[2])

        number_position.append(number_seq)
        positions.append(number_position)

    if details:
        for elem in positions:
            print "%d has %d descendant values: %s" % (elem[0], len(elem[1]), elem[1])
            time.sleep(1)
        print " "

    counter = (len(code_values) - 1)
    while counter > -1:
        for number in positions:

            if len(number[1]) == counter:
                solution.append(str(number[0]))
                counter -= 1
                if details:
                    print "Adding %d to solution. Numbers remaining: %s" % (number[0], number[1])
                    time.sleep(1)

    print " "
    print "The solution is %s." % (''.join(solution))

    if tests:
        failures = []
        print "Running test..."
        bar = progressbar.ProgressBar(max_value=50)
        counter = 0
        passes = 0
        for code in codes_list:
            index1 = int(solution.index(str(code[0])))
            index2 = int(solution.index(str(code[1])))
            index3 = int(solution.index(str(code[2])))
            if index1 < index2 < index3:
                counter += 1
                passes += 1
                bar.update(counter)
                continue
            else:
                failures.append(code)
                counter += 1
                bar.update(counter)
                continue
        time.sleep(.5)
        print " "
        print "This passcode is true in %d/50 codes." % passes
        if len(failures) > 0:
            print "The following codes do not pass with this password:"
            for failed_case in failures:
                print failed_case
        else:
            print "This solution is verified."


solve()
# SOLVED
