# Oregon licence plates consist of three letters followed by a three digit
# number (each digit can be from [0..9]).
# While driving to work Seth plays the following game:
# Whenever the numbers of two licence plates seen on his trip add to 1000
# that's a win.
#
# E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500 too. (as long as
# he sees them in the same trip).
#
# Find the expected number of plates he needs to see for a win.
# Give your answer rounded to 8 decimal places behind the decimal point.
#
# Note: We assume that each licence plate seen is equally likely to have any
# three digit number on it.


# Maximum number of license plates: (26 ** 3) * 1000 = 17576000
# Matches to a given plate: 26 ** 3 = 17576

# Odds of seeing a given plate = 1/17576000
# Odds that plate ends in 000 = 17576/17576000
# Odds that plate does NOT end in 000 = 17558424/17576000
# Odds of seeing a plate with a complementary value: 17576/17576000

import progressbar
import random
import itertools


def monte_carlo(trials):

    print "Generating sample space for trials..."

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_permutations = [''.join(i) for i in itertools.product(letters, repeat=3)]
    numbers = "0123456789"
    number_permutations = [''.join(i)for i in itertools.product(numbers, repeat=3)]
    license_plates = [i for i in itertools.product(letter_permutations, number_permutations)]
    outcomes = []
    print "Sample space generated."

    bar = progressbar.ProgressBar(max_value=trials)

    for trial in range(1, trials + 1):

        plates_seen = []
        matches = 0
        number_of_plates = 0

        while matches < 1:

            plate = random.choice(license_plates)
            number_of_plates += 1
            number_value = int(plate[1])

            if len(plates_seen) > 1:
                if any(plate + number_value == 1000 for plate in plates_seen):
                    outcomes.append(number_of_plates)
                    matches += 1
                    plates_seen.append(number_value)

            if len(plates_seen) == 0:
                plates_seen.append(number_value)
                continue

            plates_seen.append(number_value)
        bar.update(trial)
    print " "
    print "%d trials completed successfully." % trials
    print "Smallest matching plate value incidence:", min(outcomes)
    print "Largest matching plate value incidence:", max(outcomes)
    print "Expected value:", float(sum(outcomes)) / float (len(outcomes))


def monte_carlo_2(trials):

    print "Generating sample space for trials..."

    numbers = "0123456789"
    number_permutations = [''.join(i)for i in itertools.product(numbers, repeat=3)]
    license_plates = list(number_permutations)
    outcomes = []
    print "Sample space generated."

    bar = progressbar.ProgressBar(max_value=trials)

    for trial in range(1, trials + 1):

        plates_seen = []
        matches = 0
        number_of_plates = 0

        while matches < 1:

            plate = random.choice(license_plates)
            number_of_plates += 1
            number_value = int(plate)

            if len(plates_seen) > 1:
                if any(plate + number_value == 1000 for plate in plates_seen):
                    outcomes.append(number_of_plates)
                    matches += 1
                    plates_seen.append(number_value)

            if len(plates_seen) == 0:
                plates_seen.append(number_value)
                continue

            plates_seen.append(number_value)
        bar.update(trial)
    print " "
    print " "
    print "%d trials completed successfully." % trials
    print "Smallest matching plate value incidence:", min(outcomes)
    print "Largest matching plate value incidence:", max(outcomes)
    print "Expected value:", float(sum(outcomes)) / float (len(outcomes))


def old_fashioned_way():

    target = 1


    sample_space = 1000
    without_zeros = 999

    # a_plate = 1
    multiplier = 0

    expected_values = []

    # first_plate = float(a_plate) / float(without_zeros)  # a plate that isn't 000 or 500 / all plates not 000 or 500
    # expected_values.append(first_plate)

    while multiplier < 50:

        multiplier += 1
        next_plate = (float(multiplier) / float(without_zeros))  # multiplier * plates  / all plates not 000 or 500
        expected_values.append(next_plate)
        print "Plates seen:", multiplier + 1
        print "EV through here:", sum(expected_values)


    print expected_values
    return multiplier

print old_fashioned_way()










