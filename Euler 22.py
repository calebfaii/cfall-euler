import time
start = time.time()
names = []
names_list = open("p022_names.txt")
lines = names_list.read().split(',')
for name in lines:
    names.append(name.strip('"').strip("'"))
names.sort()

scores = []
for name in names:
    score = names.index(name) + 1
    scores.append(score)


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphas = []
for name in names:
    thisname = []
    this_name = list(name)
    for char in this_name:
        charscore = int((letters.index(char)) + 1)
        thisname.append(charscore)
    alpha = sum(thisname)
    alphas.append(alpha)

products = 0
for i in range(0, len(scores)):
    product = scores[i] * alphas[i]
    products += product
elapsed = (time.time() - start)
print "The answer is", products, "found in", elapsed, "seconds."


