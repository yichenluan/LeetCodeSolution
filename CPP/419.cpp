class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        if (board.empty() || board[0].empty()) {
            return 0;
        }
        int res = 0;
        char x = 'X';
        char dot = '.';
        for(decltype(board.size()) column = 0; column != board.size(); ++column) {
            for(decltype(board[0].size()) row = 0; row != board[0].size(); ++row) {
                if (board[column][row] != x) {
                    continue;
                }
                if (column > 0 && board[column-1][row] == x){
                    continue;
                }
                if (row > 0 && board[column][row-1] == x){
                    continue;
                }
                ++res;
            }
        }

        return res;
        
    }
};
