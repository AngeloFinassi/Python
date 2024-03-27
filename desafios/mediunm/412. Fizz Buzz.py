n = 3

numbers = []

for c in range(1, n + 1):
        if c % 3 == 0 and c % 5 == 0:
            numbers.append("FizzBuzz")
        elif c % 3 == 0:
            numbers.append("Fizz")
        elif c % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(str(c))

print(numbers)