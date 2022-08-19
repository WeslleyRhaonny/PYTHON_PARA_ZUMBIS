kg = int(input('digite quantos kg de peixe você pescou: '))
if kg > 50:
    excedente = kg-50
    multa = (kg-50)*4
    print ('excedente = ',excedente)
    print ('multa = ',multa)
else:
    print ('excedente = zero')
    print ('multa = zero')
