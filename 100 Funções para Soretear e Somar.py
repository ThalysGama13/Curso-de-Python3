from random import randint
def sorteia(num):
    print('Sorteando valores')
    for c in range(0,5):
        n = randint(0,30)
        num.append(n)


def somapar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            print(f'Os números pares digitados são {n}')
            soma += n
    print(f'A soma desses números é {soma}')


números = list()
sorteia(números)
print(números)

somapar(números)