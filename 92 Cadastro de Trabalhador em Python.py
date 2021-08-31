cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = 2021 - nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (digite 0 se não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro['contratação'] + 40
else:
    print('FIM')
for k, v in cadastro.items():
    print(f'-{k}: {v}')
print('FIM')