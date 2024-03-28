
nums = [16,1,0,9,100]

cont = 0

for i in range(0, len(nums)):
    if nums[i] < 0:
        nums[i] = nums[i] * -1

nums = sorted(nums)
for c in nums:
    nums[cont] = c * c
    cont += 1

print(nums)
