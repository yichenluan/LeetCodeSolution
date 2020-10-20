class Solution(object):
    def removeDuplicateLetters(self, s):
        ldict = dict()

        for char in s:
            ldict[char] = ldict.get(char, 0) + 1
        stack = []
        visited = set()
        for char in s:
            if not stack:
                stack.append(char)
                ldict[char] -= 1
                visited.add(char)
                continue
            if char not in visited:
                while stack and char < stack[-1] and ldict[stack[-1]] > 0:
                    oldChar = stack[-1]
                    stack.pop()
                    visited.remove(oldChar)
                stack.append(char)
                visited.add(char)
            ldict[char] -= 1
        return ''.join(stack)
