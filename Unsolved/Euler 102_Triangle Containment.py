# Three distinct points are plotted at random on a Cartesian plane, for which
# -1000<= x, y<= 1000, such that a triangle is formed.
#
# Consider the following two triangles:
#
# A(-340,495), B(-153,-910), C(835,-947)
#
# X(-175,41), Y(-421,-714), Z(574,-645)
#
# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
# Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing
# the co-ordinates of one thousand "random" triangles, find the number of triangles for which
# the interior contains the origin.

from sympy import Point, Line
import matplotlib.pyplot as plt

# Let's load the data before we get started...

def load_values():

    list_of_triangles = []
    with open('p102_triangles.txt', 'r') as text_file:
        for line in text_file:
            split = line.split(',')
            list_of_triangles.append([int(i) for i in split])
    return list_of_triangles

# First, let's represent each triangle as a list of three points.

def get_points(triangle):

    list_of_points = []
    for num in range(0, 6, 2):
        point = Point(triangle[num], triangle[num + 1])
        list_of_points.append(point)
    return list_of_points

# Then, plot lines AB, AC and BC.

def get_lines(list_of_points):

    A, B, C = list_of_points[0], list_of_points[1], list_of_points[2]
    AB = Line(A, B)
    AC = Line(A, C)
    BC = Line(B, C)
    list_of_lines = [AB, AC, BC]
    return list_of_lines

# Find the x and y intercept of each line.

def get_intercepts(list_of_lines):

    lower_bound = -1000
    upper_bound = 1000

    minimum_x_value = Point(lower_bound, 0)
    maximum_x_value = Point(upper_bound, 0)
    minimum_y_value = Point(0, lower_bound)
    maximum_y_value = Point(0, upper_bound)

    x_axis = Line(minimum_x_value, maximum_x_value)
    y_axis = Line(minimum_y_value, maximum_y_value)

    # Find the min and max x and y intercept.

    x_values = set()
    y_values = set()

    for line in list_of_lines:

        try:
            x_intercept = x_axis.intersection(line)[0]
            y_intercept = y_axis.intersection(line)[0]
            x_values.add(x_intercept.x)
            y_values.add(y_intercept.y)
        except Exception, e:
            print e
            return [-1, -1, -1, -1]

        xmin = min(x_values)
        xmax = max(x_values)
        ymin = min(y_values)
        ymax = max(y_values)
        values = [xmin, xmax, ymin, ymax]
    return values

def evaluate_intercepts(x_y_vals):

    result = False
    xmin, xmax, ymin, ymax = x_y_vals[0], x_y_vals[1], x_y_vals[2], x_y_vals[3]
    if xmin <= 0:
        if xmax >= 0:
            if ymin <= 0:
                if ymax >= 0:
                    result = True
    return result

def evaluate_points(points):
    result = False
    x_values = set()
    y_values = set()
    for point in points:
        x_values.add(point[0])
        y_values.add(point[1])
    smallest_x = min(x_values)
    largest_x = max(x_values)
    smallest_y = min(y_values)
    largest_y = max(y_values)
    if smallest_x <= 0:
        if largest_x >= 0:
            if smallest_y <= 0:
                if largest_y >= 0:
                    result = True
    return result


def solve():

    triangles = load_values()
    matches = 0

    for triangle in triangles:
        points = get_points(triangle)
        lines = get_lines(points)
        intercepts = get_intercepts(lines)
        plot_points(points)
        if evaluate_intercepts(intercepts):
            if evaluate_points(points):
                matches += 1
                print "TRUE"
    return "Solution: %d" % matches

def plot_points(list_of_points):

    values = [point for point in list_of_points]
    x_values = [point[0] for point in values]
    y_values = [point[1] for point in values]

    plt.xlim(-1000, 1000)
    plt.ylim(-1000, 1000)
    plt.plot(x_values, y_values, 'ro')
    plt.plot(0, 0, 'bo')

    plt.show()

print solve()
# THIS FUCKER IS AWFUL
