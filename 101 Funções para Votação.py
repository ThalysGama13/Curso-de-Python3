def voto(idade):
    from datetime import date #quando eu importo dentro de uma função a importação só serve para dentro dela
    atual = date.today().year
    idade = atual - n
    if idade < 16:
        return f'Com {idade} anos você não vota'
    if 16 <= idade < 18 or idade > 70:
       return f'Com {idade} anos seu voto é opcional'
    if 18 <= idade < 70:
        return f'Com {idade} anos seu voto é obrigatório'


n = int(input('Em que ano você nasceu? '))
print(voto(n))
