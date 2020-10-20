class Solution {
public:
    int hammingDistance(int x, int y) {

        int distance = 0;
        while (x || y) {
            int x_res = x % 2;
            x = x / 2;
            int y_res = y % 2;
            y = y / 2;
            if (x_res != y_res) {
                ++distance;
            }
        }

        return distance;
        
    }
};
