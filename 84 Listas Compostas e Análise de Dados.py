galera = list()
dado = list()
maior=menor=0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso; ')))
    if len(galera) == 0:
        maior=menor=dado[1]
    else:
        if dado[1]>maior:
            maior = dado[1]
        if dado[1]<menor:
            menor=dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar?[S/N]: '))
    if resp in 'Nn':
        break
print(galera)
print(f'Foram cadastradas {len(galera)} pessoas')
for p in galera:
    if p[1]==maior:
        print(f'A pessoa mais pesada cadastrada foi a(o) {p[0]}')
    if p[1]==menor:
        print(f'A pessoa mais leve cadastrada foi a(o) {p[0]}')
