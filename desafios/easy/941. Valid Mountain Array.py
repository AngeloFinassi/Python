#arr = [0,3,2,1]
#arr = [3,5,5]
arr = [1,3,2]

n = len(arr)
if n < 3:
    print("not a mountain")

i = 0

# Walk up
while i + 1 < n and arr[i] < arr[i + 1]:
    i += 1

# Peak can't be first or last
if i == 0 or i == n - 1:
    print("not a mountain")

# Walk down
while i + 1 < n and arr[i] > arr[i + 1]:
    i += 1

print(i == n - 1)
