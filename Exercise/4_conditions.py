print("----------------")
s = input("Do you agree? ").lower()
if s in ["y", "yes"]:
     print("Agreed")
else:
     print("Disagreed")

print("----------------")
x = int(input("x: "))
y = int(input("y: "))

if x == y:
     print("x is equal to y")
if x != y:
     print("x is diferent to y")
if x < y or x > y:
     print("x is diferent of y")

print("----------------")

#Python compare a full string, is more easy
word1 = str(input("Word 1: "))
word2 = str(input("Word 2: "))

if word1 == word2:
    print("They are the same word")