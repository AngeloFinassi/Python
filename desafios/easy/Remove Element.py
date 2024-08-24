nums = [3,2,2,3]
val = 3

for c in range(len(nums) - 1, -1, -1):
    if nums[c] == val:
        nums.pop(val)

print(nums)