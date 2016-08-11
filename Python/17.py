class Solution(object):
    def letter_combs(self,digits,combd):
        if not digits:
            yield ''
        else:
            for i in self.letter_combs(digits[:-1],combd):
                for j in combd[digits[-1]]:
                    yield i+j
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        combd='2abc 3def 4ghi 5jkl 6mno 7pqrs 8tuv 9wxyz'
        combd={i[0]:i[1:] for i in combd.split()}
        return list(self.letter_combs(digits,combd))
