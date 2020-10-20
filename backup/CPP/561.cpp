class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        int res = 0;
        sort(nums.begin(), nums.end());
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            if ((it - nums.begin()) % 2 == 0) {
                res += *it;
            }
        }
        return res;
    }
};
