class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_prod = 1
        prefix_arr = [0]*len(nums)

        for i in range(len(nums)):
            total_prod *= nums[i]
            prefix_arr[i] = total_prod

        total_prod = 1
        postfix_arr = [0]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            total_prod *= nums[i]
            postfix_arr[i] = total_prod    

        res = []
        for i in range(len(nums)):
            prefix_value = prefix_arr[i-1] if i>0 else 1
            postfix_value = postfix_arr[i+1] if i<len(nums)-1 else 1
            
            res.append(prefix_value*postfix_value)

        return res

