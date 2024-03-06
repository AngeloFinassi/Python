def cont_vog(frase:str):
    vogal = 'AEIOUaeiou'
    cont = 0
    for c in frase:
        if c in vogal:
            cont += 1
    return cont


frases = str(input("Frase: "))
print(cont_vog(frases))