class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n = len(needle)
        for i in xrange(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i+n] == needle:
                return i
        return -1
