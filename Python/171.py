class Solution(object):
    def titleToNumber(self, s):
        res = 0
        reverse_s = s[::-1]
        for i in range(len(reverse_s)):
            key = reverse_s[i]
            val = ord(key) - ord('A') + 1
            res += val * (26 ** i)
        return res
