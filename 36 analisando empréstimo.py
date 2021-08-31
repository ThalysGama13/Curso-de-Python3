casa = float(input('Qual é o valor da casa?'))
salário = float(input('Quanto você ganha?'))
tempo = int(input('Vai pagar em quantos anos?'))
prestação = casa/(tempo*12)
if prestação > 0.3*salário:
    print('\033[31m O empréstimo foi negado\033[m')
else:
    print('\033[34m Emprestimo aprovado!\033[m')
