#map
#SERVE PARA ALTERAR CADA VALOR DA LISTA, UM A UM

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]

valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

"""
for v in valor_dobrado:
    print(v)
"""