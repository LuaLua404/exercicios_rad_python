lista = []

try:
    with open("arquivo.txt", "r") as f:
        for linha in f:
            lista.append(linha.strip())

    for item in lista:
        print(item)

except FileNotFoundError:
    print("Arquivo não encontrado.")
