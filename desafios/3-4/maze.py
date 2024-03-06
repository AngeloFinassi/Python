def joe(maze, start, end):
    y = start[0] 
    x = start[1]
    pos_atual = [y, x]
    caminho = []
    visited = set()

    while pos_atual[0] != end[0] or pos_atual[1] != end[1]:
        visited.add((y, x))
        caminho.append(pos_atual[:])
        #Anda para baixo
        if y + 1 < len(maze) and maze[y + 1][x] == 0 and (y + 1, x) not in visited:
            y += 1
        #anda para cima
        elif y - 1 >= 0 and maze[y - 1][x] == 0 and (y - 1, x) not in visited:
            y -= 1
        #anda para R
        elif x + 1 < len(maze) and maze[y][x + 1] == 0 and (y, x + 1) not in visited:
            x += 1
        #anda para L
        elif x - 1 >= 0 and maze[y][x - 1] == 0 and (y, x - 1) not in visited:
            x -= 1
        else:
            #não ha movimentos possiveis
            break
        pos_atual = [y, x]

    caminho.append(pos_atual[:])
    return caminho


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

maze1 = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

maze2 = [
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

maze3 = [
    [0, 0, 1, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)
print(f"Caminho escolhido foi:{joe(maze1, start, end)}")