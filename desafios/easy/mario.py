height = int(input("Height: "))
space = height - 1
cont  = 1
while cont <= height:
    for j in range(space):
        print(" ", end="")
    for k in range(cont):
        print("#", end="")
    print(" ", end="")
    for k in range(cont):
        print("#", end="")
    for j in range(space):
        print(" ", end="")
    print()

    space = space - 1
    cont = cont + 1
