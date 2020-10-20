class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        res = strs[0]
        n = len(strs)
        for i in range(1, n):
            for j in range(len(res)):
                if j >= len(strs[i]):
                    res = res[:j]
                    break
                if res[j] != strs[i][j]:
                    res = res[:j]
                    break
        return res


if __name__ == '__main__':
    strs = ["a", "b"]
    case = Solution()
    print case.longestCommonPrefix(strs)
