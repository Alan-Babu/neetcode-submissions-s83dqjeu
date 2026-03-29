class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]* len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    print(nums[i])
                    print(nums[j])
                    print(res[j])
                    print(res)
                    res[i]*=nums[j]
        return res
        


