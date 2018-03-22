class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {

        vector<int> res;
        for (int i = left; i <= right; ++i) {
            if (isDividingNumber(i)) {
                res.push_back(i);
            }
        }
        return res;
    }

    bool isDividingNumber(int i) {
        int temp = i;
        while (temp) {
            int index = temp % 10;
            temp = temp / 10;
            if (index == 0) {
                continue;
            }
            if (i % index) {
                return false;
            }
        }
        return true;
    }
};
