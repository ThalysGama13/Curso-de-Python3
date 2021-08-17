from random import randint
jogo = list()
mega = list()
quant = int(input('Quantos jogos Vão ser feitos? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        j = randint(1, 60)
        if j not in jogo: #p/ nãp repetir os númeor dentro de uma lista
            jogo.append(j)
            cont+=1
        if cont >= 6:
            break
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
    total += 1 #p/ nãp entrar em loop infinito
for i, l in enumerate(mega): #o enumerate trata o índice e a lista
    print(f'Jogo {i+1}: {l}')
