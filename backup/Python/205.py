class Solution(object):
    def isIsomorphic(self, s, t):
        history = {}
        used_chars = set()
        if len(s) != len(t):
            return False
    
        for i in range(len(s)):
            if s[i] not in history:
                if t[i] in used_chars:
                    return False
                history[s[i]] = t[i]
                used_chars.add(t[i])
            elif history[s[i]] != t[i]:
                return False
        return True
