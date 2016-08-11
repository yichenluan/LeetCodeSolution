class Solution(object):
    def countAndSay(self, n):
        before = '1'
        for j in range(n - 1):
            then = ''
            char_num = 0
            char = before[0]
            for i in range(len(before)):
                if char == before[i]:
                    char_num += 1
                else:
                    then += (str(char_num) + str(char))
                    char = before[i]
                    char_num = 1
            then += (str(char_num) + str(char))
            before = then
        return before


if __name__ == '__main__':
    n = 5
    case = Solution()
    print case.countAndSay(n)
