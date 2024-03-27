contas = [[1,2,3],[3,2,1]]
sumx = list()
sum = 0
cont = 0
for c in contas:
    for i in c:
        sum += i
    sumx.append(sum)
    sum = 0
return max(sumx)

print(sumx)