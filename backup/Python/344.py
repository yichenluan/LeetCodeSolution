class Solution(object):
    def reverseString(self, s):
        s_list = list(s)
        reverse_s_list = s_list[::-1]
        return ''.join(reverse_s_list)
