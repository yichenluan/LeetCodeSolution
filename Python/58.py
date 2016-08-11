class Solution(object):
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        s_list = [temp for temp in s.split(' ') if temp]
        if not s_list:
            return 0
        return len(s_list[-1])
