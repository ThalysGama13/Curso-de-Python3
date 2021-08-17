def maior(*n):
    cont = mai = 0
    for v in n:
        print(v)
        if cont == 0: 
            mai = v
        else:
            if v > mai: 
                mai = v
        cont += 1
    print(f'Foram digitados {cont} valores')
    print(f'O maior valor é {mai}')


print('Coloque os valores para serem analisados')
maior(5, 6, 4, 20)
