class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]
