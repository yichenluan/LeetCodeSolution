class Solution {
public:
    string reverseWords(string s) {
        auto i_pre = s.begin();
        auto i_back = s.begin();
        while(i_back != s.end()) {
            if(*i_back != ' ' && *i_pre == ' ') {
                i_pre = i_back;
            } else if (*i_back == ' ') {
                reverseWord(i_pre, i_back);
                i_pre = i_back;
            }
            i_back++;
        }
        reverseWord(i_pre, i_back);
        return s;
    }

    void reverseWord(string::iterator i_pre, string::iterator i_back) {
        while(i_back - i_pre > 1) {
            auto temp = *(i_back - 1);
            *(i_back - 1) = *i_pre;
            *i_pre = temp;

            i_pre++;
            i_back--;
        }
    }
};
