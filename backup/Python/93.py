class Solution(object):
    def restoreIpAddresses(self, s):

        def dfs(s, n, out, result):
            if n == 4:
                if not s:
                    result.append(out)
                return
            for k in range(1, 4):
                if len(s) < k:
                    break
                val = int(s[:k])
                if val > 255 or k != len(str(val)):
                    continue
                dfs(s[k:], n+1, out + s[:k] + ('' if n==3 else '.'), result)

        result = list()
        dfs(s, 0, '', result)
        return result
