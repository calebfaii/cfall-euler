

import time

start = time.time()
line1 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
line2 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
line3 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
line4 = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
line5 = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
line6 = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
line7 = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
line8 = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
line9 = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
line10 = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
line11 = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
line12 = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
line13 = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
line14 = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
line15 = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
line16 = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
line17 = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
line18 = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
line19 = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
line20 = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

line_1 = []
line_2 = []
line_3 = []
line_4 = []
line_5 = []
line_6 = []
line_7 = []
line_8 = []
line_9 = []
line_10 = []
line_11 = []
line_12 = []
line_13 = []
line_14 = []
line_15 = []
line_16 = []
line_17 = []
line_18 = []
line_19 = []
line_20 = []

array = []


def populate_list(stringname, listname):

    num = 0
    start = 0
    stop = 2
    while num < 20:
        int_num = int(stringname[start:stop])
        listname.append(int_num)
        num += 1
        start += 3
        stop += 3
    array.append(listname)

populate_list(line1, line_1)
populate_list(line2, line_2)
populate_list(line3, line_3)
populate_list(line4, line_4)
populate_list(line5, line_5)
populate_list(line6, line_6)
populate_list(line7, line_7)
populate_list(line8, line_8)
populate_list(line9, line_9)
populate_list(line10, line_10)
populate_list(line11, line_11)
populate_list(line12, line_12)
populate_list(line13, line_13)
populate_list(line14, line_14)
populate_list(line15, line_15)
populate_list(line16, line_16)
populate_list(line17, line_17)
populate_list(line18, line_18)
populate_list(line19, line_19)
populate_list(line20, line_20)

products = []
solutions = []


def horizontal_products(Array):
    listcount = 0
    index = 0
    while listcount < 20:
        while index < 17:
            horizontal = ((Array[listcount][index])
                            * (Array[listcount][index + 1])
                            * (Array[listcount][index + 2])
                            * (Array[listcount][index + 3]))
            products.append(horizontal)
            answer = ("H",listcount,index)
            solutions.append(answer)
            index += 1
        index = 0
        listcount += 1


def vertical_products(Array):
    listcount = 0
    listcount2 = (listcount + 1)
    listcount3 = (listcount + 2)
    listcount4 = (listcount + 3)
    index = 0
    while listcount < 17:
        while index < 20:
            vertical = ((Array[listcount][index])
                        * (Array[listcount2][index])
                        * (Array[listcount3][index])
                        * (Array[listcount4][index]))
            products.append(vertical)
            answer = ("V", listcount, index)
            solutions.append(answer)
            index += 1
        index = 0
        listcount += 1
        listcount2 += 1
        listcount3 +=1
        listcount4 += 1


def diagonal_products_forward(Array):
    listcount = 0
    listcount2 = (listcount + 1)
    listcount3 = (listcount + 2)
    listcount4 = (listcount + 3)
    index = 0
    while listcount < 17:
        while index < 17:
            diagonal = ((Array[listcount][index])
                        * (Array[listcount2][index+1])
                        * (Array[listcount3][index+2])
                        * (Array[listcount4][index+3]))
            products.append(diagonal)
            answer = ("F", listcount, index)
            solutions.append(answer)
            index += 1
        index = 0
        listcount += 1
        listcount2 += 1
        listcount3 +=1
        listcount4 += 1


def diagonal_products_backward(Array):
    listcount = 0
    listcount2 = (listcount + 1)
    listcount3 = (listcount + 2)
    listcount4 = (listcount + 3)
    index = 3
    while listcount < 17:
        while index < 20:
            diagonal = ((Array[listcount][index])
                        * (Array[listcount2][index - 1])
                        * (Array[listcount3][index - 2])
                        * (Array[listcount4][index - 3]))
            products.append(diagonal)
            answer = ("B", listcount, index)
            solutions.append(answer)
            index += 1
        index = 3
        listcount += 1
        listcount2 += 1
        listcount3 += 1
        listcount4 += 1

horizontal_products(array)
vertical_products(array)
diagonal_products_forward(array)
diagonal_products_backward(array)
answerindex = (products.index(max(products)))
elapsed = (time.time() - start)
print "The maximum product of four adjacent numbers is: ", max(products)
print "_______________________________________________________________"
listnum = solutions[answerindex][1]
indexnum = solutions[answerindex][2]
print "Orientation: ", solutions[answerindex][0]
print "List Number: ", solutions[answerindex][1]
print "Index Position: ", solutions[answerindex][2]
print "First Value: ", array[listnum][indexnum]
print "Program ran in", elapsed, "seconds"

# HOLY FUCK THIS IS SOME MESSY SHIT.  WRITTEN IN DEC 12 BEFORE I
# KNEW WHAT THE FUCK I WAS DOING.  WORKS, THOUGH.

