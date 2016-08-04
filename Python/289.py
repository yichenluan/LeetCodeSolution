class Solution(object):
    def gameOfLife(self, board):
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return

        for i in xrange(0, len(board)):
            for j in xrange(0, len(board[0])):
                sum = self.checkEightNeighboursSum(i, j, board)
                if (board[i][j] == 1 and (sum in [2, 3])) or (board[i][j] == 0 and sum == 3):
                    board[i][j] |= 0x02
                    
        for i in xrange(0, len(board)):
            for j in xrange(0, len(board[0])):
                board[i][j] >>= 1
        
    def checkEightNeighboursSum(self, row, col, board):
        sum = 0
        for i in xrange(row - 1, row + 2):
            for j in xrange(col - 1, col + 2):
                if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                    continue
                if board[i][j] & 0x01 == 1:
                    sum += 1
        return sum - board[row][col]
