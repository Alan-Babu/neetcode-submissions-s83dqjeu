class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashTab = {}
        print(type(HashTab))
        for item in nums:
            if item in HashTab.keys():
                HashTab[item]+=1
                return True
            else:
                HashTab[item]=1
        return False
        