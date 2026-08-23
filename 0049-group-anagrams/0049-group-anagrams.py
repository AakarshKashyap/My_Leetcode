class Solution(object):
    def groupAnagrams(self, strs):
        group = {}
        for i in strs:
            n = tuple(sorted(i))
            if n not in group:
                group[n] = []
            group[n].append(i)
        return list(group.values())

        