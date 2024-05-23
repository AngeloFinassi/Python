import random

numbers = [random.randint(1, 100) for _ in range(5)]

def BigSmal(numbers, param):
    if not numbers:
        return None, None
    
    n_bigger = n_smaller = numbers[0]

    for c in range(0, len(numbers)): 
        n = numbers[c]
        if n > n_bigger:
            n_bigger = n
        if n < n_smaller:
            n_smaller = n
    if param == 1:
        return n_bigger
    else:
        return n_smaller

def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length):
        # range(0, length - i - 1) diminui a cada iteração do loop externo
        for k in range(0 , length - i - 1):
            if numbers[k] > numbers[k + 1]:
                numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]
    return numbers


def selection(numbers):
    for i in range(len(numbers)):
        min_index = i
        for k in range(1 + i, len(numbers)):
            if numbers[k] < numbers[min_index]:
                min_index = k
        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    return numbers


print(numbers)
print(selection(numbers))
