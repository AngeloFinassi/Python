input_text = """
Task 1
Introduction
Task 2
Windows Privilege Escalation
Task 3
Harvesting Passwords from Usual Spots
Task 4
Other Quick Wins
Task 5
Abusing Service Misconfigurations
Task 6
Abusing dangerous privileges
Task 7
Abusing vulnerable software
Task 8
Tools of the Trade
Task 9
Conclusion
"""

linhas = input_text.strip().split('\n')

for i in range(1, len(linhas), 2):
    titulo = linhas[i]
    print(f"# {titulo}")
