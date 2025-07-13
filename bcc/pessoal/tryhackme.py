input_text = """
Task 1
Introduction
Task 2
What is Intruder
Task 3
Positions
Task 4
Payloads
Task 5
Introduction to Attack Types
Task 6
Sniper
Task 7
Battering Ram
Task 8
Pitchfork
Task 9
Cluster Bomb
Task 10
Practical Example
Task 11
Practical Challenge
Task 12
Extra Mile Challenge
Task 13
Conclusion

"""

linhas = input_text.strip().split('\n')

for i in range(1, len(linhas), 2):
    titulo = linhas[i]
    print(f"# {titulo}")
