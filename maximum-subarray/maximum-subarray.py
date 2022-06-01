class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currMax = 0
        
        for n in nums:
            if currMax < 0:
                currMax = 0
            currMax += n
            maxSub = max(maxSub, currMax)
        
        return maxSub
        