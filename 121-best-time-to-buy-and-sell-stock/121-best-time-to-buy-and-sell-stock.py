class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        current_profit = 0
        max_profit = 0
        
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                current_profit = prices[r] - prices[l]
                if current_profit >= max_profit:
                    max_profit = current_profit
            r += 1
        
        return max_profit