try:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media = (nota1 + nota2) / 2

    if media >= 6:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    with open("aluno.txt", "w") as arquivo:
        arquivo.write("Nome: " + nome + "\n")
        arquivo.write("Média: " + str(media) + "\n")
        arquivo.write("Resultado: " + resultado)

except ValueError:
    print("Digite apenas números.")