class Solution(object):
    def removeOuterParentheses(self, s):
        stack = []
        depth = 0
        for ch in s:
            if ch == "(":
                if depth > 0:
                    stack.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    stack.append(ch)
        return "".join(stack)
                

       