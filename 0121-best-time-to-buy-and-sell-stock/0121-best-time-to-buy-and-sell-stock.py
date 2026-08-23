class Solution(object):
    def maxProfit(self, prices):
        l=0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l=i
            else:
                profit = prices[i] - prices[l]
                max_profit = max(max_profit, profit)
        return max_profit
                

        