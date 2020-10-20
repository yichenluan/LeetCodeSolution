class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        string mosi[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        set<string> mosi_set;
        for (string word : words) {
            string res;
            for (char c : word) {
                res += mosi[c - 'a'];
            }
            mosi_set.insert(res);
        }

        return mosi_set.size();
    }
};
