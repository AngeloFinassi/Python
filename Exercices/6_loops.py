# i = 0
# while i < 1000 + 1:
#     #print(i)
#     i += 1

# i = 0 
# for c in range(1001):
#     print(i)
#     i += 1

before = str(input("before: "))
#This throw(tirar) all formatation
print("After: ", end="")

for c in before:
    print(c.upper(), end="")
