import time

amicablenumbers = []
start = time.time()

def sumofdivisors(number):
    if number > 1:
        table = []
        if number % 2 == 0:
            numhalf = (int(number * 0.5) + 1)
            for i in range (1, numhalf):
                if number % i == 0:
                    table.append(i)
            return sum(table)
        else:
            numhalf = int((number * 0.5) + 0.5)
            for i in range (1, numhalf):
                if number % i == 0:
                    table.append(i)
            return sum(table)
    if number <= 1:
        return 0


def findAmicable():
    for num in range(3,10001):
        num_sum = int(sumofdivisors(num))
        sum_num = int(sumofdivisors(num_sum))
        if num == sum_num:
            if num_sum != sum_num:
                amicablenumbers.append(num)


findAmicable()
elapsed = (time.time() - start)
print "The soluton is", sum(amicablenumbers), "found in", elapsed, "seconds."
