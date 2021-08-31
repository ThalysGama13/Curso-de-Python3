número = int(input('Digite um número: '))
print('''Escolha uma das opções para converter:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opção = int(input('Sua opção: '))
if opção==1:
    print('A conversão de {} para binário é {}'.format(número, bin(número)[2:])) # o colchete serve p tirar o 0b, 0o e 0x da conversão
elif opção==2:
    print('A conversão de {} para Octal é {}'.format(número, oct(número)[2:]))
elif opção==3:
    print('A conversão de {} para Hexadecimal é {}'.format(número, hex(número)[2:]))
else:
    print('\033[31m Tem essa opção não, mano\033[m')
