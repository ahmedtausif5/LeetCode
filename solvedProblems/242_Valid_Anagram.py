class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_1 = {}
        map_2 = {}

        for item in s:
            if item in map_1:
                map_1[item] += 1
            else:
                map_1[item] = 1
        for item in t:
            if item in map_2:
                map_2[item] += 1
            else:
                map_2[item] = 1
                
        if map_1 == map_2:
            return True
        else:
            return False

