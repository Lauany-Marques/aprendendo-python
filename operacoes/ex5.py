#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. 

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
sinal = input("Qual operação deseja fazer? Digite apenas o sinal")
#FLOAT OU INT E PORQ?

if sinal == "+":
    op = x + y

elif sinal == "-":
        op = x - y

elif sinal == "*":
        op = x * y

elif sinal =="/":
       op = x / y

else:
    op = "sinal invalido"


print(op)