class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for index, item in enumerate(nums):

            complement = target - item

            if complement not in hash_map:
                hash_map[item] = index
                
            else:
                return [hash_map[complement], index]