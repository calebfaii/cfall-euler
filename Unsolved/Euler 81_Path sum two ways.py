# In the 5 by 5 matrix below, the minimal path sum from the
# top left to the bottom right, by only moving to the right
# and down, is indicated in bold red and is equal to 2427.
#
# Find the minimal path sum, in matrix.txt (right click and
# "Save Link/Target As..."), a 31K text file containing a 80
# by 80 matrix, from the top left to the bottom right by only
# moving right and down.

import time

array = []
array_text = open("p081_matrix.txt")
for line in array_text.read().splitlines():
    line_list = []
    for value in line.split(','):
        line_list.append(int(value))
    array.append(line_list)


def backwards_greedy(array):

    squares = []
    row = -1
    column = -1
    squares.append(array[-1][-1])
    while column > -81:
        try:
            print row, column
            current = array[row][column]
            left = array[row][column - 1]
            up = array[row - 1][column]
            if column == -80:
                while row > -81:
                    squares.append(up)
                    row -= 1
                    break
                break
            if left < up:
                squares.append(left)
                column -= 1
            if left > up:
                squares.append(up)
                row -= 1
            if left == up:
                print "Error - Row: ", row, "Col: ", column, "Square: ", current


        except IndexError:
            print "Index Error"
    print squares
    print sum(squares)


backwards_greedy(array)




