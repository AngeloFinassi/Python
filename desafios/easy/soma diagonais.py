def SumDig()
    digP = 0
    digS = 0

    count = len(matriz)
    size = len(matriz)

    for c in range(0, size):
        for i in range(0, len(matriz[c])):
            if i == c:
                digP += matriz[c][i]
        for i in range(len(matriz[c]) -1, -1, -1):
            if i + c == size -1:
                digS += matriz[c][i]
                
    return digP+digS

matriz = [
    [1, 2, 3, 4],
    [4, 5, 6, 4],
    [9, 8, 9, 4],
    [4, 4, 4, 4]
]

