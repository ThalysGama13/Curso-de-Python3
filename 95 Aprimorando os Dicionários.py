time = list()
ficha = dict()
gols = list()
while True:
    ficha.clear()
    ficha['jogador'] = str(input('Digite seu nome: '))
    n = int(input('N° de partidas jogadas: '))
    tot = 0
    gols.clear()
    for c in range(0, n):
        gols.append(int(input(f'Gols marcados na {c + 1}° partida: ')))
    ficha['gol'] = gols[:]
    ficha['total'] = sum(gols)
    time.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper()
        if resp in 'SN':
            break
        print('Responda S ou N')
    if resp in 'Nn':
        break
print('='*25)
for i in ficha.keys():
    print(i)

for k,v in enumerate(time):
    print(k)
    for d in v.values():
        print(f'{str(d)}')
while True:
    perg = int(input('Que ver os dados de qual jogador? (999 para parar): '))
    if perg == 999:
        break
    if perg >= len(time):
        print('Esse jogador não existe')
    else:
        print(f'{time[perg]["jogador"]}')
        for i, g in enumerate(time[perg]['gols']):
            print(f'    Na partida {i+1} fez {g} gols')
