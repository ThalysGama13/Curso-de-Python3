def notas(*n, sit=False):#parâmetro condicional leva True ou False
    boletim = dict()
    tam = len(n)
    boletim['tamanho'] = tam
    soma = média = 0
    soma = sum(n)
    média = soma/tam
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = média
    if sit:# se sit=True
        if média >= 5:
            boletim['situação'] = 'Aprovado'
        else:
            boletim['situação'] = 'Reprovado'
    return boletim


ficha = notas('add as notas', sit = True)
print(ficha)
