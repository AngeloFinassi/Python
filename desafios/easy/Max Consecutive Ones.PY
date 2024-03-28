nums = [1,1,0,1,1,1]
#nums = [1,0,1,1,0,1]

cont_1 = 0
cont_x = list()
for c in nums:
    if c == 1:
        cont_1 += 1
    else:
        cont_x.append(cont_1)
        cont_1 = 0
    cont_x.append(cont_1)

print(max(cont_x))