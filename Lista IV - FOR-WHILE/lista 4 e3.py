import random
x = random.sample (range(1,100),10)
print (x)
y = random.sample (range(1,100),10)
print (y)
z = []
k = 0
n = 0
while k < 10:
    z.append (x[n])
    z.append (y[n])
    k = k + 1
    n = n + 1
print (z)
