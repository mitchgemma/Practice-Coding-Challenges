class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result= []
        counter = Counter(nums1)
        
        for n in nums2:
            if counter[n] > 0:
                result.append(n)
                counter[n] -= 1
            
        return result
        