matriz = [[0,0,0], [0,0,0], [0,0,0]]  #colocar os zeros significa que não preciso usar append
somapar = maior = somacol = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input('Digite um valor: '))
print('='*30)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print() #esse print um identação atrás serve para colocar uma linha embaixo da outra
print('='*30)
print(f'A soma dos valores pares é igual a {somapar}' )
# a coluna tá fixa [2], então tenho que variar a linha e p isso usa o 'for'
for linha in range (0, 3):
    somacol += matriz[linha][2]
print(f'A soma dos valor da terceira coluna vale {somacol}')
# para achar o maior valor da segunda linha usa o mrm raciocínio. a linha tá fixa e a coluna tá variando
for coluna in range (0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é o {maior}')