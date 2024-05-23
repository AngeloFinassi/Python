import random

numbers = [random.randint(1, 1000) for _ in range(10)]

def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length):
        # range(0, n - i - 1) diminui a cada iteração do loop externo
        for k in range(0 , length - i - 1):
            if numbers[k] > numbers[k + 1]:
                numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]
    return numbers


bubble_sort(numbers)
print(numbers)

