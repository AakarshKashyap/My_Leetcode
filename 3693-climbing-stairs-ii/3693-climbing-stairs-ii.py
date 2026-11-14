class Solution(object):
    def climbStairs(self, n, costs):
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1,4):
                prev = i-j
                if prev >= 0:
                    candidate = dp[prev] + costs[i-1] + (j**2)
                dp[i] = min(dp[i], candidate)
            pass
        return dp[n]
        