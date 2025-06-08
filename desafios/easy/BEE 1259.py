N = int(input())
even = []
odd = []

for _ in range(N):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

even.sort()
odd.sort(reverse=True)

for num in even:
    print(num)

for num in odd:
    print(num)