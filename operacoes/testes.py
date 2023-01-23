#testes

x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))
sinal = input("Qual operação deseja fazer? Digite apenas o sinal: ")


if sinal == "+":
    op = x + y
    
elif sinal == "-":
    op = x - y

elif sinal == "*":
    op = x * y

elif sinal == "/":
    op = x / y

else:
    op = "Sinal invalido, tente novamente."

print("O resultado da operacao e: ", op)

