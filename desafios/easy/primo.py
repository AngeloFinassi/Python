def is_primo(n:int):
    cont_div = 0
    list = [1, 2, 3, 5, n]
    for c in list:
        if c != n:
            if (n % c) == 0:
                cont_div += 1
    if cont_div > 1:
        return False
    else:
        return True


number  = int(input("Number: "))
print(is_primo(number))