m2 = float (input('quantos m2 você deseja pintar? '))
lata = 18 * 3
qt = m2 / lata
if int(qt)== qt:
    qtreal = qt
else:
    qtreal = int(qt) + 1
preço = qtreal * 80
print (f'Você irá precisar de {qtreal} latas que custarão R$ {preço:.2f}')
