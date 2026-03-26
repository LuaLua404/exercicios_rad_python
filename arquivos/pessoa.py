try:
    nome = input("Nome: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    ano = int(input("Ano de nascimento: "))

    idade = 2026 - ano

    with open("pessoa.txt", "w") as arquivo:
        arquivo.write("Nome: " + nome + "\n")
        arquivo.write("RG: " + rg + "\n")
        arquivo.write("CPF: " + cpf + "\n")
        arquivo.write("Idade: " + str(idade))

except ValueError:
    print("Inválido!")
