Q, E = map(int, input().split())
procurados = set(map(int, input().split()))
semana = list(map(int, input().split()))

for esc in semana:
    if esc in procurados:
        print(0)
    else:
        print(1)
