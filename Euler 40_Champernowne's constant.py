import time

def genString(num):

    x = 1
    value = []
    while x < num:
        strx = str(x)
        value.append(strx)
        x += 1
    conc = ''.join(value)
    return conc

start = time.time()

check = genString(1000000)

var1 = int(check[0])
var2 = int(check[9])
var3 = int(check[99])
var4 = int(check[999])
var5 = int(check[9999])
var6 = int(check[99999])
var7 = int(check[999999])

print (var1 * var2 * var3 * var4 * var5 * var6 * var7)
elapsed = (time.time() - start)
print elapsed, "seconds"

