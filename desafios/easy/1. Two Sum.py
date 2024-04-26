nums = [2,7,11,15]
target = 9

asw = []
for c in range(len(nums)):
    for k in range(c + 1, len(nums)):
        if nums[c] + nums[k] == target:
            asw.append(c)
            asw.append(k)
#return asnwer
print(asw)