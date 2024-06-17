arr = [17,18,5,4,6,1]
n = len(arr)
for c in range(0, n):
    for k in range(1 + c, n):
        if arr[c] < arr[k] and c < n:
            arr[c + 1] = arr[k]

print(arr)

#Refazer dificuldade coisa besta