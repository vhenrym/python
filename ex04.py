a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
opcao = int(input('Esclha uma das opções acima: '))

if opcao == 1:
    print(f'Resultado da soma é {a + b}')
elif opcao == 2:
    print(f'Resultado da subtração é {a - b}')
elif opcao == 3:
    print(f'Resultado da multiplicação é {a * b}')
elif opcao == 4:
    print(f'Resultado da divisão é {a / b}')
else:
    print('Opção inválida')