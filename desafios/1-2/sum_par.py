def sum_par(a:int, b:int):
    numbers_pars = []
    #cria uma lista que vai de a -> b, intervalo aberto 
    #se o número desse intervalo for par adiciona na lista
    for c in range(a, b + 1):
        if c % 2 == 0:
            numbers_pars.append(c)
    return sum(numbers_pars)

print(sum_par(20, 30))