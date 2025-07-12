input_text = """
Task 1
Introduction
Task 2
Hash Functions
Task 3
Insecure Password Storage for Authentication
Task 4
Using Hashing for Secure Password Storage
Task 5
Recognising Password Hashes
Task 6
Password Cracking
Task 7
Hashing for Integrity Checking
Task 8
Conclusion
"""

linhas = input_text.strip().split('\n')

for i in range(1, len(linhas), 2):
    titulo = linhas[i]
    print(f"# {titulo}")
