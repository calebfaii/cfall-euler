# The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1);
# so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position
# and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
# two-thousand common English words, how many are triangle words?


def import_names():

    print "Importing words..."
    words_list = []
    words_text = open("p042_words.txt")
    lines = words_text.read().split(',')
    for word in lines:
        words_list.append(word.strip('"').strip("'"))
    print "%d words imported successfully." % len(words_list)
    print " "
    return words_list


def word_to_triangle(words_list):

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    scores = []
    for word in words_list:
        split_word = [char for char in word]
        word_score = [letters.index(char) + 1 for char in split_word]
        scores.append(sum(word_score))
    return scores


def solve():

    solution = 0
    scores = word_to_triangle(import_names())
    triangle_numbers = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,
                        66, 78, 91, 105, 120, 136, 153, 171, 190]
    for score in scores:
        if score in triangle_numbers:
            solution += 1
    return "There are %d triangle words in this list." % solution


print solve()
# SOLVED
