try:
    with open("texto_underline.txt", "r") as f:
        texto = f.read()

    novo = texto.replace(" ", "_")

    with open("novo.txt", "w") as f:
        f.write(novo)

except FileNotFoundError:
    print("Arquivo não encontrado.")
