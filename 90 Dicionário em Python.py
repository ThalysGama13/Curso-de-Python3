nome = str(input('Digite seu nome: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
média = (n1+n2)/2
if média >= 5:
    situação ='Aprovado!'
else:
    situação = 'Reprovado'
boletim = {'nome':nome, 'média':média, 'situação':situação}
for k, v in boletim.items():
    print(f'{k} é igual a {v}')

