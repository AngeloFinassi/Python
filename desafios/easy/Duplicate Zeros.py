
arr = [1,0,2,3,0,4,5,0]

arr_clone = []
for c in arr:
    if len(arr_clone) < len(arr):
        if c == 0:
            arr_clone.append(c)
            arr_clone.append(c)
        else:
            arr_clone.append(c)
arr = arr_clone.copy()
print(arr_clone)
