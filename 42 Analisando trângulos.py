a = float(input('Comprimento a:'))
b = float(input('Comprimento b:'))
c = float(input('Comprimento c:'))
if a < b + c and b<a+c and c<a+b:
    print('Forma um triângulo', end=' ')
    if a==b==c:
        print('e é equilátero')
    elif a==b or b==c or a==c:
        print('e é isóceles')
    else:
        print('e é escaleno')
else:
    print('Não forma triângulo')
