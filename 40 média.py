p1 = float(input('nota da p1: '))
p2 = float(input('nota da p2: '))
média = (p1+p2)/2
if média<5:
    print('\033[31m REPROVADO\033[m')
elif média>5 and média<7:
    print('Tá de PF')
elif média>=7:
    print('\033[34m APROVADO\033[m')
