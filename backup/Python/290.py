class Solution(object):
    def wordPattern(self, pattern, str):
        str_list = str.split(' ')
        n = len(pattern)
        if n != len(str_list):
            return False
        hash_map = dict()
        exist_val = list()
        for i in range(n):
            if pattern[i] not in hash_map:
                val = str_list[i]
                if val in exist_val:
                    return False
                hash_map[pattern[i]] = val
                exist_val.append(val)
            else:
                if hash_map[pattern[i]] != str_list[i]:
                    return False
        return True
