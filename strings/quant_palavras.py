try:
    with open("frase.txt", "r") as f:
        texto = f.read()

    palavras = texto.split()

    print("Quantidade de palavras:", len(palavras))

except FileNotFoundError:
    print("Arquivo não encontrado.")
