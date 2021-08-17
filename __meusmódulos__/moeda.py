def aumenta(num, formatação = False):
    a = num + 0.1*num
    if formatação:
        return f'R$ {a:.2f}'
    else:
        return a


def diminui(num, formatação = False):
    d = num - 0.1*num
    if formatação:
        return f'R$ {d:.2f}'
    else:
        return d


def dobro(num, formatação = False):
    dob = 2*num
    if formatação:
        return f'R$ {dob:.2f}'
    else:
        return dob


def metade(num, formatação = False):
    meio = num/2
    if formatação:
        return f'R$ {meio:.2f}'
    else:
        return meio


def resumo(num):
    res = f'''{num} com aumento de 10% fica:    \t{aumenta(num, formatação = True)}

{num} com desconto de 10% fica: \t\t{diminui(num, formatação = True)}

{num} dobrado fica: \t\t\t{dobro(num, formatação = True)}

{num} dividido por 2 fica:  \t\t{metade(num, formatação = True)}'''
    return res
