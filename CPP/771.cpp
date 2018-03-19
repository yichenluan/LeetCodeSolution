class Solution {
public:
    int numJewelsInStones(string J, string S) {

        map<char, int> stoneCount;
        for (auto stone : S) {
            ++stoneCount[stone];
        }

        int res = 0;

        for (auto jewel : J) {
            res += stoneCount[jewel];
        }

        return res;
        
    }
};
