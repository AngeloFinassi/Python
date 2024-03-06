def cont_word(word: str, frase: str):
    cont = 0
    palavras = frase.split()  # Divide a frase em palavras usando espaços em branco como separadores
    print(palavras)

    for palavra in palavras:
        if palavra == word:
            cont += 1

    return cont

frase = input("frase: ")
pala = input("palavra: ")

print(f"Temos {cont_word(pala, frase)} vezes a palavra {pala}")
