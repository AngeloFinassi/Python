def palindromo_ver(frase:str):
    inverse = ""
    cont = 0
    for c in range(len(frase) -1, -1 , -1):
        #aqui que a magica acontence, pois estou adicionando ao final de inverse o caraceter de frase de modo a copiare a strig de acordo com o looping, neste caso o inverso
        inverse += frase[c]
    if inverse == frase:
        print("é um palindromo!")
        print(f"{frase} é igual a {inverse}")
    else:
        print("Nãe é um palindromo!")
        print(f"{frase} é diferente da {inverse}")
        

palindromo_ver(input("Frase: "))