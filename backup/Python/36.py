class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                # in one row
                for k in range(j+1, 9):
                    if board[i][j] == board[i][k]:
                        return False
                # in one col
                for k in range(i+1, 9):
                    if board[i][j] == board[k][j]:
                        return False
                # in one square
                for k in range(i+1, (i/3+1)*3):
                    for h in range(j/3*3, (j/3+1)*3):
                        if h != j and board[i][j] == board[k][h]:
                            return False
        return True
