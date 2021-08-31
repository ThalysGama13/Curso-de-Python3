a1 = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
an = a1+10*r
for c in range(a1, an, r):
    print(c, end=' -> ')
print('Cabô')