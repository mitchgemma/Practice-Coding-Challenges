class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        
        for i, n in enumerate(nums):
            if (n in hash):
                return True
            else:
                hash[n] = i
        
        