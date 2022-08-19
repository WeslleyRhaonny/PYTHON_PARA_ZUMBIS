a = 80000
b = 200000
n = 0
while True:
    if a <= b:
        a = a + (a * 0.03)
        b = b + (b * 0.015)
        n = n + 1
    else:
        print (f' será necessário {n} anos para que a população do país A seja maior que a do País B')
        break
