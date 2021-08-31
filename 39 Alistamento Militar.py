nascimento = int(input('Em que ano você nasceu? '))
hoje = int(input('Ano atual: '))
idade = hoje - nascimento
if idade<18:
    print('Você ainda vai se alistar')
elif idade==18:
    print('VAI SE ALISTAR, PORRA')
elif idade>18:
    print('Passou da hora, mano')