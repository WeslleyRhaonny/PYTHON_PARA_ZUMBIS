sal = float (input('quanto você ganha por hora trabalhada? '))
tempo = int (input('quantas horas você trabalha por mes? '))
bruto = sal * tempo
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liq = bruto - ir - inss - sind
print (f'Salário Bruto: R$ {bruto:.2f} \nImposto de renda: R$ {ir:.2f} \nINSS: R$ {inss:.2f} \nSindicato: R$ {sind:.2f} \nSalário Líquido: R$: {liq:.2f}')
