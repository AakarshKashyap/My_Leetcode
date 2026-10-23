class Solution(object):
    def maxDepth(self, s):
        stack = []
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            elif s[i] == ")":
                stack.pop()
            ans = max(ans, len(stack))
        return ans
                
            
        