class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size_of_array = len(nums)
        res = [1]*size_of_array
        prefix = 1
        for i in range(size_of_array):
            res[i] = prefix
            prefix*= nums[i]
        postfix = 1
        for i in range(size_of_array-1, -1,-1):
            res[i] *= postfix
            postfix*=nums[i]

        return res     
        
     
        


