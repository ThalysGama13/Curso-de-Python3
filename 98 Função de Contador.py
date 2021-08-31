def contador(i,f,p):
    print(f'Contagem de {i} até {f} de {p} em {p}')


i = int(input('Início da contagem: '))
f = int(input('Fim da contagem: '))
p = int(input('Passo da contagem: '))
contador(i,f,p)

if i>f:
    p = -p
    for c in range(i, f, p):
        print(c)
else:
    p = p
    for c in range(i, f, p):
        print(c)
