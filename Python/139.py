class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False for _ in range(n)]
        for i in range(n-1, -1, -1):
            temp = s[i:]
            for j in range(1, len(temp)+1):
                if temp[:j] in wordDict:
                    if j == len(temp) or dp[i+j] == True:
                        dp[i] = True
                        break
        return dp[0]
