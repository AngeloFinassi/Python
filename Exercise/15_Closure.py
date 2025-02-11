"""
closures are: when a child (or nested) function "remembers" and captures variables from its 
parent function even after the parent function has already finished executing.
"""

def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins  
        coins -= 1

        if coins >= 1:
            print(f'{person} has {coins} coins with him')
        elif coins == 1:
            print(f'{person} has just one coin')
        else:
            print(f"{person} has no coins left, YOU'RE STUPID!")

    return play_game #Return the function instead of calling it

#isn't the same thing as angelo(angelo), without relation between the
#quantity of time that I called this, when i build this type of structe,
#starts a type of data structure

angelo = parent_function('angelo')

#angelo é agora uma referência para a função play_game, junto com o
#escopo fechado onde coins foi definido
 
carol = parent_function('carol')

angelo()
angelo()
carol()
angelo()
