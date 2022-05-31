class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        
        front = nums[:length - k]
        back = nums[k + 1:]
        
        nums[:] = nums[length-k:] + nums[:length - k]
        
        return nums