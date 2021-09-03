from random import randint
chances = 0
computador = randint(1,10)
print('=-'*20)
print('Vou pensar em um número entre 1 e 10. Adivinhe!')
print('=-'*20)
jogador = 1
while jogador != computador:
    jogador = int(input('Digite o número que o computador pensou: '))
    if jogador != computador:
        chances += 1
        print('\033[31m Errou OTÁRO! Tenta de novo\033[m')
    else:
        print('\033[34m AAHH EHHH !! Acertou!!')
print('=-'*20)
print(' Depois de {} tentativas, mas acertou'.format(chances))
print('FIM')
