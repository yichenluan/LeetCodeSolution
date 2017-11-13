#include <unordered_map>
#include <unordered_set>
#include <random>
#include <ctime>

class Solution {
public:
    unordered_map<string, string> long_to_short;
    unordered_map<string, string> short_to_long;
    const string prev_url = "http://tinyurl.com/";

    int random_unint(int min, int max, int seed) {
        static std::default_random_engine e(seed);
        static std::uniform_int_distribution<int> u(min, max);
        return u(e);
    }

    string encode(string longUrl) {
        if (long_to_short.find(longUrl) != long_to_short.end()) {
            return long_to_short[longUrl];
        }
        int random_value = random_unint(0, 1000, time(NULL));
        string short_url = prev_url + to_string(random_value);
        while (short_to_long.find(short_url) != short_to_long.end()) {
            random_value = random_unint(0, 1000, time(NULL));
            short_url = prev_url + to_string(random_value);
        }


        long_to_short[longUrl] = short_url;
        short_to_long[short_url] = longUrl;

        return short_url;

    }

    string decode(string shortUrl) {
        return short_to_long[shortUrl];

    }
};
