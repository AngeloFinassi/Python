def factorial(n:int):
    acu = 1
    if n == 0:
        return acu
    
    for c in range(n, 0, - 1):
        acu = acu * c
    return acu


number = int(input("Number: ")) 
print(factorial(number))
