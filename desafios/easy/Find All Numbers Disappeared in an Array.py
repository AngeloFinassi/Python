# nums = [4,3,2,7,8,2,3,1]
# not_add = []

# for c in range(1, len(nums) + 1):
#     if c not in nums:
#         not_add.append(c)

# print(not_add)
# #the problem here is 0^2 complexity ;-;-;-;-;-;-;-;-;-;-;-;-;-;
# #must be a 0 notation with modification in place if possible

def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    result = [i + 1 for i in range(len(nums)) if nums[i] > 0]

    return result

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
