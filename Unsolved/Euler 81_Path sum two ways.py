# In the 5 by 5 matrix below, the minimal path sum from the
# top left to the bottom right, by only moving to the right
# and down, is indicated in bold red and is equal to 2427.
#
# Find the minimal path sum, in matrix.txt (right click and
# "Save Link/Target As..."), a 31K text file containing a 80
# by 80 matrix, from the top left to the bottom right by only
# moving right and down.


def import_matrix():

    array = []
    array_text = open("p081_matrix.txt")
    for row in array_text.read().splitlines():
        row_list = [int(value) for value in row.split(',')]
        array.append(row_list)
    return array


class Cursor(object):

    """
    Base class for a Cursor object, which points to a given
    cell in the matrix.
    """

    matrix = None
    path_values = []
    cell_row = None
    cell_column = None
    cell_value = None
    above_value = None
    left_value = None
    next_move = None
    verbose = None

    def __init__(self, matrix=import_matrix(), verbose=False):

        self.matrix = matrix
        self.verbose = verbose
        dimension = len(matrix) - 1
        self.cell_row = dimension
        self.cell_column = dimension
        self.set_cell_value()
        self.add_value_to_path()

    def set_cell_value(self):

        self.cell_value = self.matrix[self.cell_row][self.cell_column]
        if self.verbose:
            print "Set cell value to %d." % self.cell_value

    def set_above_value(self):

        if self.cell_row == 0:
            self.above_value = None
            return
        self.above_value = self.matrix[self.cell_row - 1][self.cell_column]
        if self.verbose:
            print "Set above cell value to %d." % self.above_value

    def set_left_value(self):

        if self.cell_column == 0:
            self.left_value = None
            return
        self.left_value = self.matrix[self.cell_row][self.cell_column - 1]
        if self.verbose:
            print "Set left cell value to %d." % self.left_value

    def add_value_to_path(self):

        self.path_values.append(self.cell_value)
        if self.verbose:
            print "Added %d to path." % self.cell_value

    def compare_left_and_above(self):

        if self.verbose:
            print "Current row: %d" % self.cell_row
            print "Current column: %d" % self.cell_column

        if not self.left_value:
            self.next_move = 'UP'
            if self.verbose:
                print "Reached left-most row."
                print "Setting next move to UP."
            return

        if not self.above_value:
            self.next_move = 'LEFT'
            if self.verbose:
                print "Reached top-most row."
                print "Setting next move to left."
            return

        if self.above_value > self.left_value:
            self.next_move = 'LEFT'
            if self.verbose:
                print "Left is smaller; moving left."
            return

        if self.left_value > self.above_value:
            self.next_move = 'UP'
            if self.verbose:
                print "Up is smaller; moving up."
            return

        if self.above_value == self.left_value:
            raise NotImplementedError

    def move_cursor(self):

        if self.next_move == 'UP':
            self.move_up()
        if self.next_move == 'LEFT':
            self.move_left()

    def move_up(self):

        self.cell_row -= 1

    def move_left(self):

        self.cell_column -= 1

    def move_one_step(self):

        self.set_left_value()
        self.set_above_value()
        self.compare_left_and_above()
        self.move_cursor()
        self.set_cell_value()
        self.add_value_to_path()
        print "\n======="

    def solve(self):

        while len(self.path_values) < 159:
            self.move_one_step()
        print "Solution: %d" % sum(cursor.path_values)

cursor = Cursor(verbose=True)
cursor.solve()
