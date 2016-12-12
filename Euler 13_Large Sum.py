# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# Filename: PE13.txt

while True:
    numbers = []

    number_list = open("PE13.txt")
    lines = number_list.read().split()
    for number in lines:
        numbers.append(number)

    x = int(raw_input("How many digits? : "))

    sum_table = []

    for number in numbers:
        index = (49 - x)
        summ = int(number[index + 1: 50])
        sum_table.append(summ)
    guess = sum(sum_table)

    print "Guess: ", guess
    print "========================"
