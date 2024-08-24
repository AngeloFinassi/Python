nums = [3,1,2,4]
cont_par = 0

for c in range(0, len(nums)):
    if nums[c] % 2 == 0:
        nums[c], nums[cont_par] = nums[cont_par], nums[c]
        cont_par += 1
#return nums

print(nums)
