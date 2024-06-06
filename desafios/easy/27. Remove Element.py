nums = [3,2,2,3]
val = 2
k = 0

l = 0
for j in range(0, len(nums)):
    if nums[j] == val:
        l += 1
k = len(nums) - l

for i in range(0, l):
    nums.remove(val)

print(k, nums)
