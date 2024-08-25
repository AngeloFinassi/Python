#nums = [2,2,3,1]
nums = [3,2,1]
#nums = [5,2,2]
n = nums[0]
a = 0
t = 0
dif_n = 1
while a < len(nums):
    if nums[a] != n:
        n = nums[a]
        t = n
        dif_n += 1
    a += 1

if dif_n < 3:
    t = max(nums)


print(t)
