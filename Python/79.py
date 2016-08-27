class Solution(object):
    def exist(self, board, word):
        if board == []:
            return 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.helper(board[:], word[1:], r, c):
                        return True
        return False

    def helper(self, board, word, r, c):
        if word == "":
            return True

        tmp = board[r][c]
        board[r][c] = "#"
        if r -1 >= 0 and board[r-1][c] == word[0]:
            if self.helper(board[:], word[1:], r-1, c):
                return True
        if r+1<=len(board)-1 and board[r+1][c]==word[0]:
            if self.helper(board[:],word[1:],r+1,c):
                return True

        if c-1>=0 and board[r][c-1]==word[0]:
            if self.helper(board[:],word[1:],r,c-1):
                return True
        if c+1<=len(board[0])-1 and board[r][c+1]==word[0]:
            if self.helper(board[:],word[1:],r,c+1):
                return True

        board[r][c] = tmp
        return False
