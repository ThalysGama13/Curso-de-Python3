preço = float(input('Qual é o preço do produto? '))
print('''Escolha a forma de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('Desconto de 10% você vai pagar apenas R$ {}'.format(preço-0.1*preço))
elif opção == 2:
    print('Desconto de 5% você vai pagar apenas R$ {}'.format(preço-0.05*preço))
elif opção == 3:
    print('São duas parcelas de R$ {} '.format(preço/2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('São {} parcelas de R$ {}'.format(parcelas, (preço/parcelas)+0.2*preço))
