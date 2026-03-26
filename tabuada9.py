with open("tabuada9.txt", "w") as arquivo:
    for i in range(1, 11):
        linha = "9 x " + str(i) + " = " + str(9 * i) + "\n"
        arquivo.write(linha)
