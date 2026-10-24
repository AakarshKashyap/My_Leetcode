class Solution(object):
    def buildArray(self, target, n):
        result = []
        for i in range(1, n+1):
            result.append("Push")
            if i not in target:
                result.append("Pop")
            if i == target[-1]:
                break
        return result

        