word = str(input("The Word: "))
inverse_arr = list()

#copy the inverse word
for c in range(len(word) - 1, -1, -1):
    inverse_arr.append(word[c])

count = 0
for k in range(0, len(word) - 1):
    #If the inverse word its the same word
    if word[k] == inverse_arr[k]:
        count += 1
    
if count == len(word) - 1:
    print("Its a palindrome")
else:
    print("It's not a palindrome")

print(inverse_arr)