class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = right = 0
        vowels = 0
        max_vowels = 0
        vowel_set = ["a","e","i","o","u"]
        while right<len(s):
            if s[right] in vowel_set:
                vowels +=1
    
            if right-left+1 == k:
                max_vowels = max(max_vowels, vowels)
                if s[left] in vowel_set:
                    vowels -= 1
                left+=1
            right +=1
        return max_vowels
                
        