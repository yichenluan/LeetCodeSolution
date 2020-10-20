class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        auto a_plus_pos = a.find("+");
        string a1 = a.substr(0, a_plus_pos);
        string a2 = a.substr(a_plus_pos+1, a.size() - a_plus_pos - 2);

        auto b_plus_pos = b.find("+");
        string b1 = b.substr(0, b_plus_pos);
        string b2 = b.substr(b_plus_pos +1, b.size() - b_plus_pos - 2);

        int a_1 = atoi(a1.c_str());
        int a_2 = atoi(a2.c_str());
        int b_1 = atoi(b1.c_str());
        int b_2 = atoi(b2.c_str());

        int c_1 = a_1 * b_1 - a_2 * b_2;
        int c_2 = a_1 * b_2 + a_2 * b_1;

        string c1 = to_string(c_1);
        string c2 = to_string(c_2);

        string res = c1 + "+" + c2 + "i";
        return res;
    }
};
