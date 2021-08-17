def ficha(nome,gols):
    print(f'O jogador {nome} fez {gols} gols')


#programa pcp
n = str(input('Digite o nome do jogador: '))
g = str(input('Número de gols: ')) #para não dar erro caso o usuário escreva o número por extenso
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() =='':
    ficha(gol=g)
else:
    ficha(n,g)
