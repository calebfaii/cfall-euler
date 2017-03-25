# Using p022_names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into
# alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?

def import_names():

    print "Importing Names..."
    names_list = []
    names_text = open("p022_names.txt")
    lines = names_text.read().split(',')
    for word in lines:
        names_list.append(word.strip('"').strip("'"))
    names_list.sort()
    print "Names imported successfully."
    return names_list


names = import_names()
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

print "Solution: ", products,
# SOLVED
