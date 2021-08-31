import random
objetos = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)
print('''Escolha:
(0) PEDRA
(1) PAPEL
(2) TESOURA''')
jogador = int(input('Joga o que? '))

print('computador jogou {}'.format(objetos[computador]))
print('Jogador jogou {}'.format(objetos[jogador]))
if computador == 0: # PC joga pedra
    if jogador == 0:
        print('\033[33m EMPATE')
    elif jogador == 1:
        print('\033[34m GANHOU!!')
    elif jogador == 2:
        print('\033[31m PERDEU OTÁRO!')
    else:
        print('Não pode')
elif computador == 1: # PC joga papel
    if jogador == 0:
        print('\033[31m PERDEU OTÁRO')
    elif jogador == 1:
        print('\033[33m EMPATE')
    elif jogador == 2:
        print('\033[34m GANHOU!!')
    else:
        print('Não pode')

elif computador == 2: # PC joga tesoura
    if jogador == 0:
        print('\033[34m GANHOU!!')
    elif jogador == 1:
        print('\033[31m PERDEU')
    elif jogador == 2:
        print('\033[33m EMPATE')
    else:
        print('Não pode')
