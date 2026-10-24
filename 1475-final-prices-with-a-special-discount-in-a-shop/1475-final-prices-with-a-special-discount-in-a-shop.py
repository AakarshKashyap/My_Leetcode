class Solution(object):
    def finalPrices(self, prices):
        stack = []
        n = len(prices)
        d = 0
        for i in range(n):
            for j in range(i+1, n):
                if prices[i]>=prices[j]:
                    d = prices[j]
                    stack.append(prices[i] - d)
                    break
            else:
                stack.append(prices[i])
        return stack

        