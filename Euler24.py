import itertools
import time
start = time.time()
solution = []
sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for permutation in itertools.permutations(sequence, 10):
    solution.append(permutation)
elapsed = (time.time() - start)
print solution[999999], "found in", elapsed, "seconds."



