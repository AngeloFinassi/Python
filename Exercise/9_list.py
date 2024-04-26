scores = []

for i in range(3):
    score1 = int(input(("Score: ")))
    #append add a value in the list
    scores.append(score1)

average = sum(scores) / len(scores)
print(f"Average: {average}")