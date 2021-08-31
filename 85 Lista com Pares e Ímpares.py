números = [[], []]
for c in range (0, 7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:
        números[0].append(n)
    else:
        números[1].append(n)
números[0].sort()
números[1].sort()
print(f'Os valores pares digitados foram {números[0]}')
print(f'Os valores ímpares foram {números[1]}')

