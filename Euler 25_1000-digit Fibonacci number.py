import math

def getFibo(n):

    fibos = [1,1]
    while len(fibos) < n:
        value = fibos[-2] + fibos[- 1]
        fibos.append(value)
    return fibos



print getFibo(100)
