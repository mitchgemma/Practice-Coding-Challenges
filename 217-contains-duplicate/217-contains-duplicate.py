class Solution(object):
    def containsDuplicate(self, nums):
        map = {}
        for i, n in enumerate(nums):
            if n in map:
                return True
            else:
                map[n] = i
            