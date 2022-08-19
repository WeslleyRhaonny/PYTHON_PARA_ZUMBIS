n = int (input('digite qual número da sequencia de Fibonnaci voce quer saber: '))
a = 1
b = 1
c = 1
while True:
    print (f' f{c} = {a}')
    (a,b)= (b, a+b)
    c = c + 1
    if c == n:
        print (f'o F{n} da sequência de Fibonnaci é {a}')
        break
    
