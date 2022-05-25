class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        
        for n in s:
            if n not in hash:
                hash[n] = 1
            else:
                hash[n] += 1

        index = -1
        for l in range(len(s)):
            if (hash[s[l]] == 1):
                index = l
                break
        
        return index