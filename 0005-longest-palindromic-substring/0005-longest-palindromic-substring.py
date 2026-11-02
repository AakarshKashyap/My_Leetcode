class Solution(object):
    def longestPalindrome(self, s):
       start = 0
       maxlength = 0
       for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right <len(s) and s[left] == s[right]:
                length = right - left + 1
                if length > maxlength:
                    start = left
                    maxlength = length
                left -= 1
                right += 1
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right-left + 1
                if length > maxlength:
                    start = left
                    maxlength = length
                left -= 1
                right += 1
       return s[start:start+maxlength]
            



        