class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if the lowest comes before the highest, buy at lowest and sell on highest. 
        # if the number 
        
        r = 1
        l=0
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)

            else:
                l = r
            r += 1
            
        return maxP