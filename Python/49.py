class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hashtale {(a, b, c): ["abc", "bca"]}
        # 
        mp = {}
        for s in strs:
            lst = list(s); lst.sort(); lst = tuple(lst)
            if mp.get(lst):
                mp[lst].append(s)
            else:
                mp[lst] = [s]
        return mp.values()
