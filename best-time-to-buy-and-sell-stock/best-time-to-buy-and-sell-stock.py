class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_prof = 0
        
        while r in range(len(prices)):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            elif prices[l] < prices[r]:
                curr_prof = prices[r] - prices[l]
                if curr_prof > max_prof:
                    max_prof = curr_prof
                r += 1
            
        return max_prof