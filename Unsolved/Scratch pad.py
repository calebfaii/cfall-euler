string = "FixVersion = '5.7 SR10.%s OMS Delegate' OR"

for i in range(0, 14):
    num = str(float(i))
    print string % (num,)

