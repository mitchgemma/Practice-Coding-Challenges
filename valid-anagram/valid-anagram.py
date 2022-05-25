class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        
        for l in s:
            if l not in hash_s:
                hash_s[l] = 1
            else:
                hash_s[l] += 1
        
        for l in t:
            if l not in hash_t:
                hash_t[l] = 1
            else:
                hash_t[l] += 1
                
        if hash_t == hash_s:
            return True
        else:
            return False