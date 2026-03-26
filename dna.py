try:
    with open("dna.txt", "r") as f:
        cadeia = f.read().strip()

    invertida = ""

    for i in range(len(cadeia)-1, -1, -1):
        invertida += cadeia[i]

    print(invertida)

except FileNotFoundError:
    print("Arquivo não encontrado.")