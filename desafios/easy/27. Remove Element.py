nums = [3,2,2,3]
val = 2
k = 0

j = 0
while j < len(nums):
    if nums[j] != val:
        k += 1
        j += 1
    else:
        nums.remove(val)

print(k, nums)
