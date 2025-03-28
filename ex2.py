media = float(input('Digite a média: '))
falta = int(input('Quantidade de faltas: '))

if media >= 6:
    if falta <= 20:
        print('Aprovado')
    else:
        print('Reprovado por faltas')
else:
        print('Reprovado por media')