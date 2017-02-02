import math

def getFibo():

    fibos = [1,1]
    while True:
        value = fibos[-2] + fibos[- 1]
        fibos.append(value)
        digits = int(math.log10(value)) + 1
        if digits >= 1000:
            return len(fibos)


print getFibo()