# The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3)
# and 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly three
# permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

start = 346


def get_cube_int(num):
    return num**3


def get_cube_sorted_str(num):
    return int("".join(sorted(str(num))))


cubes = []
sorted_digit_cubes = []

for number in range(start, 10000):
    cube = get_cube_int(number)
    cubes.append(cube)
    sorted_cube = get_cube_sorted_str(cube)
    sorted_digit_cubes.append(sorted_cube)

sorted_cubes = sorted(sorted_digit_cubes)
candidates = set()
for value in sorted_cubes:
    count = sorted_cubes.count(value)
    if count == 5:
        solutions = set()
        for string in sorted_cubes:
            if string == value:
                solutions.add(sorted_cubes.index(string))
        candidates.add(cubes[min(solutions)])
candidates = list(candidates)
candidates.sort(reverse=True)
print "Solution: %d" % candidates[0]
print "Cube: %d**3" % candidates[0]**(1./3.)

# Solved, but barely.  This is not my best work.  Oh well.
