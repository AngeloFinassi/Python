def square(num): return num*num
square2 = lambda num: num* num 

#it's practically the same thing, about the result
print(square(2))
print(square2(2))

print(30*"=-")
################

def functionBuilder(x):
    return lambda num: num + x

#closure salva x como a função num + x => num + 10, quando chamo dnv ela soma como num, não mas como x
addTen = functionBuilder(10)
addFive = functionBuilder(5)

print(addTen(2))
print(addFive(2))

#High order functions are the functions that takes one more function as argument or return its

numbers = [3, 7, 12, 18, 20, 21]


#they interact with each item, function->numbers[0,1... n], without a loop, omg
squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

###############################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#############################

from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)