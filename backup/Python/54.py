class Solution(object):
    def spiralOrder(self, matrix):
        if matrix==[]: return []
        rows = len(matrix)
        cols = len(matrix[0])
        # initialize...
        l = 0; r = cols-1; u = 0; d = rows-1
        right = True; down = False; left = False; up = False
        res = []
        i=0; j=0; count = 1;
        # traverse the spiral, taking a turn whenever restricted by a boundary
        while count<=rows*cols:
            res.append(matrix[i][j])
            count += 1
            if right:
                if j+1<=r:
                    j += 1
                else: # must go down
                    right = False; down = True; u += 1; i += 1
            elif down: 
                if i+1<=d:
                    i += 1
                else: # must go left
                    down = False; left = True; r -= 1; j -= 1
            elif left: 
                if j-1>=l:
                    j -= 1
                else: # must go up
                    left = False; up = True; d -= 1; i -= 1
            elif up:
                if i-1>=u:
                    i -= 1
                else: # must go right
                    up = False; right = True; l += 1; j += 1
        return res
