horas = int(input('Digite um número inteiro: '))
minutos = int(input('Digite um número inteiro: '))

if horas > 23:
    print('O horário é inválido')
elif minutos > 59:
    print('O minuto é válido')
else:
    print(f'A hora é {horas}:{minutos}')

