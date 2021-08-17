from random import *

"""O valor de pi a partir de gotas de chuva caindo num círculo de raio L
inscrito num quadrado de lado 2L. """

raio = 1
lado = 2*raio
'O centro do círculo está em (0,0)'

'A probabilidade da gota de chuva cair no circulo é a razão entre a área do cículo com a área do quadrado'

pingos = 10000000
gotas_no_circulo = 0
for c in range(0,pingos):
    x = uniform(0,1)
    y = uniform(0,1)
    if x**2+y**2<=raio**2:
        gotas_no_circulo +=1

print(f'Cairam {gotas_no_circulo} gotas de chuva no círculo')
print(' ')
pi = 4*gotas_no_circulo/pingos
print(f'O Valor de pi é {pi:.4f}')
