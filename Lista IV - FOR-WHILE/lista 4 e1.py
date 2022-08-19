import random
k = 0
n = 0
par = []
impar = []
x = random.sample (range(1,101),20)
print (f'os numero sorteados foram {x}')
while k < 20:
    if x[n] % 2 == 0:
        par.append (x[n])
    else:
        impar.append (x[n])
    k = k + 1
    n = n + 1
print (f'os números pares são: {par}')
print (f'os números impares são: {impar}')

