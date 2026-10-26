print("**************")
print("Calculadora")
print("**************\n")

print("Olá, hoje iremos aprender a calcular... \n")

print("Escolha a operação que quer realizar:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)\n")

operação = input("Digite o número da operação desejada: ")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if operação == "1":
    resultado = n1 + n2
    print(f"O resultado da soma é: {resultado}")

elif operação == "2":
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")

elif operação == "3":
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado}")

elif operação == "4":
    if n2 != 0:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Não é possível dividir!")

else:
    print("Opção inválida!")
