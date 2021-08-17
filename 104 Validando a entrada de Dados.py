def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if num.isnumeric():
            valor = int(n)
            ok = True
            return valor
            print('Esse vale')
        else:
            print('Erro! Isso não é um número')
        if ok:
            break
    

leiaInt('Digite um número: ')

