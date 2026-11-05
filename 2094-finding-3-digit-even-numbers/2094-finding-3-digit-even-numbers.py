class Solution(object):
    def findEvenNumbers(self, digits):
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
        result = []
        for num in range(100, 999, 2):
            a = num//100
            b = (num//10)%10
            c = num %10
            count = [0] *10
            count[a] += 1
            count[b] += 1
            count[c] += 1
            valid = True
            for i in range(10):
                if count[i] > freq[i]:
                    valid = False
                    break
            if valid:
                result.append(num)
        return result 

        