class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0;
        int y = 0;

        for(auto c: moves) {
            switch (c) {
                case 'R':
                    ++x;
                    break;
                case 'L':
                    --x;
                    break;
                case 'U':
                    ++y;
                    break;
                case 'D':
                    --y;
                    break;
            }
        }

        return !(x || y);
        
    }
};
