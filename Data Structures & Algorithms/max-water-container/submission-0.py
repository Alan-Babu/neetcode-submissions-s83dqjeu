class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        max_area = 0
        current_max = 1

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
               current_max = min(heights[i], heights[j]) *(j-i)
               max_area = max(current_max,max_area)
        return max_area'''
        l, r= 0, len(heights)-1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(area, res)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res


        