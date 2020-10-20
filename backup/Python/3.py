class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <= 1:
            return n
        dict1, start, end, lg_len = {}, 0, 0, 1
        for i in range(n):
            if s[i] in dict1 and dict1[s[i]] >= start:
                start = dict1[s[i]] + 1
            end += 1
            lg_len = max(lg_len, end-start)
            dict1[s[i]] = i
        return lg_len
