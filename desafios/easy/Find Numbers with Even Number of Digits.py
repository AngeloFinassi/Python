nums = [12,345,2,6,7896]

cont_par = 0
for c in nums:
    if len(str(c)) % 2 == 0:
        cont_par += 1


print(cont_par)