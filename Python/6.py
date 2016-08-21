class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
    		return s
    	length=len(s)
    	wordlist=[""]*numRows
    	charclass=[0]*length
    	for i in range(length):
    		charclass[i] = i%(2*numRows-2)
    		if charclass[i] > numRows-1:
    			charclass[i]=2*numRows-2-charclass[i] 
    	for i in range(length):
    		wordlist[charclass[i]]+=(s[i])
    	return "".join(wordlist)
