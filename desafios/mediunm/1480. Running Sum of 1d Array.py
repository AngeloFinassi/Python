class Solution(object):
    def runningSum(self, nums):
        output_list = list()
        sum = 0
        for c in nums:
            sum += c
            output_list.append(sum)
        return output_list

