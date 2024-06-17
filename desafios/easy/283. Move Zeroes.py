nums = [0,1,0,3,12]

for c in range(0, len(nums)):
    if nums[c] == 0:
        nums.remove(nums[c])
        nums.append(0)

print(nums)