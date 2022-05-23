class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for i, n in enumerate(nums):
            if n in dups:
                return True
            else:
                dups[n] = i
            
        