while True:
    height = int(input("Height: "))
    if height > 0:
        break

for c in range(height):
    for j in range(height):
        print("#", end  = "")
    print()
