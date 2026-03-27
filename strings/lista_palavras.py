lista = []

try:
    with open("frase_lista.txt", "r") as f:
        for linha in f:
            palavras = linha.split()
            
            for p in palavras:
                p = p.strip()
                if p not in lista:
                    lista.append(p)

    print(lista)

except FileNotFoundError:
    print("Arquivo não encontrado.")
