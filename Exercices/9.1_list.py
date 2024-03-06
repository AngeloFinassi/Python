names = ["Am", "An", "Al"]

name  = input("Name: ")

#loops can have Else, wtf???
#if have a break, never read, the else is call
# for c in names:
#     if name == c:
#         print("found")
#         break

if name in names:
    print("Found")
else:
    print("Not Found")