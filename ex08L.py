numero1 = int(input('Digite primeiro número : '))
numero2 = int(input('Digite o segundo número : '))
numero3 = int(input('Digite o terceiro número : '))


if numero1 < numero2 < numero3:
    print(f'O número {numero1} é menor')
elif numero2 < numero1 < numero3:
    print(f'O número {numero2} é menor')
elif numero3 < numero2 < numero1:
    print(f'O número {numero3} é menor')
elif numero1 == numero2 == numero3:
    print('Os números são iguais')
