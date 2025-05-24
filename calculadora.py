def calculadora():
    while True:
        try:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /) ou 'sair' para encerrar: ")
            if num1 == "sair":
                print("Encerrando a calculadora.")
                break
            elif operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida. Tente novamente.")
                continue
            print(f"O resultado de {num1} {operacao} {num2} = {resultado}")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira números válidos.")
    