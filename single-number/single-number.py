class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        
        for n in nums:
            if (n in hash):
                hash[n] += 1
            else:
                hash[n] = 1
        for n in hash:
            if (hash[n] == 1):
                return n