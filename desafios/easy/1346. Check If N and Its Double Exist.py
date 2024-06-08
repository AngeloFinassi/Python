arr = [10,2,5,3]
#arr = [3,1,7,11]
arr = [-2,0,10,-19,4,6,-8]

for c in range(0, len(arr)):
    
    for k in range(0, len(arr)):
        if c != k and arr[c] == (2 * arr[k]):
            print(arr[c], arr[k])
            