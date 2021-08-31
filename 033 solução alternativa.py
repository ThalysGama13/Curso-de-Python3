n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
n3 = int(input('Digite um valor:'))
#vendo quem menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#vendo quem é maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('o menor valor é {}'.format(menor))
print('o maior valor é {}'.format(maior))
