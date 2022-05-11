class Solution(object):
    def twoSum(self, nums, target):
        d = {} # value : index
    
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], i]
            d[n] = i
        