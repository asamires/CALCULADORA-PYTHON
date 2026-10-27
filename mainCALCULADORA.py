while True:
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
        print(f"O resultado da soma é: {n1} + {n2} = {resultado}")

    elif operação == "2":
        resultado = n1 - n2
        print(f"O resultado da subtração é: {n1} - {n2} = {resultado}")

    elif operação == "3":
        resultado = n1 * n2
        print(f"O resultado da multiplicação é: {n1} * {n2} = {resultado}")

    elif operação == "4":
        if n2 != 0:
            resultado = n1 / n2
            print(f"O resultado da divisão é: {n1} / {n2} = {resultado}")
        else:
            print("Erro: Não é possível dividir por zero!")

    else:
        print("Opção inválida! Escolha uma operação válida (1, 2, 3 ou 4).")

    continuar = input(
        "\nDeseja iniciar um novo cálculo? Digite S para sim ou N para não: "
    ).strip().lower()

    if continuar == "s" or continuar == "sim":
        print("\nReiniciando calculadora...\n")

    else:
        print("Calculadora encerrada!")
        break
