class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        duplicate_map = {}

        for item in nums:
            if item in duplicate_map:
                return True
            else:
                duplicate_map[item] = 1
        
        return False
    

    