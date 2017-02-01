import time

start = time.time()

value = str(2**1000)
init = 0
for num in value:
    init += int(num)

print init
elapsed = (time.time() - start)
print "Found in", elapsed, "seconds"
