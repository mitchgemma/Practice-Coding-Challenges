class Solution(object):
    def isAnagram(self, s, t):
        mapS = {}
        mapT = {}
        for l in s:
            if l in mapS:
                mapS[l] += 1
            else:
                mapS[l] = 1
        for l in t:
            if l in mapT:
                mapT[l] += 1
            else:
                mapT[l] = 1
        if mapS == mapT:
            return (True)
        else:
            return (False)
        