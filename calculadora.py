try:
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2

    try:
        div = n1 / n2
    except ZeroDivisionError:
        div = "Erro (divisão por zero)"

    with open("calculadora.txt", "w") as arquivo:
        arquivo.write("Soma: " + str(soma) + "\n")
        arquivo.write("Subtração: " + str(sub) + "\n")
        arquivo.write("Multiplicação: " + str(mult) + "\n")
        arquivo.write("Divisão: " + str(div))

except ValueError:
    print("Digite apenas números.")
    