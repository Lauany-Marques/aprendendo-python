#zip

lista1 = [1, 2, 3, 4, 5]
lista2 = ["Abacate", "Bola", "Carro", "Dolar", "Estopa"]
lista3 = ["R$10,00", "R$5,00", "R$20.000", "R$5,50", "R$2,50"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)