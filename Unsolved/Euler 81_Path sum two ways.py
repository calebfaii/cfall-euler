# In the 5 by 5 matrix below, the minimal path sum from the
# top left to the bottom right, by only moving to the right
# and down, is indicated in bold red and is equal to 2427.
#
# Find the minimal path sum, in matrix.txt (right click and
# "Save Link/Target As..."), a 31K text file containing a 80
# by 80 matrix, from the top left to the bottom right by only
# moving right and down.

import itertools

def import_matrix():

    array = []
    array_text = open("p081_matrix.txt")
    for row in array_text.read().splitlines():
        row_list = []
        for value in row.split(','):
            row_list.append(int(value))
        array.append(row_list)
    return array


def solve():

    matrix = import_matrix()

    zero = 0
    one = 1
    paths = [1, 0]

    print len(list(itertools.permutations(paths, r=158)))

# NOT SOLVED










