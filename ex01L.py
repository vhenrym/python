nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
nota3 = float(input('Digite a nota da terceira prova: '))

media = (nota1 + nota2 + nota3) / 3
if media >= 6:
        print(f'Aprovado, sua média foi de {media}')
else:
        print(f'Reprovado, sua média foi de {media}')