numero1 = float(input('Digite o valor do lado 1: '))
numero2 = float(input('Digite o valor do lado 2: '))
numero3 = float(input('Digite o valor do lado 3: '))

if numero1 == numero2 == numero3:
        print(f'O triângulo é equilátero')
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        print(f'O triângulo é isóceles')
else:
        print(f'O triângulo é escaleno')