class Solution(object):
    def reverseVowels(self, s):
        VOWELS = ('A','a','e','E','i','I','o','O','U','u')
        str_list = list(s)
        len_s = len(str_list)
        l_point = 0
        r_point = len_s - 1
        while l_point < r_point:
            while str_list[l_point] not in VOWELS and l_point < r_point:
                l_point += 1
            while str_list[r_point] not in VOWELS and l_point < r_point:
                r_point -= 1
            if l_point < r_point:
                str_list[l_point], str_list[r_point] = str_list[r_point], str_list[l_point]
                l_point += 1
                r_point -= 1
        return ''.join(str_list)


if __name__ == '__main__':
    string = 'leetcode'
    case = Solution()
    print case.reverseVowels(string)

