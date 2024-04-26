x = int(input("x: "))
y = int(input("y: "))
#don't have Trucation, int/ int = float if its possible
z = x / y

#to edit the float number like 0.33333 -> 0.33
#50 is a number after the 0._____
print(f"{z:.50f}")