n1 = int (input('digite um número inteiro: '))
n2 = int (input('digite outro número inteiro: '))
while (n1 % n2) != 0:
    (n1,n2) = (n2, n1%n2)
    if (n1%n2)==0:
        print (f'MDC = {n2}')
