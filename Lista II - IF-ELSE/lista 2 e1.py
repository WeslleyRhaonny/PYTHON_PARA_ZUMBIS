a= int(input('digite o primeiro lado do triangulo: '))
b= int(input('digite o segundo lado do triangulo: '))
c= int(input('digite o terceiro lado do triangulo: '))
if a==b==c:
    print ('o triangulo é equilatero')
if a==b!=c or c==a!=b or c==b!=a:
    print ('o triangulo é isósceles')

if a!=b!=c and c!=a:
    print ('o triangulo é escaleno')
