from math import sqrt
# Escreva um programa que resolva uma equação de segundo grau. 

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - 4*a*c
print("delta = " + str(delta))

if delta <= 0:
    print("delta negativo")
    
else:

    raiz_delta = sqrt(delta)

    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
    print ("A raiz de x1 e: ", x1)
    print ("A raiz de x2 e: ", x2)

    #print("As raizes sao", x1, "e", x2)





