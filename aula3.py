media = float(input('Digite a média: '))
falta = int(input('Quantidade de faltas: '))

if media >= 6 and faltas <= 20:
    print('Aprovado')
elif media >= 6 and faltas > 20:
    print('Reprovado por falta')
else:
    print('Reprovado por média')