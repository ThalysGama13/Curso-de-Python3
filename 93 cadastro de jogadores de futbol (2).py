ficha = dict()
ficha['jogador'] = str(input('Digite seu nome: '))
gols = list()
n = int(input('N° de partidas jogadas: '))
tot = 0
for c in range(0, n):
    gols.append(int(input(f'Gols marcados na {c + 1}° partida: ')))
ficha['gol'] = gols[:]
ficha['total'] = sum(gols)
print(ficha)
for k,v in ficha.items():
    print(f'{k} -> {v}')
for i,v in enumerate(ficha['gol']):
    print(f'    Na partida {i+1}, fez {v} gols')
print(f'Total de gols foi {ficha["total"]}')
