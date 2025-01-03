from random import randint

n = int(input("Type a Number: "))
temp = 0
print("-="*30)

for j in range(0, n):
    array = list()
    #Array Generator
    k = 0
    while k < 5:
        number = randint(0, 10)
        array.append(number)
        
        k += 1   
    print(f"Array gerado: {array}")

    #Bubble Sort
    for i in range(0, len(array) - 1):
        for c in range(0, len(array) - 1):
            if array[c] > array[c + 1]:
                temp = array[c]
                array[c] = array[c + 1]
                array[c + 1] = temp
    print(f"Sorted Array: {array}")
    print("-="*30)
