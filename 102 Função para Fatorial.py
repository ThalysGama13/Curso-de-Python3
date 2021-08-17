def fatorial(n, r='Nn'):
    """
    -> Calcula o fatorial de um número
    n -> é o valor a ser calculado
    Show -> É opcional. Mostra a conta que foi feita
    """
    f=1
    r = ' '
    for c in range(n,0,-1):
        if r in 'Ss':
            print(c)
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*=c
    return f


num = int(input('Digite um número: ')
resp = str(input('Quer ver a conta? [S/N]: '))
fatorial(num,resp)