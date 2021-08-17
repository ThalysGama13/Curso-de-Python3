grupo = list()
mulheres = list()
velhos = list()
soma = média = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Digite seu nome: '))
    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo [M/F]: '))
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa)
    grupo.append(pessoa)
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(' ')
print(grupo)
print(' ')
print(f'A) Foram cadastradas {len(grupo)} pessoas')
print(' ')
for i,v in enumerate(grupo):
    for k,v in pessoa.items():
        print(f'O campo {k} recebe o valor {v}')
print(' ')
média = soma/len(grupo)
print(f'B) A média de idade das pessoas cadastradas é {média}')
print(f'C) As mulheres cadastradas são {mulheres}')
for p in grupo:
    if p['idade'] > média:
        velhos.append(pessoa)
        for i,v in enumerate(velhos):
            print(f'D) As pessoas com {i} acima da média são: {v}')
