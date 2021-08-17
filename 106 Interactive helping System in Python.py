def ihs(n):
    help(n)
    

def lin(msg):
    tam = len(msg)
    print('~='*tam)
    print(msg)
    print('~='*tam)


ordem = ' '
while True:
    ordem = str(input('Função ou Biblioteca? Digite "fim" para sair: '))
    if ordem == 'fim':
        break
    else:
        ihs(ordem)