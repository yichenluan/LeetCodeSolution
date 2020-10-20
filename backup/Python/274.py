class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = citations
        i = 0
        h = 0
        if n:
            n.sort(reverse=True)
            while i<len(n):
                if n[i]>=i+1:
                    h += 1
                i += 1    
            return h
        else:
            return 0
