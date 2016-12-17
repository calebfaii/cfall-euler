##Using p022_names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
##Then working out the alphabetical value for each name, multiply this value by its alphabetical 
##position in the list to obtain a name score.
##For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
##is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
##What is the total of all the name scores in the file?

# Test

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


