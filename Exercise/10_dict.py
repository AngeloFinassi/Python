people = [
    {"name": "An", "number": "123"},
    {"name": "Am", "number": "456"},
    {"name": "Al", "number": "789"},
]

name = str(input("Name: "))

for person in people:
    if(name in person["name"]):
        print(f"Found: {person['number']}")
        break
else:
    print("Not Found")
