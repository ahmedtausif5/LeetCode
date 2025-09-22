class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, item in enumerate(nums):
            complement = target - item
            if complement in hash_map:
                return [hash_map[complement], index]
            else:
                hash_map[item] = index


