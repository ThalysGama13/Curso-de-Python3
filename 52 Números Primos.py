n = int(input('Digite um número: '))
total = 0 # Número de divisores
for c in range(1, n+1):
    if n % c == 0:
        print('', end='')
        total = total +1 # ou total+=1
    else:
        print('', end='')
if total == 2: # Um num primo só faz duas divisões (1 e ele mrm)
    print('É primo!')
else:
    print('Não é primo')
