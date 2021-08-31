matriz = [[0,0,0], [0,0,0], [0,0,0]]  #colocar os zeros significa que não preciso usar append
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input('Digite um valor: '))
print('='*30)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

