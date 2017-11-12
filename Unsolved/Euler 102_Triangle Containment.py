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

from sympy import Point, Line, Segment

# Let's load the data before we get started...

def load_values():

    listOfTriangles = []
    with open('p102_triangles.txt', 'r') as text_file:
        for line in text_file:
            split = line.split(',')
            listOfTriangles.append([int(i) for i in split])
    return listOfTriangles

# First,represent each point.

def get_points(t_list):

    points = []
    for num in range(0, 6, 2):
        point = Point(t_list[num], t_list[num + 1])
        points.append(point)
    return points

# Then, plot lines AB, AC and BC.

def get_lines(p_list):

    A, B, C = p_list[0], p_list[1], p_list[2]
    AB = Line(A, B)
    AC = Line(A, C)
    BC = Line(B, C)

    return [AB, AC, BC]

# Find the x and y intercept of each line.

def get_intercepts(L_list):

    min = -1000
    max = 1000

    xMin = Point(min, 0)
    xMax = Point(max, 0)
    yMin = Point(0, min)
    yMax = Point(0, max)

    x_axis = Line(xMin, xMax)
    y_axis = Line(yMin, yMax)
    print x_axis

    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0

    # Find the min and max x and y intercept.

    for line in L_list:

        x = x_axis.intersection(line)
        y = y_axis.intersection(line)

        if x[0].x < xmin:
            xmin = x[0].x
        if x[0].x > xmax:
            xmax = x[0].x
        if y[0].y < ymin:
            ymin = y[0].y
        if y[0] > ymax:
            ymax = y[0].y

    return [xmin, xmax, ymin, ymax]

# If xMin < 0 < xMax and yMin < 0 < yMax, return True; else, return False

def evaluate(x_y_vals):

    xmin, xmax, ymin, ymax = x_y_vals[0], x_y_vals[1], x_y_vals[2], x_y_vals[3]
    if xmin < 0 < xmax and ymin < 0 < ymax:
        return True
    else:
        return False

def solve():

    triangles = load_values()
    matches = 0

    for triangle in triangles:
        point = get_points(triangle)
        lines = get_lines(point)
        intercepts = get_intercepts(lines)
        if evaluate(intercepts):
            matches += 1
    return "Solution: %d" % matches


print solve()

