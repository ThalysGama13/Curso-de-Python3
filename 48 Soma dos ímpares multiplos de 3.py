s = 0
cont = 0
for c in range(1,501,2):
    if c%3==0:
        s = s+c # acumulador. Soma, multiplica,... aculuma de alguma forma os valores do intervalo
        cont = cont+1 # contador. Conta quantos valores tem no intervalo
print('A soma dos {} valores é {}'.format(cont, s))
