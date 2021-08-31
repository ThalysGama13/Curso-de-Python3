from random import randint
from operator import itemgetter
from typing import List
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('-='*20)
for k,v in jogo.items():
    print(f'O {k} tirou o valor {v}')
ranking = sorted(jogo.items(), key=itemgetter(1)) #o itemgetter da parte 1 coloca em ordem o valor tirado no dado
print('-='*20)
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
