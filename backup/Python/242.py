class Solution(object):
    def isAnagram(self, s, t):
        judge = dict()
        for char in s:
            judge[char] = judge.get(char, 0) + 1
        for char in t:
            judge[char] = judge.get(char, 0) - 1
            if judge[char] == 0:
                judge.pop(char)
        if judge == {}:
            return True
        else:
            return False
