class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_map_s = {}
        count_map_t = {}

        for item in s:
            if item not in count_map_s:
                count_map_s[item] = 1
            else:
                count_map_s[item] += 1

        for item in t:
            if item not in count_map_t:
                count_map_t[item] = 1
            else:
                count_map_t[item] += 1

        return count_map_t == count_map_s
