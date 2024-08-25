nums = [16,1,0,9,100]
cont = 0
nums = sorted(nums)
for c in nums:
    nums[cont] = c * c
    cont += 1

print(nums)
